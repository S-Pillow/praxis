#!/usr/bin/env python3
"""Optional, read-only UI reference lookup for a coding AI.

Invoked by a skill-aware agent for the user's normal UI request. It neither
edits a project nor installs tools, approves designs, or grants asset rights.
"""
import argparse
import json
import re

if __package__:
    from .search_catalog import load_catalog, positive_fields, rank_entries, terms
else:
    from search_catalog import load_catalog, positive_fields, rank_entries, terms

FILLER = frozenset('''build create make design redesign improve update fix website webapp app
application page pages screen screens interface interfaces ui ux for a an the and to
of that this with using use want need needs me my please modern beautiful professional
clean good great nice looking look new existing current project product responsive
its not our their while where which whose should could would will must every each per several
there here also very just only show clearly quick quicker refine
does did can may might whether how what why when who is are was were been being has have had
they them without never rely relying relies
'''.split())
# Platform context ("a web app") is not topical evidence; platform fit is handled by --platform.
PLATFORM_CONTEXT = frozenset({'web'})
# Words that name an interface feature only in interface context ("help center", "support chat");
# elsewhere they describe a domain ("help-desk", "support agents") or act as verbs.
AMBIGUOUS_TERMS = frozenset({'help', 'support'})
INTERFACE_NOUNS = frozenset('''text texts center centre page pages panel menu link links button buttons
tooltip tooltips widget widgets chat article articles docs documentation section content mechanism
mechanisms interface flow guide guides screen screens icon overlay dialog drawer'''.split())
# Visual-direction intent makes a theme or style reference meaningful in a critique.
VISUAL_DIRECTION_CUES = re.compile(
    r'\b(?:aesthetics?|style|styles|styling|stylistic|themes?|look and feel|visual (?:identity|direction|language|style)|'
    r'identity|brand|branding|mood|art direction|palettes?|colou?r schemes?|typography|typefaces?|fonts?)\b')
# Clearly non-visual work gets no visual recommendation; UI cues always win.
NON_VISUAL_CUES = re.compile(r'\b(?:backend|back-end|serializers?|database|migrations?|schema|endpoints?|'
                             r'cron|sql|server-side|worker|webhooks?)\b')
UI_CUES = re.compile(r'\b(?:ui|ux|interface|page|screen|layout|visual|view|style|theme|colou?rs?|fonts?|'
                     r'typography|button|form|table|dashboard|component|modal|navigation|accessib\w*|'
                     r'keyboard|focus|contrast|responsive|mobile|desktop|onboarding|checkout|landing|'
                     r'website|icon|chart|menu|design|critique|frontend|front-end|display)\b')
ALIASES = {'finance': 'financial', 'fintech': 'financial', 'ecommerce': 'e-commerce',
           'shop': 'ecommerce', 'docs': 'documentation', 'a11y': 'accessibility',
           'colour': 'color', 'colours': 'colors'}
AUDIT_CUES = frozenset({'accessible', 'accessibility', 'keyboard', 'focus',
                        'contrast', 'navigation', 'mobile', 'touch', 'readability',
                        'readable', 'legibility', 'wcag'})
# Narrow accessibility corrections should not recommend a replacement visual identity.
FOCUSED_ACCESSIBILITY_CUES = frozenset({'keyboard', 'focus', 'wcag', 'accessibility', 'a11y', 'screenreader'})
CORRECTION_CUES = frozenset({'improve', 'fix', 'repair', 'correct', 'ensure', 'check', 'audit'})
NEW_DESIGN_CUES = frozenset({'build', 'create', 'make', 'redesign', 'new'})
EXPLICIT_STYLE_CUES = frozenset({'palette', 'theme', 'typography', 'font', 'branding', 'rebrand', 'restyle'})
GROUPS = {
    'build': (
        ('direction', ('theme', 'style', 'design_system')),
        ('palette', ('palette',)),
        ('typography', ('font_pairing',)),
    ),
    'critique': (
        ('usability_reference', ('guideline', 'anti_pattern')),
        ('design_reference', ('theme', 'style')),
    ),
    'audit': (('check_reference', ('guideline',)),),
}
# Extra guidelines must score at least half of the best match to fill the budget.
FILL_MIN_SHARE = 0.5
TOKEN_ROLES = frozenset({
    'Primary', 'Secondary', 'Accent', 'Background', 'Foreground',
    'Card', 'Card Foreground', 'Muted Foreground', 'Border', 'Ring',
    '--color-paper', '--color-ink', '--color-accent', '--color-focus',
    'color.bg', 'color.surface', 'color.fg', 'color.accent', 'color.border',
})


