"""Build three static resume layouts from shared, evidence-based project copy."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CONTACT = '''<div class="contact"><a href="mailto:ianjamesburke@gmail.com">ianjamesburke@gmail.com</a><a href="https://ianjamesburke.github.io">ianjamesburke.github.io</a><a href="https://github.com/ianjamesburke">github.com/ianjamesburke</a></div>'''
HEADER = f'''<header><h1>Ian Burke</h1><p class="role">Software Engineer &middot; AI Integration</p>{CONTACT}</header>'''
SUMMARY = '''<p class="summary">I build AI applications, data pipelines, and tools for working with coding agents. My work covers the interface, integrations, and backend. I came to software through video production.</p>'''
EXPERIENCE = '''<section class="experience"><h2>Experience</h2>
<div class="job"><div><p class="title">Davenport University</p><p class="position">AI Integration Specialist</p></div><span class="date">Current</span></div>
<div class="job"><div><p class="title">Narrative Ads</p><p class="position">Freelance Software Engineer</p></div><span class="date">2022 &ndash; Present</span></div>
<div class="job"><div><p class="title">Narrative Ads</p><p class="position">Video Producer &amp; Editor</p></div><span class="date">2018 &ndash; 2022</span></div>
</section>'''
SKILLS = '''<section class="skills"><h2>Technical Skills</h2><p>Python, TypeScript, JavaScript, Rust &middot; React / Next.js, SvelteKit, FastAPI &middot; Firebase, Google Cloud, SQLite &middot; AI integrations, structured extraction, agent workflows</p></section>'''
PROJECTS = [
    {
        "name": "NarratorAI", "subtitle": "AI media tools for Narrative Ads",
        "url": "https://ianjamesburke.github.io/narrator-ai.html",
        "image": "images/narrator-ai-video-review.png", "crop": True,
        "alt": "Narrative video-review interface with upload states and AI review badges",
        "copy": "Build and maintain AI media tools and ad analytics for Narrative Ads. Develop provider integrations, investigate generation failures, and report on infrastructure costs.",
        "long": "I work across the interface, provider integrations, and cloud backend. That includes image, video, and voiceover workflows, generation-failure investigation, capacity changes, and monthly provider-cost reports.",
        "intro": "An internal application for media production and advertising analytics. The review queue keeps uploads, variants, and review states together.",
        "stack": "TypeScript &middot; Next.js &middot; Firebase &middot; Gemini &middot; fal.ai",
        "status": "Client work / Ongoing development and operations",
        "role": "Freelance Software Engineer",
    },
    {
        "name": "PLEXI", "subtitle": "A desktop workspace for coding agents",
        "url": "https://plexiapp.com", "image": "images/plexi-workspace.png", "crop": False,
        "alt": "PLEXI project contexts, editor, and terminal panes",
        "copy": "Built my daily workspace for coding agents, with terminal panes, project contexts, a CLI, and a WASM app runtime.",
        "intro": "I wanted terminals, project context, and small tools in the same place while working with coding agents. PLEXI is the desktop application I built for that workflow.",
        "long": "The Rust host manages panes and project contexts. An agent-accessible CLI exposes workspace controls, and a WASM runtime supports apps. I use it daily and keep developing it as my workflow changes.",
        "stack": "Rust &middot; egui &middot; Wasmtime",
        "status": "Open source / macOS pre-release",
        "role": "Creator &amp; Developer",
    },
    {
        "name": "Kill Tony Archive", "subtitle": "From long recordings to browsable data",
        "url": "https://killtonyarchive.com", "image": "images/kill-tony-sets.png", "crop": False,
        "alt": "Kill Tony Archive score distribution and browsable set rankings",
        "copy": "Built an audio-to-data pipeline and web app. Separates transcription from analysis and cleans up duplicate records. The September 2026 local dataset holds 1,422 sets across 110 episodes.",
        "intro": "A pipeline that turns long podcast recordings into transcripts and structured records, with a web interface for exploring the results.",
        "long": "I built separate transcription and analysis stages, transcript deduplication, and speaker normalization. The application adds rankings, voting, and shareable stat cards. The September 2026 local dataset contains 1,422 set records across 110 episodes.",
        "stack": "Python &middot; Gemini &middot; SQLite &middot; FastAPI &middot; SvelteKit",
        "status": "Independent project / AI data pipeline and web application",
        "role": "Creator &amp; Developer",
    },
]


def figure(project, extra=""):
    classes = extra + (" video-review-crop" if project["crop"] else "")
    return f'<figure class="{classes.strip()}"><img src="{project["image"]}" alt="{project["alt"]}"></figure>'


def document(title, variant, pages, filename):
    articles = "".join(f'<article class="page {variant}">{body}</article>' for body in pages)
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ian Burke | {title}</title><link rel="stylesheet" href="portfolio-options.css"><link rel="stylesheet" href="video-review-crop.css"></head>
<body><nav class="toolbar" aria-label="Resume options"><a href="portfolio-options.html">&larr; Compare versions</a><a href="index.html">Portfolio site</a><a class="download" href="{filename}.pdf" download>Download PDF</a></nav><main>{articles}</main></body></html>'''


rows = "".join(f'''<article class="project">{figure(p)}<div><h3><a href="{p['url']}">{p['name']}</a></h3><p>{p['copy']}</p><p class="detail">{p['stack']}{' &middot; macOS pre-release' if p['name'] == 'PLEXI' else ''}</p></div></article>''' for p in PROJECTS)
compact = HEADER + SUMMARY + EXPERIENCE + '<section><h2>Selected Work</h2>' + rows + '</section>' + SKILLS
(ROOT / 'portfolio-option-1.html').write_text(document('Compact visual resume', 'compact', [compact], 'Ian-Burke-Option-1'))

work_pages = []
for p in PROJECTS:
    body = f'''<header class="small-header"><a href="https://ianjamesburke.github.io"><strong>Ian Burke</strong></a><a href="mailto:ianjamesburke@gmail.com">ianjamesburke@gmail.com</a></header>
<h1 class="case-title">{p['name']}</h1><p class="case-subtitle">{p['subtitle']}</p>
{figure(p, 'wide-image')}
<div class="case-copy"><p>{p['intro']}</p><p>{p['long']}</p></div>
<footer class="case-meta"><div><p><strong>{p['role']}</strong></p><p>{p['stack']}</p><p>{p['status']}</p></div><a href="{p['url']}">View project &nearr;</a></footer>'''
    work_pages.append(body)
(ROOT / 'portfolio-option-2.html').write_text(document('Project showcase', 'work-first', work_pages, 'Ian-Burke-Option-2'))

p = PROJECTS[0]
balanced_first = HEADER + SUMMARY + EXPERIENCE + f'''<section><h2>Client Work</h2><h3 class="case-title"><a href="{p['url']}">{p['name']}</a></h3><p class="project-copy">{p['copy']}</p>{figure(p, 'wide-image')}</section>''' + SKILLS
balanced_second = '''<header class="small-header"><a href="https://ianjamesburke.github.io"><strong>Ian Burke</strong></a><span>Selected independent projects</span></header>'''
for p in PROJECTS[1:]:
    balanced_second += f'''<section class="personal-project"><h2 class="case-title"><a href="{p['url']}">{p['name']}</a></h2><p class="case-subtitle">{p['subtitle']}</p><div class="project-split">{figure(p)}<div><p>{p['intro']}</p><p>{p['copy'] if p['name'] != 'PLEXI' else 'A Rust host with pane and project-context controls, an agent-accessible CLI, and a WASM app runtime.'}</p><p class="detail">{p['stack']}<br>{p['status']}</p></div></div></section>'''
balanced_second += '<footer class="page-note">' + CONTACT + '</footer>'
(ROOT / 'portfolio-option-3.html').write_text(document('Two-page visual resume', 'balanced', [balanced_first, balanced_second], 'Ian-Burke-Option-3'))

print('Built portfolio-option-1.html, portfolio-option-2.html, portfolio-option-3.html')
