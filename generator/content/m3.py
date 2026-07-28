# Module 3 · Get recommended — authority & reputation
LESSONS = [
{
"id": "3.1",
"slug": "3-1-why-77-percent",
"title": "Why 77 percent",
"h1": 'Why 77 <span class="te-editorial">percent</span>',
"description": "Only 23% of AI citations come from your own website. The other 77% come from third-party sources: reviews, forums, media. This module is how you earn them.",
"tag": "Authority",
"mins": 5,
"lead": "Everything you've built so far lives on your own site. Now for the uncomfortable number that reframes the whole game: most of what makes AI recommend you doesn't live on your site at all.",
"body": """
    <h2>The number</h2>
    <div class="pullquote">
      <span class="label">The 77% problem</span>
      <p>Only 23% of the sources AI cites when answering buying questions come from brands' own websites. The other 77% come from third-party sources: review platforms, forums, media, communities.</p>
    </div>
    <p>Go deeper and it gets starker. 48% of LLM citations come from earned media specifically. 85% of the brand mentions that drive AI citations sit on third-party pages, not brand-owned ones. And brand mentions correlate nearly 3x more strongly with AI visibility than backlinks do (0.664 vs 0.218). <span class="src">(AirOps research, 2026)</span></p>
    <p>Read that last one again slowly: the metric SEO spent twenty years chasing (links) now matters less than the thing PR was always about (being talked about).</p>

    <h2>Why AI works this way</h2>
    <p>Put yourself in the model's position. A brand's own site says the brand is great. Of course it does. So when the model decides what's safe to recommend, it weighs what everyone else says: reviewers, Reddit threads, comparison articles, forum answers, the press. Corroboration is the currency.</p>
    <p>One more stat that changes tactics: 59.6% of AI Overview citations come from URLs that aren't even in the top 20 organic results. <span class="src">(AirOps)</span> The AI isn't just reading page one of Google. It's reading the places people actually talk.</p>

    <h2>The five channels of the 77%</h2>
    <p>This module works through them in order of effort-to-impact:</p>
    <ol>
      <li><strong>Review velocity</strong> (3.2): a steady stream of recent reviews, on autopilot.</li>
      <li><strong>Third-party review platforms</strong> (3.3): the trusted sites that vouch for you.</li>
      <li><strong>Reddit, Quora and forums</strong> (3.4): where AI reads real opinions.</li>
      <li><strong>Digital PR and earned media</strong> (3.5): the 48% channel.</li>
      <li><strong>LinkedIn and founder presence</strong> (3.6): the human face engines connect to the entity.</li>
    </ol>
    <p>One honest note before you start: this is the slowest module and the most defensible. Technical fixes are copyable by any competitor with a developer. A reputation is not. This is where the moat gets dug.</p>
""",
"donow": [
"Ask ChatGPT and Perplexity: \"what are the best [your category] brands?\" and \"is [your brand] any good?\". Note every source cited in the answers. That list of third-party sites is your module 3 target list, the places your reputation is currently being decided without you.",
],
"prompt": """Research my brand's third-party footprint. My brand: [name], category: [category], market: [NZ/AU/etc]. Search for: 1) every review platform with a profile or reviews of us, 2) Reddit and forum threads mentioning us or asking about our category, 3) media coverage or roundup articles including us, 4) the same for my top competitor [name]. Output a table: channel, our presence, competitor's presence, gap. Rank the gaps by likely impact on AI recommendations.""",
"app": True,
},
{
"id": "3.2",
"slug": "3-2-review-velocity",
"title": "Review velocity on autopilot",
"h1": 'Review velocity on <span class="te-editorial">autopilot</span>',
"description": "50 recent reviews beat 800 old ones. Build the post-purchase sequence that generates a steady stream of specific, attribute-rich reviews, compliantly.",
"tag": "Authority",
"mins": 7,
"lead": "Reviews are the most controllable piece of the 77%, because the raw material walks through your checkout every day. The key is velocity: engines and AI trust the brand that's being reviewed now, not the one that was popular in 2023.",
"body": """
    <h2>Velocity beats volume</h2>
    <p><strong>50 reviews in the last 90 days beats 800 old reviews with none recent.</strong> Recency signals a brand that's alive and still delivering. A wall of reviews from two years ago signals the opposite, whatever the star average says.</p>
    <p>So the goal is a system that produces reviews continuously, not a burst campaign every time someone remembers.</p>

    <h2>Ask specifically, get quoted</h2>
    <p>"How did we do?" gets you "Great, fast shipping". Lovely, and useless: it could describe any store on earth. The reviews that move AI recommendations mention the product, the use case and the outcome, because those are the details a model can match to a buyer's question.</p>
    <p>Prompt for them. Ask about the specific product by name, and nudge with the attributes buyers care about: "How's the fit? What are you using it for? How does it compare to what you had before?" Each answered question is a searchable, quotable fact about your product, written by someone the machine trusts more than you.</p>

    <h2>The post-purchase sequence</h2>
    <ol>
      <li><strong>Time it to delivery plus real usage.</strong> Long enough to have genuinely used the product: days for consumables, weeks for durables.</li>
      <li><strong>One ask, one product, one click.</strong> The email asks for a review of the specific product with the form embedded or one tap away. Every extra step halves completion.</li>
      <li><strong>Follow up once.</strong> A single gentle nudge a week later to non-responders. Then stop.</li>
      <li><strong>Respond to what arrives</strong>, especially the critical ones. Future buyers and machines both read how you handle a problem.</li>
    </ol>

    <h2>Play it clean (the AU/NZ rules)</h2>
    <p>Consumer law here is blunt: no fake reviews, no editing or suppressing genuine negatives, no review gating (asking only happy customers), and any incentive must be offered for a review, never for a positive one, and disclosed. Beyond legality, a 4.6 with real texture converts better than a suspicious 5.0 anyway. The negative review you answer well is a trust asset.</p>
""",
"donow": [
"Check your last 90 days of review count versus the 90 before. If it's flat or falling, your sequence is the fix: set up the timed ask with product-specific prompts this week. Then reply to your five most recent reviews, including every negative.",
],
"prompt": """Write my post-purchase review sequence. I sell [products], typical delivery is [X days], and a customer knows if they love it after about [X days/weeks]. Draft: 1) the first ask email (timed, one product, specific attribute prompts for my category), 2) the single follow-up, 3) response templates for a glowing review, a mixed review, and an angry one, in my voice: [paste voice note]. Keep every ask compliant for NZ/AU: no gating, no incentives for positive reviews.""",
"app": True,
},
{
"id": "3.3",
"slug": "3-3-third-party-review-platforms",
"title": "Third-party review platforms",
"h1": 'Third-party review <span class="te-editorial">platforms</span>',
"description": "Trustpilot, Google, ProductReview and the platforms AI actually reads: where to build profiles, why crawlability is strange, and how to respond like a pro.",
"tag": "Authority",
"mins": 6,
"lead": "Reviews on your own site are you hosting your own applause. Reviews on platforms you don't control are evidence, and that's exactly why AI weighs them heavier.",
"body": """
    <h2>Independence is the point</h2>
    <p>A third-party platform is credible precisely because you can't edit it. The strangest proof of how much this matters: <strong>brands with a Trustpilot profile are 3x more likely to be cited by AI, even though Trustpilot blocks AI crawlers.</strong> <span class="src">(AirOps research)</span> The reputation leaks out through aggregate scores, mentions and syndication even when the reviews themselves are walled off. Presence on trusted platforms changes how the whole web describes you.</p>

    <h2>Pick your platforms deliberately</h2>
    <p>You can't be everywhere and don't need to be. The APAC-relevant shortlist:</p>
    <ul>
      <li><strong>Google reviews</strong>: non-negotiable for any brand, and the most visible surface in classic search.</li>
      <li><strong>Trustpilot</strong>: the ecommerce default, strong in NZ/AU/UK, and the 3x stat above speaks for itself.</li>
      <li><strong>ProductReview.com.au</strong>: heavily weighted for the Australian market specifically.</li>
      <li><strong>Facebook recommendations</strong>: low effort, still read.</li>
      <li><strong>Your category's specialist platforms</strong>: outdoor gear, beauty, supplements all have their own trusted reviewers, and category-specific trust runs deep.</li>
    </ul>
    <p>Claim and complete every profile you choose: logo, description, links, consistent brand details everywhere (entity consistency, again). An unclaimed profile with 12 unanswered reviews is worse than no profile.</p>

    <h2>Route the velocity</h2>
    <p>Your post-purchase sequence from 3.2 is the engine; now point some of its traffic off-site. The simple pattern: alternate your asks between on-site reviews and your chosen platform, or route your happiest segment (repeat buyers, high NPS) to the third-party ask. On-site fuels conversion, off-site fuels reputation. You need both flowing.</p>

    <h2>Respond like it's marketing, because it is</h2>
    <p>Every response is public copy. Thank the specific detail in positive reviews (it reinforces the attribute for the next reader). For negatives: acknowledge fast, take it to resolution, then close the loop publicly. Machines summarising your brand read the pattern of how you respond, and so does every human deciding whether to trust the 4.6.</p>
""",
"donow": [
"Pick your two platforms (Google plus one). Claim and complete both profiles today, respond to every unanswered review sitting on them, then wire the third-party ask into your 3.2 sequence.",
],
"prompt": """Audit my third-party review presence. Brand: [name], market: [NZ/AU], category: [category]. 1) Find my profiles (claimed or not) on Google, Trustpilot, ProductReview.com.au, Facebook and any category-specific platforms. 2) Summarise the state of each: count, average, recency, unanswered reviews. 3) Compare with [competitor]. 4) Recommend which two platforms I should focus on and why, and draft responses for my three oldest unanswered reviews.""",
"app": True,
},
{
"id": "3.4",
"slug": "3-4-reddit-quora-and-the-forums-ai-reads",
"title": "Reddit, Quora and the forums AI reads",
"h1": 'Reddit, Quora and the forums AI <span class="te-editorial">reads</span>',
"description": "Reddit appears in up to 24% of AI answers and drives 4x higher ChatGPT citation rates. How to show up in communities credibly, without getting banned.",
"tag": "Authority",
"mins": 7,
"lead": "When AI wants a real opinion, it reads the places real people argue about products. One platform dominates that diet, and most brands are terrified of it. That's the opportunity.",
"body": """
    <h2>The numbers on community citations</h2>
    <ul>
      <li>Reddit appears in <strong>21-24% of AI answers</strong>: it's the #1 cited domain in Perplexity and Google AI Mode, and #2 in ChatGPT.</li>
      <li>Brands with a Reddit presence see a <strong>4x higher ChatGPT citation rate</strong>.</li>
      <li><strong>88% of Reddit citations come from category-level queries</strong> ("best merino socks"), not branded ones. People discover brands there.</li>
      <li><strong>99% of Reddit citations point to discussion threads</strong>, not brand pages. The conversation is the asset. <span class="src">(AirOps research, 2026)</span></li>
    </ul>
    <p>Quora and the classic forums (plus the big category Facebook groups) run the same logic at smaller scale: real people, real opinions, machine-readable trust.</p>

    <h2>The rules of engagement</h2>
    <p>Communities detect marketing like an immune system, and getting banned is worse than never showing up. The playbook that works:</p>
    <ol>
      <li><strong>Find your rooms.</strong> The 3-5 subreddits and forums where your category genuinely gets discussed. Search your category plus your brand and competitors to map them.</li>
      <li><strong>Declare yourself.</strong> A named account, flaired or bio'd as the founder/team. Transparency converts scepticism into respect. Astroturfing, when caught (and it gets caught), torches everything this module builds.</li>
      <li><strong>Be the expert, mostly.</strong> The 90/10 rule: 90% genuinely useful answers with no brand mention, 10% mentioning your product where it's honestly the answer, disclosure included. The 90% is what earns the right to the 10%.</li>
      <li><strong>Show up when named.</strong> Someone asks "anyone tried [your brand]?": that thread will be read by buyers and models for years. Answer questions honestly, own any failures, fix things publicly.</li>
    </ol>

    <h2>Founder beats brand account</h2>
    <p>A named human ("founder at [brand], flagging my bias") gets warmth and upvotes a logo never will. Communities want to talk to people. Conveniently, the same founder presence is the whole of lesson 3.6.</p>
""",
"donow": [
"Map your rooms today: search Reddit for your category and your brand name. Read the top 10 threads. If your brand has ever been mentioned, read every word of those threads, that's your reputation as AI currently reads it. Set up your declared account before you post anything.",
],
"prompt": """Map my community landscape. Category: [category], brand: [name], market: [NZ/AU/global]. 1) Find the subreddits, Quora topics and forums where my category gets discussed, with rough activity levels. 2) Find every thread mentioning my brand and summarise the sentiment honestly. 3) Find the 10 most-viewed unanswered or poorly-answered questions in my category I could credibly answer. 4) Draft my declared-account bio and a 90/10 engagement plan for the next month.""",
"app": True,
},
{
"id": "3.5",
"slug": "3-5-digital-pr-and-earned-media",
"title": "Digital PR and earned media",
"h1": 'Digital PR and earned <span class="te-editorial">media</span>',
"description": "48% of LLM citations come from earned media. Get into the roundups, the press and the publications AI trusts, without a PR agency retainer.",
"tag": "Authority",
"mins": 7,
"lead": "Here's the channel doing the heaviest lifting in the 77%: media coverage. Almost half of what LLMs cite is earned media. You don't need a PR agency to earn it, you need a story and a system.",
"body": """
    <h2>Why media moves models</h2>
    <p><strong>48% of LLM citations come from earned media.</strong> <span class="src">(AirOps research)</span> And the compounding version: brands present on Wikidata and Wikipedia plus four third-party platforms achieve <strong>2.8x citation likelihood</strong>. Media coverage is how a small brand borrows a big publication's trust, and models inherit that trust wholesale.</p>
    <p>The most valuable single placement for ecommerce: <strong>the roundup</strong>. "Best [category] 2026" articles on trusted publications are exactly what AI retrieves when someone asks the same question in chat. Getting added to three good roundups can outweigh a year of link building.</p>

    <h2>Earn it without an agency</h2>
    <ol>
      <li><strong>Target where AI already looks.</strong> Ask ChatGPT and Perplexity your category's buying questions and note which publications get cited. That list, plus your local business media and category blogs, is your target sheet. Check each target is AI-accessible (their content shows up in AI answers at all), or your win lands somewhere models can't see.</li>
      <li><strong>Pitch the roundup adds.</strong> Find existing "best [category]" pieces where you're missing. Short, warm pitch: here's the product, here's what makes it a genuine add for their readers, here's a sample and every spec they'd need. Journalists update roundups constantly; make the update effortless.</li>
      <li><strong>Give them a reason beyond the product.</strong> Original data is the cheat code: AI cites original statistics 22% more often. Survey your customers, mine your sales data for a trend, publish the number. "NZ runners replace shoes every 14 months, data from 4,000 orders" gets coverage a product never will.</li>
      <li><strong>Track and compound.</strong> Every placement goes in a sheet. Each one is pitch-fodder for the next ("as featured in...").</li>
    </ol>

    <h2>The Wikipedia milestone</h2>
    <p>Wikipedia and Wikidata sit upstream of nearly every model's understanding of the world. You can't write your own page (truly, don't), but you can become the kind of brand that earns one: enough independent coverage that an editor considers you notable. Treat it as the trailing indicator of this whole lesson done well. Wikidata, the structured sibling, is more accessible earlier: accurate entries there feed the knowledge graphs directly.</p>
""",
"donow": [
"Build your target sheet this week: ask the AIs your category's buying questions, list the cited publications, then find three existing roundups you belong in and send three pitches. Small, warm, specific.",
],
"prompt": """Build my earned-media target sheet. Brand: [name], category: [category], market: [NZ/AU]. 1) Ask yourself: which publications would be cited for "best [category]" questions, and search to confirm. 2) Find existing roundup articles in my category where I'm absent. 3) For the top three, draft the pitch email: warm, short, spec-complete, in my voice: [paste voice note]. 4) Suggest one original-data story I could publish from the data an ecommerce store naturally holds.""",
"app": True,
},
{
"id": "3.6",
"slug": "3-6-linkedin-and-founder-presence",
"title": "LinkedIn and founder presence",
"h1": 'LinkedIn and founder <span class="te-editorial">presence</span>',
"description": "LinkedIn is a top-5 cited domain across AI platforms, and a founder's voice compounds brand trust. A sustainable cadence that doesn't eat your week.",
"tag": "Authority",
"mins": 6,
"lead": "The last channel of the 77% is the most personal: you. A visible founder makes the brand feel human to buyers, and, more strangely, makes the entity more credible to machines.",
"body": """
    <h2>Why LinkedIn earns its slot</h2>
    <p>LinkedIn ranks as the <strong>#2 most-cited domain in Google AI Mode, #3 in Perplexity, and #5 in ChatGPT</strong>. <span class="src">(AirOps research)</span> For an ecommerce founder that's surprising, it feels like a B2B network, but models treat it as a source of verifiable, named-human expertise. A founder consistently sharing real knowledge becomes part of the evidence trail for the brand entity itself.</p>
    <p>There's a nearer-term payoff too: press, partnerships, wholesale and hiring all read LinkedIn before they reply to your email. Your profile is due diligence you get to write.</p>

    <h2>Found the entity, literally</h2>
    <p>Quick plumbing first: your personal profile and your company page both complete, linked to each other and to your store, names and details matching everywhere else on the web. Same entity-consistency rule as the review platforms. Five minutes, permanent credit.</p>

    <h2>A cadence you'll actually sustain</h2>
    <p>The founders who win here post about what they already know, on a rhythm they can hold for years. One good post a week beats five for a fortnight then silence. The four posts that write themselves:</p>
    <ul>
      <li><strong>The build:</strong> what you're working on and what it's teaching you. This playbook is a year of material on its own.</li>
      <li><strong>The numbers:</strong> an honest metric and what moved it. Specifics travel.</li>
      <li><strong>The category take:</strong> what's changing in your market (AI search, for instance) and what you're doing about it.</li>
      <li><strong>The customer story:</strong> a real problem a real customer brought you, and what happened.</li>
    </ul>
    <p>Write like you talk. The polished-corporate register dies on LinkedIn now, and it's also the one register machines can't attribute any personality to.</p>

    <h2>Module 3, done</h2>
    <p>Reviews flowing, platforms claimed, communities engaged, media earned, founder visible. Every channel of the 77% now has a system behind it. What's left is proving it all works, which is Module 4.</p>
""",
"donow": [
"Complete the plumbing today (profile, company page, cross-links). Then book 30 minutes weekly for one post, and write the first one now: what you're changing about your store after Module 1 of this playbook. Genuinely useful, and it starts the trail.",
],
"prompt": """Draft my next four LinkedIn posts, one per week. I'm the founder of [brand], we sell [products], and here's what's true right now: current project [X], a real number I can share [X], my take on AI search in my category [X], a recent customer story [X]. My voice: [paste voice note]. Each post: a hook first line, a specific middle, no hashtag soup, no corporate polish, ends with something people can respond to.""",
"app": True,
},
]
