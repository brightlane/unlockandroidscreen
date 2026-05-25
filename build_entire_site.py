import os
from datetime import datetime

def get_base_css():
    """Returns a centralized, high-conversion design system tailored for interactive SaaS conversions."""
    return """<link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #ec4899; /* Outgrow Vibrant Pink Accent */
            --primary-dark: #db2777;
            --secondary: #0f172a;
            --accent: #10b981; /* High CTR Conversion Green */
            --accent-dark: #059669;
            --text-main: #334155;
            --text-dark: #0f172a;
            --bg-light: #f8fafc;
            --border: #e2e8f0;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: 'Plus Jakarta Sans', system-ui, sans-serif; line-height: 1.6; color: var(--text-main); background: #ffffff; -webkit-font-smoothing: antialiased; }
        .container { max-width: 1000px; margin: 0 auto; padding: 0 24px; }
        .hero { padding: 80px 0 60px 0; text-align: center; background: linear-gradient(135deg, #ec4899, #f59e0b); color: white; border-bottom: 1px solid var(--border); border-radius: 0 0 24px 24px; }
        .hero h1 { font-size: 3rem; font-weight: 800; margin-bottom: 20px; letter-spacing: -0.03em; color: white; }
        .hero-lead { font-size: 1.25rem; color: rgba(255, 255, 255, 0.9); max-width: 750px; margin: 0 auto 32px auto; }
        .cta-btn { display: inline-flex; align-items: center; background: var(--accent); color: white; padding: 16px 36px; font-size: 1.2rem; font-weight: 700; text-decoration: none; border-radius: 12px; box-shadow: 0 10px 25px rgba(16,185,129,0.35); transition: all 0.2s ease; }
        .cta-btn:hover { background: var(--accent-dark); transform: translateY(-2px); box-shadow: 0 12px 30px rgba(16,185,129,0.45); }
        .disclosure { font-size: 0.85rem; color: rgba(255,255,255,0.8); margin-top: 16px; }
        h2 { font-size: 2.2rem; color: var(--text-dark); margin: 44px 0 20px 0; letter-spacing: -0.02em; }
        .card-matrix { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 20px; margin: 32px 0; }
        .feature-card { background: white; border: 1px solid var(--border); padding: 24px; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); }
        .feature-card h3 { color: var(--text-dark); font-size: 1.25rem; margin-bottom: 10px; }
        table { width: 100%; border-collapse: collapse; margin: 24px 0; font-size: 1rem; }
        th, td { border: 1px solid var(--border); padding: 14px; text-align: left; }
        th { background: var(--bg-light); color: var(--text-dark); font-weight: 700; }
        .calc-box { background: var(--secondary); color: white; padding: 40px; border-radius: 24px; margin: 48px 0; }
        .calc-box h3 { color: white; font-size: 1.6rem; margin-bottom: 8px; }
        .slider-container { margin: 32px 0; }
        input[type=range] { width: 100%; accent-color: var(--primary); margin: 12px 0; cursor: pointer; }
        .calc-results { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; background: rgba(255,255,255,0.05); padding: 24px; border-radius: 16px; }
        .stat-label { font-size: 0.85rem; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.05em; }
        .stat-val { font-size: 1.8rem; font-weight: 800; margin-top: 4px; }
        .blog-list { list-style: none; margin: 24px 0; display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
        @media (max-width: 768px) { .blog-list { grid-template-columns: 1fr; } }
        .blog-list li { background: var(--bg-light); border: 1px solid var(--border); padding: 20px; border-radius: 12px; }
        .blog-list a { color: var(--text-dark); font-weight: 700; text-decoration: none; font-size: 1.1rem; display: block; margin-bottom: 4px; }
        .blog-list a:hover { color: var(--primary); }
        .affiliate-disclosure { background: #fffbeb; border-left: 4px solid #f59e0b; padding: 15px; margin: 20px 0; font-size: 0.9em; border-radius: 4px; color: #78350f; }
        footer { border-top: 1px solid var(--border); padding: 40px 0; text-align: center; font-size: 0.9rem; color: #64748b; background: var(--bg-light); margin-top: 80px; }
        @media (max-width: 768px) { .calc-results { grid-template-columns: 1fr; } .hero h1 { font-size: 2.2rem; } }
    </style>"""

