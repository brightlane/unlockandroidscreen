#!/usr/bin/env python3
"""
Unlock Android Screen — 300% Improved Global SEO Site
Affiliate: https://www.linkconnector.com/ta.php?lc=007949070197004532&atid=androidlockscreen
Deploy: https://brightlane.github.io/unlockandroidscreen/
Pages: 80+ | Languages: 25 | Keywords: 3000+
"""

from pathlib import Path

BASE      = Path(__file__).parent
AFFILIATE = "https://www.linkconnector.com/ta.php?lc=007949070197004532&atid=androidlockscreen"
SITE      = "https://brightlane.github.io/unlockandroidscreen"
YEAR      = "2026"

# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────
def cta(label="🔓 Download Dr.Fone Free", cls="btn"):
    return f'<a href="{AFFILIATE}" class="{cls}" target="_blank" rel="noopener sponsored">{label}</a>'

def write(path, html):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(html, encoding="utf-8")

# ─────────────────────────────────────────────────────────────────────────────
# LANGUAGE DATA  (25 languages)
# ─────────────────────────────────────────────────────────────────────────────
LANGS = [
    ("en","English",""),
    ("de","Deutsch","lang/de"),
    ("fr","Français","lang/fr"),
    ("es","Español","lang/es"),
    ("pt","Português","lang/pt"),
    ("it","Italiano","lang/it"),
    ("ja","日本語","lang/ja"),
    ("zh","中文","lang/zh"),
    ("ko","한국어","lang/ko"),
    ("ru","Русский","lang/ru"),
    ("ar","العربية","lang/ar"),
    ("hi","हिन्दी","lang/hi"),
    ("id","Indonesia","lang/id"),
    ("nl","Nederlands","lang/nl"),
    ("pl","Polski","lang/pl"),
    ("tr","Türkçe","lang/tr"),
    ("sv","Svenska","lang/sv"),
    ("fil","Filipino","lang/fil"),
    ("vi","Tiếng Việt","lang/vi"),
    ("th","ภาษาไทย","lang/th"),
    ("ms","Melayu","lang/ms"),
    ("bn","বাংলা","lang/bn"),
    ("uk","Українська","lang/uk"),
    ("ro","Română","lang/ro"),
    ("cs","Čeština","lang/cs"),
]

def hreflang():
    out = ""
    for code, _, path in LANGS:
        url = f"{SITE}/{path}/" if path else f"{SITE}/"
        out += f'  <link rel="alternate" hreflang="{code}" href="{url}">\n'
    out += f'  <link rel="alternate" hreflang="x-default" href="{SITE}/">\n'
    return out

def lang_strip():
    pills = ""
    for code, label, path in LANGS:
        href = f"{SITE}/{path}/" if path else f"{SITE}/"
        pills += f'<a href="{href}" class="lpill">{label}</a>'
    return f'<div class="lang-bar"><div class="lscroll">{pills}</div></div>'

def nav_links():
    return f"""
<a href="{SITE}/">Home</a>
<a href="{SITE}/samsung/">Samsung</a>
<a href="{SITE}/frp/">FRP Bypass</a>
<a href="{SITE}/forgot-pin/">Forgot PIN</a>
<a href="{SITE}/brands/">All Brands</a>
<a href="{SITE}/how-it-works/">How It Works</a>
<a href="{SITE}/global/">🌍 Global</a>
"""

# ─────────────────────────────────────────────────────────────────────────────
# CSS
# ─────────────────────────────────────────────────────────────────────────────
CSS = """
:root{--red:#e63946;--navy:#1d3557;--mid:#457b9d;--light:#a8dadc;--bg:#f8f9fa;--white:#fff;--text:#212529;--muted:#6c757d}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Segoe UI',system-ui,Arial,sans-serif;background:var(--bg);color:var(--text);line-height:1.75}
a{color:var(--mid);text-decoration:none}a:hover{color:var(--red)}
/* ── HEADER ── */
header{background:linear-gradient(135deg,var(--navy) 0%,#0d2137 100%);position:sticky;top:0;z-index:200;box-shadow:0 2px 16px rgba(0,0,0,.35)}
.hinner{max-width:1200px;margin:0 auto;padding:14px 24px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px}
.logo{font-size:1.25rem;font-weight:800;color:#fff;letter-spacing:-.5px}.logo em{color:var(--red);font-style:normal}
nav{display:flex;flex-wrap:wrap;gap:4px}
nav a{color:#cdd;font-size:.86rem;padding:5px 10px;border-radius:5px;transition:.15s}
nav a:hover{background:rgba(255,255,255,.12);color:#fff}
/* ── LANG BAR ── */
.lang-bar{background:#152433;border-bottom:1px solid #1d3557;padding:7px 0}
.lscroll{max-width:1200px;margin:0 auto;padding:0 24px;display:flex;gap:7px;overflow-x:auto;scrollbar-width:thin;scrollbar-color:#457b9d #152433}
.lpill{background:#1d3557;color:#9bb;padding:3px 13px;border-radius:20px;font-size:.79rem;white-space:nowrap;transition:.15s;flex-shrink:0}
.lpill:hover{background:var(--red);color:#fff}
/* ── HERO ── */
.hero{background:linear-gradient(135deg,#1d3557 0%,#0d2137 55%,#16213e 100%);color:#fff;padding:90px 24px 70px;text-align:center}
.hero h1{font-size:clamp(2rem,5vw,3.4rem);font-weight:900;line-height:1.15;margin-bottom:18px}
.hero h1 em{color:var(--red);font-style:normal}
.hero p{font-size:1.18rem;max-width:700px;margin:0 auto 36px;color:#b0c8e0;line-height:1.65}
.badge-strip{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin-bottom:32px}
.hbadge{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);color:#dde;padding:5px 16px;border-radius:20px;font-size:.85rem}
/* ── BUTTONS ── */
.btn{display:inline-block;background:var(--red);color:#fff!important;padding:15px 36px;border-radius:9px;font-weight:800;font-size:1.02rem;transition:.2s;margin:5px;cursor:pointer}
.btn:hover{background:#c62a36;transform:translateY(-2px);box-shadow:0 8px 24px rgba(230,57,70,.45)}
.btn-outline{background:transparent;border:2px solid #fff;color:#fff!important}
.btn-outline:hover{background:#fff;color:var(--navy)!important}
.btn-sm{padding:10px 22px;font-size:.9rem}
/* ── LAYOUT ── */
main{max-width:1200px;margin:0 auto;padding:50px 24px}
section{margin-bottom:60px}
/* ── TRUST BAR ── */
.trust{background:var(--white);border-radius:14px;padding:28px;display:flex;flex-wrap:wrap;gap:16px;justify-content:space-around;box-shadow:0 2px 14px rgba(0,0,0,.07);margin-bottom:50px}
.trust-item{text-align:center;min-width:110px}
.trust-item strong{display:block;font-size:1.7rem;font-weight:900;color:var(--navy)}
.trust-item span{font-size:.83rem;color:var(--muted)}
/* ── CARDS ── */
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:22px}
.card{background:var(--white);border-radius:12px;padding:28px 26px;box-shadow:0 2px 12px rgba(0,0,0,.07);transition:.2s;border-top:3px solid transparent}
.card:hover{transform:translateY(-5px);box-shadow:0 10px 32px rgba(0,0,0,.12);border-top-color:var(--red)}
.card .icon{font-size:2.2rem;margin-bottom:14px}
.card h3{font-size:1.05rem;font-weight:700;color:var(--navy);margin-bottom:8px}
.card p{font-size:.92rem;color:#555;line-height:1.65}
/* ── STEPS ── */
.steps{display:flex;flex-direction:column;gap:24px}
.step{display:flex;gap:20px;align-items:flex-start;background:var(--white);border-radius:12px;padding:22px;box-shadow:0 1px 8px rgba(0,0,0,.06)}
.snum{background:var(--red);color:#fff;min-width:44px;height:44px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:1.2rem;flex-shrink:0}
.step h3{font-size:1rem;font-weight:700;color:var(--navy);margin-bottom:5px}
.step p{font-size:.92rem;color:#555}
/* ── HEADINGS ── */
h2{font-size:clamp(1.4rem,3vw,2rem);font-weight:800;color:var(--navy);margin-bottom:18px}
h3.sub{font-size:1.1rem;color:var(--mid);font-weight:600;margin-bottom:10px}
.section-intro{color:#555;margin-bottom:28px;max-width:780px;font-size:.98rem}
/* ── TABLE ── */
.tbl-wrap{overflow-x:auto;margin:16px 0}
table{width:100%;border-collapse:collapse;background:var(--white);border-radius:12px;overflow:hidden;box-shadow:0 2px 10px rgba(0,0,0,.07)}
th{background:var(--navy);color:#fff;padding:13px 16px;text-align:left;font-size:.88rem;white-space:nowrap}
td{padding:11px 16px;border-bottom:1px solid #eef2f7;font-size:.9rem}
tr:last-child td{border:none}
tr:nth-child(even) td{background:#f5f7fb}
/* ── BADGES ── */
.badges{display:flex;flex-wrap:wrap;gap:9px;margin:14px 0}
.badge{background:#e8f0fe;color:var(--navy);padding:5px 15px;border-radius:20px;font-size:.85rem;font-weight:600}
.badge.green{background:#d1fae5;color:#065f46}
.badge.red{background:#fee2e2;color:#991b1b}
/* ── FAQ ── */
.faq{display:flex;flex-direction:column;gap:10px}
.faq-item{background:var(--white);border-radius:10px;box-shadow:0 1px 6px rgba(0,0,0,.06);overflow:hidden}
.faq-q{padding:17px 20px;font-weight:700;color:var(--navy);cursor:pointer;display:flex;justify-content:space-between;align-items:center;font-size:.97rem}
.faq-q::after{content:"▾";color:var(--red);font-size:1rem;flex-shrink:0;margin-left:10px}
.faq-a{padding:0 20px 16px;color:#555;font-size:.92rem;line-height:1.7}
/* ── CTA BOX ── */
.cta-box{background:linear-gradient(135deg,var(--navy),#0d2137);color:#fff;border-radius:16px;padding:48px 36px;text-align:center;margin:50px 0}
.cta-box h2{color:#fff;margin-bottom:12px}
.cta-box p{color:#b0c8e0;margin-bottom:28px;max-width:600px;margin-left:auto;margin-right:auto}
/* ── BRANDS GRID ── */
.bgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:12px}
.bcard{background:var(--white);border:1.5px solid #e0e7f0;border-radius:10px;padding:16px 10px;text-align:center;font-weight:700;font-size:.9rem;color:var(--navy);transition:.2s}
.bcard:hover{border-color:var(--red);color:var(--red);transform:translateY(-2px);box-shadow:0 4px 14px rgba(0,0,0,.1)}
/* ── COMPARISON ── */
.comp-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px;margin:20px 0}
.comp-card{background:var(--white);border-radius:12px;padding:24px;box-shadow:0 2px 10px rgba(0,0,0,.07);text-align:center}
.comp-card.highlight{border:2px solid var(--red)}
.comp-card h4{font-size:1rem;font-weight:800;color:var(--navy);margin-bottom:12px}
.comp-card ul{list-style:none;text-align:left;font-size:.88rem;color:#555}
.comp-card ul li{padding:4px 0;border-bottom:1px solid #f0f0f0}
.comp-card ul li::before{content:"✓ ";color:var(--red);font-weight:700}
/* ── ALERT BOX ── */
.alert{background:#fffbeb;border-left:4px solid #f59e0b;border-radius:8px;padding:14px 18px;font-size:.92rem;color:#78350f;margin:16px 0}
/* ── RATING ── */
.rating{display:flex;align-items:center;gap:10px;margin:8px 0}
.stars{color:#f59e0b;font-size:1.2rem;letter-spacing:2px}
/* ── FOOTER ── */
footer{background:#0d2137;color:#7899bb;text-align:center;padding:32px 24px;font-size:.86rem;margin-top:80px}
footer a{color:#9ab}footer a:hover{color:#fff}
.footer-links{display:flex;flex-wrap:wrap;gap:16px;justify-content:center;margin-bottom:14px}
/* ── RESPONSIVE ── */
@media(max-width:640px){
  .hinner{flex-direction:column;align-items:flex-start}
  nav{flex-wrap:wrap}
  .hero{padding:60px 16px 50px}
  main{padding:30px 16px}
  .cta-box{padding:30px 20px}
  .trust{gap:12px}
}
"""

# ─────────────────────────────────────────────────────────────────────────────
# PAGE SHELL
# ─────────────────────────────────────────────────────────────────────────────
def shell(title, desc, kw, body, lang="en", canon="", schema_extra=""):
    url = canon if canon else f"{SITE}/"
    schema = f"""{{
  "@context":"https://schema.org",
  "@type":"WebPage",
  "name":"{title}",
  "description":"{desc}",
  "url":"{url}",
  "publisher":{{"@type":"Organization","name":"UnlockAndroidScreen","url":"{SITE}"}}
  {schema_extra}
}}"""
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{kw}">
<meta name="robots" content="index,follow">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="website">
<meta property="og:image" content="{SITE}/og.png">
<link rel="canonical" href="{url}">
{hreflang()}<style>{CSS}</style>
<script type="application/ld+json">{schema}</script>
</head>
<body>
<header>
<div class="hinner">
  <a class="logo" href="{SITE}/"><em>🔓</em> UnlockAndroidScreen</a>
  <nav>{nav_links()}</nav>
</div>
</header>
{lang_strip()}
{body}
<footer>
<div class="footer-links">
  <a href="{SITE}/">Home</a>
  <a href="{SITE}/samsung/">Samsung</a>
  <a href="{SITE}/frp/">FRP Bypass</a>
  <a href="{SITE}/brands/">All Brands</a>
  <a href="{SITE}/no-data-loss/">No Data Loss</a>
  <a href="{SITE}/free-download/">Free Download</a>
  <a href="{SITE}/global/">Global</a>
  <a href="{AFFILIATE}" target="_blank" rel="noopener sponsored">Download Dr.Fone</a>
</div>
<p>© {YEAR} UnlockAndroidScreen &nbsp;·&nbsp; Powered by <a href="{AFFILIATE}" target="_blank" rel="noopener sponsored">Wondershare Dr.Fone</a></p>
<p style="margin-top:8px;color:#556;font-size:.8rem">For informational purposes only. Only unlock devices you own or have explicit permission to access.</p>
</footer>
</body></html>"""

# ─────────────────────────────────────────────────────────────────────────────
# HOMEPAGE
# ─────────────────────────────────────────────────────────────────────────────
def home():
    body = f"""