IDENTITY_TYPES = frozenset({'theme', 'style', 'design_system', 'palette', 'font_pairing',
                            'font_family', 'motion_preset'})
NEGATION = re.compile(
    r"\b(?:do not|don't|does not|must not|should not|never|avoid|avoiding|without|no|not)\b"
    r"(?P<scope>[^.;:!?]*?)(?=[.;:!?]|\b(?:but|while|instead|because|prioriti[sz]e)\b|$)")
NEGATED_FILLER = frozenset('''use using introduce introducing add adding any change changing
apply applying include including rely relying want new more extra'''.split())
# A generic head noun stands for its modifier: "dark mode" prohibits dark grounds.
GENERIC_HEADS = frozenset({'mode', 'style', 'styles', 'theme', 'themes', 'effect', 'effects', 'look', 'aesthetic'})
PRIORITY_FIRST = {p: re.compile(rf'\b{p}[- ]first\b') for p in ('desktop', 'mobile')}
PRIORITY_MENTIONS = {
    'desktop': re.compile(r'\b(?:desktop|desktops|pcs?|large monitors?|widescreen)\b'),
    'mobile': re.compile(r'\b(?:mobile|phones?|smartphones?|touch|thumb|one hand|one-handed|tablets?)\b'),
}


def norm(term):
    term = {'colour': 'color', 'colours': 'colors'}.get(term, term)
    return term[:-1] if len(term) > 3 and term.endswith('s') and not term.endswith('ss') else term


EXCLUSIVE_RELIANCE = re.compile(r'\b(?:alone|only|solely|exclusively|sole)\b')


def negation_scopes(text):
    """Split negated phrases into prohibited items and limits on exclusive reliance.

    "Do not use dark mode or glassmorphism" prohibits both items. "Without
    relying on colour alone" limits reliance: colour stays allowed with an
    additional cue. A negated statement about something absent ("no existing
    brand") is neither.
    """
    prohibited, reliance = [], []
    for match in NEGATION.finditer(text.lower()):
        scope = match.group('scope')
        if re.search(r'\b(?:existing|current)\b', scope):
            continue
        for part in re.split(r',|\bor\b|\bnor\b|\band\b', scope):
            if EXCLUSIVE_RELIANCE.match(part.strip()):
                # "do not use glassmorphism, only flat surfaces": a stated alternative, not negated.
                continue
            words = [t for t in terms(part) if t not in FILLER and t not in NEGATED_FILLER
                     and len(t) > 2 and not EXCLUSIVE_RELIANCE.fullmatch(t)]
            if words:
                (reliance if EXCLUSIVE_RELIANCE.search(part) else prohibited).append(tuple(words))
    return prohibited, reliance


def negated_items(text):
    """Explicitly prohibited items, e.g. "do not use dark mode or glassmorphism"."""
    return negation_scopes(text)[0]


def interface_priority(text):
    """Interface priority is distinct from delivery platform (a web UI may be either)."""
    low = text.lower()
    explicit = [p for p, rx in PRIORITY_FIRST.items() if rx.search(low)]
    if len(explicit) == 1:
        return explicit[0]
    mentioned = [p for p, rx in PRIORITY_MENTIONS.items() if rx.search(low)]
    return mentioned[0] if len(mentioned) == 1 else None


IDENTITY_GROUPS = ('direction', 'palette', 'typography')
# Words naming part of a visual identity, mapped to the build groups they cover.
IDENTITY_OBJECTS = (
    (re.compile(r'\b(?:identity|brand|branding|theme|design[- ]system|tokens|aesthetic|look and feel)\b'),
     IDENTITY_GROUPS),
    (re.compile(r'\b(?:style|styling|component library|components)\b'), ('direction',)),
    (re.compile(r'\b(?:palette|colou?rs?)\b'), ('palette',)),
    (re.compile(r'\b(?:fonts?|typography|typefaces?)\b'), ('typography',)),
)
PRESERVE_CUES = re.compile(r'\b(?:keep|keeping|preserve|preserving|retain|retaining|maintain|maintaining|'
                           r'reuse|reusing|established|unchanged)\b')