def generate_programmatic_data():
    """Generates 100 highly contextual data blocks to prevent Google duplicate content flags."""
    niches = [
        {"name": "Digital Marketing Agencies", "hook": "client retainers and campaign pitches", "metric": "pitch conversion metrics"},
        {"name": "SaaS Startups", "hook": "product demo upgrades and trial signs", "metric": "trial signup volume"},
        {"name": "Real Estate Brokers", "hook": "home value estimation lookups", "metric": "seller listings"},
        {"name": "E-commerce Brands", "hook": "interactive product recommendation paths", "metric": "average cart values"},
        {"name": "Fitness Coaches", "hook": "personalized caloric macronutrient calculators", "metric": "coaching client retention"},
        {"name": "Financial Advisors", "hook": "interactive net-worth assets and retirement forecasts", "metric": "inbound high-net-worth consults"},
        {"name": "Insurance Brokers", "hook": "instant personalized auto and home rate premium estimators", "metric": "policy quotes generated"},
        {"name": "Mortgage Lenders", "hook": "real-time amortization payment tables", "metric": "pre-approval applications completed"},
        {"name": "Online Educators", "hook": "skill level mastery diagnostics", "metric": "student course enrollment levels"},
        {"name": "B2B Sales Teams", "hook": "complex platform ROI metrics engines", "metric": "sales discovery calls scheduled"},
        {"name": "Conversion Rate Optimizers", "hook": "interactive site audit checklists", "metric": "revenue-per-visitor optimization output"},
        {"name": "SEO Consultants", "hook": "domain authority impact evaluation sheets", "metric": "monthly SEO retainers closed"},
        {"name": "Growth Hackers", "hook": "viral assessment loops and feedback systems", "metric": "organic network invitations"},
        {"name": "Affiliate Marketers", "hook": "value-packed recommendation sorting questions", "metric": "affiliate commission revenue"},
        {"name": "Local Service Businesses", "hook": "fair-market project estimator tables", "metric": "onsite service quotes booked"},
        {"name": "Ebook Publishers", "hook": "reader content preference matching parameters", "metric": "digital download book orders"},
        {"name": "Creative Agencies", "hook": "brand design aesthetic selection matrices", "metric": "premium design clients signed"},
        {"name": "Crypto Platforms", "hook": "staking rewards APY simulators", "metric": "active wallet registrations"},
        {"name": "Healthcare Recruiters", "hook": "travel nurse placement compatibility screening", "metric": "qualified nursing hires"},
        {"name": "Legal Consultants", "hook": "case damage settlement evaluation forms", "metric": "retained legal case evaluations"}
    ]
    
    topics = [
        {"pattern": "outgrow-review-for-{slug}", "title": "Outgrow Review 2026: The Best Funnel Upgrade for {niche}"},
        {"pattern": "how-to-build-calculators-for-{slug}", "title": "How to Generate 3x More Leads for {niche} Using Calculators"},
        {"pattern": "outgrow-pricing-guide-for-{slug}", "title": "Outgrow Pricing Analysis: Which Tier Fits a Scaling {niche}?"},
        {"pattern": "outgrow-vs-typeform-for-{slug}", "title": "Outgrow vs Typeform for {niche}: Stop Using Static Forms"},
        {"pattern": "interactive-lead-generation-for-{slug}", "title": "Top 5 High-Converting Interactive Content Blueprints for {niche}"}
    ]
    
    posts = []
    for item in niches:
        niche = item["name"]
        niche_slug = niche.lower().replace(" ", "-")
        for topic in topics:
            slug = topic["pattern"].format(slug=niche_slug)
            title = topic["title"].format(niche=niche)
            desc = f"Discover why switching from standard landing pages to interactive forms helps a modern {niche} secure up to 3x higher opt-in metrics."
            content = (
                f"For any scaling {niche}, traditional text-heavy landing pages are suffering from serious conversion decay. "
                f"Audiences want immediate, personalized value, and deploying interactive assets—like automated {item['hook']}—gives them that value in seconds. "
                f"By using native interactive frameworks through Outgrow, a modern {niche} can scale up their {item['metric']} up to 3x higher compared to static lead capture templates. "
                f"Whether you need simple, drag-and-drop lead scoring parameters or advanced HubSpot/Zapier webhooks to segment your list instantly, "
                f"Outgrow streamlines your data flows so your sales pipelines convert predictably and your overall customer acquisition costs shift sharply downward."
            )
            posts.append({"slug": slug, "title": title, "desc": desc, "content": content})
    return posts