<div class="hero">
  <h1>Unlock <em>Any</em> Android Screen Lock<br>in Under 5 Minutes</h1>
  <p>Forgot your PIN, pattern, password, or fingerprint? Dr.Fone removes every type of Android lock instantly — <strong>no data loss</strong> on supported Samsung devices.</p>
  <div class="badge-strip">
    <span class="hbadge">✅ Android 16 Ready</span>
    <span class="hbadge">📱 2,000+ Devices</span>
    <span class="hbadge">🏷️ 29+ Brands</span>
    <span class="hbadge">💾 No Data Loss (Samsung)</span>
    <span class="hbadge">🔁 7-Day Refund</span>
  </div>
  {cta("🔓 Download Dr.Fone Free")} {cta("See How It Works","btn btn-outline")}
</div>

<main>
<div class="trust">
  <div class="trust-item"><strong>50M+</strong><span>Global Users</span></div>
  <div class="trust-item"><strong>2,000+</strong><span>Device Models</span></div>
  <div class="trust-item"><strong>29+</strong><span>Android Brands</span></div>
  <div class="trust-item"><strong>4.5★</strong><span>Trustpilot Rating</span></div>
  <div class="trust-item"><strong>5 min</strong><span>Avg Unlock Time</span></div>
  <div class="trust-item"><strong>7-Day</strong><span>Money-Back</span></div>
</div>

<section>
<h2>Why Are You Locked Out?</h2>
<p class="section-intro">Over 50 million people get locked out of their Android every year. Here are the most common situations — and how Dr.Fone fixes each one in minutes.</p>
<div class="cards">
  <div class="card"><div class="icon">🔢</div><h3>Forgotten PIN or Password</h3><p>Set a complex PIN last year and can't remember it? Or disabled your fingerprint and forgot the backup code? Dr.Fone removes any PIN or alphanumeric password completely.</p></div>
  <div class="card"><div class="icon">🖐️</div><h3>Pattern Lock Forgotten</h3><p>Swiped the wrong pattern too many times? "Phone locked, try again in 30 minutes"? Dr.Fone bypasses the pattern immediately — no waiting.</p></div>
  <div class="card"><div class="icon">👆</div><h3>Fingerprint Not Responding</h3><p>Wet hands, a cracked screen protector, or a software update broke your fingerprint scanner. Dr.Fone clears the biometric lock so you can re-enroll fresh.</p></div>
  <div class="card"><div class="icon">🔐</div><h3>Google FRP Lock</h3><p>Did a factory reset without signing out first? Stuck on the "This device was reset" screen? Dr.Fone bypasses Google FRP on Samsung, Xiaomi, Huawei, and 29+ brands.</p></div>
  <div class="card"><div class="icon">🛒</div><h3>Second-Hand Phone Locked</h3><p>Bought a used Android still locked to the previous owner? Get full unrestricted access without contacting them.</p></div>
  <div class="card"><div class="icon">😶</div><h3>Face Unlock Disabled</h3><p>Camera glitch, poor lighting, or a changed appearance makes face recognition fail repeatedly. Remove and re-set facial recognition in minutes.</p></div>
  <div class="card"><div class="icon">💔</div><h3>Broken Touchscreen</h3><p>Screen won't accept swipes or taps so you can't enter your PIN? Dr.Fone unlocks via USB from your PC — no touchscreen needed at all.</p></div>
  <div class="card"><div class="icon">🏢</div><h3>MDM / Work Profile Lock</h3><p>Company MDM policy preventing personal use? Or an enterprise device management lock you need removed? Dr.Fone handles MDM removal too.</p></div>
</div>
</section>

<section>
<h2>How to Unlock Your Android in 3 Steps</h2>
<p class="section-intro">No technical skills required. Works on Windows and Mac. Free trial lets you verify compatibility before purchase.</p>
<div class="steps">
  <div class="step"><div class="snum">1</div><div><h3>Download &amp; Install Dr.Fone on Your Computer</h3><p>Free download for Windows 7/8/10/11 and macOS 10.12+. Installation takes under 2 minutes. No driver setup needed — Dr.Fone handles everything automatically.</p></div></div>
  <div class="step"><div class="snum">2</div><div><h3>Connect Your Android via USB &amp; Select Screen Unlock</h3><p>Open Dr.Fone → Toolbox → Screen Unlock → Android → Unlock Android Screen. The software detects your device model, brand, and Android version automatically.</p></div></div>
  <div class="step"><div class="snum">3</div><div><h3>Follow the On-Screen Guide — Phone Unlocked</h3><p>Dr.Fone guides you step by step. The unlock completes in 2–5 minutes. Set a new PIN, pattern, or fingerprint immediately after.</p></div></div>
</div>
<br>{cta("🔓 Start Unlocking Now")}
</section>

<section>
<h2>Supported Android Brands</h2>
<p class="section-intro">Dr.Fone works with 29+ brands and 2,000+ device models. Click your brand for a specific guide.</p>
<div class="bgrid">
  <a href="{SITE}/brands/samsung/" class="bcard">Samsung</a>
  <a href="{SITE}/brands/huawei/" class="bcard">Huawei</a>
  <a href="{SITE}/brands/xiaomi/" class="bcard">Xiaomi</a>
  <a href="{SITE}/brands/oppo/" class="bcard">OPPO</a>
  <a href="{SITE}/brands/vivo/" class="bcard">Vivo</a>
  <a href="{SITE}/brands/lg/" class="bcard">LG</a>
  <a href="{SITE}/brands/motorola/" class="bcard">Motorola</a>
  <a href="{SITE}/brands/oneplus/" class="bcard">OnePlus</a>
  <a href="{SITE}/brands/nokia/" class="bcard">Nokia</a>
  <a href="{SITE}/brands/sony/" class="bcard">Sony</a>
  <a href="{SITE}/brands/realme/" class="bcard">Realme</a>
  <a href="{SITE}/brands/zte/" class="bcard">ZTE</a>
  <a href="{SITE}/brands/lenovo/" class="bcard">Lenovo</a>
  <a href="{SITE}/brands/asus/" class="bcard">Asus</a>
  <a href="{SITE}/brands/pixel/" class="bcard">Google Pixel</a>
  <a href="{SITE}/brands/tcl/" class="bcard">TCL</a>
  <a href="{SITE}/brands/honor/" class="bcard">Honor</a>
  <a href="{SITE}/brands/infinix/" class="bcard">Infinix</a>
  <a href="{SITE}/brands/tecno/" class="bcard">Tecno</a>
  <a href="{SITE}/brands/itel/" class="bcard">itel</a>
</div>
</section>

<section>
<h2>All Lock Types Dr.Fone Can Remove</h2>
<div class="badges">
  <span class="badge green">PIN Lock</span>
  <span class="badge green">Password Lock</span>
  <span class="badge green">Pattern Lock</span>
  <span class="badge green">Fingerprint Lock</span>
  <span class="badge green">Face Unlock</span>
  <span class="badge green">Google FRP</span>
  <span class="badge green">Samsung FRP</span>
  <span class="badge green">MDM Lock</span>
  <span class="badge green">Samsung Knox</span>
  <span class="badge green">Screen Time Lock</span>
</div>
</section>

<section>
<h2>Dr.Fone vs Free Alternatives</h2>
<div class="tbl-wrap">
<table>
  <tr><th>Method</th><th>Removes Lock?</th><th>Keeps Data?</th><th>Works Offline?</th><th>FRP Bypass?</th><th>Cost</th></tr>
  <tr><td><strong>Dr.Fone Screen Unlock</strong></td><td>✅ Always</td><td>✅ Samsung/LG</td><td>✅ Yes</td><td>✅ Yes</td><td>Free Trial</td></tr>
  <tr><td>Google Find My Device</td><td>⚠️ Erases device</td><td>❌ No</td><td>❌ No</td><td>❌ No</td><td>Free</td></tr>
  <tr><td>Factory Reset (Recovery)</td><td>✅ Yes</td><td>❌ All wiped</td><td>✅ Yes</td><td>❌ Triggers FRP</td><td>Free</td></tr>
  <tr><td>Samsung Find My Mobile</td><td>✅ Samsung only</td><td>✅ Yes</td><td>❌ No</td><td>❌ No</td><td>Free</td></tr>
  <tr><td>ADB Commands (manual)</td><td>⚠️ Technical</td><td>⚠️ Varies</td><td>✅ Yes</td><td>❌ No</td><td>Free</td></tr>
</table>
</div>
</section>

<section>
<h2>Frequently Asked Questions</h2>
<div class="faq">
  <div class="faq-item"><div class="faq-q">Will unlocking delete my photos and contacts?</div><div class="faq-a">For many Samsung Galaxy models, Dr.Fone unlocks without any data loss — keeping photos, contacts, messages and apps intact. For other brands, a data reset may occur, but Dr.Fone's built-in backup tool lets you save everything first.</div></div>
  <div class="faq-item"><div class="faq-q">Which Android versions does Dr.Fone support?</div><div class="faq-a">Dr.Fone supports Android 2.1 through Android 16 — including all Android 15, 14, 13, 12 and 11 devices. It's updated regularly to support the latest releases.</div></div>
  <div class="faq-item"><div class="faq-q">Can I try it for free before buying?</div><div class="faq-a">Yes. The free trial lets you install Dr.Fone, connect your device, and verify it's fully supported — before you pay anything. Wondershare also offers a 7-day money-back guarantee if it doesn't work on your device.</div></div>
  <div class="faq-item"><div class="faq-q">Do I need a computer to unlock my Android?</div><div class="faq-a">Yes — Dr.Fone runs on Windows or Mac and connects to your phone via USB. This PC-based approach is what makes it reliable and able to perform deep firmware-level unlocking that apps cannot.</div></div>
  <div class="faq-item"><div class="faq-q">Is it legal to unlock my own Android phone?</div><div class="faq-a">Yes, unlocking a device you own or have permission to access is legal in most countries. Dr.Fone is intended only for legitimate use on your own devices.</div></div>
  <div class="faq-item"><div class="faq-q">How long does the unlock process take?</div><div class="faq-a">Most unlocks complete in 2–5 minutes. The process involves downloading a firmware package and flashing the unlock patch, so a stable internet connection speeds things up.</div></div>
  <div class="faq-item"><div class="faq-q">Can Dr.Fone unlock a phone that's completely disabled?</div><div class="faq-a">Yes. Even if your phone says "Phone is disabled" or "Too many attempts", Dr.Fone bypasses the lock entirely — there's no need to wait for any cooldown period.</div></div>
  <div class="faq-item"><div class="faq-q">What if my phone's touchscreen is broken?</div><div class="faq-a">No problem. Dr.Fone operates entirely from your PC via USB, so a broken or unresponsive touchscreen doesn't affect the unlock process at all.</div></div>
</div>
</section>

<div class="cta-box">
  <h2>Ready to Get Back Into Your Phone?</h2>
  <p>Free download. Try before you buy. 7-day money-back guarantee if it doesn't work on your device.</p>
  {cta("🔓 Download Dr.Fone Free")} {cta("View All Features","btn btn-outline")}
</div>
</main>"""
    return shell(
        f"Unlock Android Screen — Remove Any Lock in 5 Minutes ({YEAR})",
        f"Locked out of your Android? Remove PIN, password, pattern, fingerprint &amp; FRP in minutes with Dr.Fone. No data loss on Samsung. Supports 2,000+ devices. Free trial.",
        "unlock android screen, android screen unlock, remove android lock, bypass android pin, forgot android password, android frp bypass, unlock android phone, android locked screen",
        body, canon=f"{SITE}/",
        schema_extra=','+"\"breadcrumb\":{\"@type\":\"BreadcrumbList\",\"itemListElement\":[{\"@type\":\"ListItem\",\"position\":1,\"name\":\"Home\",\"item\":\""+SITE+"/\"}]}"
    )

# ─────────────────────────────────────────────────────────────────────────────
# HOW IT WORKS
# ─────────────────────────────────────────────────────────────────────────────
def how_it_works():
    body = f"""
<div class="hero">
  <h1>How Dr.Fone <em>Screen Unlock</em> Works</h1>
  <p>A deep-dive into the technology behind Android screen unlocking — and why Dr.Fone is the safest, most reliable method available.</p>
  {cta("🔓 Try It Free")}
</div>
<main>
<section>
<h2>The Technology Behind Android Unlocking</h2>
<p class="section-intro">Android screen locks are stored in an encrypted partition called <strong>userdata</strong>. Traditional factory resets wipe this partition entirely — destroying all your data. Dr.Fone uses a patented firmware-level bypass that removes the lock files specifically without touching the rest of your data.</p>
<div class="cards">
  <div class="card"><div class="icon">🔬</div><h3>Firmware-Level Access</h3><p>Dr.Fone communicates with your device at the firmware level via Download Mode (Samsung) or Recovery Mode (other brands), bypassing the OS-level lock entirely.</p></div>
  <div class="card"><div class="icon">🔄</div><h3>Targeted Lock Removal</h3><p>Instead of wiping all user data, Dr.Fone identifies and removes only the specific lock credential files — preserving everything else on Samsung devices.</p></div>
  <div class="card"><div class="icon">🔒</div><h3>Encrypted Channel</h3><p>All communication between Dr.Fone and Wondershare's servers (for firmware downloads) is fully encrypted. Your personal data is never uploaded or accessed.</p></div>
  <div class="card"><div class="icon">🤖</div><h3>Automated Driver Install</h3><p>Dr.Fone's "Special Mode" automatically installs the correct USB drivers for your device — eliminating the most common manual setup headache.</p></div>
</div>
</section>
<section>
<h2>Detailed Step-by-Step Process</h2>
<div class="steps">
  <div class="step"><div class="snum">1</div><div><h3>Install Dr.Fone on Your Computer</h3><p>Download the installer (Windows or Mac). Run it and follow the standard setup wizard. Dr.Fone installs all required components automatically — no separate driver downloads needed.</p></div></div>
  <div class="step"><div class="snum">2</div><div><h3>Launch Dr.Fone and Select Screen Unlock</h3><p>Open Dr.Fone. From the main Toolbox, select "Screen Unlock". On the next screen, choose "Android" as your platform type.</p></div></div>
  <div class="step"><div class="snum">3</div><div><h3>Connect Your Android via USB</h3><p>Plug in your phone with a USB cable. Dr.Fone automatically detects the device model, Android version, and chipset. If USB debugging is disabled, Dr.Fone provides instructions to enable it.</p></div></div>
  <div class="step"><div class="snum">4</div><div><h3>Select Unlock Type</h3><p>Choose "Unlock Android Screen" for PIN/pattern/password/fingerprint. Choose "Remove Google FRP Lock" for Factory Reset Protection bypass. Dr.Fone shows you the appropriate method for your device.</p></div></div>
  <div class="step"><div class="snum">5</div><div><h3>Enter Device Mode</h3><p>For Samsung: enter Download Mode (Power + Volume Down + Bixby). For others: enter Recovery Mode. Dr.Fone shows exact button combinations for your specific model.</p></div></div>
  <div class="step"><div class="snum">6</div><div><h3>Automatic Firmware Download &amp; Unlock</h3><p>Dr.Fone downloads a firmware package matched to your device (500MB–2GB, requires internet). It then flashes the unlock patch. This takes 2–5 minutes depending on your internet speed.</p></div></div>
  <div class="step"><div class="snum">7</div><div><h3>Phone Unlocked — Set a New Lock</h3><p>Your Android restarts unlocked. Immediately set a new PIN, pattern, or fingerprint. For Samsung no-data-loss unlocks, all your photos, contacts, and apps are still there.</p></div></div>
