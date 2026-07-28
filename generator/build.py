#!/usr/bin/env python3
"""Build all lesson pages for The AI Search Playbook.

Usage:  python3 generator/build.py   (from the playbook/ repo root)

Reads generator/content/m0..m4.py, renders each lesson through
generator/chrome.py, writes public/lessons/<slug>/index.html, and
regenerates public/sitemap.xml, public/robots.txt and public/llms.txt.
"""
import os
import sys
import importlib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PUB = os.path.join(ROOT, "public")
sys.path.insert(0, HERE)

import chrome  # noqa: E402

modules = []
for name in ["m0", "m1", "m2", "m3", "m4"]:
    mod = importlib.import_module(f"content.{name}")
    modules.append(mod.LESSONS)

ALL = [l for m in modules for l in m]

# --- lesson pages ---
for i, l in enumerate(ALL):
    prev_l = ALL[i - 1] if i > 0 else None
    next_l = ALL[i + 1] if i < len(ALL) - 1 else None
    html = chrome.render_lesson(l, prev_l, next_l)
    outdir = os.path.join(PUB, "lessons", l["slug"])
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "index.html"), "w") as f:
        f.write(html)
    print(f"  built {l['id']}  {l['slug']}")

# --- sitemap ---
urls = [f"{chrome.SITE}/"] + [f"{chrome.SITE}/lessons/{l['slug']}/" for l in ALL]
sm = ['<?xml version="1.0" encoding="UTF-8"?>',
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u in urls:
    sm.append(f"  <url><loc>{u}</loc></url>")
sm.append("</urlset>\n")
with open(os.path.join(PUB, "sitemap.xml"), "w") as f:
    f.write("\n".join(sm))

# --- robots.txt: every door open, AI crawlers explicitly welcome ---
robots = """# The AI Search Playbook — teamempathy.co.nz
# We teach stores to open the doors to AI crawlers. Ours are open.

User-agent: *
Allow: /

User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

Sitemap: https://playbook.teamempathy.co.nz/sitemap.xml
"""
with open(os.path.join(PUB, "robots.txt"), "w") as f:
    f.write(robots)

# --- llms.txt ---
lines = ["# The AI Search Playbook for Ecommerce",
         "",
         "> A free, self-paced course by Team Empathy (teamempathy.co.nz), the Auckland",
         "> AI search agency. It teaches Shopify ecommerce stores how to become the brand",
         "> AI recommends: technical foundations, content, authority and measurement.",
         "> 31 lessons across 5 modules. All lessons are free and open.",
         "",
         "## Lessons",
         ""]
for l in ALL:
    lines.append(f"- [{l['id']} {l['title']}]({chrome.SITE}/lessons/{l['slug']}/): {l['description']}")
lines += ["", "## About",
          "- [Team Empathy](https://teamempathy.co.nz): Search & AI visibility for ecommerce. We make Shopify brands the brand AI recommends.", ""]
with open(os.path.join(PUB, "llms.txt"), "w") as f:
    f.write("\n".join(lines))

print(f"\nBuilt {len(ALL)} lessons + sitemap.xml + robots.txt + llms.txt")