def build_entire_site():
    # ADJUST THIS path to your final destination domain name layout
    base_url = "https://brightlane.github.io/SkyScanner" 
    affiliate_url = "https://share.outgrow.biz/u8908n3q0pp7?utm_source=deploy"
    today_str = datetime.today().strftime('%Y-%m-%d')

    blog_posts = generate_programmatic_data()
    os.makedirs("blog", exist_ok=True)
    
    # Pre-populate all urls for the sitemap mapping loop correctly
    urls_for_sitemap = [f"{base_url}/index.html"]
    for post in blog_posts:
        urls_for_sitemap.append(f"{base_url}/blog/{post['slug']}.html")

    # ==========================================
    # 1. BUILD INDEX.HTML HUB NODE
    # ==========================================
    index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Outgrow Review 2026: Best Quiz/Calculator Builder - 7-Day Trial</title>
    <meta name="description" content="Outgrow: $25/mo Freelancer (100 responses), $95 Business (1K). Interactive quizzes, calculators, chatbots, lead magnets. 3x lead conversion vs static pages. Perfect for agencies.">
    <link rel="canonical" href="{base_url}/index.html" />
    {get_base_css()}
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Product",
      "name": "Outgrow Interactive Content Suite",
      "description": "Premium quiz, calculation, and chatbot builder engine designed to triple lead capture performance metrics.",
      "brand": {{"@type": "Brand", "name": "Outgrow"}},
      "offers": {{
        "@type": "AggregateOffer",
        "priceCurrency": "USD",
        "lowPrice": "25",
        "highPrice": "545",
        "offerCount": "4"
      }}
    }}
    </script>