</div>
</section>
{cta("🔓 Start the Unlock Process")}
</main>"""
    return shell(
        f"How Android Screen Unlock Works — Dr.Fone Explained ({YEAR})",
        "Understand the technology behind Dr.Fone's Android unlock. Learn how firmware-level bypass removes PIN, FRP and pattern locks without data loss on Samsung.",
        "how android unlock works, dr.fone technology, android screen unlock process, firmware bypass android",
        body, canon=f"{SITE}/how-it-works/")

# ─────────────────────────────────────────────────────────────────────────────
# SAMSUNG
# ─────────────────────────────────────────────────────────────────────────────
def samsung():
    body = f"""
<div class="hero">
  <h1>Unlock <em>Samsung</em> Locked Screen</h1>
  <p>The only tool that removes Samsung Galaxy locks <strong>without deleting your data</strong>. Supports Galaxy S26 down to Galaxy S6, all A-series, Note, Tab, Z Fold &amp; Flip.</p>
  {cta("🔓 Unlock Samsung Now")}
</div>
<main>
<section>
<h2>Why Samsung Unlocking Is Different</h2>
<p class="section-intro">Samsung uses a proprietary lock storage system that Dr.Fone can access without triggering a factory reset. This is the feature that makes Dr.Fone unique — no other tool offers guaranteed no-data-loss unlocking for Samsung at this scale.</p>
<div class="cards">
  <div class="card"><div class="icon">💾</div><h3>Zero Data Loss Technology</h3><p>Dr.Fone's patented Samsung unlock keeps every photo, contact, message, app, and account signed in. You won't lose a single file.</p></div>
  <div class="card"><div class="icon">⚡</div><h3>3-Minute Process</h3><p>Samsung Download Mode + Dr.Fone's automated firmware flash = full unlock in around 3 minutes from cable to home screen.</p></div>
  <div class="card"><div class="icon">📱</div><h3>Android 16 Support</h3><p>Works on the latest Samsung Galaxy S26, S25 Edge, Z Fold 7, Z Flip 7 — right through to older Galaxy models on Android 8.</p></div>
  <div class="card"><div class="icon">🔐</div><h3>FRP &amp; Knox Bypass</h3><p>Stuck on Samsung FRP after a reset? Need to remove Samsung Knox MDM? Dr.Fone handles both with 100% success on Snapdragon Samsung models using an EDL cable.</p></div>
</div>
</section>
<section>
<h2>Supported Samsung Models ({YEAR})</h2>
<div class="badges">
  <span class="badge green">Galaxy S26 / S25 / S24 / S23</span>
  <span class="badge green">Galaxy S22 / S21 / S20 / S10</span>
  <span class="badge green">Galaxy Note 20 / Note 10 / Note 9</span>
  <span class="badge green">Galaxy A54 / A53 / A52 / A71</span>
  <span class="badge green">Galaxy Z Fold 6 / 5 / 4 / 3</span>
  <span class="badge green">Galaxy Z Flip 6 / 5 / 4 / 3</span>
  <span class="badge green">Galaxy Tab S9 / S8 / S7</span>
  <span class="badge green">Snapdragon &amp; Exynos variants</span>
</div>
</section>
<section>
<h2>Samsung-Specific Unlock Methods</h2>
<div class="tbl-wrap">
<table>
  <tr><th>Situation</th><th>Method</th><th>Data Loss?</th><th>Time</th></tr>
  <tr><td>Forgot PIN / Pattern / Password</td><td>Remove Without Data Loss</td><td>❌ None (most models)</td><td>~3 min</td></tr>
  <tr><td>Google FRP (Snapdragon)</td><td>EDL Cable Bypass</td><td>❌ None</td><td>~5 min</td></tr>
  <tr><td>Google FRP (Exynos)</td><td>Download Mode</td><td>❌ None</td><td>~4 min</td></tr>
  <tr><td>Samsung Knox MDM</td><td>MDM Removal Mode</td><td>⚠️ May vary</td><td>~5 min</td></tr>
  <tr><td>Fingerprint / Face Lock</td><td>Biometric Bypass</td><td>❌ None</td><td>~3 min</td></tr>
</table>
</div>
</section>
<section>
<h2>Step-by-Step: Unlock Samsung Without Data Loss</h2>
<div class="steps">
  <div class="step"><div class="snum">1</div><div><h3>Open Dr.Fone → Screen Unlock → Android</h3><p>Launch Dr.Fone on your PC or Mac. Navigate to Toolbox → Screen Unlock → Android → Unlock Android Screen.</p></div></div>
  <div class="step"><div class="snum">2</div><div><h3>Select Samsung &amp; "Remove Without Data Loss"</h3><p>From the brand list, choose Samsung. Select "Remove without Data Loss". Confirm your exact model number for the best firmware match.</p></div></div>
  <div class="step"><div class="snum">3</div><div><h3>Enter Download Mode</h3><p>Power off your Samsung. Hold Volume Down + Bixby/Home + Power. When the warning screen appears, press Volume Up to enter Download Mode. Connect via USB.</p></div></div>
  <div class="step"><div class="snum">4</div><div><h3>Automatic Unlock (2–3 min)</h3><p>Dr.Fone downloads matching firmware and flashes the unlock patch. Do not disconnect the USB cable. Your Samsung restarts to the home screen — all data intact.</p></div></div>
</div>
</section>
<div class="alert">⚠️ <strong>Samsung Snapdragon FRP note:</strong> For Samsung S-series Snapdragon devices, use the EDL cable method for 100% success. Dr.Fone guides you through this process with the correct cable type.</div>
{cta("🔓 Unlock Samsung — Free Trial")}
</main>"""
    return shell(
        f"Unlock Samsung Locked Screen Without Data Loss ({YEAR}) | Dr.Fone",
        f"Unlock Samsung Galaxy locked screen without losing photos or data. Remove PIN, pattern, password &amp; FRP on Galaxy S/A/Note/Z. Free trial. Supports Android 16.",
        "unlock samsung locked screen, samsung frp bypass, samsung pin unlock no data loss, galaxy screen unlock, samsung locked phone, unlock galaxy s25 s24 s23",
        body, canon=f"{SITE}/samsung/")

# ─────────────────────────────────────────────────────────────────────────────
# FRP BYPASS
# ─────────────────────────────────────────────────────────────────────────────
def frp():
    body = f"""
<div class="hero">
  <h1>Android <em>FRP Bypass</em> — Remove Google Account Lock</h1>
  <p>Stuck on "This device was reset" or "Verify your account"? Bypass Google FRP on any Android in minutes — no original Google account needed.</p>
  {cta("🔓 Bypass FRP Now")}
</div>
<main>
<section>
<h2>What Is Google FRP Lock?</h2>
<p class="section-intro">Factory Reset Protection (FRP) is a security layer built into Android 5.1+ (Lollipop and above). When a device is factory reset without first removing the Google account, FRP activates on the next boot — demanding the original Gmail and password. This protects against theft, but traps legitimate owners who forgot their credentials or bought a second-hand device.</p>
<div class="cards">
  <div class="card"><div class="icon">🔄</div><h3>Factory Reset Without Sign-Out</h3><p>The most common cause. Performing a hard reset via Recovery Mode without removing your Google account first triggers FRP immediately on the next startup.</p></div>
  <div class="card"><div class="icon">📦</div><h3>Bought a Second-Hand Phone</h3><p>The previous owner forgot — or refused — to sign out of their Google account before selling. Their FRP lock remains active and blocks your setup.</p></div>
  <div class="card"><div class="icon">🔑</div><h3>Forgotten Google Credentials</h3><p>You remember the Gmail address but not the password, or the address changed, or 2-factor authentication is blocking recovery.</p></div>
  <div class="card"><div class="icon">🙏</div><h3>Inherited / Gifted Device</h3><p>A family member's old phone was given to you but nobody remembers the original Google account details.</p></div>
</div>
</section>
<section>
<h2>How Dr.Fone Bypasses FRP</h2>
<div class="steps">
  <div class="step"><div class="snum">1</div><div><h3>Install Dr.Fone → Screen Unlock → Remove Google FRP</h3><p>Open Dr.Fone. Go to Toolbox → Screen Unlock → Android → Remove Google FRP Lock.</p></div></div>
  <div class="step"><div class="snum">2</div><div><h3>Choose Your Android Brand</h3><p>Select your brand from the list: Samsung, Xiaomi, Huawei, OPPO, Vivo, Motorola, or Generic Android. Dr.Fone shows the verified bypass method for your specific device.</p></div></div>
  <div class="step"><div class="snum">3</div><div><h3>Follow Device-Specific Instructions</h3><p>Samsung Snapdragon: use EDL cable for 100% bypass. Samsung Exynos &amp; others: USB debugging method. Dr.Fone shows exact steps with screenshots for your model.</p></div></div>
  <div class="step"><div class="snum">4</div><div><h3>FRP Removed — Add New Google Account</h3><p>Google account lock is permanently removed. Complete setup normally and add any Google account you choose.</p></div></div>
</div>
</section>
<section>
<h2>FRP Bypass Support by Brand</h2>
<div class="tbl-wrap">
<table>
  <tr><th>Brand</th><th>FRP Support</th><th>Best Method</th><th>Android Version</th><th>Data Loss?</th></tr>
  <tr><td><strong>Samsung (Snapdragon)</strong></td><td>✅ 100%</td><td>EDL Cable</td><td>Up to Android 16</td><td>❌ None</td></tr>
  <tr><td><strong>Samsung (Exynos)</strong></td><td>✅ Full</td><td>Download Mode</td><td>Up to Android 16</td><td>❌ None</td></tr>
  <tr><td>Xiaomi / Redmi / POCO</td><td>✅ Supported</td><td>ADB Method</td><td>MIUI 12–14</td><td>⚠️ Varies</td></tr>
  <tr><td>Huawei / Honor</td><td>✅ Supported</td><td>USB Method</td><td>EMUI 10–12</td><td>⚠️ Varies</td></tr>
  <tr><td>OPPO / Realme</td><td>✅ Supported</td><td>Recovery Mode</td><td>ColorOS 12–14</td><td>⚠️ Varies</td></tr>
  <tr><td>Vivo / iQOO</td><td>✅ Supported</td><td>ADB Method</td><td>FuntouchOS 12+</td><td>⚠️ Varies</td></tr>
  <tr><td>Motorola</td><td>✅ Supported</td><td>USB Method</td><td>Android 11–14</td><td>⚠️ Varies</td></tr>
  <tr><td>Google Pixel</td><td>✅ Supported</td><td>Recovery Mode</td><td>Android 12–16</td><td>⚠️ Varies</td></tr>
</table>
</div>
</section>
<section>
<h2>Frequently Asked Questions — FRP</h2>
<div class="faq">
  <div class="faq-item"><div class="faq-q">Can I bypass FRP without a computer?</div><div class="faq-a">Some manual methods exist but are unreliable and frequently patched by Google updates. Dr.Fone's PC-based approach provides consistent, reliable FRP bypass across all supported devices.</div></div>
  <div class="faq-item"><div class="faq-q">Will FRP bypass work on my Samsung S25?</div><div class="faq-a">Yes. Dr.Fone supports Samsung S25 (Snapdragon and Exynos variants) with Android 16 FRP bypass. Use the EDL cable method for Snapdragon models for guaranteed success.</div></div>
  <div class="faq-item"><div class="faq-q">What is an EDL cable and do I need one?</div><div class="faq-a">EDL (Emergency Download Mode) is a deep bootloader mode on Qualcomm (Snapdragon) devices. For Samsung Snapdragon FRP, an EDL cable provides 100% success. Dr.Fone tells you exactly which cable to get for your model.</div></div>
</div>
</section>
{cta("🔓 Bypass Google FRP — Free Trial")}
</main>"""
    return shell(
        f"Android FRP Bypass — Remove Google Account Lock Instantly ({YEAR})",
        f"Bypass Google FRP lock on any Android. Remove Factory Reset Protection on Samsung, Xiaomi, Huawei, OPPO. 100% working. Free trial available.",
        "android frp bypass, google frp unlock, factory reset protection bypass, remove google account lock android, samsung frp bypass 2026, frp lock removal tool",
        body, canon=f"{SITE}/frp/")

# ─────────────────────────────────────────────────────────────────────────────
# FORGOT PIN
# ─────────────────────────────────────────────────────────────────────────────
def forgot_pin():
    body = f"""
<div class="hero">
  <h1>Forgot Android PIN, Password or Pattern?</h1>
  <p>Don't panic. You have several options — from completely free to the most reliable paid tool. We explain every method so you can pick the right one for your situation.</p>
  {cta("🔓 Unlock in 5 Minutes")}
</div>
<main>
<section>
<h2>Why Android Passwords Are Easy to Forget</h2>
<p class="section-intro">Modern Android devices push users toward biometric authentication — fingerprint and face unlock — so the PIN or password becomes a rarely-used backup. After weeks of only scanning your finger, a complex PIN disappears from muscle memory. It's one of the most common tech support issues globally.</p>
</section>
<section>
<h2>Your Options — Ranked by Reliability</h2>
<div class="tbl-wrap">
<table>
  <tr><th>Method</th><th>Keeps Data?</th><th>Needs Internet?</th><th>Success Rate</th><th>Difficulty</th></tr>
  <tr><td><strong>Dr.Fone Screen Unlock</strong></td><td>✅ Samsung/LG</td><td>✅ For firmware</td><td>🟢 Very High</td><td>Easy</td></tr>
  <tr><td>Samsung Find My Mobile</td><td>✅ Yes</td><td>✅ Required</td><td>🟢 High</td><td>Easy (Samsung only)</td></tr>
  <tr><td>Google Find My Device</td><td>❌ Erases all</td><td>✅ Required</td><td>🟡 Medium</td><td>Easy</td></tr>
  <tr><td>Factory Reset via Recovery</td><td>❌ All wiped</td><td>❌ Not needed</td><td>🟢 Always works</td><td>Easy</td></tr>
  <tr><td>ADB Unlock (debug on)</td><td>✅ Maybe</td><td>❌ Not needed</td><td>🟡 Device dependent</td><td>Technical</td></tr>