REQUEST_CUES = re.compile(r'\b(?:create|design|choose|pick|propose|suggest|new|redesign|rebrand|restyle|refresh)\b')
CLAUSE_SPLIT = re.compile(r'[.;!?]|\bwhile\b|\bbut\b')
PLATFORM_LABELS = {
    'web': {'web', 'svg'},
    'mobile': {'mobile', 'ios/android/react native', 'native', 'ios', 'android'},
    'desktop': {'desktop'},
}
# Framework labels name code-level guidance, not a delivery platform.
FRAMEWORK_LABELS = {'react/next.js': re.compile(r'\b(?:react|next\.?js)\b'),
                    'react': re.compile(r'\breact\b')}


def identity_groups(text):
    found = set()
    for rx, groups in IDENTITY_OBJECTS:
        if rx.search(text):
            found.update(groups)
    return found


def identity_intent(task, prohibited):
    """Identity groups the task protects or explicitly asks for.

    Protection needs an explicit cue ("keep the current theme", "do not
    introduce new colours"); merely improving an existing UI is not enough.
    """
    preserved, requested = set(), set()
    for clause in CLAUSE_SPLIT.split(task.lower()):
        named = identity_groups(clause)
        if not named:
            continue
        if PRESERVE_CUES.search(clause):
            preserved.update(named)
        elif REQUEST_CUES.search(clause) and not NEGATION.search(clause):
            requested.update(named)
    for item in prohibited:
        preserved.update(identity_groups(' '.join(item)))
    return preserved - requested, requested


def compound_only_terms(task):
    """Hyphenated compounds ("help-desk", "first-run") whose parts occur nowhere else.

    Such parts only count for records containing the whole phrase; interface
    priorities ("desktop-first") are interpreted separately.
    """
    low = str(task).lower()
    compounds = [m.group(0) for m in re.finditer(r'\b[a-z0-9]+(?:-[a-z0-9]+)+\b', low)
                 if not any(rx.fullmatch(m.group(0)) for rx in PRIORITY_FIRST.values())]
    standalone = re.sub(r'\b[a-z0-9]+(?:-[a-z0-9]+)+\b', ' ', low)
    elsewhere = set(terms(standalone))
    result = {}
    for compound in compounds:
        parts = tuple(terms(compound.replace('-', ' ')))
        only = frozenset(t for t in parts if t not in elsewhere)
        if only:
            result[' '.join(parts)] = only
    return result


def contextual_ambiguous_terms(task):
    """Ambiguous words that the task uses in an interface sense ("help center")."""
    tokens = re.findall(r'[a-z0-9]+', str(task).lower())
    keep = set()
    for i, token in enumerate(tokens):
        if token in AMBIGUOUS_TERMS:
            neighbours = set(tokens[max(0, i - 1):i]) | set(tokens[i + 1:i + 2])
            if neighbours & (INTERFACE_NOUNS | {'inline', 'contextual', 'onboarding'}):
                keep.add(token)
    return keep


def analyse_task(task):
    prohibited, reliance = negation_scopes(task)
    preserved, requested = identity_intent(task, prohibited)
    return {
        'prohibited': prohibited,
        'reliance': reliance,
        'priority': interface_priority(task),
        'preserved': preserved,
        'requested': requested,
        'frameworks': frozenset(label for label, rx in FRAMEWORK_LABELS.items() if rx.search(task.lower())),
        'ambiguous_kept': contextual_ambiguous_terms(task),
        'compounds': compound_only_terms(task),
    }


def query_terms(task, signals=None):
    """Avoid inferring a style from generic compliments alone."""
    signals = signals or {}
    text = PRIORITY_FIRST['desktop'].sub('desktop', str(task).lower())
    excluded = {t for item in signals.get('prohibited', ()) for t in item}
    excluded |= PLATFORM_CONTEXT
    excluded |= AMBIGUOUS_TERMS - set(signals.get('ambiguous_kept', AMBIGUOUS_TERMS))
    found = []
    for term in terms(text):
        if term not in FILLER and len(term) > 2 and term not in excluded:
            found.extend(terms(ALIASES.get(term, term)))
    return list(dict.fromkeys(found))


def contextual_fields(signals):
    """Positive fields, crediting compound-only query parts only where the record has the phrase."""
    compounds = signals.get('compounds') or {}
    if not compounds:
        return positive_fields

    def fields(entry):
        tokens = positive_fields(entry)
        text = ' ' + ' '.join(terms(_positive_text(entry).replace('-', ' '))) + ' '
        drop = set()
        for phrase, only in compounds.items():
            if f' {phrase} ' not in text:
                drop |= only
        return [t for t in tokens if t not in drop] if drop else tokens
    return fields