</head>
<body>
    <header class="hero">
        <div class="container">
            <h1>🧠 Outgrow 2026: #1 Interactive Quiz/Calculator Builder</h1>
            <p class="hero-lead">Quizzes + calculators + chatbots + surveys = 3x more leads than static pages. Drag-drop builder. 1,000+ templates. Perfect for affiliate lead magnets & agency clients.</p>
            <div>
                <a href="{affiliate_url}" class="cta-btn" rel="sponsored">Start 7-Day Free Trial</a>
            </div>
            <p class="disclosure">Links earn commissions at no extra operational premium to your custom setup.</p>
        </div>
    </header>

    <main class="container">
        <div class="affiliate-disclosure">
            <strong>Affiliate Disclosure:</strong> Links earn commissions at no extra cost.
        </div>

        <h2>Why Outgrow Wins for Agencies</h2>
        <p>Interactive content converts 3x better than static landing pages. AI quiz generator + conditional logic + 1,000+ templates. Embed anywhere (custom domains Business+).</p>

        <div class="card-matrix">
            <div class="feature-card">
                <h3>🧩 Quiz/Calculator Builder</h3>
                <p>Drag-drop + conditional logic + personalized results</p>
            </div>
            <div class="feature-card">
                <h3>🤖 AI Content Generator</h3>
                <p>Auto-create quizzes in your brand tone (minutes)</p>
            </div>
            <div class="feature-card">
                <h3>📊 Lead Qualification</h3>
                <p>Score leads automatically. Segment by quiz results</p>
            </div>
            <div class="feature-card">
                <h3>🔗 1,000+ Integrations</h3>
                <p>HubSpot, Mailchimp, ActiveCampaign, Stripe, Zapier</p>
            </div>
        </div>

        <section class="calc-box">
            <h3>Calculate Your Lead Pipeline Lift</h3>
            <div class="slider-container">
                <label for="trafficRange" style="font-weight: 600; display: block; margin-bottom: 8px;">Estimated Monthly Page Traffic: <span id="trafficLabel" style="color: var(--primary); font-weight:800;">5,000</span></label>
                <input type="range" id="trafficRange" min="1000" max="50000" step="1000" value="5000" oninput="updateCalculations(this.value)">
            </div>
            <div class="calc-results">
                <div>
                    <div class="stat-label">Standard Form Leads (Avg 2%)</div>
                    <div id="standardVal" class="stat-val" style="color: #ef4444;">100</div>
                </div>
                <div>
                    <div class="stat-label">Outgrow Interactive Leads (Avg 6%)</div>
                    <div id="interactiveVal" class="stat-val" style="color: var(--accent);">300</div>
                </div>
            </div>
        </section>

        <h2>Outgrow Pricing 2026</h2>
        <table>
            <tr><th>Plan</th><th>Price/mo</th><th>Responses/mo</th></tr>
            <tr><td>Freelancer</td><td>$25</td><td>100</td></tr>
            <tr><td>Business</td><td>$95</td><td>1,000</td></tr>
            <tr><td>Business Pro</td><td>$195</td><td>5,000</td></tr>
            <tr><td>Enterprise</td><td>$545</td><td>25,000</td></tr>
        </table>
        <p style="margin-bottom: 30px;"><strong>7-day FREE trial</strong>. Annual saves 10%.</p>

        <h2>Outgrow vs Typeform vs Interact Quiz</h2>
        <table>
            <tr><th>Feature</th><th>Outgrow</th><th>Typeform</th></tr>
            <tr><td>Calculators</td><td>✅ Yes</td><td>❌ No</td></tr>
            <tr><td>Lead Scoring</td><td>✅ Built-in</td><td>❌ Add-on</td></tr>
            <tr><td>AI Generator</td><td>✅ Yes</td><td>❌ No</td></tr>
            <tr><td>Custom Domains</td><td>✅ Business+</td><td>❌ $59+/mo</td></tr>
        </table>

        <h2>Perfect Agency Use Cases</h2>
        <ul style="margin: 20px 0; padding-left: 20px;">
            <li>SEO lead magnets: "What's your SEO score?" quizzes</li>
            <li>Affiliate offers: ROI calculators (3x conversions)</li>
            <li>PPC campaigns: Interactive quiz funnels</li>
            <li>Client retainers: "Website audit" assessments</li>
        </ul>

        <div style="background: #e8f5e8; padding: 35px; text-align: center; border-radius: 16px; margin: 40px 0; border: 1px solid #c2e7c2;">
            <h2 style="margin-top: 0;">3x Your Leads with Interactive Content</h2>
            <p style="margin-bottom: 20px; color: var(--text-main);">Join thousands of marketers using interactive funnels to lower acquisition overheads.</p>
            <a href="{affiliate_url}" class="cta-btn" rel="sponsored">7-Day Free Trial</a>
        </div>

        <h2>Deep-Dive Niche Optimization Directives</h2>
        <ul class="blog-list">"""
        
    for post in blog_posts:
        index_html += f'\n            <li><a href="blog/{post["slug"]}.html">→ {post["title"]}</a><p style="color:#64748b; font-size:0.9rem; margin-top:4px;">{post["desc"]}</p></li>'
        
    index_html += f"""
        </ul>
    </main>

    <footer>
        <div class="container">
            <p>© 2026 Benny Palmarino | Langhorne, PA | Conversion Optimization Specialist</p>
        </div>
    </footer>

    <script>
        function updateCalculations(val) {{
            const traffic = parseInt(val);
            document.getElementById('trafficLabel').innerText = traffic.toLocaleString();
            document.getElementById('standardVal').innerText = Math.round(traffic * 0.02).toLocaleString() + ' leads';
            document.getElementById('interactiveVal').innerText = Math.round(traffic * 0.06).toLocaleString() + ' leads';
        }}
        updateCalculations(5000);
    </script>
