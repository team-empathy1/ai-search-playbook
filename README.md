# The AI Search Playbook — live course site

Self-paced course hub for ecommerce stores building AI search visibility. Built on the
Team Empathy design system (light brand, `course/playbook` template). Static site, no build
step, deployable to Cloudflare Pages at **playbook.teamempathy.co.nz**.

## Structure

```
playbook/
└── public/                 # ← deploy this folder (Cloudflare Pages output dir)
    ├── index.html          # the course hub (data-driven: edit the ACTS array in <script>)
    ├── ds/                 # design system (copied from .claude/skills/team-empathy-design)
    │   ├── styles.css      # entry point — @imports tokens + components/ui.css
    │   ├── tokens/         # colours, type, spacing, fonts, base
    │   ├── components/ui.css
    │   └── assets/fonts/   # self-hosted woff2
    └── img/                # logos (forest / white / navy) + chart-sprout illustration
```

## Editing content

**Lesson pages are generated.** All 31 lessons' content lives in `generator/content/m0.py`
through `m4.py` (one file per module). Edit the content there, then rebuild:

```bash
python3 generator/build.py
```

That emits every `public/lessons/<slug>/index.html` (pure static HTML, no JS needed for
content — AI crawlers don't run JavaScript), plus `sitemap.xml`, `robots.txt` and `llms.txt`.
Shared page chrome (nav, styles, footer, JSON-LD, mark-complete) lives in `generator/chrome.py`.

Each lesson dict: `id, slug, title, h1, description, tag, mins, lead, body (HTML), donow
(list), prompt (optional Claude prompt), app (show the app-coming-soon chip)`.

**The hub** (`public/index.html`) holds the module/lesson index in its `ACTS` array — keep it
in sync with the generator content when adding lessons. Lesson completion persists per-browser
in `localStorage` (`te_playbook_state_v1`), shared between hub and lesson pages.

## Preview locally

```bash
python3 -m http.server 4321 --directory "playbook/public"
# → http://localhost:4321
```
(Or use the Claude Code preview: config is in `.claude/launch.json`, server name `playbook`.)

## Deploy to Cloudflare Pages

Two routes — pick one:

**A. Direct upload (fastest, no GitHub):**
```bash
npx wrangler pages deploy "playbook/public" --project-name=te-playbook
# needs CLOUDFLARE_API_TOKEN + CLOUDFLARE_ACCOUNT_ID in env
```
Then in the Cloudflare dashboard: Pages → te-playbook → Custom domains → add
`playbook.teamempathy.co.nz` (Cloudflare adds the CNAME automatically if the zone is on Cloudflare).

**B. GitHub auto-deploy (living document, matches the AI OS direction):**
Push this folder to a public repo, connect it in Cloudflare Pages with output dir `playbook/public`.
Every commit redeploys. SOP markdown files can live alongside and the hub links to their raw URLs.

## Design system note

`ds/` is a **copy** of the design skill at `.claude/skills/team-empathy-design`. If the brand
tokens change there, re-copy `tokens/`, `components/ui.css`, `styles.css` and the fonts.