def _positive_text(entry):
    return ' '.join([str(entry.get('original_name', '')), ' '.join(map(str, entry.get('keywords', []))),
                     str(entry.get('description', ''))]).lower()


def _avoid_text(entry):
    return ' '.join(str(c) for c in entry.get('compatibility_restrictions', [])
                    if str(c).lower().startswith('avoid')).lower()


def conflicts_with_task(entry, signals):
    """Explicit conflicts only: the record advocates what the task rules out."""
    priority = signals.get('priority')
    if priority:
        other = 'mobile' if priority == 'desktop' else 'desktop'
        name_terms = set(terms(entry.get('original_name', '')))
        if (PRIORITY_FIRST[other].search(_positive_text(entry)) or other in name_terms
                or PRIORITY_FIRST[priority].search(_avoid_text(entry))):
            return True
    if entry.get('entry_type') in IDENTITY_TYPES and signals.get('prohibited'):
        present = {norm(t) for t in terms(_positive_text(entry))}
        for item in signals['prohibited']:
            needed = [norm(t) for t in item if not (len(item) > 1 and t in GENERIC_HEADS)]
            if needed and all(t in present for t in needed):
                return True
    return False


def compatible(entry, platform, priority=None, frameworks=frozenset()):
    """Delivery-platform fit; source labels such as "iOS/Android/React Native"
    are normalized. A mobile-priority web interface may use mobile guidance."""
    if not platform:
        return True
    platforms = {str(p).casefold() for p in entry.get('platforms', [])}
    # Missing platform metadata still requires the AI to check real fit.
    if not platforms or 'all' in platforms or platform in platforms:
        return True
    if platforms & PLATFORM_LABELS[platform]:
        return True
    if platform == 'web' and platforms & frameworks:
        return True
    return platform == 'web' and priority == 'mobile' and 'mobile' in platforms


def exact_tokens(entry, max_items=10):
    """Copy a few exact color-role values, never synthesize code or media."""
    tree = entry.get('design_tokens')
    if not isinstance(tree, dict):
        return {}
    flat = {}

    def descend(data, prefix='', depth=0):
        if depth > 5:
            return
        for key, value in data.items():
            name = f'{prefix}.{key}' if prefix else str(key)
            if isinstance(value, dict):
                descend(value, name, depth + 1)
            elif isinstance(value, (str, int, float)) and not isinstance(value, bool):
                if len(str(value)) <= 180:
                    flat[name] = value

    descend(tree)
    selected = {k: v for k, v in flat.items() if k in TOKEN_ROLES}
    return dict(list(selected.items())[:max_items])


def reference(role, entry, score):
    result = {
        'role': role,
        'catalog_id': entry['catalog_id'],
        'entry_type': entry['entry_type'],
        'original_name': entry['original_name'],
        'description': entry.get('description', ''),
        'source_repo': entry['source_repo'],
        'source_ref': entry['source_ref'],
        'source_url': entry['source_url'],
        'source_path_or_key': entry['source_path_or_key'],
        'evidence_status': entry.get('evidence_status'),
        'redistribution_status': entry.get('redistribution_status'),
        'asset_license_status': entry.get('asset_license_status'),
        'platforms': entry.get('platforms', []),
        'compatibility_restrictions': entry.get('compatibility_restrictions', []),
        'relevance_score': score,
    }
    token_excerpt = exact_tokens(entry)
    if token_excerpt:
        result['source_tokens_excerpt'] = token_excerpt
    return result


