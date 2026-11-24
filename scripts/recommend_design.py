#!/usr/bin/env python3
"""Optional, read-only UI reference lookup for a coding AI.

Invoked by a skill-aware agent for the user's normal UI request. It neither
edits a project nor installs tools, approves designs, or grants asset rights.
"""
import argparse
import json

if __package__:
    from .search_catalog import load_catalog, rank_entries, terms
else:
    from search_catalog import load_catalog, rank_entries, terms

FILLER = frozenset('''build create make design redesign improve update fix website webapp app
application page pages screen screens interface interfaces ui ux for a an the and to
of that this with using use want need needs me my please modern beautiful professional
clean good great nice looking look new existing current project product responsive
'''.split())
ALIASES = {'finance': 'financial', 'fintech': 'financial', 'ecommerce': 'e-commerce',
           'shop': 'ecommerce', 'docs': 'documentation', 'a11y': 'accessibility'}
AUDIT_CUES = frozenset({'accessible', 'accessibility', 'keyboard', 'focus',
                        'contrast', 'navigation', 'mobile', 'touch', 'readability',
                        'readable', 'legibility', 'wcag'})
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
TOKEN_ROLES = frozenset({
    'Primary', 'Secondary', 'Accent', 'Background', 'Foreground',
    'Card', 'Card Foreground', 'Muted Foreground', 'Border', 'Ring',
    '--color-paper', '--color-ink', '--color-accent', '--color-focus',
    'color.bg', 'color.surface', 'color.fg', 'color.accent', 'color.border',
})


def query_terms(task):
    """Avoid inferring a style from generic compliments alone."""
    found = []
    for term in terms(task):
        if term not in FILLER and len(term) > 2:
            found.extend(terms(ALIASES.get(term, term)))
    return list(dict.fromkeys(found))


def compatible(entry, platform):
    if not platform:
        return True
    platforms = {str(p).casefold() for p in entry.get('platforms', [])}
    # Missing platform metadata still requires the AI to check real fit.
    return not platforms or 'all' in platforms or platform in platforms


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
    words = query_terms(task)
    selected = []
    if words:
        groups = list(GROUPS[mode])
        if mode == 'build' and set(words).intersection(AUDIT_CUES):
            # Keep accessibility inside the default three-result budget.
            groups.insert(2, ('usability_reference', ('guideline',)))
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
                    and compatible(e, platform)]
            ranked = rank_entries(' '.join(words), pool, limit=1)
            if ranked:
                score, entry = ranked[0]
                selected.append(reference(role, entry, score))
            if len(selected) >= limit:
                break
    return {
        'task': task,
        'mode': mode,
        'platform': platform or 'unspecified',
        'catalog_records_searched': len(entries),
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
    print(json.dumps(recommend(args.task, load_catalog(), args.mode,
                               args.platform, args.limit), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
