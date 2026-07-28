# Module 2 · Become the answer — content engine
LESSONS = [
{
"id": "2.1",
"slug": "2-1-keywords-with-buying-intent",
"title": "Keywords with buying intent",
"h1": 'Keywords with buying <span class="te-editorial">intent</span>',
"description": "Stop guessing what to write. Find the searches with money behind them, and decide what your store actually needs to target across Google and AI.",
"tag": "Content",
"mins": 7,
"lead": "Content without research is a diary. This lesson is how you find the searches with money behind them, so every page you build from here has a job.",
"body": """
    <h2>Coverage beats volume</h2>
    <p>The old game chased the biggest keyword in the category and spent years fighting for it. The new game is different: AI assistants answer thousands of variations of every buying question, and they assemble answers from whoever covers the topic best. Owning a topic thoroughly beats ranking once for its biggest keyword.</p>
    <p>So the research question changes from "what has the most volume" to "what does a buyer ask on the way to buying what I sell, and how much of it do I cover".</p>

    <h2>Mine the sources you already own</h2>
    <p>Before any tool, you're sitting on intent data nobody else has:</p>
    <ul>
      <li><strong>Search Console.</strong> The queries you already show up for (and the ones you show up for on page 3, which are your fastest wins).</li>
      <li><strong>Your store search.</strong> What people type into your own search box is pure, unfiltered demand.</li>
      <li><strong>Support email and chat.</strong> Every pre-purchase question is a keyword phrased as a sentence.</li>
      <li><strong>Ask the AI directly.</strong> Ask ChatGPT what buyers in your category want to know before purchasing. It has read more buyer conversations than any tool.</li>
    </ul>

    <h2>Sort by intent, then by winnability</h2>
    <p>Group everything you find into three buckets:</p>
    <ol>
      <li><strong>Buy now:</strong> "buy", "best", "vs", "for [use case]", price qualifiers. Highest value, target with collections, comparison content and product pages.</li>
      <li><strong>Choosing:</strong> "how to choose", "what size", "is X good for Y". Buying guides and FAQs. This bucket is where AI assistants live.</li>
      <li><strong>Learning:</strong> broader category questions. Worth covering to own the topic, but it feeds the first two buckets rather than converting on its own.</li>
    </ol>
    <p>Then be honest about winnability. Long-tail, specific queries ("waterproof merino beanie for running") are winnable this quarter. Head terms ("beanie") are a two-year campaign. Stack the early wins; they fund the patience for the big ones.</p>

    <h2>The output: a keyword map</h2>
    <p>The deliverable from this lesson is a simple sheet: query, intent bucket, monthly interest (rough is fine), the page that should answer it (existing or to-be-built), and priority. That map is the input for the next lesson, where we cluster it into a content plan.</p>
""",
"donow": [
"Pull your last 90 days of Search Console queries, export your store-search terms, and skim your support inbox for repeated pre-purchase questions. Get it all into one sheet. Don't polish, just collect: next lesson we turn it into a plan.",
],
"prompt": """I sell [what you sell] to [who buys it]. Here's my raw keyword collection: [paste your queries/questions, or attach the sheet].

1) Deduplicate and group them by intent: buy-now, choosing, learning. 2) Flag the 15 with the clearest buying intent. 3) Flag the 10 most winnable long-tail queries for a store my size. 4) Note the questions where an AI assistant (not a web page) is probably answering buyers today. Output as a table: query, intent, winnability, suggested page type.""",
"app": True,
},
{
"id": "2.2",
"slug": "2-2-topic-clusters",
"title": "Topic clusters: map what AI maps",
"h1": 'Topic clusters: map what AI <span class="te-editorial">maps</span>',
"description": "Pillar and spoke architecture for ecommerce: organise your keyword map into clusters so engines and AI see you as the authority on your whole category.",
"tag": "Content",
"mins": 6,
"lead": "Engines and AI models understand topics as webs of related ideas, and they decide who the authority is by seeing who covers the whole web. Clusters are how you build that on purpose.",
"body": """
    <h2>What a cluster is</h2>
    <p>A cluster is one big topic your buyers care about, covered completely: a <strong>pillar page</strong> that owns the broad topic, and <strong>spokes</strong> that each answer one specific question underneath it, all linked together.</p>
    <p>Say you sell natural sleep products. The pillar is a definitive guide to magnesium for sleep. The spokes: glycinate vs citrate, dosage and timing, magnesium for kids, side effects, magnesium vs melatonin. Each spoke links up to the pillar and down to the products. Cover that whole web and you become the entity AI associates with the topic, which is exactly the thesis of this playbook.</p>

    <h2>Build your clusters from the map</h2>
    <p>Take your keyword map from 2.1 and group it:</p>
    <ol>
      <li><strong>Find the natural centres of gravity.</strong> The recurring nouns in your queries are your cluster candidates. You're looking for 3-6 clusters, tied directly to what you sell.</li>
      <li><strong>Assign every query to one cluster.</strong> Queries that fit nowhere are usually a sign of a cluster you haven't noticed, or a topic you shouldn't chase.</li>
      <li><strong>Pick each cluster's pillar.</strong> The broadest "choosing" query usually names it. The pillar targets the topic; the spokes target the questions.</li>
      <li><strong>Sequence by money.</strong> Start with the cluster closest to your bestsellers. Authority you build there converts fastest.</li>
    </ol>

    <h2>The ecommerce twist</h2>
    <p>In ecommerce, your collections are pillars too. A collection page with real guidance copy (lesson 1.5) plus a supporting web of guides and comparisons is the strongest cluster shape there is: the informational spokes catch buyers mid-research, and the links hand them straight to the shelf.</p>
    <p>One rule as you plan: <strong>one page per question.</strong> Two pages chasing the same query split your authority and confuse the engines. If two planned spokes would answer the same question, merge them.</p>
""",
"donow": [
"Group your keyword map into 3-6 clusters. Name each one, pick its pillar, list its spokes, and note which collection and products it feeds. One page per question. That one-sheet is your content plan for the next quarter.",
],
"prompt": """Here's my keyword map: [paste it]. My main collections are: [list them].

Build my cluster plan: 1) 3-6 clusters with names, 2) each cluster's pillar page (and whether an existing collection should play that role), 3) the spokes underneath each, one page per question, 4) which products/collections each spoke should link to, 5) the order to build them for fastest revenue impact. Flag any of my existing pages that already partially cover a spoke and should be upgraded rather than duplicated.""",
"app": True,
},
{
"id": "2.3",
"slug": "2-3-write-for-chunk-retrieval",
"title": "Write for chunk retrieval",
"h1": 'Write for chunk <span class="te-editorial">retrieval</span>',
"description": "AI quotes passages, not pages. Answer-first structure, questions as subheadings, and formatting machines can lift: how to write content that gets cited.",
"tag": "Content",
"mins": 7,
"lead": "AI systems don't read your page top to bottom like a person. They break it into chunks, and they quote the chunk that answers the question. Write for the chunk and you get cited. Write a warm-up essay and you don't.",
"body": """
    <h2>How retrieval actually works</h2>
    <p>When an assistant answers a buying question, it retrieves passages from pages it trusts and assembles them into an answer. The unit of competition has shrunk: it used to be your page against other pages, now it's your paragraph against every other paragraph on the topic.</p>
    <p>A chunk wins when it's self-contained: the question is clear from the text, the answer is direct, and it doesn't depend on the three paragraphs before it to make sense.</p>

    <h2>The answer-first pattern</h2>
    <p>Every section of every page you write from now on:</p>
    <ol>
      <li><strong>The subheading is the question</strong>, phrased how a buyer would ask it. "How much magnesium should I take for sleep?" beats "Dosage considerations".</li>
      <li><strong>The first sentence is the answer.</strong> Direct, specific, quotable on its own.</li>
      <li><strong>Then the evidence:</strong> the caveats, the detail, the numbers, the honest limits. This earns the trust that gets the answer quoted.</li>
    </ol>
    <p>Add a TL;DR box at the top of long pieces: three or four sentences summarising the whole answer. It reads like a courtesy to skimmers, and it's also the easiest chunk on the page for a machine to lift.</p>

    <h2>Formatting machines can parse</h2>
    <ul>
      <li><strong>Short paragraphs</strong>, one idea each. A 12-line paragraph is one blurry chunk; three 4-line paragraphs are three clean ones.</li>
      <li><strong>Real lists and tables.</strong> Steps as numbered lists, comparisons as tables. AI lifts structured content far more readily than prose, and it cites original stats 22% more often and quotations 37% more often than generic text. Specifics get quoted.</li>
      <li><strong>Consistent claims.</strong> If your homepage says 30-day returns and a blog post says 14, the machine's confidence in both drops. One set of facts, everywhere they appear.</li>
    </ul>

    <h2>The honesty dividend</h2>
    <p>Here's the part most brands can't bring themselves to do: state the honest limits. "This works for X, and it's the wrong choice for Y." Models weight balanced, specific content over hype, and so do the buyers reading the answer. Honest caveats are a citation strategy.</p>
""",
"donow": [
"Take your best existing article. Rewrite every subheading as the question a buyer would ask, then make the first sentence under each one a direct answer. Add a TL;DR box at the top. That one edit pattern is the highest-leverage rewrite in content.",
],
"prompt": """Fetch my article at [URL]. Restructure it for chunk retrieval: 1) rewrite each subheading as the buyer's actual question, 2) rewrite each section's first sentence as a direct, self-contained answer, 3) write a 3-4 sentence TL;DR box for the top, 4) convert any buried steps or comparisons into lists or tables, 5) flag vague claims that need a number or a specific. Keep my voice, keep the facts, change the structure.""",
"app": True,
},
{
"id": "2.4",
"slug": "2-4-buying-guides-and-comparisons",
"title": "Buying guides and comparisons AI quotes",
"h1": 'Buying guides and comparisons AI <span class="te-editorial">quotes</span>',
"description": "The content formats AI assistants lean on hardest when recommending products: honest buying guides, comparison pages and FAQs that lead to a cart.",
"tag": "Content",
"mins": 7,
"lead": "When an AI answers a buying question, certain content shapes get quoted constantly: guides that help people choose, comparisons that weigh options honestly, and FAQs that answer exactly what was asked. Build those shapes deliberately.",
"body": """
    <h2>Write for buyers, not browsers</h2>
    <p>The blog advice of the 2010s said publish consistently and the traffic will come. Plenty of stores did, and got readers who never bought. The fix is choosing formats where the reader is already shopping:</p>
    <ul>
      <li><strong>Buying guides:</strong> "How to choose [category]", for buyers who know what they want but not which one.</li>
      <li><strong>Comparisons:</strong> "X vs Y", for buyers down to a shortlist. Highest intent content there is.</li>
      <li><strong>Use-case pages:</strong> "Best [category] for [situation]", the exact phrasing of half the questions AI gets asked.</li>
      <li><strong>FAQs:</strong> the pre-purchase questions from your inbox, answered in public.</li>
    </ul>

    <h2>The buying guide that gets cited</h2>
    <p>Structure it as the decision, in order: open with who the category is for and the 2-3 decisions that matter (answer-first, per lesson 2.3), walk each decision with specifics and honest trade-offs, then recommend by use case, linking to your products. Include real numbers everywhere: weights, temperatures, dimensions, prices. Specifics get you quoted; adjectives get you skipped.</p>

    <h2>Comparisons: yes, include competitors</h2>
    <p>The brave version wins here. A comparison page that honestly weighs your product against a competitor, including where the competitor wins, is one of the most-cited content shapes in AI answers. The model is going to make the comparison anyway. The only question is whether your version of the facts is in the room when it does.</p>
    <p>Structure: a comparison table with real specs, then "choose ours if... choose theirs if...". You'll close the buyers you fit, and you'll earn trust (human and machine) that outlasts any single sale.</p>

    <h2>Wire every piece to the shelf</h2>
    <p>Each guide and comparison links down to the products and collections it discusses, with descriptive anchors (lesson 1.6). Add FAQ schema where your theme supports it. And end every piece with the next step a convinced buyer needs, which is usually just the product.</p>
""",
"donow": [
"Pick the one comparison your buyers most often make (you know it from your inbox). Draft that page this week using the choose-ours-if structure. It'll feel exposed. Ship it anyway, it's the highest-intent page you can build.",
],
"prompt": """I sell [product] and buyers regularly compare us with [competitor]. Using my product page [URL] and their public specs, draft an honest comparison page: 1) a spec-by-spec table with real numbers, 2) where we genuinely win and where they do, 3) a "choose us if / choose them if" section by use case, 4) five FAQs buyers ask when choosing between us. Confident and factual, no trash talk, and flag any claim you can't verify so I can check it.""",
"app": True,
},
{
"id": "2.5",
"slug": "2-5-drafting-with-claude",
"title": "Drafting with Claude",
"h1": 'Drafting with <span class="te-editorial">Claude</span>',
"description": "A drafting workflow that produces content in your voice at scale: brand voice setup, structured briefs, and the honest limits of AI-drafted content.",
"tag": "Content",
"mins": 6,
"lead": "You've got a cluster plan that needs maybe 30 pieces of content. Written by hand, that's a year. Here's the workflow that makes it a quarter, without shipping the generic AI sludge your competitors are shipping.",
"body": """
    <h2>Good enough wins (when the structure is right)</h2>
    <p>The brutal truth about content in 2026: a well-structured, honest, specific article drafted with AI and edited by a human beats a perfect hand-written one that never ships. Coverage compounds. Perfectionism doesn't.</p>
    <p>The equally brutal flip side: unedited AI content, generic and fact-free, is exactly what engines are getting better at ignoring. The difference between the two is the workflow.</p>

    <h2>Teach it your voice once</h2>
    <p>Before drafting anything, build a voice note: 5-10 lines on how your brand talks, with two or three real paragraphs from your best existing copy as examples. Include your no-list (words and patterns you never use). Paste it at the top of every drafting session, or save it as a project instruction in Claude so it's always on.</p>

    <h2>Brief hard, draft fast, edit honest</h2>
    <ol>
      <li><strong>Brief hard.</strong> Give Claude the target query, the cluster it belongs to, the answer-first structure from 2.3, your voice note, and the specifics only you know: your product details, your customers' actual questions, your real numbers. The brief is where quality is decided.</li>
      <li><strong>Draft fast.</strong> Generate the full draft, then interrogate it: tighten the answers, demand specifics where it waffled.</li>
      <li><strong>Edit honest.</strong> You supply what the model can't: verify every fact, inject real experience ("we tested this", "customers tell us"), and cut anything that sounds like everyone else. If a paragraph could appear on a competitor's blog, it's not done.</li>
    </ol>
    <p>Fact-check rule: any number or claim in a draft gets verified or cut. One invented stat that ships can cost you the exact trust this whole playbook is building.</p>

    <h2>Where DIY tops out</h2>
    <p>This workflow will genuinely carry you to a cluster or two per quarter. The ceiling is scale with consistency: ten clusters, three markets, refreshes on a rhythm, every piece on-voice. That's an operations problem more than a writing problem, and it's the layer we build for clients (and the layer our app is being built to run). You'll know you've hit the ceiling when the bottleneck stops being writing and starts being managing.</p>
""",
"donow": [
"Build your voice note today: 5-10 lines plus two real sample paragraphs and your no-list. Save it where you'll reuse it. Then draft your first spoke article from the 2.2 plan using the brief-hard workflow.",
],
"prompt": """Here's my voice note: [paste it]. Here's the brief: target question [query], part of my [cluster name] cluster, audience [who], my product specifics: [details, real numbers, customer questions].

Draft the article: TL;DR box up top, every subheading a buyer question, first sentence of each section a direct answer, specifics over adjectives, one honest limitation included. 800-1200 words. Then list every factual claim you made so I can verify each one before publishing.""",
"app": True,
},
{
"id": "2.6",
"slug": "2-6-refresh-and-freshness",
"title": "Refresh and freshness cycles",
"h1": 'Refresh and freshness <span class="te-editorial">cycles</span>',
"description": "Find decaying content in Search Console, make substantial updates, and run the 90-day refresh rhythm that keeps your best pages compounding instead of fading.",
"tag": "Content",
"mins": 6,
"lead": "Content decays. Rankings slip, answers go stale, and AI moves on to fresher sources. The refresh cycle is how a content library becomes an appreciating asset instead of a graveyard.",
"body": """
    <h2>Why freshness moved up the priority list</h2>
    <p>AI systems weight recency hard, especially for anything with a "best" or a price in it. A 2024 buying guide is invisible in a 2026 answer. And the payoff for maintaining freshness is real: Webflow's refresh programme drove a 40% traffic uplift within days of updating decayed pieces, at 5x their old refresh velocity. <span class="src">(AirOps customer stories)</span></p>
    <p>Refreshing an existing page that's slipping is nearly always faster and higher-return than writing something new. It has history, links and authority. It just needs to be current again.</p>

    <h2>Find the decay in Search Console</h2>
    <p>Every quarter, open Search Console and compare the last 90 days against the previous 90:</p>
    <ol>
      <li><strong>Falling clicks or impressions</strong> on a page that used to perform: refresh it.</li>
      <li><strong>Position 5-15 queries</strong> with real impressions: these are your close-to-the-money refreshes, small improvements move real traffic.</li>
      <li><strong>Rising queries your page doesn't quite answer:</strong> the intent shifted. Add the missing section.</li>
    </ol>

    <h2>Refresh substantially or not at all</h2>
    <p>Changing the date on an unchanged page fools nobody, engines least of all. A real refresh: update every stale fact, price and example, add what's changed in the category since publishing (new products, new questions), tighten the answer-first structure while you're in there, and check every link still works and still points at the right products. Then update the visible date and the dateModified in your schema, honestly.</p>

    <h2>The 90-day biology</h2>
    <p>Set a quarterly rhythm: audit for decay, refresh the top five decaying pieces, then publish new spokes with whatever capacity is left. Refreshes come before new content. It feels less productive and it compounds faster, because you're reinforcing pages that already have equity instead of always starting from zero.</p>
""",
"donow": [
"Open Search Console now and run the 90-day comparison. Find your five biggest decays and your five position-5-to-15 near-wins. That's your refresh list for this quarter, and it comes before any new content.",
],
"prompt": """Here's my Search Console data comparing the last 90 days to the previous 90: [paste or export]. And here's the article I want to refresh: [URL].

1) Confirm which pages are decaying versus near-winning (position 5-15 with impressions). 2) For the article: list every stale fact, missing subtopic and structural gap versus the answer-first pattern. 3) Give me the refresh edit list in priority order, and note which queries the refresh should target harder.""",
"app": True,
},
{
"id": "2.7",
"slug": "2-7-stitch-it-together",
"title": "Stitch it together with internal links",
"h1": 'Stitch it together with internal <span class="te-editorial">links</span>',
"description": "Wire your clusters into the web AI can follow: pillar to spokes, spokes to products, and the linking audit that closes Module 2.",
"tag": "Content",
"mins": 5,
"lead": "You've built the pages. Now wire them together so engines, AI and buyers can all follow the thread from question to answer to checkout. This is the lesson that makes the cluster a cluster.",
"body": """
    <h2>The wiring diagram</h2>
    <p>Every cluster follows the same pattern, and it's deliberately boring:</p>
    <ul>
      <li><strong>Every spoke links up to its pillar</strong>, early in the piece, with the topic as the anchor text.</li>
      <li><strong>The pillar links down to every spoke</strong>, naturally, where each question comes up.</li>
      <li><strong>Spokes link sideways</strong> to the 2-3 sibling spokes a reader would logically want next.</li>
      <li><strong>Everything links to the shelf:</strong> every piece points to the products and collections it discusses, descriptive anchors, no orphan advice.</li>
    </ul>
    <p>This is how a machine learns your site's shape. A tight cluster says: this store owns this topic, here's the map, and here's where the answers lead. That structure is readable to a crawler in a single visit.</p>

    <h2>The audit</h2>
    <p>Run this on each cluster as you finish it, and quarterly after that:</p>
    <ol>
      <li><strong>Orphans:</strong> any published spoke with no links pointing to it? It's invisible. Wire it in.</li>
      <li><strong>Dead-end pillars:</strong> does the pillar link to all its live spokes? New spokes are easy to forget.</li>
      <li><strong>Weak anchors:</strong> any "read more" or "click here" carrying a link that deserves a descriptive anchor?</li>
      <li><strong>Missing shelf links:</strong> any piece discussing a product it doesn't link to?</li>
    </ol>

    <h2>Module 2, done</h2>
    <p>Research with intent, clusters with a plan, chunks machines can quote, formats buyers convert from, a drafting engine, a refresh rhythm, and now the wiring. That's the content system. It compounds every quarter you run it, and Module 3 is where we go get the rest of the internet to vouch for it.</p>
""",
"donow": [
"Run the four-check audit on your most complete cluster today. Fix the orphans and dead-ends first, then upgrade the weak anchors. Book the same audit into your calendar quarterly.",
],
"prompt": """Read these pages from my cluster: pillar [URL], spokes [URLs]. Audit the internal linking: 1) which spokes the pillar fails to link to, 2) which spokes don't link back to the pillar, 3) orphan pages with no inbound links from the cluster, 4) weak anchor text that should be descriptive, 5) products/collections discussed but not linked. Output the exact edit list: on [page], add link to [page] with anchor [text].""",
"app": True,
},
]