def recommend(task, entries, mode='build', platform=None, limit=3):
    """Return a small topical shortlist, not approved design decisions."""
    if mode not in GROUPS:
        raise ValueError('unsupported mode')
    if platform not in {None, 'web', 'mobile', 'desktop'}:
        raise ValueError('unsupported platform')
    if not 1 <= limit <= 5:
        raise ValueError('limit must be between 1 and 5')
    signals = analyse_task(task)
    words = query_terms(task, signals)
    lowered = str(task).lower()
    non_visual = bool(NON_VISUAL_CUES.search(lowered) and not UI_CUES.search(lowered))
    if non_visual:
        words = []
    selected = []
    task_words = set(terms(task))
    focused_a11y_fix = bool(
        mode == 'build'
        and task_words.intersection(FOCUSED_ACCESSIBILITY_CUES)
        and task_words.intersection(CORRECTION_CUES)
        and not task_words.intersection(NEW_DESIGN_CUES)
        and not task_words.intersection(EXPLICIT_STYLE_CUES)
    )
    preserved = signals['preserved']
    visual_direction = mode != 'critique' or bool(VISUAL_DIRECTION_CUES.search(lowered))
    scope = ('non_visual_task' if non_visual
             else 'focused_accessibility_correction' if focused_a11y_fix else 'normal')
    if words:
        groups = ([('usability_reference', ('guideline',))] if focused_a11y_fix
                  else list(GROUPS[mode]))
        if mode == 'build' and not focused_a11y_fix and set(words).intersection(AUDIT_CUES):
            # Keep accessibility inside the default three-result budget.
            groups.insert(2, ('usability_reference', ('guideline',)))
        if preserved and not focused_a11y_fix:
            # A protected identity is not replaced; component and usability guidance still applies.
            kept = [g for g in groups if not (
                (g[0] in IDENTITY_GROUPS and g[0] in preserved)
                or (g[0] == 'design_reference' and 'direction' in preserved))]
            if not any(role in IDENTITY_GROUPS or role == 'design_reference' for role, _ in kept):
                scope = 'preserve_identity'
                kept = [g for g in kept if g[0] == 'usability_reference'] or [('usability_reference', ('guideline',))]
            groups = kept
        if not visual_direction:
            # Usability and operational critiques need no replacement-theme reference.
            groups = [g for g in groups if g[0] != 'design_reference']
        # Guideline-only shortlists fill the budget with further strong guidelines.
        fill = (not focused_a11y_fix and len(groups) == 1
                and groups[0][0] in ('usability_reference', 'check_reference'))
        fields = contextual_fields(signals)
        for role, types in groups:
            if role == 'usability_reference':
                uses = {'audit', 'critique', 'multiple'}
            elif mode == 'critique':
                uses = {'build', 'critique', 'multiple'}
            else:
                uses = {mode, 'multiple'}
            pool = [e for e in entries
                    if e.get('entry_type') in types
                    and e.get('evidence_status') == 'source_inspected'
                    and e.get('specialist_use') in uses
                    and compatible(e, platform, signals['priority'], signals['frameworks'])
                    and not conflicts_with_task(e, signals)]
            ranked = rank_entries(' '.join(words), pool, limit=limit if fill else 1, fields=fields)
            if role == 'design_reference':
                # A visual reference needs more than one incidental word in common with the task.
                ranked = [(s, e) for s, e in ranked if len(set(words) & set(fields(e))) >= 2]
            if ranked:
                top = ranked[0][0]
                for score, entry in ranked:
                    if score >= FILL_MIN_SHARE * top and len(selected) < limit:
                        selected.append(reference(role, entry, score))
            if len(selected) >= limit:
                break
    return {
        'task': task,
        'mode': mode,
        'platform': platform or 'unspecified',
        'catalog_records_searched': len(entries),
        'selection_scope': scope,
        'task_signals': {
            'interface_priority': signals['priority'],
            'prohibited': [' '.join(item) for item in signals['prohibited']],
            'preserved_identity': [g for g in IDENTITY_GROUPS if g in preserved],
            'requested_identity': [g for g in IDENTITY_GROUPS if g in signals['requested']],
            'not_sole_reliance': [' '.join(item) for item in signals['reliance']],
        },
        'references': selected,
        'selection_method': 'heuristic text matching; not design or legal approval',
        'use_boundary': (
            'Suggestions are optional and unapproved. Existing project identity, '
            'design system, behavior, and applicable AIPF authorization take priority. '
            'Do not copy third-party fonts, photos, icons, branded assets or code '
            'based on metadata. Confirm source rights and actual access. Inspect '
            'the rendered UI before claiming visual acceptance. This command does '
            'not build, modify, install, deploy, or verify an interface.'
        ),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('task', help='Normal language UI request from user')
    parser.add_argument('--mode', choices=GROUPS, default='build')
    parser.add_argument('--platform', choices=['web', 'mobile', 'desktop'])
    parser.add_argument('--limit', type=int, default=3, help='Maximum results, 1–5')
    args = parser.parse_args()
    if not 1 <= args.limit <= 5:
        parser.error('--limit must be between 1 and 5')
    if not args.task.strip():
        parser.error('task must not be empty')
    entries = load_catalog()
    if not entries:
        # An absent catalog must never look like an empty recommendation.
        parser.exit(1, 'error: catalog entries not found\n')
    print(json.dumps(recommend(args.task, entries, args.mode,
                               args.platform, args.limit), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
