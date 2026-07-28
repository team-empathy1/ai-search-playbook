# Module 4 · Keep winning — measurement & rhythm
LESSONS = [
{
"id": "4.1",
"slug": "4-1-measure-what-matters",
"title": "Measure what matters",
"h1": 'Measure what <span class="te-editorial">matters</span>',
"description": "Re-run your baseline, track AI share of voice and sentiment, and watch competitors: the measurement layer that tells you the system is working.",
"tag": "Measurement",
"mins": 6,
"lead": "You started this playbook by writing down a score. Now you build the habit of measuring against it, because in AI search the scoreboard is a conversation, and you have to keep asking.",
"body": """
    <h2>Re-run the baseline</h2>
    <p>Back in lesson 0.2 you scored yourself out of 100 and saved the date. Re-run that scorecard now, honestly, same gating rules. If you've worked the modules, Technical and Content have almost certainly moved. Authority moves slower; that's its nature, and it's why it's the moat.</p>
    <p>Keep every score. The trendline is the point: it's how you know the asset is compounding, and it's what makes the quarterly effort feel like progress instead of chores.</p>

    <h2>Track share of voice</h2>
    <p>The AI-era metric that matters most: <strong>when buyers ask the questions in your category, how often are you in the answer?</strong></p>
    <p>The manual version costs an hour a month. Take your 10-15 most valuable buying questions (your prompt list from lesson 0.1 and Module 2's research). Ask each one in ChatGPT, Perplexity and Google AI Mode. Log: were you named, in what position, with what sentiment, and who else was named. Same questions, same platforms, every month.</p>
    <p>Track each platform separately. <strong>Only 11% of domains cited by ChatGPT are also cited by Perplexity</strong> <span class="src">(AirOps research)</span>, so being visible in one says nothing about the others. Three columns, not one.</p>

    <h2>Watch the competitors in the answers</h2>
    <p>Your monthly log doubles as competitor intel. Who keeps showing up? What sources do the models cite when recommending them? Those citations are the exact roundups, platforms and threads your Module 3 work should target next. Reverse-engineering the winners' evidence trail is the whole competitive strategy, and it's sitting in the answers.</p>

    <h2>Sentiment is the silent half</h2>
    <p>Being named is half the game; how you're described is the other half. "Popular but pricey" steering buyers away is a different problem from not appearing at all, and it's fixed in different places (usually reviews and community threads, Module 3). Log the adjectives the models use about you. They're your reputation, compressed.</p>
""",
"donow": [
"Build your tracking sheet today: your 10-15 questions down the side, ChatGPT / Perplexity / Google AI Mode across the top, named yes-no, position, sentiment, competitors cited. Run month one now, and calendar the monthly re-run.",
],
"prompt": """Here are my category's buying questions: [paste 10-15]. Here's this month's log of AI answers: [paste what each platform said, or the named brands + sources per question].

Analyse: 1) my share of voice per platform (questions where I'm named / total), 2) sentiment summary: the exact adjectives used about me, 3) the competitor leaderboard, 4) the sources cited most across all answers, ranked, flagging which ones I have no presence on, 5) the three moves most likely to lift next month's share.""",
"app": True,
},
{
"id": "4.2",
"slug": "4-2-prove-the-money",
"title": "Prove the money",
"h1": 'Prove the <span class="te-editorial">money</span>',
"description": "Find the traffic ChatGPT and Perplexity send you in GA4, tie it to revenue, and see whether AI visitors really do convert better. Spoiler: they do.",
"tag": "Measurement",
"mins": 6,
"lead": "Share of voice tells you the system is working. This lesson tells you what it's worth, in dollars, so the effort survives contact with your accountant.",
"body": """
    <h2>AI traffic hides in your referrals</h2>
    <p>When someone clicks through from ChatGPT or Perplexity, it lands in your analytics as a referral: chatgpt.com, perplexity.ai, copilot.microsoft.com, gemini.google.com. GA4 sees it all; it just doesn't group it for you.</p>
    <p>The fix is one custom piece of setup: build a channel group or an exploration in GA4 that collects those referral sources into one "AI traffic" bucket. Twenty minutes, and every AI-referred session, order and dollar is visible from then on. (Google's AI Mode traffic mostly hides inside ordinary google organic, so treat your measured AI number as the floor, the real figure is higher.)</p>

    <h2>The numbers to pull monthly</h2>
    <ol>
      <li><strong>Sessions from AI sources</strong>, and the trend. Industry-wide, AI referral traffic is running at 12-18% of referral traffic and growing roughly 1% a month, so a flat line means you're losing share while the pool grows.</li>
      <li><strong>Revenue and conversion rate from AI traffic</strong>, against your site average. The benchmark you're hoping to see: AI visitors convert <strong>31% better</strong> than non-branded organic <span class="src">(Profound, 94 brands)</span>. They arrive pre-sold, because the AI already did the comparison for them.</li>
      <li><strong>Landing pages of AI visits.</strong> This tells you which content is earning citations that actually get clicked, which is Module 2's report card.</li>
      <li><strong>Average order value of AI visitors</strong> versus everyone else. Often higher, and it changes what a citation is worth.</li>
    </ol>

    <h2>Count the invisible with a proxy</h2>
    <p>The uncomfortable truth from lesson 0.1 still applies: 93% of AI sessions end without a click, so your GA4 number captures a sliver of the influence. The proxy that catches more: <strong>branded search volume and direct traffic trends</strong>. When AI recommends you, people google your name. A rising branded-search line alongside rising share of voice is the influence showing up. Some stores add a "how did you hear about us" field at checkout with an AI option; crude, and genuinely useful.</p>
    <p>Put it on one page: share of voice, AI sessions, AI revenue, branded search trend. That's your AI dashboard, and it's the page that justifies every hour this playbook asked of you.</p>
""",
"donow": [
"Set up the AI channel group in GA4 today (chatgpt.com, perplexity.ai, copilot, gemini as one bucket). Then pull the last 90 days retroactively: sessions, revenue, conversion rate versus site average. Whatever the number is, it's your baseline, and it only grows from here.",
],
"prompt": """Here's my GA4 data: AI-source sessions [X], revenue [$X], conversion rate [X%] versus site average [X%], AOV [$X] vs [$X], top AI landing pages [list], and my branded search trend from Search Console [paste]. Analyse: 1) what AI traffic is actually worth to me monthly (direct + a reasonable influence estimate given 93% of AI sessions are zero-click), 2) how my AI conversion premium compares to the 31% benchmark, 3) which cited content is pulling weight and what that says about where to invest next quarter.""",
"app": True,
},
{
"id": "4.3",
"slug": "4-3-the-operating-rhythm",
"title": "The operating rhythm",
"h1": 'The operating <span class="te-editorial">rhythm</span>',
"description": "The weekly, monthly and quarterly cadence that keeps the whole system compounding without eating your calendar: observe, decide, delegate.",
"tag": "Rhythm",
"mins": 5,
"lead": "Everything you've built is a system, and systems run on rhythm, a repeating cadence that's light enough to sustain and regular enough to compound. Here's the whole thing on one page.",
"body": """
    <h2>The loop: observe, decide, delegate</h2>
    <p>Each cycle is the same three moves. <strong>Observe:</strong> check the scoreboard (share of voice, AI revenue, decay, reviews). <strong>Decide:</strong> pick the few actions the data actually justifies. <strong>Delegate:</strong> hand each one to the right pair of hands, yours, your team's, or increasingly an AI's. The trap this protects you from: doing everything, reactively, forever.</p>

    <h2>Weekly, 30 minutes</h2>
    <ul>
      <li>Reviews: new ones in, responses out (3.2, 3.3).</li>
      <li>Community: any brand mentions or answerable threads in your rooms (3.4).</li>
      <li>One founder post (3.6).</li>
      <li>Content: whatever's next on the cluster plan moves one step (2.5).</li>
    </ul>

    <h2>Monthly, half a morning</h2>
    <ul>
      <li>Share-of-voice run: the questions, the three platforms, the log (4.1).</li>
      <li>The money pull: AI sessions, revenue, branded search trend (4.2).</li>
      <li>One media pitch or original-data move (3.5).</li>
      <li>Read the competitor citations and adjust next month's targets.</li>
    </ul>

    <h2>Quarterly, one honest afternoon</h2>
    <ul>
      <li>Re-score the maturity model, update the trendline (0.2, 4.1).</li>
      <li>Decay audit and top-five refreshes, before any new content (2.6).</li>
      <li>Cluster audit: orphans, dead-ends, weak anchors (2.7).</li>
      <li>Technical sweep: crawlers, schema validation, speed scores (Module 1).</li>
      <li>Plan next quarter's cluster and media targets from what the data said.</li>
    </ul>

    <h2>Protect the rhythm, not the tasks</h2>
    <p>Some weeks the 30 minutes becomes 10, and that's fine. The habit surviving matters more than any single cycle being complete, because the compounding comes from the years, not the weeks. Put the three recurring blocks in the calendar today and treat them like customer meetings: movable, never deletable.</p>
""",
"donow": [
"Book the three recurring blocks now: 30 minutes weekly, half a morning monthly, an afternoon quarterly. Then run your first weekly loop with the checklist above, whatever's overdue becomes this week's decide-and-delegate list.",
],
"prompt": """Act as my AI search operations manager. Here's this week's state: new reviews [X], community mentions [paste any], content in progress [status], last share-of-voice run [date + result]. Run my weekly loop: 1) what needs a response today, 2) what moves one step this week and what specifically that step is, 3) what gets skipped this week without guilt, 4) anything that should escalate to the monthly or quarterly agenda.""",
"app": True,
},
{
"id": "4.4",
"slug": "4-4-the-100-day-plan",
"title": "The 100-day plan",
"h1": 'The 100-day <span class="te-editorial">plan</span>',
"description": "The whole playbook sequenced into a day-by-day plan: foundations first, quick wins early, authority and AI proof compounding by day 100.",
"tag": "Rhythm",
"mins": 6,
"lead": "Everything in this playbook, laid end to end as one plan. If you're starting from scratch and want the fastest route to a store that compounds, run these 100 days in this order.",
"body": """
    <h2>Days 1-10: baseline and open doors</h2>
    <p>Run Module 0 completely: score yourself (0.2), plug Claude in (0.3), run the 30-minute audit (0.4). Then the two fastest technical wins: unblock every AI crawler (1.1) and verify Search Console (1.9). By day 10 you have a number, a plan, and open doors.</p>

    <h2>Days 11-40: the technical clean-up</h2>
    <p>Module 1, in order of impact: fix the URL traps (1.2), rewrite your top-20 product titles and descriptions (1.3), fill the GTIN gaps and validate schema (1.4), write real copy onto your five biggest collections (1.5), fix the internal link votes (1.6), connect the free feeds (1.7), set your agentic storefront stance (1.8), and clear the speed blockers (1.9). This is the least glamorous month and the highest-certainty gains; most stores finish it already visible in surfaces they'd never appeared in.</p>

    <h2>Days 41-80: become the answer</h2>
    <p>Module 2 as a production run: research week (2.1), cluster plan (2.2), then the drafting engine (2.3-2.5) shipping two pieces a week, starting with your money cluster's pillar and its highest-intent comparisons (2.4). Wire the links as you go (2.7). In parallel, start the flywheels that need calendar time to spin: the review sequence (3.2) and your community rooms (3.4), both light-touch from here on.</p>

    <h2>Days 81-100: authority and proof</h2>
    <p>Module 3's bigger swings: platforms claimed and responding (3.3), three roundup pitches out (3.5), founder cadence running (3.6). Then close the loop with Module 4: the share-of-voice baseline, the GA4 money view, the operating rhythm booked. Day 100: re-run your 0.2 scorecard and put the two numbers side by side.</p>

    <h2>What honestly to expect</h2>
    <p>Days 1-40 produce visible technical wins almost immediately. Content and authority compound slower: Google typically takes 60-90 days to fully reflect the changes, and AI answers refresh on their own uneven schedules. The realistic day-100 picture: a meaningfully higher maturity score, your first AI citations on long-tail questions, review velocity climbing, and a trendline that's finally yours. That's the asset, early. The years after are where it gets unfair.</p>
""",
"donow": [
"Open your calendar and block the phases: a day-10 checkpoint, a day-40 checkpoint, day-80, day-100. Put your current 0.2 score in the day-100 event so future-you gets the before-and-after in one glance. Then start day 1, which is literally a 30-minute audit.",
],
"prompt": """Build my personalised 100-day plan. My 0.2 scorecard: Technical [X], Content [X], Authority [X], Measurement [X]. My quick-win audit results: [paste from 0.4]. My capacity: [X hours/week, who's helping]. Re-sequence the standard plan (days 1-10 baseline, 11-40 technical, 41-80 content, 81-100 authority + proof) around my weakest pillars and real capacity, with a specific checkpoint list for days 10, 40, 80 and 100.""",
"app": True,
},
{
"id": "4.5",
"slug": "4-5-when-to-diy-when-to-bring-us-in",
"title": "When to DIY, when to bring us in",
"h1": 'When to DIY, when to bring us <span class="te-editorial">in</span>',
"description": "An honest build-vs-buy guide: what this playbook gets you on your own, where the ceiling is, and what working with Team Empathy actually looks like.",
"tag": "The path",
"mins": 5,
"lead": "Last lesson, and it's the honest conversation: what you can absolutely do yourself, where doing it yourself stops being the best use of you, and what the options look like from here.",
"body": """
    <h2>What DIY genuinely gets you</h2>
    <p>Everything in this playbook is the real methodology, the same one we install for clients. A founder or marketing lead running the 100-day plan with the weekly rhythm will reach a real Level 3, often brushing Level 4, on most pillars: doors open, catalogue structured, first clusters live, reviews flowing, measurement honest. For a lot of stores, that's the right place to operate, and if that's you, run the rhythm and enjoy the compounding. Genuinely.</p>

    <h2>Where the ceiling shows up</h2>
    <p>Three signals, from watching this play out across a lot of stores:</p>
    <ol>
      <li><strong>The rhythm keeps losing to the business.</strong> The weekly loop skips three weeks running because you're doing the actual job of running the store. The system compounds only while it runs.</li>
      <li><strong>Scale with consistency.</strong> One cluster in one market is a person's job. Ten clusters, refresh cycles, three markets, every piece on-voice: that's an operations problem, and ecommerce content ops is a genuinely different skill from ecommerce.</li>
      <li><strong>The last 20 points.</strong> From 60 to 80+ lives in the places DIY struggles: entity-linked schema at depth, digital PR that lands, authority quality (not volume). The gap between Structured and Certified is mostly specialist hours.</li>
    </ol>

    <h2>The options from here</h2>
    <p><strong>Keep running it yourself.</strong> The playbook stays yours, we keep it current as the models change, and the lessons' prompts get you a long way. <strong>Get the app.</strong> The AI Search OS for Shopify we're building runs the audits, the monitoring and the busywork of this playbook automatically, DIY, minus the grind. It's coming soon, and playbook readers hear first. <strong>Or have us install the whole thing.</strong> A done-for-you transformation: we take a store to Certified (80+) and hand you back a compounding asset with the rhythm running. It starts with a working session on your real data, and the honest version of this conversation, including "you don't need us yet" when that's true.</p>
    <p>Whichever path: you now know exactly how this game works, which puts you ahead of most of your category. The window from lesson 0.1 is still open. Go compound.</p>
""",
"donow": [
"Decide your path for the next quarter, out loud, to someone: DIY on the rhythm, wait for the app, or talk to us. Then take the one action that matches: book the weekly loop, join the app waitlist below, or book the diagnostic. The expensive option is deciding nothing.",
],
"prompt": """Help me make the build-vs-buy call honestly. My situation: maturity score [X/100], weakest pillars [X], hours I can genuinely give this weekly [X], team [who], revenue stage [rough band], and what stalled (if anything) during the playbook: [honest answer]. Recommend: DIY with the rhythm, DIY plus tooling, or done-for-you, with the reasoning, the risks of each for someone in my position, and what I should have achieved before re-evaluating in 90 days.""",
"app": True,
},
]