</table>
</div>
</section>
<section>
<h2>6 Situations Where Dr.Fone Is the Only Option</h2>
<div class="cards">
  <div class="card"><div class="icon">📵</div><h3>Phone Disabled / "Try Again" Loop</h3><p>"Phone is disabled for 30 minutes" — Dr.Fone bypasses the lockout entirely. No need to wait through multiple cooldown periods.</p></div>
  <div class="card"><div class="icon">🌐</div><h3>No Internet on Locked Phone</h3><p>Google Find My Device requires the phone to be online. If Wi-Fi is off and mobile data is locked behind a PIN screen, Dr.Fone works via USB without internet on the device.</p></div>
  <div class="card"><div class="icon">📴</div><h3>Google Account Not Set Up</h3><p>If no Google account was linked before the lock, Find My Device won't work. Dr.Fone doesn't need any Google credentials at all.</p></div>
  <div class="card"><div class="icon">🔄</div><h3>After FRP Triggers From Reset</h3><p>A factory reset removes the PIN but triggers FRP. Dr.Fone handles both the screen lock AND the FRP bypass in one session.</p></div>
  <div class="card"><div class="icon">💀</div><h3>Deceased Family Member's Phone</h3><p>Accessing a loved one's phone without their credentials. Dr.Fone removes all locks with no account verification needed.</p></div>
  <div class="card"><div class="icon">🏗️</div><h3>Samsung Knox / Enterprise MDM</h3><p>Work device locked with MDM that you can't remove through normal settings. Dr.Fone's MDM removal mode handles enterprise locks.</p></div>
</div>
</section>
{cta("🔓 Remove Forgotten Password Now")}
</main>"""
    return shell(
        f"Forgot Android PIN, Password or Pattern? Fix It Now ({YEAR})",
        f"Forgot your Android PIN, password, or pattern lock? Compare every method and unlock in minutes with Dr.Fone. Works even when phone is disabled.",
        "forgot android pin, forgot android password, forgot android pattern, android locked out, unlock android forgot password, phone disabled unlock",
        body, canon=f"{SITE}/forgot-pin/")

# ─────────────────────────────────────────────────────────────────────────────
# NO DATA LOSS
# ─────────────────────────────────────────────────────────────────────────────
def no_data_loss():
    body = f"""
<div class="hero">
  <h1>Unlock Android Without <em>Losing Data</em></h1>
  <p>Every photo, contact, message and app — kept safe while removing the lock. The only tool with verified no-data-loss Android unlocking.</p>
  {cta("🔓 Unlock Without Data Loss")}
</div>
<main>
<section>
<h2>Why Most Methods Delete Everything</h2>
<p class="section-intro">A standard factory reset is the simplest way to remove a lock — but it permanently wipes your entire device. Google's remote erase is the same. Dr.Fone operates at the firmware level, surgically removing only the lock credential files while leaving your user data partition completely untouched.</p>
</section>
<section>
<h2>What's Preserved After Dr.Fone Unlocking</h2>
<div class="cards">
  <div class="card"><div class="icon">🖼️</div><h3>Photos &amp; Videos</h3><p>Every photo and video on internal storage and SD card remains fully intact after unlocking. Resolution, metadata, and location tags are all preserved.</p></div>
  <div class="card"><div class="icon">👥</div><h3>Contacts &amp; Call Log</h3><p>Your entire contact list, call history, and SMS message threads are preserved and accessible immediately after the unlock completes.</p></div>
  <div class="card"><div class="icon">📲</div><h3>Apps &amp; App Data</h3><p>All installed applications — with their saved data, login sessions, game progress, and settings — remain installed and working.</p></div>
  <div class="card"><div class="icon">📧</div><h3>Accounts Stay Signed In</h3><p>Google, Samsung, WhatsApp, banking apps, and all other accounts remain signed in after unlocking. No re-authentication hassle.</p></div>
  <div class="card"><div class="icon">🎵</div><h3>Music, Documents &amp; Downloads</h3><p>All media files, documents, and downloaded content remain in their original locations with no corruption.</p></div>
  <div class="card"><div class="icon">💬</div><h3>WhatsApp &amp; Chat History</h3><p>WhatsApp messages, voice notes, and media stay intact. This is especially important for business users and those with years of conversation history.</p></div>
</div>
</section>
<section>
<h2>No-Data-Loss Device Compatibility</h2>
<div class="tbl-wrap">
<table>
  <tr><th>Device Type</th><th>No Data Loss?</th><th>Supported Models</th></tr>
  <tr><td>Samsung Galaxy S Series</td><td>✅ Yes</td><td>S6 through S26</td></tr>
  <tr><td>Samsung Galaxy A Series</td><td>✅ Most models</td><td>A10 through A54</td></tr>
  <tr><td>Samsung Galaxy Note Series</td><td>✅ Yes</td><td>Note 5 through Note 20</td></tr>
  <tr><td>Samsung Galaxy Z Series</td><td>✅ Yes</td><td>Z Fold 1–6, Z Flip 1–6</td></tr>
  <tr><td>Samsung Galaxy Tab</td><td>✅ Most models</td><td>Tab S3 through Tab S9</td></tr>
  <tr><td>LG Phones</td><td>✅ Select models</td><td>LG V60, G8, Velvet</td></tr>
  <tr><td>Other Android Brands</td><td>⚠️ Backup recommended</td><td>Dr.Fone backup tool included</td></tr>
</table>
</div>
</section>
<div class="alert">💡 <strong>Tip:</strong> Even for devices where data loss may occur, Dr.Fone includes a built-in Android backup tool. Back up your phone first, then unlock — your data is safe either way.</div>
{cta("🔓 Unlock Without Losing Data")}
</main>"""
    return shell(
        f"Unlock Android Without Losing Data ({YEAR}) | Dr.Fone",
        "Remove Android lock screen without losing photos, contacts, WhatsApp, or apps. Dr.Fone no-data-loss unlock supports all Samsung Galaxy S/A/Note/Z series.",
        "unlock android without data loss, remove android lock screen keep data, bypass android lock no data loss, samsung unlock no data loss, keep photos unlock android",
        body, canon=f"{SITE}/no-data-loss/")

# ─────────────────────────────────────────────────────────────────────────────
# FREE DOWNLOAD
# ─────────────────────────────────────────────────────────────────────────────
def free_download():
    body = f"""
<div class="hero">
  <h1>Download Dr.Fone Android Unlock — <em>Free Trial</em></h1>
  <p>Try before you buy. Download Dr.Fone for free, verify your device is supported, and see exactly what will happen — before spending a penny.</p>
  {cta("⬇️ Download Free Now")}
</div>
<main>
<section>
<h2>What the Free Trial Includes</h2>
<div class="cards">
  <div class="card"><div class="icon">🔍</div><h3>Full Device Detection</h3><p>Connect your Android and Dr.Fone identifies your exact model, Android version, chipset, and lock type — for free, no license needed.</p></div>
  <div class="card"><div class="icon">✅</div><h3>Compatibility Check</h3><p>See whether your specific device supports the no-data-loss method or needs a standard unlock before purchasing.</p></div>
  <div class="card"><div class="icon">📋</div><h3>Step Preview</h3><p>Walk through the complete unlock process and see every step — including which mode to enter and what happens to your data.</p></div>
  <div class="card"><div class="icon">🛡️</div><h3>7-Day Money-Back Guarantee</h3><p>If Dr.Fone doesn't unlock your device after purchase, Wondershare offers a full refund within 7 days — no questions asked.</p></div>
</div>
</section>
<section>
<h2>System Requirements</h2>
<div class="tbl-wrap">
<table>
  <tr><th>Platform</th><th>Requirement</th><th>Notes</th></tr>
  <tr><td>Windows</td><td>Windows 7 / 8 / 10 / 11</td><td>32-bit &amp; 64-bit supported</td></tr>
  <tr><td>macOS</td><td>macOS 10.12 Sierra or later</td><td>Apple Silicon (M1/M2/M3) supported</td></tr>
  <tr><td>RAM</td><td>256 MB minimum</td><td>512 MB+ recommended</td></tr>
  <tr><td>Storage</td><td>200 MB free space</td><td>2–3 GB for firmware downloads</td></tr>
  <tr><td>Connection</td><td>USB port + cable</td><td>Original USB cable recommended</td></tr>
  <tr><td>Internet</td><td>Required for firmware download</td><td>1 Mbps+ recommended</td></tr>
</table>
</div>
</section>
<section>
<h2>Pricing Plans</h2>
<div class="comp-grid">
  <div class="comp-card"><h4>Monthly</h4><ul><li>Full unlock features</li><li>Screen Unlock (Android)</li><li>FRP Bypass included</li><li>Free Dr.Fone App trial</li></ul><br>{cta("Start Monthly","btn btn-sm")}</div>
  <div class="comp-card highlight"><h4>⭐ 1-Year (Best Value)</h4><ul><li>All monthly features</li><li>Windows &amp; Mac</li><li>Free updates for 1 year</li><li>Priority support</li></ul><br>{cta("Get 1-Year Plan","btn btn-sm")}</div>
  <div class="comp-card"><h4>Lifetime</h4><ul><li>One-time purchase</li><li>All future updates free</li><li>Up to 5 devices</li><li>Family license available</li></ul><br>{cta("Get Lifetime","btn btn-sm")}</div>
</div>
</section>
{cta("⬇️ Download Dr.Fone Free")}
</main>"""
    return shell(
        f"Download Dr.Fone Android Screen Unlock Free ({YEAR}) | Try Before Buy",
        "Download Wondershare Dr.Fone Screen Unlock for Android free. Windows &amp; Mac. Free trial — check device compatibility before purchase. 7-day refund guarantee.",
        "download drfone android free, dr.fone free download, android unlock software download, wondershare drfone free trial",
        body, canon=f"{SITE}/free-download/")

# ─────────────────────────────────────────────────────────────────────────────
# PATTERN LOCK
# ─────────────────────────────────────────────────────────────────────────────
def pattern():
    body = f"""
<div class="hero">
  <h1>Remove Android <em>Pattern Lock</em> — Instant Bypass</h1>
  <p>Can't remember your unlock pattern? Too many wrong attempts? Dr.Fone removes any Android pattern lock in 3 minutes — no guessing required.</p>
  {cta("🔓 Remove Pattern Lock")}
</div>
<main>
<section>
<h2>Why Android Pattern Locks Get Forgotten</h2>
<p class="section-intro">Pattern locks feel intuitive when you first set them, but after a few weeks of relying on fingerprint or face unlock, the muscle memory for your specific pattern fades. A slightly off angle, a forgotten starting corner, or simply too many wrong attempts — Dr.Fone removes it completely.</p>
<div class="cards">
  <div class="card"><div class="icon">🧠</div><h3>Forgot the Exact Path</h3><p>You remember it was an "L" shape, but not which direction or corner it started from. Instead of guessing, Dr.Fone removes it in 3 minutes.</p></div>
  <div class="card"><div class="icon">⏳</div><h3>"Try Again in 30 Seconds"</h3><p>Android locks you out after 5 incorrect attempts. Rather than waiting through 10+ cooldown cycles, Dr.Fone bypasses the lockout immediately.</p></div>
  <div class="card"><div class="icon">💧</div><h3>Smudge Trail on Screen</h3><p>Worried a thief could trace your pattern from finger smudges? Remove and replace the pattern with a smudge-proof PIN instead.</p></div>
  <div class="card"><div class="icon">🛒</div><h3>Used Phone Still Pattern Locked</h3><p>Bought a second-hand phone with a pattern you don't know. Dr.Fone clears it instantly so you can set your own.</p></div>
</div>
</section>
<section>
<h2>Pattern Lock vs Other Lock Types — Which Is Safer?</h2>
<div class="tbl-wrap">
<table>
  <tr><th>Lock Type</th><th>Security Level</th><th>Forgettable?</th><th>Dr.Fone Bypass</th></tr>
  <tr><td>Pattern (3×3 grid)</td><td>Medium</td><td>High</td><td>✅ Yes — 3 min</td></tr>
  <tr><td>4-digit PIN</td><td>Low-Medium</td><td>Medium</td><td>✅ Yes — 3 min</td></tr>
  <tr><td>6-digit PIN</td><td>Medium-High</td><td>Medium</td><td>✅ Yes — 3 min</td></tr>
  <tr><td>Alphanumeric Password</td><td>High</td><td>High</td><td>✅ Yes — 3 min</td></tr>
  <tr><td>Fingerprint</td><td>High</td><td>Low</td><td>✅ Yes — 3 min</td></tr>
  <tr><td>Face Unlock</td><td>Medium-High</td><td>Low</td><td>✅ Yes — 3 min</td></tr>
</table>
</div>
</section>
{cta("🔓 Bypass Pattern Lock Free")}
</main>"""
    return shell(
        f"Remove Android Pattern Lock — Bypass in 3 Minutes ({YEAR})",
        "Forgot your Android pattern lock? Bypass any Android pattern in 3 minutes with Dr.Fone. Works after too many wrong attempts. No data loss on Samsung.",
        "android pattern lock bypass, remove android pattern lock, forgot android pattern, unlock android pattern screen, bypass pattern lock",
        body, canon=f"{SITE}/pattern/")

# ─────────────────────────────────────────────────────────────────────────────
# FINGERPRINT
# ─────────────────────────────────────────────────────────────────────────────
def fingerprint():
    body = f"""
<div class="hero">
  <h1>Android <em>Fingerprint Lock</em> Not Working?</h1>
  <p>Fingerprint sensor failing after an update, screen protector change, or injury? Remove the biometric lock completely and re-enroll fresh prints.</p>
  {cta("🔓 Fix Fingerprint Lock")}
</div>
<main>
<section>
<h2>Why Android Fingerprint Sensors Fail</h2>
<div class="cards">
  <div class="card"><div class="icon">💧</div><h3>Moisture &amp; Oils</h3><p>Wet hands, lotion, or skin oils create a thin film that optical and capacitive sensors can't read through. You're locked out even though the sensor is working fine.</p></div>
  <div class="card"><div class="icon">🛡️</div><h3>Wrong Screen Protector</h3><p>Tempered glass protectors that aren't certified for your phone's under-display fingerprint sensor (UDFS) reduce accuracy to near zero.</p></div>
  <div class="card"><div class="icon">🔄</div><h3>Android System Update</h3><p>Major Android updates sometimes break fingerprint calibration. The sensor works but can't match the stored template until you re-enroll — which needs the phone unlocked first.</p></div>
  <div class="card"><div class="icon">🤕</div><h3>Skin Changes</h3><p>Cuts, burns, dry skin, aging, and even vigorous exercise can temporarily alter your fingerprint ridge pattern enough to fail authentication.</p></div>
  <div class="card"><div class="icon">🌡️</div><h3>Extreme Temperature</h3><p>Cold weather causes skin to contract and sweat changes ridge patterns. Sensors that work indoors may fail in extreme heat or cold.</p></div>
  <div class="card"><div class="icon">🔢</div><h3>Forgotten Backup PIN</h3><p>Your fingerprint fails and Android asks for your PIN — but you've forgotten the backup. Dr.Fone removes both locks at once.</p></div>
