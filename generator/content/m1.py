# Module 1 · Get found — technical foundations
LESSONS = [
{
"id": "1.1",
"slug": "1-1-open-the-doors",
"title": "Open the doors to AI crawlers",
"h1": 'Open the doors to AI <span class="te-editorial">crawlers</span>',
"description": "robots.txt, CDN and WAF settings, and llms.txt: how to stop accidentally blocking the AI crawlers that power ChatGPT, Perplexity and Google AI shopping answers.",
"tag": "Technical",
"mins": 6,
"lead": "85% of brands are blocking AI crawlers without knowing it. Before anything else in this module, make sure the engines you want recommending you can actually get in the door.",
"body": """
    <h2>The crawlers that matter now</h2>
    <p>Every AI assistant that recommends products gets its knowledge from crawlers. ChatGPT and Copilot lean on Bing's index plus OpenAI's own bots. Gemini and AI Overviews use Google's. Perplexity and Claude run their own. If those bots can't read your store, you don't exist in the answer.</p>
    <p>The names to know: <strong>GPTBot</strong> and <strong>OAI-SearchBot</strong> (OpenAI), <strong>ClaudeBot</strong> (Anthropic), <strong>PerplexityBot</strong>, <strong>Google-Extended</strong> (Google's AI training bot), plus the classic Googlebot and Bingbot.</p>

    <h2>Where stores accidentally slam the door</h2>
    <ol>
      <li><strong>robots.txt.</strong> Somewhere along the way, an agency or a plugin added a blanket disallow. Open yourstore.com/robots.txt and read it. Any line disallowing the bots above is turning away customers.</li>
      <li><strong>CDN and firewall settings.</strong> Cloudflare and similar services now ship one-click "block AI bots" toggles, and they're sometimes on by default. Check your security settings for anything labelled AI scrapers or bot fight mode.</li>
      <li><strong>App bloat.</strong> Some Shopify security and speed apps quietly filter bot traffic. If a bot-blocker app is installed, check its allowlist.</li>
    </ol>
    <p>Shopify's own defaults are sensible here, which is one of the perks of the platform. The blocks almost always come from something added on top.</p>

    <h2>Roll out the welcome mat: llms.txt</h2>
    <p>llms.txt is a simple text file at yourstore.com/llms.txt that tells AI systems what your site is and where your most useful pages are. Think of it as a menu you hand the model. It's early days for the standard, but it costs 20 minutes, and the stores that adopt early tend to be the stores that show up early.</p>
    <p>Keep it short: who you are, what you sell, and direct links to your best collections, buying guides and FAQ. Plain language, no marketing fluff. Machines are the audience.</p>

    <h2>What good looks like</h2>
    <p>Your robots.txt allows every major AI crawler, your CDN isn't silently filtering them, and llms.txt points the models at your best pages. That's Technical level 4 behaviour on the maturity model, and for most stores it's an afternoon of work.</p>
""",
"donow": [
"Open yourstore.com/robots.txt right now and read every Disallow line. Then check your CDN or firewall for AI-bot blocking toggles. Fix anything blocking GPTBot, ClaudeBot, PerplexityBot or Google-Extended.",
],
"prompt": """Read my robots.txt at [yourstore.com/robots.txt]. Tell me: 1) which AI crawlers (GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot, Google-Extended) are blocked or allowed, 2) any rules that look like they'd block more than intended, 3) the corrected robots.txt I should use. Then draft an llms.txt for my store: I sell [what you sell] and my most important pages are [list 3-5 URLs].""",
"app": True,
},
{
"id": "1.2",
"slug": "1-2-escape-shopifys-url-traps",
"title": "Escape Shopify's URL traps",
"h1": "Escape Shopify's URL <span class='te-editorial'>traps</span>",
"description": "Duplicate product URLs, canonicals, index control and redirects: the Shopify-specific plumbing that quietly leaks rankings, and how to take back control.",
"tag": "Technical",
"mins": 7,
"lead": "Shopify is a brilliant platform with a few sharp edges, and most of them are URLs. Here's where the platform quietly duplicates your pages, and how to keep Google and AI focused on the versions that matter.",
"body": """
    <h2>The duplicate URL trap</h2>
    <p>Shopify gives every product two addresses: the clean one at <strong>/products/your-product</strong>, and a collection-scoped one at <strong>/collections/collection-name/products/your-product</strong>. Same product, different URLs. Left alone, your link equity and your rankings get split across the copies.</p>
    <p>Shopify handles most of this with canonical tags (a signal that says "this is the real version"), and the canonical always points to /products/. Good. But your theme's internal links often point to the /collections/ versions, which means you're spending your own link power on pages that redirect authority elsewhere. If your theme does this, have a developer point product links at the canonical /products/ URL.</p>

    <h2>Control what gets indexed</h2>
    <p>Not every page deserves a place in the index. Tag pages, filtered views, internal search results and thin utility pages dilute how engines see your store. The pattern you want:</p>
    <ul>
      <li><strong>Index:</strong> home, collections, products, blog posts, your key pages.</li>
      <li><strong>Don't index:</strong> filtered collection variants, internal search results, cart, account pages, and tag pages you haven't deliberately built out.</li>
    </ul>
    <p>Most of this is theme-level (a noindex tag on the right templates). If you're unsure what's currently indexed, search <strong>site:yourstore.com</strong> on Google and skim what comes back. Surprises in that list are your to-do list.</p>

    <h2>Redirects: never lose what you've earned</h2>
    <p>Every time you rename a product, change a handle, or retire a collection, the old URL dies, and any rankings or links it earned die with it, unless you redirect. Shopify creates redirects automatically when you change a handle, but deletions and migrations don't get that safety net.</p>
    <p>The rule: any URL that ever earned traffic or links gets a 301 redirect to its closest living relative. Shopify's redirect manager is under Online Store, then Navigation. Check it after every catalogue cleanup.</p>

    <h2>Why this matters more in the AI era</h2>
    <p>AI crawlers have less patience than Googlebot. They crawl less often and less deeply, so every duplicate they hit is budget you wasted, and every dead URL is a trust signal you dropped. Clean URL plumbing means the crawl budget you get goes entirely on pages that sell.</p>
""",
"donow": [
"Search site:yourstore.com on Google. Skim the first five pages of results. Note anything indexed that shouldn't be (filtered views, search results, thin tags) and anything important that's missing.",
],
"prompt": """Audit my Shopify store's URL hygiene at [yourstore.com]. Read the sitemap at /sitemap.xml. Check: 1) whether my theme links to /collections/.../products/ style URLs instead of canonical /products/ URLs (fetch my homepage and one collection page to look), 2) what a site: search would likely surface that shouldn't be indexed, 3) which templates typically need noindex on Shopify. Give me a prioritised fix list I can hand to a developer.""",
"app": True,
},
{
"id": "1.3",
"slug": "1-3-product-pages-that-sell-themselves",
"title": "Product pages that sell themselves",
"h1": 'Product pages that sell <span class="te-editorial">themselves</span>',
"description": "Product titles, descriptions and variants that rank on Google and get quoted by AI, without the supplier copy that half your competitors also shipped.",
"tag": "Technical",
"mins": 7,
"lead": "Your product page is where the sale happens, and in AI search it's also your evidence. Here's how to write titles and descriptions that machines can quote and buyers can trust.",
"body": """
    <h2>Titles that get found and clicked</h2>
    <p>A product title has two jobs: match what buyers actually type, and win the click when it shows up. "The Cloudrunner" does neither. "Cloudrunner Merino Running Socks, Cushioned, NZ Made" does both.</p>
    <p>The pattern that works: <strong>[Brand] [Product name] [Category], [Key attribute], [Key attribute]</strong>. Front-load the words a stranger would search. Keep it under about 70 characters so it doesn't truncate in results. Your bestsellers deserve this treatment first.</p>

    <h2>Kill the supplier description</h2>
    <p>If you sell other brands' products, there's a decent chance your descriptions arrived with the stock, and the same paragraph is live on 40 other stores. Engines have seen it 40 times. There's no reason to quote your copy of it, and duplicate copy is one of the most common reasons product pages never rank.</p>
    <p>Rewrite in your own words, and structure it for a machine to parse:</p>
    <ul>
      <li><strong>First two sentences answer "what is this and who is it for".</strong> That's the chunk AI lifts.</li>
      <li><strong>Real specs in a list</strong>: materials, dimensions, weight, care, compatibility. Specifics are what get you into "best X for Y" answers.</li>
      <li><strong>Answer the pre-purchase questions</strong> you hear on email and chat, right on the page. Sizing, shipping, returns, "will it work with...".</li>
    </ul>

    <h2>Variants without the mess</h2>
    <p>One product in five colours should almost always be one page, with variants, rather than five pages competing with each other. Shopify handles this well by default. The trap is creating separate products for what should be variants, splitting your reviews and rankings five ways. Consolidate unless the variants genuinely get searched differently.</p>

    <h2>Reviews on the page</h2>
    <p>Reviews are conversion fuel, and in the AI era they're also machine-readable proof. Get your review app rendering reviews in the page (not in a JavaScript widget engines can't see), and you feed both the buyer and the bot. Module 3 covers generating review velocity; here, just make sure what you have is visible.</p>
""",
"donow": [
"Open your top three products. Rewrite each title with the pattern above, and check whether the description's first two sentences would make sense read aloud to someone who's never seen the product. If not, rewrite them today.",
],
"prompt": """Read my product data at [yourstore.com/products.json]. Pick my 10 weakest product titles and descriptions. For each: 1) diagnose the problem (vague title, supplier copy, no specs, buried answer), 2) rewrite the title using [Brand] [Name] [Category], [Attribute], [Attribute], 3) write a new first paragraph that answers "what is this and who is it for" in two sentences. Match my brand voice from the copy you can see.""",
"app": True,
},
{
"id": "1.4",
"slug": "1-4-product-schema-and-gtins",
"title": "Product schema and GTINs",
"h1": 'Product schema and <span class="te-editorial">GTINs</span>',
"description": "Structured data and product identifiers: the single most-missed variable in ecommerce AI visibility. Get stars, prices and stock into your listings and get recommended by AI.",
"tag": "Technical",
"mins": 7,
"lead": "This is the single most-missed variable we see in audits. Schema is how you tell machines exactly what you sell, and GTINs are how they know your product is the same one the rest of the web is talking about.",
"body": """
    <h2>What schema does for you</h2>
    <p>Schema (structured data) is a block of code on your page that states the facts outright: this is a product, here's its name, price, availability, rating, brand. Engines stop guessing and start knowing.</p>
    <p>The payoff is visible: stars, prices and stock status in your Google listings, and eligibility for AI shopping answers. 88% of sites haven't implemented schema at all, while 73% of first-page Google results use it. <span class="src">(Webflow; industry studies)</span> That gap is your opening.</p>

    <h2>GTINs: the missing key</h2>
    <p>A GTIN is the barcode number on the product, the global ID that says "this exact item". When your product carries its GTIN, an AI can connect your listing to every review, spec sheet and mention of that product across the web. Without it, you're a stranger claiming to sell something.</p>
    <p><strong>60% of ecommerce catalogues have missing GTINs.</strong> <span class="src">(AirOps)</span> In Shopify, the field is called Barcode, on every variant. If you sell other brands' products, the GTINs exist and your supplier has them. If you make your own products, you can buy a GTIN range from GS1. Either way, filling that field is some of the highest-leverage data entry in ecommerce.</p>

    <h2>Getting schema right on Shopify</h2>
    <p>Most modern Shopify themes ship with basic Product schema. Basic is the operative word. The checklist that takes you from basic to Professional:</p>
    <ol>
      <li><strong>Product schema on every product</strong> with name, description, image, brand, price, currency and availability.</li>
      <li><strong>GTIN included</strong> once your Barcode fields are filled (most themes pass it through automatically).</li>
      <li><strong>Review schema wired to your review app</strong> so your stars are machine-readable, not just pixels.</li>
      <li><strong>Organization schema</strong> on your store: who you are, your logo, your official social profiles. This is how engines connect your store to your brand as an entity.</li>
      <li><strong>Validate.</strong> Run your top pages through Google's Rich Results Test. Fix what it flags.</li>
    </ol>
    <p>If your theme is short on any of this, apps can fill the gap, or a developer can add it properly in an afternoon.</p>
""",
"donow": [
"In Shopify admin, filter your products by empty Barcode field. Count them. That number is your gap. Start filling it with your 20 bestsellers this week, supplier data has the GTINs if you don't.",
],
"prompt": """Fetch [yourstore.com/products/your-best-seller] and inspect its structured data. Tell me: 1) what schema types are present, 2) which Product schema fields are missing or empty (especially gtin, brand, aggregateRating, availability), 3) whether reviews are machine-readable, 4) exactly what the completed Product JSON-LD should look like for this page. Then list every spec a buyer would ask about that isn't in the markup.""",
"app": True,
},
{
"id": "1.5",
"slug": "1-5-collections-your-biggest-traffic-pages",
"title": "Collections: your biggest traffic pages",
"h1": 'Collections: your biggest traffic <span class="te-editorial">pages</span>',
"description": "Your collection pages target the broadest, highest-intent searches you can win. Most stores leave them empty. Fill them, tame the filters, and fix pagination.",
"tag": "Technical",
"mins": 8,
"lead": "Here's the deal: your collection pages are built to win the broad, high-intent searches (think merino base layers NZ) where the real volume lives. And on most Shopify stores, they're a product grid with zero words on them.",
"body": """
    <h2>Why collections outrank products</h2>
    <p>When someone searches a category ("linen bedding", "trail running shoes"), engines want to return a page that shows the range, and that's exactly what a collection page is. Your product pages win the specific searches; your collections win the categories. The categories are where the volume is.</p>
    <p>An empty collection page gives an engine nothing to rank and an AI nothing to quote. A collection with 300 good words of real guidance becomes your most powerful page type.</p>

    <h2>Fill them with copy that earns its place</h2>
    <p>Collection copy has a bad reputation because most of it is keyword sludge nobody reads. Write it like a knowledgeable shop assistant instead:</p>
    <ul>
      <li><strong>Open with two sentences that define the category and who it's for.</strong> That's your quotable chunk.</li>
      <li><strong>Help them choose:</strong> the 2-3 things that actually matter when picking within this category (fabric weight, fit, use case). This is the guidance AI assistants lift into answers.</li>
      <li><strong>Answer the category's common questions</strong> at the bottom of the page, marked up with FAQ schema if your theme supports it.</li>
    </ul>
    <p>A note on placement: a short intro above the grid, the deeper guidance below it. Buyers see products first, engines get the full story.</p>

    <h2>Tame the filters before they wreck you</h2>
    <p>Filtered views (size, colour, price) can each generate their own URL. Left unmanaged, one collection becomes hundreds of near-identical pages soaking up crawl budget. The default: filtered URLs stay out of the index (canonical to the main collection or noindex). The exception: if a filtered view matches a real search ("black linen dress"), consider making it a proper collection of its own, with its own copy.</p>

    <h2>Kill the thin, fix the pagination</h2>
    <p>Collections with two products and no copy drag your whole store's quality down. Merge them or build them out. And check your pagination: page 2 and beyond of each collection should be crawlable links (not infinite scroll only), or engines never see the products deeper in your catalogue.</p>
""",
"donow": [
"List your 10 highest-traffic collections (or your 10 most important if you're not sure). Count how many have real copy on them. Every one without is a page one of your competitors is winning instead. Write the first one today using the structure above.",
],
"prompt": """Fetch my collection page [yourstore.com/collections/your-biggest-collection]. Write collection copy for it: 1) a two-sentence opener defining the category and who it's for, 2) a "how to choose" section covering the 2-3 decisions that matter in this category, 3) five FAQs with direct answers based on what buyers in this category ask. Match the tone of my existing site copy. Keep it useful over keyword-stuffed, around 300-400 words total.""",
"app": True,
},
{
"id": "1.6",
"slug": "1-6-structure-and-internal-links",
"title": "Structure and internal links that feed your money pages",
"h1": 'Internal links that feed your money <span class="te-editorial">pages</span>',
"description": "Site architecture and internal linking on Shopify: make every page reachable, stop burying your best sellers, and funnel authority to the pages that make money.",
"tag": "Technical",
"mins": 6,
"lead": "Structure decides how much of your store engines ever see, and internal links decide which pages they think matter. Both are fully in your control, and most stores never touch them.",
"body": """
    <h2>The three-click rule</h2>
    <p>Every product you sell should be reachable within about three clicks of your homepage. Deeper than that and crawlers visit less often, index less reliably, and rank the page lower. The fix is structural: strong collection architecture, sensible menus, and no orphan pages sitting outside the navigation entirely.</p>
    <p>Quick test: pick a slow-moving product you still care about. Start at your homepage and count the clicks to reach it. If you can't get there through menus and collections at all, neither can a crawler.</p>

    <h2>Links are votes, and you're the electorate</h2>
    <p>Every internal link tells engines "this page matters". Right now your store is already voting, it's just probably voting for your cart and your contact page. Redirect those votes deliberately:</p>
    <ul>
      <li><strong>Homepage links are your loudest votes.</strong> Feature the collections you want to rank, by name, in real HTML links.</li>
      <li><strong>Blog posts should link down to products and collections.</strong> Every buying guide that doesn't link to the products it discusses is a wasted vote.</li>
      <li><strong>Products should cross-link sideways</strong>: related products, "pairs with", "the rest of the range". This keeps crawlers moving and spreads authority through the catalogue.</li>
    </ul>

    <h2>Anchor text does the talking</h2>
    <p>"Click here" tells an engine nothing. "Merino base layers" as the clickable text tells it exactly what the destination page is about. Use descriptive anchors that match what the target page should rank for. Vary the phrasing naturally, but keep the meaning on target.</p>

    <h2>The AI angle</h2>
    <p>AI crawlers follow links with less patience and less budget than Googlebot. A tight structure with deliberate internal links means the pages they do reach are your best ones. In Module 2 you'll build content clusters, and this lesson is the plumbing they run on: pillar pages linking to spokes, spokes linking to products, everything feeding the money.</p>
""",
"donow": [
"Do the three-click test on five products across different collections. Then open your last three blog posts and count the links to your own products and collections. Add the missing ones now, with descriptive anchor text.",
],
"prompt": """Read my store's structure from [yourstore.com/sitemap.xml] and fetch my homepage. Map: 1) which collections get homepage link votes and which don't, 2) products likely deeper than three clicks based on the collection structure, 3) the 10 internal links I should add this week to push authority toward my highest-value collections, with the exact anchor text to use.""",
"app": True,
},
{
"id": "1.7",
"slug": "1-7-merchant-feeds",
"title": "Merchant feeds: the universal AI shopping key",
"h1": 'Merchant feeds: the universal AI shopping <span class="te-editorial">key</span>',
"description": "Google Merchant Center, Microsoft and beyond: your product feed is now an SEO channel that decides whether AI shopping surfaces can show your products at all.",
"tag": "Technical",
"mins": 6,
"lead": "Your product feed used to be a paid-ads thing. Now it's the data backbone AI shopping runs on, and optimising it is free traffic most stores never claim.",
"body": """
    <h2>Feeds went from ads-only to everywhere</h2>
    <p>Google shows free product listings pulled straight from Merchant Center feeds. Microsoft does the same for Bing and Copilot. And the AI shopping experiences rolling out across ChatGPT, Gemini and Perplexity lean on this same structured product data to know what exists, what it costs, and whether it's in stock.</p>
    <p>Your feed is your store, translated into the language every shopping machine reads. If it's thin, wrong or missing, you're invisible in surfaces that cost nothing to be in.</p>

    <h2>Set up the free channels</h2>
    <ol>
      <li><strong>Google:</strong> install the Google &amp; YouTube app on Shopify, connect Merchant Center, and make sure free listings are on. Your catalogue syncs automatically.</li>
      <li><strong>Microsoft:</strong> the Microsoft Channel app does the same for Bing, and Bing's index is what ChatGPT search leans on. This one is chronically ignored and takes 20 minutes.</li>
      <li><strong>Everything else:</strong> your products.json and schema (lesson 1.4) already feed the crawlers that don't take formal feeds. Keeping product data complete in Shopify flows through everywhere.</li>
    </ol>

    <h2>The fields that decide who wins</h2>
    <p>Within a feed, ranking comes down to data quality. The fields that move the needle:</p>
    <ul>
      <li><strong>Title:</strong> same pattern as lesson 1.3, brand, product, category, attributes. The feed title can differ from your on-site title, but there's rarely a reason to.</li>
      <li><strong>GTIN and brand:</strong> the identity fields. Feeds with them get shown; feeds without get filtered.</li>
      <li><strong>Product category and product type:</strong> be specific. "Apparel" loses to "Apparel &amp; Accessories &gt; Clothing &gt; Activewear &gt; Base Layers".</li>
      <li><strong>Images, price, availability:</strong> accurate, current, and matching your site exactly. Mismatches get products suspended.</li>
    </ul>
    <p>Fix your product data at the source in Shopify rather than patching the feed downstream. One clean source, every surface benefits.</p>
""",
"donow": [
"Check whether your store is connected to Google Merchant Center with free listings enabled, and whether the Microsoft Channel app is installed at all. If either is missing, that's this week's job, both are free traffic.",
],
"prompt": """Read my product data at [yourstore.com/products.json]. Audit it as if it were my merchant feed: 1) titles that won't perform in shopping surfaces and their rewrites, 2) products missing barcode/GTIN or vendor/brand, 3) how specific my product types are versus what they should be, 4) a prioritised data-cleanup list ordered by bestsellers first.""",
"app": True,
},
{
"id": "1.8",
"slug": "1-8-agentic-storefronts",
"title": "Agentic storefronts: sell inside ChatGPT",
"h1": 'Agentic storefronts: sell inside <span class="te-editorial">ChatGPT</span>',
"description": "Shopify now syndicates your catalogue into ChatGPT, Google AI Mode, Copilot and Perplexity, and buyers can check out inside the chat. Set it up deliberately.",
"tag": "Technical",
"mins": 7,
"lead": "The newest surface in commerce: your products, discoverable and buyable inside the AI chat itself. Shopify has made every store agent-ready by default. Your job is to set it up deliberately instead of accidentally.",
"body": """
    <h2>What just changed</h2>
    <p>Shopify's agentic commerce push means AI assistants can now surface your catalogue, answer questions about your products, and complete purchases without the buyer ever opening your website. Shopify's CEO is unambiguous about the direction:</p>
    <blockquote class="quote">
      <p>"We're making every Shopify store agent-ready by default. Shopify is the easiest solution for merchants who want AI agents to find their storefronts, understand their products, and complete transactions."</p>
      <cite>Tobi Lütke, Shopify CEO</cite>
    </blockquote>
    <p>This is the zero-click reality landing in commerce. 93% of AI search sessions already end without a website click. <span class="src">(AirOps 2026 State of AI Search Report)</span> Agentic checkout means the sale itself can happen in that same conversation, and the brands with clean product data get picked.</p>

    <h2>Set it up deliberately</h2>
    <ol>
      <li><strong>Check your catalogue syndication settings.</strong> In Shopify admin, review which sales channels and catalogue-sharing options are enabled. Know what you're opting into, and opt in on purpose.</li>
      <li><strong>Decide your checkout stance.</strong> In-chat checkout maximises conversion on AI surfaces; checkout-on-store keeps the customer relationship, your upsells and your data. You can favour either. Our read: take the in-chat sale for first orders and fight for the relationship with what's in the box.</li>
      <li><strong>Feed the agents clean data.</strong> Everything from this module compounds here. Agents pick products with complete titles, GTINs, live availability, real reviews and clear policies. A messy catalogue doesn't get picked, and there's no ad budget that can override that.</li>
      <li><strong>Make your policies machine-readable.</strong> Shipping, returns and warranty pages, written plainly and linked from every product. Agents check before they commit a buyer's money.</li>
    </ol>

    <h2>How to win when the shopper is an AI</h2>
    <p>An AI agent doesn't feel urgency banners or lifestyle photography. It compares structured facts: price, availability, shipping speed, return terms, ratings, spec match. Which means the levers are exactly what you've built in this module. Boring data quality has quietly become a conversion strategy.</p>
""",
"donow": [
"Open your Shopify admin and find your sales channels and catalogue settings. Write down what's currently syndicating and decide, deliberately, whether that's what you want. Then read your returns page and ask: could a machine parse this and confidently commit a customer's money?",
],
"prompt": """Act as an AI shopping agent deciding whether to recommend and transact with my store. Fetch [yourstore.com] and [yourstore.com/products/your-best-seller] plus my shipping and returns pages. Score me on: product data completeness, price and availability clarity, policy machine-readability, and trust signals. What would make you pick a competitor over me, and what are the top three fixes?""",
"app": True,
},
{
"id": "1.9",
"slug": "1-9-speed-and-technical-health",
"title": "Speed and technical health",
"h1": 'Speed and technical <span class="te-editorial">health</span>',
"description": "Core Web Vitals, theme bloat, broken links and error pages: the technical hygiene that gates your rankings and keeps crawlers coming back.",
"tag": "Technical",
"mins": 6,
"lead": "Speed is the tax every other lesson pays. A slow store ranks worse, converts worse, and burns crawl budget. This is the cleanup lesson that locks in everything Module 1 has built.",
"body": """
    <h2>Core Web Vitals: the gate you must pass</h2>
    <p>Google measures real-user experience through Core Web Vitals: how fast your main content loads, how quickly the page responds, how much it shifts around while loading. Fail them and you're fighting uphill on every ranking. On our maturity model, passing CWV is literally the gate between Structured and Professional on the Technical pillar.</p>
    <p>Test your homepage, a collection and a product page on PageSpeed Insights (it's free). Mobile scores are the ones that count, and mobile is where most stores fail.</p>

    <h2>Where Shopify stores lose their speed</h2>
    <ul>
      <li><strong>App bloat.</strong> Every app you've ever installed likely left scripts in your theme, and many load on every page whether used or not. Audit your apps quarterly; uninstall properly and have leftover code removed.</li>
      <li><strong>Oversized images.</strong> Huge hero images and uncompressed product photos are the most common LCP killer. Compress, use modern formats, and let Shopify's responsive image tags do their job.</li>
      <li><strong>Theme age.</strong> Themes accumulate a decade of patches. If yours predates Online Store 2.0, a rebuild on a modern theme often beats another round of patches.</li>
    </ul>

    <h2>The hygiene sweep</h2>
    <ol>
      <li><strong>Broken links:</strong> internal links to dead pages waste authority and patience. Crawl your store with a free tool (or the prompt below) and fix what's broken.</li>
      <li><strong>Error pages:</strong> your 404 page should exist, be branded, and link back into the catalogue.</li>
      <li><strong>Search Console:</strong> if you haven't verified your store in Google Search Console, do it today. It's free, it shows you exactly what Google sees (errors, indexing, queries), and Module 4 runs on it.</li>
    </ol>

    <h2>Module 1, done</h2>
    <p>If you've worked through all nine lessons: crawlers welcomed, URLs clean, products and collections structured and identified, links feeding your money pages, feeds live, agents served, and the whole thing fast. That's a store machines can read, trust and recommend. Now we go make you the answer.</p>
""",
"donow": [
"Run your homepage, one collection and one product page through PageSpeed Insights on mobile. Write down the three scores and the biggest flagged issue for each. If you're failing, image compression and app cleanup are almost always the first two fixes.",
],
"prompt": """My PageSpeed Insights mobile results: homepage [score + top issue], collection page [score + top issue], product page [score + top issue]. My store is on Shopify with these apps installed: [list your apps]. Diagnose the likely causes, tell me which apps are probably costing me the most, and give me a fix plan ordered by speed gain per hour of work. Flag anything I should hand to a developer versus do myself.""",
"app": True,
},
]
