'use strict';
const $ = (id) => document.getElementById(id);
const state = { view: 'explore', type: '', query: '', entries: [], total: null, dataset: null, byId: new Map(), active: null, lastFocus: null, requestNo: 0, hasMore: false };
const KEY = 'aipf-design-index-saved-v1';
let saved;
try { saved = new Set(JSON.parse(localStorage.getItem(KEY) || '[]')); } catch { saved = new Set(); }
const allowedColor = /^(#[0-9a-fA-F]{3,8}|oklch\([\d.]+%?\s+[\d.]+\s+[\d.]+(?:\s*\/\s*[\d.]+%?)?\)|rgba?\([\d.,%\s]+\))$/;
const cleanColor = (val, fallback) => typeof val === 'string' && allowedColor.test(val.trim()) ? val.trim() : fallback;
const categoryNames = {theme:'Theme', palette:'Palette', design_system:'Design system', style:'Style', font_pairing:'Typography', guideline:'UX guidance'};
const repoShort = { 'Nutlope/hallmark':'Hallmark', 'nextlevelbuilder/ui-ux-pro-max-skill':'UI UX Pro Max', 'feimacode/open-design-agent-kit':'Open Design Kit' };
const bookmarkSvg = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M6 4.75h12v15.5l-6-4.15-6 4.15V4.75Z"/></svg>';
function create(tag, className='', txt) { const el=document.createElement(tag); if(className) el.className=className; if(txt!==undefined) el.textContent=txt; return el; }
function savePersist() { try { localStorage.setItem(KEY, JSON.stringify([...saved])); } catch {} $('savedCount').textContent=String(saved.size); }
function tokensFor(entry) {
  const t=entry.design_tokens || {};
  if(entry.entry_type==='palette') return {paper:cleanColor(t.Background,'#f5f1e9'),ink:cleanColor(t.Foreground,'#27352a'),accent:cleanColor(t.Accent,'#487b58'),surface:cleanColor(t.Card,'#fff')};
  if(entry.entry_type==='theme') return {paper:cleanColor(t['--color-paper'],'#eef0e9'),ink:cleanColor(t['--color-ink'],'#283629'),accent:cleanColor(t['--color-accent'],'#6d966c'),surface:'#fff'};
  if(entry.entry_type==='design_system') {const c=t.color || {};return {paper:cleanColor(c.bg,'#f4f4ef'),ink:cleanColor(c.fg,'#27332b'),accent:cleanColor(c.accent,'#487b58'),surface:cleanColor(c.surface,'#fff')};}
  return {paper:'#eaf0e7',ink:'#2b4533',accent:'#487f58',surface:'#f6f8f4'};
}
function preview(entry) {
  const col=tokensFor(entry), type=entry.entry_type;
  const art=create('div','card-art art-'+(type==='design_system'?'system':type==='font_pairing'?'typography':type==='guideline'?'guideline':type));
  art.setAttribute('aria-hidden','true');
  for(const [k,v] of Object.entries({'--paper':col.paper,'--ink':col.ink,'--accent':col.accent,'--surface':col.surface})) art.style.setProperty(k,v);
  if(type==='theme') {let h=create('div','art-masthead'); h.append(create('span','', 'DESIGN / '));h.append(document.createTextNode(entry.original_name.length>15?entry.original_name.slice(0,15):entry.original_name));art.append(h,create('div','art-rule'),create('div','art-accent')); let ls=create('div','art-lines');ls.append(create('i'),create('i'),create('i'));art.append(ls);}
  else if(type==='palette') {let p=create('div','art-palette'); [col.paper,col.ink,col.accent,col.surface].forEach(c=>{let x=create('span');x.style.background=c;p.append(x);});art.append(p,create('div','art-palette-label','Color study / 04'));}
  else if(type==='design_system') {let panel=create('div','art-system'),top=create('div','sys-top');top.append(create('div','sys-circle'),create('div','sys-mini'));let con=create('div','sys-content'),side=create('div','sys-side');side.append(create('i'),create('i'),create('i'));con.append(create('div','sys-primary'),side);panel.append(top,con);art.append(panel);}
  else if(type==='font_pairing'){art.append(create('span','', 'Aa'),create('small','','TYPE STUDY / 01'));}
  else if(type==='guideline'){let frame=create('div','guideline-frame');frame.append(create('div','guide-control'),create('div','guide-line'));art.append(frame);}
  else {art.append(create('strong','',entry.original_name));}
  return art;
}
function card(entry) {
  const root=create('article','ref-card');root.dataset.id=entry.catalog_id;
  root.append(preview(entry));
  const body=create('div','card-body'), top=create('div','card-top');
  top.append(create('span','card-kind',categoryNames[entry.entry_type]||entry.entry_type));
  const save=create('button','save-btn'+(saved.has(entry.catalog_id)?' saved':''));save.type='button';save.innerHTML=bookmarkSvg;save.setAttribute('aria-label', (saved.has(entry.catalog_id)?'Remove saved reference: ':'Save reference: ')+entry.original_name);save.setAttribute('aria-pressed',String(saved.has(entry.catalog_id)));save.addEventListener('click',()=>toggleSave(entry.catalog_id));top.append(save);
  body.append(top,create('h3','card-name',entry.original_name),create('p','card-desc',entry.description));
  const bottom=create('div','card-bottom');bottom.append(create('span','card-source',repoShort[entry.source_repo]||entry.source_repo));const inspect=create('button','inspect-btn','Inspect ↗');inspect.type='button';inspect.setAttribute('aria-label','Inspect '+entry.original_name);inspect.addEventListener('click',()=>openDrawer(entry,inspect));bottom.append(inspect);body.append(bottom);root.append(body);return root;
}
function toggleSave(id){if(saved.has(id)) saved.delete(id);else saved.add(id);savePersist();if(state.view==='saved')load();else {for(const btn of document.querySelectorAll('.ref-card[data-id] .save-btn')){const c=btn.closest('.ref-card'), yes=saved.has(c.dataset.id);btn.classList.toggle('saved',yes);btn.setAttribute('aria-pressed',String(yes));const e=state.byId.get(c.dataset.id);btn.setAttribute('aria-label',(yes?'Remove saved reference: ':'Save reference: ')+(e?.original_name||''));}} if(state.active?.catalog_id===id)updateDrawerSave();}
function updateDrawerSave(){const yes=saved.has(state.active?.catalog_id);$('drawerSave').textContent=yes?'Remove from saved':'Save reference';}
function showView(view){state.view=view;document.querySelectorAll('.nav-item[data-view]').forEach(btn=>{const selected=btn.dataset.view===view;btn.classList.toggle('active',selected);if(selected)btn.setAttribute('aria-current','page');else btn.removeAttribute('aria-current');});$('hero-title').innerHTML=view==='saved'?'A little collection of<br/><em>ideas worth keeping.</em>':'A better place to find<br/><em>your next direction.</em>';$('resultsEyebrow').textContent=view==='saved'?'02 / YOUR SELECTION':'01 / COLLECTION';$('resultsTitle').textContent=view==='saved'?'Saved references':'Selected references';$('resultsDescription').textContent=view==='saved'?'Your references, saved in this browser only.':'A few worthwhile starting points from the unified catalog.';load();}
let debounce;
function searchChanged(){state.query=$('searchInput').value.trim();$('clearSearch').hidden=!state.query;clearTimeout(debounce);debounce=setTimeout(()=>{load()},180);}
function reset(){state.type='';state.query='';$('searchInput').value='';$('clearSearch').hidden=true;setChips();if(state.view==='saved')showView('explore');else load();}
function setChips(){document.querySelectorAll('.chip').forEach(ch=>{let on=ch.dataset.type===state.type;ch.classList.toggle('selected',on);ch.setAttribute('aria-pressed',String(on));});$('moreTypes').value=Array.from($('moreTypes').options).some(o=>o.value===state.type)?state.type:'';}
async function load(more=false){
  if(more && !state.hasMore)return;
  const current=++state.requestNo, params=new URLSearchParams();
  if(state.query)params.set('q',state.query);
  if(state.type)params.set('type',state.type);
  if(state.view==='saved')params.set('ids',[...saved].join(','));
  const offset=more?state.entries.length:0;
  params.set('limit','12');params.set('offset',String(offset));
  $('cards').setAttribute('aria-busy','true');$('loadMore').disabled=true;$('errorState').hidden=true;
  try{
    const response=await fetch('/api/catalog?'+params,{cache:'no-store'});
    if(!response.ok)throw Error('catalog query failed');
    const data=await response.json();if(current!==state.requestNo)return;
    state.entries=more?[...state.entries,...data.results]:data.results;
    state.total=data.total;state.dataset=data.dataset;state.hasMore=data.has_more;
    data.results.forEach(e=>state.byId.set(e.catalog_id,e));render();
    $('sidebarCatalogCount').textContent=`${data.total.toLocaleString()} entries · Full catalog`;
    $('resultCount').textContent=`${state.entries.length.toLocaleString()} of ${data.matches.toLocaleString()} ${data.matches===1?'reference':'references'}`;
    $('resultsDescription').textContent=state.view==='saved'?'Saved on this device':state.query?`Search results for “${state.query}”`:state.type?`Catalog references in ${categoryNames[state.type]||state.type.replaceAll('_',' ')}`:'Browse the unified catalog, with original sources and usage restrictions.';
    $('aboutDataset').textContent=`Full catalog: ${data.total.toLocaleString()} source entries.`;
    $('loadMore').hidden=!data.has_more;
  }catch(err){
    if(current!==state.requestNo)return;
    if(!more){$('cards').replaceChildren();$('emptyState').hidden=true;}
    $('errorState').hidden=false;$('resultCount').textContent='Unavailable';console.error(err);
    $('loadMore').hidden=true;
  }finally{if(current===state.requestNo){$('cards').setAttribute('aria-busy','false');$('loadMore').disabled=false;}}
}
function render(){const frag=document.createDocumentFragment();state.entries.forEach(e=>frag.append(card(e)));$('cards').replaceChildren(frag);$('emptyState').hidden=state.entries.length>0;$('cards').hidden=state.entries.length===0;$('emptyState').querySelector('h3').textContent=state.view==='saved'?'No saved references yet':'No matching references';$('emptyState').querySelector('p').textContent=state.view==='saved'?'Save a few references while exploring the catalog.':'Try another term or choose a broader category.';}
function tokensList(tokens,prefix=''){const out=[];if(!tokens || typeof tokens!=='object')return out;for(const [key,val] of Object.entries(tokens)){if(val && typeof val==='object'&&!Array.isArray(val))out.push(...tokensList(val,prefix?prefix+'.'+key:key));else if(typeof val==='string')out.push([prefix?prefix+'.'+key:key,val]);}return out.slice(0,60);}
function openDrawer(entry, trigger){state.active=entry;state.lastFocus=trigger||document.activeElement;$('drawerPreview').replaceChildren(preview(entry));$('detailType').textContent=categoryNames[entry.entry_type]||entry.entry_type;$('detailTitle').textContent=entry.original_name;$('detailDescription').textContent=entry.description;$('detailSource').textContent=entry.source_repo;$('detailStatus').textContent=entry.evidence_status==='source_inspected'?'Source inspected':'Candidate — not fully verified';$('detailLicense').textContent=entry.redistribution_status==='reference_only'?'Reference only; copying not cleared':'Metadata only; source assets not cleared';let url=entry.source_url;if(!/^https:\/\/github\.com\//.test(url))url='https://github.com';$('detailSourceLink').href=url;
const tok=$('detailTokens');tok.replaceChildren();const list=tokensList(entry.design_tokens);if(list.length){tok.append(create('h3','','AVAILABLE SOURCE TOKENS'));for(const [key,val] of list){const row=create('div','token-row'),sw=create('div','token-swatch');const color=cleanColor(val,'transparent');sw.style.background=color;row.append(sw,create('span','token-name',key),create('span','token-value',val));tok.append(row);}}else tok.append(create('p','drawer-description','No exact tokens in this catalog entry.'));updateDrawerSave();$('drawerBackdrop').hidden=false;$('detailDrawer').hidden=false;$('detailDrawer').setAttribute('aria-hidden','false');document.body.style.overflow='hidden';$('closeDrawer').focus();}
function closeDrawer(){if($('detailDrawer').hidden)return;$('drawerBackdrop').hidden=true;$('detailDrawer').hidden=true;$('detailDrawer').setAttribute('aria-hidden','true');document.body.style.overflow='';state.active=null;state.lastFocus?.focus();}
let aboutFocus;
function openAbout(){aboutFocus=document.activeElement;$('aboutBackdrop').hidden=false;$('aboutDialog').hidden=false;document.body.style.overflow='hidden';$('closeAbout').focus();}
function closeAbout(){$('aboutBackdrop').hidden=true;$('aboutDialog').hidden=true;document.body.style.overflow='';aboutFocus?.focus();}
function trapDialog(e, dialog){const focusables=[...dialog.querySelectorAll('button:not([disabled]),a[href]')].filter(x=>x.offsetParent!==null);if(!focusables.length)return;const first=focusables[0],last=focusables[focusables.length-1];if(e.shiftKey&&document.activeElement===first){e.preventDefault();last.focus();}else if(!e.shiftKey&&document.activeElement===last){e.preventDefault();first.focus();}}
function init(){savePersist();document.querySelectorAll('.nav-item[data-view]').forEach(btn=>btn.addEventListener('click',()=>showView(btn.dataset.view)));document.querySelectorAll('.chip').forEach(btn=>btn.addEventListener('click',()=>{state.type=btn.dataset.type;setChips();load();}));$('moreTypes').addEventListener('change',()=>{state.type=$('moreTypes').value;setChips();load();});$('loadMore').addEventListener('click',()=>load(true));$('searchInput').addEventListener('input',searchChanged);$('clearSearch').addEventListener('click',reset);$('resetButton').addEventListener('click',reset);$('closeDrawer').addEventListener('click',closeDrawer);$('drawerBackdrop').addEventListener('click',closeDrawer);$('drawerSave').addEventListener('click',()=>{if(state.active)toggleSave(state.active.catalog_id)});$('aboutButton').addEventListener('click',openAbout);$('aboutTopButton').addEventListener('click',openAbout);$('closeAbout').addEventListener('click',closeAbout);$('aboutDone').addEventListener('click',closeAbout);$('aboutBackdrop').addEventListener('click',closeAbout);document.addEventListener('keydown',e=>{if(e.key==='Escape'){if(!$('aboutDialog').hidden)closeAbout();else if(!$('detailDrawer').hidden)closeDrawer();return;}if(e.key==='Tab'){if(!$('aboutDialog').hidden)trapDialog(e,$('aboutDialog'));else if(!$('detailDrawer').hidden)trapDialog(e,$('detailDrawer'));}if(e.key==='/'&&document.activeElement.tagName!=='INPUT'&&$('detailDrawer').hidden&&$('aboutDialog').hidden){e.preventDefault();$('searchInput').focus();}});load();}
init();