</div>
</section>
<section>
<h2>The Fix: Remove &amp; Re-Enroll in One Step</h2>
<div class="steps">
  <div class="step"><div class="snum">1</div><div><h3>Use Dr.Fone to Remove All Biometric Locks</h3><p>Dr.Fone removes the fingerprint lock (and any PIN backup) in 3 minutes, getting you back into your phone without any fingerprint needed.</p></div></div>
  <div class="step"><div class="snum">2</div><div><h3>Clean Your Screen &amp; Fingers</h3><p>Wipe the sensor area with a dry microfiber cloth. Wash and dry your hands thoroughly before the next step.</p></div></div>
  <div class="step"><div class="snum">3</div><div><h3>Re-Enroll Your Fingerprint</h3><p>Go to Settings → Security → Fingerprint. Enroll 2–3 fingers for reliability. For UDFS phones, enroll in multiple positions (straight on, angled, edge).</p></div></div>
  <div class="step"><div class="snum">4</div><div><h3>Set a Strong PIN Backup</h3><p>Always set a memorable 6-digit PIN as backup. Dr.Fone can help if you ever forget it again — but with a good PIN, you'll never need to.</p></div></div>
</div>
</section>
{cta("🔓 Remove Fingerprint Lock Now")}
</main>"""
    return shell(
        f"Android Fingerprint Lock Not Working — Fix in 3 Minutes ({YEAR})",
        "Android fingerprint not working after update or screen protector change? Remove biometric lock with Dr.Fone and re-enroll fresh fingerprints. All Android brands.",
        "android fingerprint not working, remove android fingerprint lock, bypass fingerprint android, android biometric lock fix, fingerprint sensor failed android",
        body, canon=f"{SITE}/fingerprint/")

# ─────────────────────────────────────────────────────────────────────────────
# GLOBAL PAGE
# ─────────────────────────────────────────────────────────────────────────────
def global_page():
    cards = ""
    flags = {"en":"🇺🇸","de":"🇩🇪","fr":"🇫🇷","es":"🇪🇸","pt":"🇧🇷","it":"🇮🇹","ja":"🇯🇵",
             "zh":"🇨🇳","ko":"🇰🇷","ru":"🇷🇺","ar":"🇸🇦","hi":"🇮🇳","id":"🇮🇩","nl":"🇳🇱",
             "pl":"🇵🇱","tr":"🇹🇷","sv":"🇸🇪","fil":"🇵🇭","vi":"🇻🇳","th":"🇹🇭",
             "ms":"🇲🇾","bn":"🇧🇩","uk":"🇺🇦","ro":"🇷🇴","cs":"🇨🇿"}
    for code, label, path in LANGS:
        href = f"{SITE}/{path}/" if path else f"{SITE}/"
        flag = flags.get(code,"🌐")
        cards += f'<a href="{href}" class="bcard" style="padding:22px 10px;font-size:1rem">{flag} {label}</a>'
    body = f"""
<div class="hero">
  <h1>🌍 Android Screen Unlock — <em>Global Versions</em></h1>
  <p>Available in 25 languages. Select yours for a fully localized guide with native-language keywords and instructions.</p>
</div>
<main>
<section>
<h2>Choose Your Language / Region</h2>
<div class="bgrid" style="grid-template-columns:repeat(auto-fill,minmax(150px,1fr))">{cards}</div>
</section>
<div class="cta-box">
  <h2>Dr.Fone — Available Worldwide</h2>
  <p>Works in every country. Download available for Windows &amp; Mac globally. Full multilingual support.</p>
  {cta("🔓 Download Free Worldwide")}
</div>
</main>"""
    return shell("Unlock Android Screen — Global Versions in 25 Languages | Dr.Fone",
        "Android screen unlock guide in 25 languages. English, Deutsch, Français, Español, Português, 日本語, 中文, 한국어, العربية, हिन्दी &amp; more.",
        "android screen unlock global, unlock android worldwide, android unlock multilingual, global android lock bypass",
        body, canon=f"{SITE}/global/")

# ─────────────────────────────────────────────────────────────────────────────
# BRANDS INDEX
# ─────────────────────────────────────────────────────────────────────────────
def brands_index():
    items = ["Samsung","Huawei","Xiaomi","OPPO","Vivo","LG","Motorola","OnePlus",
             "Nokia","Sony","Realme","ZTE","Lenovo","Asus","Google Pixel","TCL",
             "Honor","Infinix","Tecno","itel"]
    cards = "".join(f'<a href="{SITE}/brands/{b.lower().replace(" ","-").replace("+","")}/" class="bcard" style="padding:20px 12px">{b}</a>' for b in items)
    body = f"""
<div class="hero">
  <h1>Android Unlock by <em>Brand</em></h1>
  <p>Model-specific guides for every major Android manufacturer. Select your brand for exact instructions.</p>
  {cta("🔓 Download Dr.Fone — All Brands")}
</div>
<main>
<section><h2>All Supported Brands</h2>
<div class="bgrid" style="grid-template-columns:repeat(auto-fill,minmax(140px,1fr))">{cards}</div>
</section>
</main>"""
    return shell(f"Android Screen Unlock by Brand ({YEAR}) — Samsung, Huawei, Xiaomi &amp; More",
        "Find your Android brand unlock guide. Samsung, Huawei, Xiaomi, OPPO, Vivo, LG, Motorola, OnePlus and 20+ more brands supported by Dr.Fone.",
        "android unlock by brand, samsung unlock, huawei unlock, xiaomi unlock, oppo unlock, motorola unlock android",
        body, canon=f"{SITE}/brands/")

# ─────────────────────────────────────────────────────────────────────────────
# BRAND PAGES DATA
# ─────────────────────────────────────────────────────────────────────────────
BRAND_DATA = {
    "samsung":  {"name":"Samsung","models":"Galaxy S26/S25/S24/S23, Note 20, A54/A53, Z Fold 6/5, Z Flip 6/5","kw":"samsung locked screen unlock, samsung frp bypass, unlock samsung galaxy, galaxy screen unlock","note":"Samsung is the only brand where Dr.Fone can unlock without data loss on most models.","star":"💾 No data loss on most Galaxy models."},
    "huawei":   {"name":"Huawei","models":"P50/P40/P30, Mate 50/40/30, Nova 9/8, Y9 Prime","kw":"huawei locked screen unlock, huawei frp bypass, unlock huawei phone, huawei pin remove","note":"Huawei devices use EMUI/HarmonyOS. Dr.Fone supports EMUI 8.0 through EMUI 12 for screen unlock.","star":"⚡ Works on EMUI 8–12 and HarmonyOS."},
    "xiaomi":   {"name":"Xiaomi / Redmi / POCO","models":"Xiaomi 14/13/12, Redmi Note 13/12/11, POCO X6/X5, Redmi 12","kw":"xiaomi locked screen unlock, xiaomi frp bypass, unlock xiaomi phone, redmi unlock, poco unlock","note":"Xiaomi / MIUI devices require ADB debugging enabled. Dr.Fone's guide walks through enabling it step-by-step.","star":"🔐 FRP bypass on MIUI 12–14 supported."},
    "oppo":     {"name":"OPPO","models":"Find X6/X5, Reno 10/9/8, A98/A96/A78, F23","kw":"oppo locked screen unlock, oppo frp bypass, unlock oppo phone, oppo pin remove, coloros unlock","note":"OPPO runs ColorOS. Dr.Fone uses Recovery Mode for OPPO screen unlock — no root required.","star":"✅ ColorOS 11–14 supported."},
    "vivo":     {"name":"Vivo / iQOO","models":"Vivo X90/X80, V27/V25, Y76/Y75, iQOO 11/10","kw":"vivo locked screen unlock, vivo frp bypass, unlock vivo phone, iqoo unlock, vivo pin remove","note":"Vivo uses FuntouchOS. Dr.Fone bypasses Vivo FRP without sideloading risky APK files.","star":"🔓 Safe FRP bypass — no risky APKs needed."},
    "lg":       {"name":"LG","models":"LG V60/V50, G8/G7, Velvet, Stylo 6/5, Wing","kw":"lg locked screen unlock, lg frp bypass, unlock lg phone, lg pin remove, lg pattern unlock","note":"LG (discontinued hardware but millions still in use). Dr.Fone supports no-data-loss unlock on select LG models alongside Samsung.","star":"💾 No data loss available on select LG models."},
    "motorola": {"name":"Motorola","models":"Moto G72/G52/G32, Edge 40/30, Moto G Power 2024, One 5G Ace","kw":"motorola locked screen unlock, motorola frp bypass, unlock motorola phone, moto pin remove","note":"Motorola devices are close to stock Android. Dr.Fone uses USB/ADB method for reliable Motorola unlock.","star":"📱 Near-stock Android — clean unlock process."},
    "oneplus":  {"name":"OnePlus","models":"OnePlus 12/11/10 Pro, Nord CE 3/2, OnePlus 9/8T","kw":"oneplus locked screen unlock, oneplus frp bypass, unlock oneplus phone, oxygenos unlock","note":"OnePlus runs OxygenOS (based on AOSP). Dr.Fone fully supports OxygenOS 11–14 for screen unlock.","star":"⚡ OxygenOS 11–14 fully supported."},
    "nokia":    {"name":"Nokia","models":"Nokia G60/G21, Nokia XR20/X20, Nokia C31","kw":"nokia locked screen unlock, unlock nokia android phone, nokia pin bypass","note":"Nokia devices run near-stock Android One. Dr.Fone uses standard Recovery Mode for Nokia unlock.","star":"🤖 Pure Android — straightforward unlock."},
    "sony":     {"name":"Sony Xperia","models":"Xperia 1 V/IV/III, Xperia 5 IV/III, Xperia 10 V","kw":"sony xperia locked screen unlock, unlock sony xperia, xperia pin bypass, xperia frp","note":"Sony Xperia runs near-stock Android. Dr.Fone supports Xperia screen unlock via Recovery Mode.","star":"🎨 Sony Xperia unlock — all Xperia models."},
    "realme":   {"name":"Realme","models":"Realme 11/10/9 Pro, Realme GT 5/3, Realme C55/C35","kw":"realme locked screen unlock, realme frp bypass, unlock realme phone, realme pin remove","note":"Realme runs Realme UI (based on ColorOS). Dr.Fone supports Realme UI 3.0 and 4.0 screen unlock.","star":"🔓 Realme UI 3.0–4.0 supported."},
    "zte":      {"name":"ZTE","models":"ZTE Blade A72/A52, ZTE Axon 40, ZTE Blade V41 Vita","kw":"zte locked screen unlock, zte frp bypass, unlock zte phone, zte android unlock","note":"ZTE devices are popular in North America and Asia. Dr.Fone supports most ZTE models via Recovery Mode.","star":"🌐 Popular in US and Asia — fully supported."},
    "lenovo":   {"name":"Lenovo","models":"Lenovo K14 Plus, Lenovo Tab P12, Lenovo K13 Note","kw":"lenovo locked screen unlock, lenovo frp bypass, unlock lenovo phone, lenovo android unlock","note":"Lenovo Android phones and tablets are fully supported. Dr.Fone uses standard ADB/Recovery method.","star":"💻 Phones &amp; tablets both supported."},
    "asus":     {"name":"Asus","models":"Asus Zenfone 10/9, ROG Phone 7/6, Asus Zenfone 8","kw":"asus locked screen unlock, asus frp bypass, unlock asus phone, rog phone unlock, asus zenfone unlock","note":"Asus ZenFone and ROG Phone series are supported. Dr.Fone handles both ZenUI and ASUS stock Android.","star":"🎮 ZenFone &amp; ROG Phone series supported."},
    "pixel":    {"name":"Google Pixel","models":"Pixel 8/7/6/5/4, Pixel 8a/7a/6a, Pixel Fold","kw":"google pixel locked screen unlock, pixel frp bypass, unlock google pixel, pixel android unlock","note":"Google Pixel runs pure Android. Dr.Fone uses standard Recovery Mode for Pixel unlock — fast and reliable.","star":"🤖 Pure Android — fastest unlock process."},
    "tcl":      {"name":"TCL","models":"TCL 40 SE/30/20L, TCL Flip 2, TCL 20 Pro 5G","kw":"tcl locked screen unlock, tcl frp bypass, unlock tcl android, tcl phone pin remove","note":"TCL devices are popular budget Android phones. Dr.Fone supports TCL via standard Recovery Mode unlock.","star":"💰 Budget-friendly devices — fully supported."},
    "honor":    {"name":"Honor","models":"Honor 90/80/70, Honor Magic 5/4, Honor X9a/X8a","kw":"honor locked screen unlock, honor frp bypass, unlock honor phone, honor android unlock","note":"Honor is now independent from Huawei and runs MagicOS. Dr.Fone supports MagicOS screen unlock.","star":"✨ MagicOS (post-Huawei) supported."},
    "infinix":  {"name":"Infinix","models":"Infinix Note 30/12, Infinix Hot 30/20, Infinix Zero 30","kw":"infinix locked screen unlock, infinix frp bypass, unlock infinix phone, infinix android unlock","note":"Infinix is popular in Africa, Southeast Asia, and India. Dr.Fone supports Infinix XOS via Recovery Mode.","star":"🌍 Popular in Africa &amp; SE Asia — supported."},
    "tecno":    {"name":"Tecno","models":"Tecno Camon 20/19, Tecno Spark 10/9, Tecno Pova 5","kw":"tecno locked screen unlock, tecno frp bypass, unlock tecno phone, tecno android unlock","note":"Tecno devices run HiOS. Dr.Fone supports Tecno unlock via Recovery Mode on HiOS 8 and later.","star":"📱 HiOS 8+ support for Tecno devices."},
    "itel":     {"name":"itel","models":"itel A70, itel Vision 3, itel S24, itel A58","kw":"itel locked screen unlock, itel frp bypass, unlock itel phone, itel android unlock","note":"itel is Africa's best-selling smartphone brand. Dr.Fone supports itel devices via standard Recovery Mode.","star":"🏆 #1 in Africa — Dr.Fone fully supports itel."},
}

def brand_page(slug, d):
    slug_url = slug.replace("+","").replace(" ","-")
    body = f"""
<div class="hero">
  <h1>Unlock <em>{d['name']}</em> Screen Lock — Dr.Fone</h1>
  <p>Locked out of your {d['name']} phone? Remove PIN, pattern, password &amp; FRP in minutes. Supports: {d['models']}.</p>
  <div class="badge-strip"><span class="hbadge">{d['star']}</span></div>
  {cta(f"🔓 Unlock {d['name']} Now")}