</body>
</html>"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(index_html.strip())

    # ==========================================
    # 2. BUILD THE 100 UNIQUE SUB-PAGES
    # ==========================================
    for post in blog_posts:
        slug = post["slug"]
        post_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{post["title"]}</title>
    <meta name="description" content="{post["desc"]}">
    <link rel="canonical" href="{base_url}/blog/{slug}.html" />
    {get_base_css()}
</head>
<body>
    <div class="container" style="padding-top: 50px;">
        <div style="margin-bottom: 24px;"><a href="../index.html" style="color: var(--primary); text-decoration:none; font-weight:700;">← Back to Performance Hub</a></div>
        <h1>{post["title"]}</h1>
        
        <article class="feature-card" style="background:#ffffff; margin-top:24px; border-left: 4px solid var(--primary); line-height:1.8;">
            <p style="font-size:1.15rem; color:var(--text-dark);">{post["content"]}</p>
        </article>

        <section class="calc-box" style="text-align:center; background: linear-gradient(135deg, var(--secondary) 0%, #1e293b 100%);">
            <h3 style="margin-bottom:12px;">Scale Up Lead Capture Channels Today</h3>
            <p style="color:#cbd5e1; margin-bottom:24px; max-width:600px; margin-left:auto; margin-right:auto;">Stop losing pipeline volume on stale, static web design forms. Spin up customized calculators and interactive quizzes to lower customer acquisition costs.</p>
            <a href="{affiliate_url}" class="cta-btn" rel="sponsored">Claim Your 7-Day Free Outgrow Gate</a>
        </section>
    </div>
    <footer>
        <div class="container">
            <p>© 2026 Benny Palmarino | Langhorne, PA</p>
        </div>
    </footer>
</body>
</html>"""
        with open(f"blog/{slug}.html", "w", encoding="utf-8") as f:
            f.write(post_html.strip())

    # ==========================================
    # 3. BUILD AGENT COMPONENT: LLMS.TXT
    # ==========================================
    llms_txt = f"# Outgrow Conversion Directory Context\n> Programmatic matrix mappings for search indexing engines and LLM scrapers.\n\n## Platform Nodes\n"
    llms_txt += f"- [Outgrow Performance Review 2026]({base_url}/index.html): Core pricing structures and feature assessments.\n"
    for post in blog_posts:
        llms_txt += f"- [{post['title']}]({base_url}/blog/{post['slug']}.html): {post['desc']}\n"
    with open("llms.txt", "w", encoding="utf-8") as f:
        f.write(llms_txt.strip())

    # ==========================================
    # 4. BUILD ACCESS COMPONENT: ROBOTS.TXT
    # ==========================================
    with open("robots.txt", "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {base_url}/sitemap.xml")

    # ==========================================
    # 5. BUILD SEO INDEX: SITEMAP.XML
    # ==========================================
    sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for url in urls_for_sitemap:
        sitemap_xml += f"    <url>\n        <loc>{url}</loc>\n        <lastmod>{today_str}</lastmod>\n        <changefreq>daily</changefreq>\n        <priority>0.8</priority>\n    </url>\n"
    sitemap_xml += "</urlset>"
    
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap_xml.strip())
        
    print(f"Success! Built 1 Hub, {len(blog_posts)} Context-Rich Pages, robots.txt, llms.txt, and sitemap.xml layouts.")

if __name__ == "__main__":
    build_entire_site()