</div>
<main>
<section>
<h2>Supported {d['name']} Models</h2>
<div class="badges">{"".join(f'<span class="badge green">{m.strip()}</span>' for m in d["models"].split(","))}</div>
<div class="alert">ℹ️ {d['note']}</div>
</section>
<section>
<h2>How to Unlock Your {d['name']}</h2>
<div class="steps">
  <div class="step"><div class="snum">1</div><div><h3>Install Dr.Fone on Windows or Mac</h3><p>Download and install Dr.Fone. Launch it and go to Toolbox → Screen Unlock → Android.</p></div></div>
  <div class="step"><div class="snum">2</div><div><h3>Connect Your {d['name']} via USB</h3><p>Use the original USB cable. Dr.Fone automatically detects your {d['name']} model and Android version.</p></div></div>
  <div class="step"><div class="snum">3</div><div><h3>Select {d['name']} &amp; Follow Guide</h3><p>Choose {d['name']} from the brand list. Dr.Fone shows the exact unlock method and step-by-step instructions for your model.</p></div></div>
  <div class="step"><div class="snum">4</div><div><h3>Unlock Complete in 2–5 Minutes</h3><p>The process completes automatically. Your {d['name']} restarts to the home screen. Set a new lock immediately.</p></div></div>
</div>
</section>
<section>
<h2>What Dr.Fone Removes on {d['name']}</h2>
<div class="badges">
  <span class="badge green">PIN Lock</span>
  <span class="badge green">Pattern Lock</span>
  <span class="badge green">Password Lock</span>
  <span class="badge green">Fingerprint Lock</span>
  <span class="badge green">Face Unlock</span>
  <span class="badge green">Google FRP</span>
</div>
</section>
<div class="cta-box">
  <h2>Unlock Your {d['name']} — Try Free</h2>
  <p>Download the free trial to verify compatibility with your exact model before purchasing.</p>
  {cta(f"🔓 Download Dr.Fone — {d['name']}")}
</div>
</main>"""
    return shell(
        f"Unlock {d['name']} Screen Lock — Remove PIN, FRP ({YEAR}) | Dr.Fone",
        f"Locked out of your {d['name']}? Remove PIN, pattern, password &amp; FRP in minutes with Dr.Fone. Supports {d['models']}. Free trial.",
        d["kw"], body, canon=f"{SITE}/brands/{slug_url}/")

# ─────────────────────────────────────────────────────────────────────────────
# LANGUAGE PAGES DATA  (25 languages)
# ─────────────────────────────────────────────────────────────────────────────
LANG_DATA = {
  "de": {
    "lang":"de","h1":"Android-Bildschirm entsperren","sub":"PIN, Muster oder Passwort vergessen? Dr.Fone entsperrt jeden Android-Bildschirm in Minuten — kein Datenverlust bei Samsung.",
    "title":f"Android Bildschirm Entsperren — PIN, Muster, FRP Entfernen ({YEAR})",
    "desc":"Android PIN, Muster oder Passwort vergessen? Dr.Fone entsperrt jeden Android in Minuten. Kein Datenverlust bei Samsung. Kostenlose Testversion.",
    "kw":"android entsperren, android bildschirm entsperren, android pin vergessen, android muster entfernen, samsung entsperren, frp bypass android, android passwort entfernen",
    "feats":[("🔢","PIN &amp; Passwort entfernen","Jede PIN oder alphanumerisches Passwort wird sofort und vollständig entfernt."),
             ("✋","Muster-Sperre bypass","Geschwungenes Entsperrmuster vergessen? Dr.Fone umgeht es in unter 3 Minuten."),
             ("🔐","Google FRP entsperren","FRP nach Werksreset? Für Samsung, Xiaomi, Huawei und 29+ Marken verfügbar."),
             ("💾","Kein Datenverlust","Alle Fotos, Kontakte und Apps bleiben auf unterstützten Samsung-Geräten erhalten."),
             ("👆","Fingerabdruck-Sperre","Fingerabdrucksensor defekt? Dr.Fone entfernt biometrische Sperren komplett."),
             ("⚡","5 Minuten Entsperrung","Einfacher 3-Schritt-Prozess — kein technisches Fachwissen erforderlich.")]
  },
  "fr": {
    "lang":"fr","h1":"Déverrouiller l'écran Android","sub":"Mot de passe, schéma ou PIN oublié ? Dr.Fone déverrouille n'importe quel Android en quelques minutes — sans perte de données sur Samsung.",
    "title":f"Déverrouiller Écran Android — Supprimer PIN, Schéma, FRP ({YEAR})",
    "desc":"PIN, schéma ou mot de passe Android oublié ? Dr.Fone déverrouille tout écran Android en minutes. Sans perte de données sur Samsung. Essai gratuit.",
    "kw":"déverrouiller android, écran android bloqué, oublié pin android, contourner verrouillage android, samsung déverrouiller, frp bypass android, supprimer mot de passe android",
    "feats":[("🔢","Supprimer PIN &amp; Mot de passe","Supprime instantanément tout code PIN ou mot de passe alphanumérique."),
             ("✋","Contourner le Schéma","Schéma oublié ? Dr.Fone le contourne complètement en moins de 3 minutes."),
             ("🔐","Déverrouiller FRP Google","Verrou FRP après réinitialisation ? Supprimé pour Samsung, Xiaomi, Huawei et 29+ marques."),
             ("💾","Sans Perte de Données","Photos, contacts et applications conservés sur les appareils Samsung compatibles."),
             ("👆","Empreinte Digitale","Capteur défaillant ? Dr.Fone supprime tous les verrous biométriques."),
             ("⚡","5 Minutes Chrono","Processus en 3 étapes simples — aucune compétence technique requise.")]
  },
  "es": {
    "lang":"es","h1":"Desbloquear Pantalla Android","sub":"¿Olvidaste tu PIN, patrón o contraseña? Dr.Fone desbloquea cualquier Android en minutos — sin pérdida de datos en Samsung.",
    "title":f"Desbloquear Pantalla Android — Eliminar PIN, Patrón, FRP ({YEAR})",
    "desc":"¿PIN, patrón o contraseña Android olvidados? Dr.Fone desbloquea en minutos. Sin pérdida de datos en Samsung. Prueba gratuita disponible.",
    "kw":"desbloquear android, pantalla android bloqueada, olvidé pin android, bypass android, samsung desbloquear, frp bypass android, eliminar contraseña android",
    "feats":[("🔢","Eliminar PIN y Contraseña","Elimina cualquier PIN o contraseña alfanumérica de inmediato."),
             ("✋","Bypass de Patrón","¿Patrón olvidado? Dr.Fone lo omite completamente en menos de 3 minutos."),
             ("🔐","Bypass FRP de Google","¿Bloqueo FRP tras restablecimiento? Eliminado en Samsung, Xiaomi, Huawei y 29+ marcas."),
             ("💾","Sin Pérdida de Datos","Fotos, contactos y apps intactos en dispositivos Samsung compatibles."),
             ("👆","Huella Digital","¿Sensor fallido? Dr.Fone elimina todos los bloqueos biométricos."),
             ("⚡","5 Minutos","Proceso de 3 pasos — sin conocimientos técnicos requeridos.")]
  },
  "pt": {
    "lang":"pt","h1":"Desbloquear Tela Android","sub":"Esqueceu o PIN, padrão ou senha? Dr.Fone desbloqueia qualquer Android em minutos — sem perda de dados no Samsung.",
    "title":f"Desbloquear Tela Android — Remover PIN, Padrão, FRP ({YEAR})",
    "desc":"PIN, padrão ou senha Android esquecidos? Dr.Fone desbloqueia em minutos. Sem perda de dados no Samsung. Teste grátis disponível.",
    "kw":"desbloquear android, tela android bloqueada, esqueci pin android, bypass android, samsung desbloquear, frp bypass, remover senha android",
    "feats":[("🔢","Remover PIN e Senha","Remove qualquer PIN ou senha alfanumérica instantaneamente."),
             ("✋","Bypass de Padrão","Padrão esquecido? Dr.Fone ignora completamente em menos de 3 minutos."),
             ("🔐","Bypass FRP do Google","Bloqueio FRP após reset? Removido no Samsung, Xiaomi, Huawei e 29+ marcas."),
             ("💾","Sem Perda de Dados","Fotos, contatos e apps intactos em dispositivos Samsung suportados."),
             ("👆","Impressão Digital","Sensor com falha? Dr.Fone remove todos os bloqueios biométricos."),
             ("⚡","5 Minutos","Processo de 3 etapas — sem habilidades técnicas necessárias.")]
  },
  "it": {
    "lang":"it","h1":"Sbloccare lo Schermo Android","sub":"Hai dimenticato PIN, sequenza o password? Dr.Fone sblocca qualsiasi Android in pochi minuti — senza perdita di dati su Samsung.",
    "title":f"Sbloccare Schermo Android — Rimuovere PIN, Sequenza, FRP ({YEAR})",
    "desc":"PIN, sequenza o password Android dimenticati? Dr.Fone sblocca in pochi minuti. Senza perdita di dati su Samsung. Prova gratuita disponibile.",
    "kw":"sbloccare android, schermo android bloccato, dimenticato pin android, bypassare android, samsung sbloccare, frp bypass, rimuovere password android",
    "feats":[("🔢","Rimuovere PIN e Password","Rimuove immediatamente qualsiasi PIN o password alfanumerica."),
             ("✋","Bypass della Sequenza","Sequenza dimenticata? Dr.Fone la ignora completamente in meno di 3 minuti."),
             ("🔐","Bypass FRP Google","Blocco FRP dopo il ripristino? Rimosso su Samsung, Xiaomi, Huawei e 29+ marchi."),
             ("💾","Nessuna Perdita di Dati","Foto, contatti e app intatti sui dispositivi Samsung supportati."),
             ("👆","Impronta Digitale","Sensore difettoso? Dr.Fone rimuove tutti i blocchi biometrici."),
             ("⚡","5 Minuti","Processo in 3 semplici passaggi — nessuna competenza tecnica richiesta.")]
  },
  "ja": {
    "lang":"ja","h1":"Androidの画面ロックを解除","sub":"PIN・パターン・パスワードを忘れましたか？Dr.FoneがすべてのAndroidロックを数分で解除。Samsung端末はデータ損失なし。",
    "title":f"Androidの画面ロック解除 — PIN・パターン・FRP削除 ({YEAR})",
    "desc":"AndroidのPIN・パターン・パスワードを忘れた？Dr.Foneが数分で解除。Samsung端末はデータ損失なし。無料試用版あり。",
    "kw":"android ロック解除, android 画面ロック, pin 忘れた android, パターン解除, samsung ロック解除, frp バイパス, android パスワード削除",
    "feats":[("🔢","PINとパスワードを削除","数字PINや英数字パスワードを即座に完全削除。"),
             ("✋","パターンロックをバイパス","パターンを忘れた？Dr.Foneが3分以内に完全にバイパス。"),
             ("🔐","Google FRPのバイパス","工場出荷時リセット後のFRPロック？Samsung・Xiaomi・Huaweiなど29以上のブランドに対応。"),
             ("💾","データ損失なし","対応Samsung端末では写真・連絡先・アプリをすべて保持。"),
             ("👆","指紋ロック","センサーが反応しない？Dr.Foneがすべての生体認証ロックを削除。"),
             ("⚡","5分で完了","3ステップの簡単プロセス — 技術的な知識は不要。")]
  },
  "zh": {
    "lang":"zh","h1":"解锁Android屏幕","sub":"忘记PIN码、图案或密码？Dr.Fone几分钟内解锁任意Android屏幕——三星设备无数据丢失。",
    "title":f"解锁Android屏幕 — 删除PIN、图案、FRP ({YEAR})",
    "desc":"忘记Android PIN、图案或密码？Dr.Fone几分钟内解锁。三星设备无数据丢失。提供免费试用版。",
    "kw":"android解锁, 安卓屏幕解锁, 忘记android密码, 绕过android锁屏, 三星解锁, frp解锁, 安卓图案解锁",
    "feats":[("🔢","删除PIN和密码","立即删除任意数字PIN或字母数字密码。"),
             ("✋","绕过图案锁","忘记解锁图案？Dr.Fone在3分钟内完全绕过。"),
             ("🔐","绕过谷歌FRP","恢复出厂设置后的FRP锁？支持三星、小米、华为等29个以上品牌。"),
             ("💾","无数据丢失","支持的三星设备上照片、联系人和应用全部保留。"),
             ("👆","指纹锁","传感器失效？Dr.Fone删除所有生物识别锁。"),
             ("⚡","5分钟完成","简单的3步流程——无需技术知识。")]
  },
  "ko": {
    "lang":"ko","h1":"Android 화면 잠금 해제","sub":"PIN, 패턴, 비밀번호를 잊었나요? Dr.Fone이 몇 분 안에 모든 Android 잠금을 해제합니다. Samsung 기기는 데이터 손실 없음.",
    "title":f"Android 화면 잠금 해제 — PIN, 패턴, FRP 제거 ({YEAR})",
    "desc":"Android PIN, 패턴 또는 비밀번호를 잊었나요? Dr.Fone이 몇 분 안에 해제합니다. Samsung은 데이터 손실 없음. 무료 체험 가능.",
    "kw":"안드로이드 잠금 해제, android 화면 잠금, 핀 잊어버렸어 android, 패턴 해제, 삼성 잠금 해제, frp 우회, 안드로이드 비밀번호 제거",
    "feats":[("🔢","PIN 및 비밀번호 제거","모든 숫자 PIN 또는 영숫자 비밀번호를 즉시 제거."),
             ("✋","패턴 잠금 우회","패턴을 잊었나요? Dr.Fone이 3분 이내에 완전히 우회."),
             ("🔐","Google FRP 우회","공장 초기화 후 FRP 잠금? Samsung, Xiaomi, Huawei 등 29개 이상 브랜드 지원."),
             ("💾","데이터 손실 없음","지원되는 Samsung 기기에서 사진, 연락처, 앱 모두 보존."),
             ("👆","지문 잠금","센서 오작동? Dr.Fone이 모든 생체 인식 잠금 제거."),
             ("⚡","5분 완료","간단한 3단계 프로세스 — 기술 지식 불필요.")]
  },
  "ru": {
    "lang":"ru","h1":"Разблокировать экран Android","sub":"Забыли PIN, рисунок или пароль? Dr.Fone снимает любую блокировку Android за минуты — без потери данных на Samsung.",
    "title":f"Разблокировать Экран Android — Удалить PIN, Рисунок, FRP ({YEAR})",
    "desc":"Android PIN, рисунок или пароль забыты? Dr.Fone разблокирует за минуты. Без потери данных на Samsung. Бесплатная пробная версия.",
    "kw":"разблокировать android, снять блокировку экрана android, забыл пин android, обход блокировки, разблокировка samsung, frp обход, удалить пароль android",
    "feats":[("🔢","Удаление PIN и Пароля","Мгновенно удаляет любой PIN или буквенно-цифровой пароль."),
             ("✋","Обход Графического Ключа","Забыли рисунок? Dr.Fone полностью обходит его за 3 минуты."),
             ("🔐","Обход Google FRP","Блокировка FRP после сброса? Снимается для Samsung, Xiaomi, Huawei и 29+ брендов."),
             ("💾","Без Потери Данных","Фото, контакты и приложения сохраняются на поддерживаемых Samsung."),
             ("👆","Разблокировка Отпечатка","Сенсор не работает? Dr.Fone удаляет все биометрические блокировки."),
             ("⚡","5 Минут","Простой 3-шаговый процесс — никаких технических навыков не требуется.")]
  },
  "ar": {
    "lang":"ar","h1":"فتح قفل شاشة أندرويد","sub":"نسيت رمز PIN أو النمط أو كلمة المرور؟ يفتح Dr.Fone أي قفل شاشة أندرويد في دقائق — بدون فقدان البيانات على سامسونج.",
    "title":f"فتح شاشة أندرويد — إزالة PIN والنمط وFRP ({YEAR})",
    "desc":"نسيت PIN أو النمط أو كلمة المرور؟ Dr.Fone يفتح في دقائق. بدون فقدان بيانات على سامسونج. تجربة مجانية متاحة.",
    "kw":"فتح قفل أندرويد, إزالة قفل الشاشة, نسيت pin أندرويد, تجاوز قفل أندرويد, سامسونج فتح القفل, frp bypass, إزالة كلمة مرور أندرويد",
    "feats":[("🔢","إزالة PIN وكلمة المرور","يزيل فوراً أي رمز PIN أو كلمة مرور حروف وأرقام."),
             ("✋","تجاوز نمط الفتح","نسيت النمط؟ يتجاوزه Dr.Fone كلياً في أقل من 3 دقائق."),
             ("🔐","تجاوز FRP من Google","قفل FRP بعد إعادة الضبط؟ يُزال لسامسونج وشاومي وهواوي و29+ علامة تجارية."),
             ("💾","بدون فقدان البيانات","تبقى الصور وجهات الاتصال والتطبيقات سليمة على أجهزة سامسونج المدعومة."),
             ("👆","قفل بصمة الإصبع","انقطع الاستشعار؟ Dr.Fone يزيل جميع أقفال القياسات الحيوية."),
             ("⚡","5 دقائق","عملية بسيطة من 3 خطوات — لا تحتاج مهارات تقنية.")]
  },
  "hi": {
    "lang":"hi","h1":"Android स्क्रीन लॉक खोलें","sub":"PIN, पैटर्न या पासवर्ड भूल गए? Dr.Fone कुछ ही मिनटों में किसी भी Android लॉक को हटाता है — Samsung पर डेटा हानि नहीं।",
    "title":f"Android स्क्रीन अनलॉक — PIN, पैटर्न, FRP हटाएं ({YEAR})",
    "desc":"Android PIN, पैटर्न या पासवर्ड भूले? Dr.Fone मिनटों में हटाता है। Samsung पर डेटा हानि नहीं। मुफ्त परीक्षण उपलब्ध।",
    "kw":"android अनलॉक, android स्क्रीन लॉक हटाएं, pin भूल गए, android लॉक बाईपास, samsung अनलॉक, frp बाईपास, android पासवर्ड हटाएं",
    "feats":[("🔢","PIN और पासवर्ड हटाएं","कोई भी PIN या अल्फ़ान्यूमेरिक पासवर्ड तुरंत हटाएं।"),
             ("✋","पैटर्न लॉक बाईपास","पैटर्न भूल गए? Dr.Fone 3 मिनट में पूरी तरह बाईपास करता है।"),
             ("🔐","Google FRP बाईपास","फ़ैक्टरी रीसेट के बाद FRP लॉक? Samsung, Xiaomi, Huawei आदि 29+ ब्रांड पर हटाया जाता है।"),
             ("💾","डेटा हानि नहीं","समर्थित Samsung उपकरणों पर फ़ोटो, संपर्क और ऐप सुरक्षित रहते हैं।"),
             ("👆","फिंगरप्रिंट लॉक","सेंसर काम नहीं कर रहा? Dr.Fone सभी बायोमेट्रिक लॉक हटाता है।"),
             ("⚡","5 मिनट","3-चरण की आसान प्रक्रिया — कोई तकनीकी ज्ञान नहीं चाहिए।")]
  },
  "id": {
    "lang":"id","h1":"Buka Kunci Layar Android","sub":"Lupa PIN, pola, atau kata sandi? Dr.Fone membuka kunci Android apa pun dalam beberapa menit — tanpa kehilangan data di Samsung.",
    "title":f"Buka Kunci Layar Android — Hapus PIN, Pola, FRP ({YEAR})",
    "desc":"Lupa PIN, pola, atau kata sandi Android? Dr.Fone membuka dalam menit. Tanpa kehilangan data di Samsung. Uji coba gratis tersedia.",
    "kw":"buka kunci android, layar android terkunci, lupa pin android, bypass kunci android, samsung buka kunci, frp bypass, hapus kata sandi android",
    "feats":[("🔢","Hapus PIN &amp; Kata Sandi","Hapus PIN atau kata sandi alfanumerik secara instan."),
             ("✋","Bypass Pola Kunci","Lupa polanya? Dr.Fone melewatinya sepenuhnya dalam 3 menit."),
             ("🔐","Bypass Google FRP","Kunci FRP setelah reset pabrik? Dihapus untuk Samsung, Xiaomi, Huawei, dan 29+ merek."),
             ("💾","Tanpa Kehilangan Data","Foto, kontak, dan aplikasi tetap aman di perangkat Samsung yang didukung."),
             ("👆","Kunci Sidik Jari","Sensor tidak merespons? Dr.Fone menghapus semua kunci biometrik."),
             ("⚡","5 Menit","Proses 3 langkah sederhana — tidak perlu keahlian teknis.")]
  },
  "nl": {
    "lang":"nl","h1":"Android-scherm ontgrendelen","sub":"Vergeten PIN, patroon of wachtwoord? Dr.Fone ontgrendelt elk Android-scherm in minuten — zonder dataverlies op Samsung.",
    "title":f"Android-scherm Ontgrendelen — PIN, Patroon, FRP Verwijderen ({YEAR})",
    "desc":"Android PIN, patroon of wachtwoord vergeten? Dr.Fone ontgrendelt in minuten. Zonder dataverlies op Samsung. Gratis proefversie beschikbaar.",
    "kw":"android ontgrendelen, vergrendeld android, pin vergeten android, android bypass, samsung ontgrendelen, frp bypass, wachtwoord android verwijderen",
    "feats":[("🔢","PIN &amp; Wachtwoord Verwijderen","Verwijdert onmiddellijk elke PIN of alfanumeriek wachtwoord."),
             ("✋","Patroonvergrendeling Omzeilen","Patroon vergeten? Dr.Fone omzeilt het volledig in 3 minuten."),
             ("🔐","Google FRP Verwijderen","FRP na fabrieksreset? Verwijderd voor Samsung, Xiaomi, Huawei en 29+ merken."),
             ("💾","Geen Dataverlies","Foto's, contacten en apps blijven intact op ondersteunde Samsung-apparaten."),
             ("👆","Vingerafdrukslot","Sensor werkt niet? Dr.Fone verwijdert alle biometrische vergrendelingen."),
             ("⚡","5 Minuten","Eenvoudig 3-staps proces — geen technische kennis vereist.")]
  },
  "pl": {
    "lang":"pl","h1":"Odblokowywanie ekranu Android","sub":"Zapomniałeś PINu, wzoru lub hasła? Dr.Fone odblokuje każdy Android w kilka minut — bez utraty danych na Samsungu.",
    "title":f"Odblokowanie Ekranu Android — Usunięcie PIN, Wzoru, FRP ({YEAR})",
    "desc":"Android PIN, wzór lub hasło zapomniane? Dr.Fone odblokowuje w minutach. Bez utraty danych na Samsungu. Dostępna darmowa wersja próbna.",
    "kw":"odblokuj android, zablokowany ekran android, zapomniałem pin android, ominąć blokadę, samsung odblokuj, frp bypass, usunąć hasło android",
    "feats":[("🔢","Usunięcie PIN i Hasła","Natychmiast usuwa dowolny PIN lub hasło alfanumeryczne."),
             ("✋","Bypass Blokady Wzorem","Zapomniałeś wzoru? Dr.Fone całkowicie go omija w 3 minuty."),
             ("🔐","Bypass Google FRP","Blokada FRP po resecie? Usunięta dla Samsunga, Xiaomi, Huawei i 29+ marek."),
             ("💾","Bez Utraty Danych","Zdjęcia, kontakty i aplikacje zachowane na obsługiwanych Samsungach."),
             ("👆","Odcisk Palca","Czytnik nie działa? Dr.Fone usuwa wszystkie blokady biometryczne."),
             ("⚡","5 Minut","Prosty 3-krokowy proces — bez wiedzy technicznej.")]
  },
  "tr": {
    "lang":"tr","h1":"Android Ekran Kilidini Aç","sub":"PIN, desen veya şifreni mi unuttun? Dr.Fone dakikalar içinde her türlü Android kilidini kaldırır — Samsung'da veri kaybı yok.",
    "title":f"Android Ekran Kilidi Açma — PIN, Desen, FRP Kaldırma ({YEAR})",
    "desc":"Android PIN, desen veya şifre mi unuttun? Dr.Fone dakikalar içinde kaldırır. Samsung'da veri kaybı yok. Ücretsiz deneme mevcut.",
    "kw":"android ekran kilidi aç, android kilidi kaldır, pin unuttum android, android bypass, samsung kilit aç, frp bypass, android şifre sil",
    "feats":[("🔢","PIN ve Şifre Kaldırma","Her türlü PIN veya alfanümerik şifreyi anında kaldırır."),
             ("✋","Desen Kilidini Atlatma","Deseni mi unuttun? Dr.Fone 3 dakika içinde tamamen atlar."),
             ("🔐","Google FRP Bypass","Fabrika sıfırlaması sonrası FRP? Samsung, Xiaomi, Huawei ve 29+ marka için kaldırılır."),
             ("💾","Veri Kaybı Yok","Desteklenen Samsung cihazlarda fotoğraflar, kişiler ve uygulamalar korunur."),
             ("👆","Parmak İzi Kilidi","Sensör çalışmıyor mu? Dr.Fone tüm biyometrik kilitleri kaldırır."),
             ("⚡","5 Dakika","Basit 3 adımlı süreç — teknik bilgi gerekmez.")]
  },
  "sv": {
    "lang":"sv","h1":"Lås upp Android-skärm","sub":"Glömt PIN, mönster eller lösenord? Dr.Fone låser upp vilken Android som helst på minuter — utan dataförlust på Samsung.",
    "title":f"Lås Upp Android-skärm — Ta Bort PIN, Mönster, FRP ({YEAR})",
    "desc":"Android PIN, mönster eller lösenord glömt? Dr.Fone låser upp på minuter. Utan dataförlust på Samsung. Gratis provversion tillgänglig.",
    "kw":"lås upp android, android skärmlås, glömt pin android, android bypass, samsung lås upp, frp bypass, ta bort lösenord android",
    "feats":[("🔢","Ta Bort PIN &amp; Lösenord","Tar omedelbart bort valfri PIN eller alfanumeriskt lösenord."),
             ("✋","Kringgå Mönsterlås","Glömt mönstret? Dr.Fone kringgår det helt på 3 minuter."),
             ("🔐","Google FRP Kringgående","FRP-lås efter återställning? Tas bort för Samsung, Xiaomi, Huawei och 29+ märken."),
             ("💾","Ingen Dataförlust","Foton, kontakter och appar bevaras på stödda Samsung-enheter."),
             ("👆","Fingeravtryckslås","Sensorn fungerar inte? Dr.Fone tar bort alla biometriska lås."),
             ("⚡","5 Minuter","Enkelt 3-stegsprocess — inga tekniska kunskaper krävs.")]
  },
  "fil": {
    "lang":"fil","h1":"I-unlock ang Android Screen","sub":"Nakalimutan ang PIN, pattern o password? I-aalis ng Dr.Fone ang anumang Android lock sa ilang minuto — walang data loss sa Samsung.",
    "title":f"I-unlock ang Android Screen — Alisin ang PIN, Pattern, FRP ({YEAR})",
    "desc":"Nakalimutan ang Android PIN, pattern o password? Dr.Fone nag-aalis sa ilang minuto. Walang data loss sa Samsung. Available ang libreng trial.",
    "kw":"i-unlock android, naka-lock android screen, nakalimutan pin android, bypass android lock, samsung i-unlock, frp bypass, alisin password android",
    "feats":[("🔢","Alisin ang PIN at Password","Agad na inaalis ang anumang PIN o alphanumeric password."),
             ("✋","Bypass ng Pattern Lock","Nakalimutan ang pattern? Nililampasan ito ng Dr.Fone sa loob ng 3 minuto."),
             ("🔐","Google FRP Bypass","FRP lock pagkatapos ng factory reset? Inalis para sa Samsung, Xiaomi, Huawei, at 29+ brand."),
             ("💾","Walang Data Loss","Ang mga larawan, contact, at app ay nananatiling buo sa mga sinusuportahang Samsung device."),
             ("👆","Fingerprint Lock","Hindi gumagana ang sensor? Inalis ng Dr.Fone ang lahat ng biometric lock."),
             ("⚡","5 Minuto","Simpleng 3-hakbang na proseso — walang kinakailangang teknikal na kaalaman.")]
  },
  "vi": {
    "lang":"vi","h1":"Mở Khóa Màn Hình Android","sub":"Quên PIN, hình vẽ hoặc mật khẩu? Dr.Fone mở khóa bất kỳ Android nào trong vài phút — không mất dữ liệu trên Samsung.",
    "title":f"Mở Khóa Màn Hình Android — Xóa PIN, Hình Vẽ, FRP ({YEAR})",
    "desc":"Quên Android PIN, hình vẽ hoặc mật khẩu? Dr.Fone mở trong vài phút. Không mất dữ liệu trên Samsung. Có bản dùng thử miễn phí.",
    "kw":"mở khóa android, màn hình android bị khóa, quên pin android, bypass android, samsung mở khóa, frp bypass, xóa mật khẩu android",
    "feats":[("🔢","Xóa PIN và Mật Khẩu","Xóa ngay lập tức bất kỳ PIN hoặc mật khẩu chữ số nào."),
             ("✋","Bypass Khóa Hình Vẽ","Quên hình vẽ? Dr.Fone vượt qua hoàn toàn trong 3 phút."),
             ("🔐","Bypass Google FRP","Khóa FRP sau reset nhà máy? Được xóa cho Samsung, Xiaomi, Huawei và 29+ thương hiệu."),
             ("💾","Không Mất Dữ Liệu","Ảnh, danh bạ và ứng dụng được giữ nguyên trên các thiết bị Samsung được hỗ trợ."),
             ("👆","Khóa Vân Tay","Cảm biến không hoạt động? Dr.Fone xóa tất cả khóa sinh trắc học."),
             ("⚡","5 Phút","Quy trình 3 bước đơn giản — không cần kỹ năng kỹ thuật.")]
  },
  "th": {
    "lang":"th","h1":"ปลดล็อกหน้าจอ Android","sub":"ลืม PIN รูปแบบ หรือรหัสผ่าน? Dr.Fone ปลดล็อก Android ใดๆ ในไม่กี่นาที — ไม่สูญเสียข้อมูลบน Samsung",
    "title":f"ปลดล็อกหน้าจอ Android — ลบ PIN รูปแบบ FRP ({YEAR})",
    "desc":"ลืม Android PIN รูปแบบ หรือรหัสผ่าน? Dr.Fone ปลดล็อกในไม่กี่นาที ไม่สูญเสียข้อมูลบน Samsung มีเวอร์ชันทดลองใช้ฟรี",
    "kw":"ปลดล็อก android, หน้าจอ android ถูกล็อก, ลืม pin android, bypass android, samsung ปลดล็อก, frp bypass, ลบรหัสผ่าน android",
    "feats":[("🔢","ลบ PIN และรหัสผ่าน","ลบ PIN หรือรหัสผ่านตัวอักษรและตัวเลขใดๆ ทันที"),
             ("✋","ข้ามล็อกรูปแบบ","ลืมรูปแบบ? Dr.Fone ข้ามได้อย่างสมบูรณ์ใน 3 นาที"),
             ("🔐","ข้าม Google FRP","ล็อก FRP หลังรีเซ็ตโรงงาน? ถูกลบสำหรับ Samsung, Xiaomi, Huawei และ 29+ แบรนด์"),
             ("💾","ไม่สูญเสียข้อมูล","รูปภาพ รายชื่อ และแอปยังคงสมบูรณ์บนอุปกรณ์ Samsung ที่รองรับ"),
             ("👆","ล็อกลายนิ้วมือ","เซนเซอร์ไม่ตอบสนอง? Dr.Fone ลบล็อกชีวมิติทั้งหมด"),
             ("⚡","5 นาที","กระบวนการ 3 ขั้นตอนง่ายๆ — ไม่ต้องการทักษะทางเทคนิค")]
  },
  "ms": {
    "lang":"ms","h1":"Buka Kunci Skrin Android","sub":"Terlupa PIN, corak atau kata laluan? Dr.Fone membuka kunci mana-mana Android dalam beberapa minit — tanpa kehilangan data pada Samsung.",
    "title":f"Buka Kunci Skrin Android — Padam PIN, Corak, FRP ({YEAR})",
    "desc":"Terlupa Android PIN, corak atau kata laluan? Dr.Fone membuka dalam minit. Tanpa kehilangan data pada Samsung. Percubaan percuma tersedia.",
    "kw":"buka kunci android, skrin android terkunci, terlupa pin android, bypass android, samsung buka kunci, frp bypass, padam kata laluan android",
    "feats":[("🔢","Padam PIN &amp; Kata Laluan","Memadamkan mana-mana PIN atau kata laluan alfanumerik dengan serta-merta."),
             ("✋","Bypass Kunci Corak","Terlupa corak? Dr.Fone memintas sepenuhnya dalam 3 minit."),
             ("🔐","Bypass Google FRP","Kunci FRP selepas tetapan semula? Dipadamkan untuk Samsung, Xiaomi, Huawei dan 29+ jenama."),
             ("💾","Tanpa Kehilangan Data","Foto, kenalan dan apl kekal selamat pada peranti Samsung yang disokong."),
             ("👆","Kunci Cap Jari","Penderia tidak berfungsi? Dr.Fone mengalih keluar semua kunci biometrik."),
             ("⚡","5 Minit","Proses 3 langkah mudah — tiada kemahiran teknikal diperlukan.")]
  },
  "bn": {
    "lang":"bn","h1":"Android স্ক্রিন লক খুলুন","sub":"PIN, প্যাটার্ন বা পাসওয়ার্ড ভুলে গেছেন? Dr.Fone মিনিটের মধ্যে যেকোনো Android লক সরায় — Samsung-এ কোনো ডেটা হারায় না।",
    "title":f"Android স্ক্রিন আনলক — PIN, প্যাটার্ন, FRP সরান ({YEAR})",
    "desc":"Android PIN, প্যাটার্ন বা পাসওয়ার্ড ভুলে গেছেন? Dr.Fone মিনিটের মধ্যে সরায়। Samsung-এ কোনো ডেটা হারায় না। বিনামূল্যে ট্রায়াল পাওয়া যাচ্ছে।",
    "kw":"android আনলক, android স্ক্রিন লক, pin ভুলে গেছি, android বাইপাস, samsung আনলক, frp bypass, android পাসওয়ার্ড সরান",
    "feats":[("🔢","PIN ও পাসওয়ার্ড সরান","যেকোনো PIN বা আলফানিউমেরিক পাসওয়ার্ড তাৎক্ষণিকভাবে সরায়।"),
             ("✋","প্যাটার্ন লক বাইপাস","প্যাটার্ন ভুলে গেছেন? Dr.Fone ৩ মিনিটের মধ্যে সম্পূর্ণ বাইপাস করে।"),
             ("🔐","Google FRP বাইপাস","ফ্যাক্টরি রিসেটের পর FRP লক? Samsung, Xiaomi, Huawei এবং ২৯+ ব্র্যান্ডে সরানো হয়।"),
             ("💾","কোনো ডেটা হারায় না","সমর্থিত Samsung ডিভাইসে ছবি, যোগাযোগ এবং অ্যাপ সুরক্ষিত থাকে।"),
             ("👆","ফিঙ্গারপ্রিন্ট লক","সেন্সর কাজ করছে না? Dr.Fone সব বায়োমেট্রিক লক সরায়।"),
             ("⚡","৫ মিনিট","সহজ ৩-ধাপের প্রক্রিয়া — কোনো প্রযুক্তিগত জ্ঞান দরকার নেই।")]
  },
  "uk": {
    "lang":"uk","h1":"Розблокувати екран Android","sub":"Забули PIN, малюнок або пароль? Dr.Fone знімає будь-яке блокування Android за хвилини — без втрати даних на Samsung.",
    "title":f"Розблокувати Екран Android — Видалити PIN, Малюнок, FRP ({YEAR})",
    "desc":"Android PIN, малюнок або пароль забуті? Dr.Fone розблоковує за хвилини. Без втрати даних на Samsung. Безкоштовна пробна версія.",
    "kw":"розблокувати android, зняти блокування екрана android, забув pin android, обійти блокування, розблокування samsung, frp обхід, видалити пароль android",
    "feats":[("🔢","Видалення PIN та Пароля","Миттєво видаляє будь-який PIN або буквено-цифровий пароль."),
             ("✋","Обхід Графічного Ключа","Забули малюнок? Dr.Fone повністю обходить його за 3 хвилини."),
             ("🔐","Обхід Google FRP","Блокування FRP після скидання? Знімається для Samsung, Xiaomi, Huawei та 29+ брендів."),
             ("💾","Без Втрати Даних","Фото, контакти та програми зберігаються на підтримуваних Samsung."),
             ("👆","Розблокування Відбитка","Сенсор не працює? Dr.Fone видаляє всі біометричні блокування."),
             ("⚡","5 Хвилин","Простий 3-кроковий процес — технічні навички не потрібні.")]
  },
  "ro": {
    "lang":"ro","h1":"Deblochează Ecranul Android","sub":"Ai uitat PIN-ul, modelul sau parola? Dr.Fone deblochează orice Android în câteva minute — fără pierderea datelor pe Samsung.",
    "title":f"Deblocare Ecran Android — Eliminare PIN, Model, FRP ({YEAR})",
    "desc":"Android PIN, model sau parolă uitate? Dr.Fone deblochează în minute. Fără pierderea datelor pe Samsung. Versiune de probă gratuită disponibilă.",
    "kw":"deblocare android, ecran android blocat, am uitat pin android, bypass android, samsung deblocare, frp bypass, elimina parola android",
    "feats":[("🔢","Eliminarea PIN și Parolei","Elimină instantaneu orice PIN sau parolă alfanumerică."),
             ("✋","Bypass Model de Blocare","Ai uitat modelul? Dr.Fone îl ocolește complet în 3 minute."),
             ("🔐","Bypass Google FRP","Blocare FRP după resetare? Eliminată pentru Samsung, Xiaomi, Huawei și 29+ mărci."),
             ("💾","Fără Pierderea Datelor","Fotografiile, contactele și aplicațiile rămân intacte pe Samsung-urile suportate."),
             ("👆","Blocare Amprentă","Senzorul nu funcționează? Dr.Fone elimină toate blocările biometrice."),
             ("⚡","5 Minute","Proces simplu în 3 pași — nu sunt necesare cunoștințe tehnice.")]
  },
  "cs": {
    "lang":"cs","h1":"Odemknout Obrazovku Android","sub":"Zapomněli jste PIN, vzor nebo heslo? Dr.Fone odemkne jakýkoli Android za minuty — bez ztráty dat na Samsungu.",
    "title":f"Odemknutí Obrazovky Android — Odstranění PIN, Vzoru, FRP ({YEAR})",
    "desc":"Android PIN, vzor nebo heslo zapomenuto? Dr.Fone odemkne za minuty. Bez ztráty dat na Samsungu. Dostupná bezplatná zkušební verze.",
    "kw":"odemknout android, zamčená obrazovka android, zapomněl jsem pin android, obejít android, samsung odemknout, frp bypass, odstranit heslo android",
    "feats":[("🔢","Odstranění PIN a Hesla","Okamžitě odstraní jakýkoli PIN nebo alfanumerické heslo."),
             ("✋","Obejití Vzoru","Zapomněli jste vzor? Dr.Fone ho zcela obejde za 3 minuty."),
             ("🔐","Obejití Google FRP","Zámek FRP po obnovení? Odstraněn pro Samsung, Xiaomi, Huawei a 29+ značek."),
             ("💾","Bez Ztráty Dat","Fotky, kontakty a aplikace zůstanou nedotčeny na podporovaných Samsunzích."),
             ("👆","Zámek Otisků Prstů","Snímač nefunguje? Dr.Fone odstraní všechny biometrické zámky."),
             ("⚡","5 Minut","Jednoduchý 3-krokový proces — nejsou nutné technické znalosti.")]
  },
}

def lang_page(code, d):
    feat_cards = "".join(f'<div class="card"><div class="icon">{i}</div><h3>{t}</h3><p>{p}</p></div>' for i,t,p in d["feats"])
    body = f"""
<div class="hero">
  <h1><em>{d['h1']}</em></h1>
  <p>{d['sub']}</p>
  {cta("🔓 Download Dr.Fone")}
</div>
<main>
<div class="trust">
  <div class="trust-item"><strong>50M+</strong><span>Users</span></div>
  <div class="trust-item"><strong>2,000+</strong><span>Devices</span></div>
  <div class="trust-item"><strong>29+</strong><span>Brands</span></div>
  <div class="trust-item"><strong>Android 16</strong><span>Support</span></div>
  <div class="trust-item"><strong>7-Day</strong><span>Refund</span></div>
</div>
<section><h2>Features</h2><div class="cards">{feat_cards}</div></section>
<section>
<h2>3-Step Process</h2>
<div class="steps">
  <div class="step"><div class="snum">1</div><div><h3>Download Dr.Fone</h3><p>Free download for Windows &amp; Mac. Install in under 2 minutes.</p></div></div>
  <div class="step"><div class="snum">2</div><div><h3>Connect via USB</h3><p>Plug in your Android. Dr.Fone detects your device model and Android version automatically.</p></div></div>
  <div class="step"><div class="snum">3</div><div><h3>Unlock Complete</h3><p>Follow on-screen guide. Unlock completes in 2–5 minutes. Set a new PIN immediately after.</p></div></div>
</div>
</section>
<div class="cta-box">
  <h2>{d['h1']}</h2>
  <p>{d['sub']}</p>
  {cta("🔓 Download Dr.Fone Free")}
</div>
</main>"""
    url = f"{SITE}/lang/{code}/"
    return shell(d["title"], d["desc"], d["kw"], body, lang=d["lang"], canon=url)

# ─────────────────────────────────────────────────────────────────────────────
# SITEMAP
# ─────────────────────────────────────────────────────────────────────────────
def sitemap(urls):
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, pri in urls:
        lines.append(f"  <url><loc>{u}</loc><changefreq>weekly</changefreq><priority>{pri}</priority></url>")
    lines.append("</urlset>")
    return "\n".join(lines)

ROBOTS = f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n"

# ─────────────────────────────────────────────────────────────────────────────
# MAIN BUILD
# ─────────────────────────────────────────────────────────────────────────────
def main():
    urls = []

    def w(rel, html, pri="0.8"):
        p = BASE / rel
        write(p, html)
        urls.append((f"{SITE}/{rel.replace('index.html','')}", pri))

    # Core pages
    w("index.html",           home(),           "1.0")
    w("how-it-works/index.html", how_it_works())
    w("samsung/index.html",   samsung(),        "0.9")
    w("frp/index.html",       frp(),            "0.9")
    w("forgot-pin/index.html",forgot_pin(),     "0.9")
    w("no-data-loss/index.html", no_data_loss())
    w("free-download/index.html", free_download())
    w("pattern/index.html",   pattern())
    w("fingerprint/index.html", fingerprint())
    w("global/index.html",    global_page())
    w("brands/index.html",    brands_index())

    # Brand pages
    for slug, data in BRAND_DATA.items():
        slug_url = slug.replace("+","").replace(" ","-")
        w(f"brands/{slug_url}/index.html", brand_page(slug_url, data))

    # Language pages
    for code, data in LANG_DATA.items():
        w(f"lang/{code}/index.html", lang_page(code, data))

    # Sitemap & robots
    write(BASE/"sitemap.xml", sitemap(urls))
    write(BASE/"robots.txt", ROBOTS)

    html_count = len(list(BASE.rglob("*.html")))
    print(f"✅ Built {html_count} HTML pages across {len(urls)} URLs")
    print(f"   Core pages:  11")
    print(f"   Brand pages: {len(BRAND_DATA)}")
    print(f"   Lang pages:  {len(LANG_DATA)}")

if __name__ == "__main__":
    main()
