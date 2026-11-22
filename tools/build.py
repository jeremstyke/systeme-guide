#!/usr/bin/env python3
# Genere le site statique multilingue dans le dossier passe en argument.
import os, sys, json, html
sys.path.insert(0, os.path.dirname(__file__))
from i18n import LANGS

OUT = sys.argv[1]
BASE = "https://jeremstyke.github.io/systeme-guide/"
SA = "saf63423d0e3bb82b406a7beae792cc107"
E = html.escape

SEP = {"en": ",", "jp": ",", "id": ".", "de": ".", "es": ".", "it": ".", "pt": ".", "br": ".", "ro": ".", "sq": "."}
def num(n, code):
    s = f"{n:,}"
    sep = SEP.get(code, " ")  # espace insecable par defaut (fr, pl, ru, sv, no, sk)
    return s.replace(",", sep)

def aff(L):
    return f"https://systeme.io/{L['sio']}?sa={SA}" if L["sio"] else f"https://systeme.io/?sa={SA}"

def url(L):
    return BASE + (L["path"] + "/" if L["path"] else "")

CSS = """
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;font-family:system-ui,-apple-system,'Segoe UI',Roboto,'Noto Sans','Noto Sans JP',sans-serif;color:#1d2433;background:#fff;line-height:1.6}
a{color:#2457d6}.wrap{max-width:1040px;margin:0 auto;padding:0 20px}
header{position:sticky;top:0;background:rgba(255,255,255,.95);backdrop-filter:blur(6px);border-bottom:1px solid #eceff5;z-index:5}
header .wrap{display:flex;align-items:center;justify-content:space-between;height:60px;gap:10px}
.logo{font-weight:800;font-size:18px;color:#1d2433;text-decoration:none}.logo span{color:#2457d6}
details.lang{position:relative}details.lang summary{cursor:pointer;list-style:none;font-size:14px;padding:6px 10px;border:1px solid #dfe4ee;border-radius:8px}
details.lang summary::-webkit-details-marker{display:none}
details.lang div{position:absolute;right:0;top:40px;background:#fff;border:1px solid #dfe4ee;border-radius:10px;padding:8px;width:230px;max-height:60vh;overflow:auto;box-shadow:0 10px 30px rgba(0,0,0,.08)}
details.lang a{display:block;padding:6px 10px;border-radius:6px;text-decoration:none;color:#1d2433;font-size:14px}details.lang a:hover{background:#f2f5fb}
.btn{display:inline-block;background:#ff7a1a;color:#fff;font-weight:800;text-decoration:none;padding:15px 26px;border-radius:12px;font-size:17px;box-shadow:0 6px 18px rgba(255,122,26,.3)}
.btn:hover{background:#f06a08}.btn.small{padding:9px 16px;font-size:14px;box-shadow:none}
.hero{background:linear-gradient(160deg,#eef3ff 0%,#fff 70%);padding:64px 0 54px;text-align:center}
.hero h1{font-size:clamp(30px,5.5vw,50px);line-height:1.15;margin:0 0 16px;letter-spacing:-.5px}
.hero p.sub{font-size:19px;color:#4a5568;max-width:720px;margin:0 auto 26px}.note{font-size:14px;color:#6b7690;margin-top:12px}
section{padding:54px 0}section h2{font-size:clamp(24px,4vw,32px);text-align:center;margin:0 0 26px}
.lead{max-width:760px;margin:0 auto;font-size:18px;color:#3d4659;text-align:center}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px}
.card{border:1px solid #eceff5;border-radius:16px;padding:22px;background:#fff}.card h3{margin:0 0 6px;font-size:18px}.card p{margin:0;color:#4a5568}
.ico{width:40px;height:40px;border-radius:10px;background:#eef3ff;color:#2457d6;display:flex;align-items:center;justify-content:center;font-weight:900;margin-bottom:10px}
.alt{background:#f7f9fc}
.plans{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:14px}
.plan{background:#fff;border:1px solid #e2e7f0;border-radius:16px;padding:22px;text-align:center}
.plan.hl{border:2px solid #2457d6;box-shadow:0 10px 30px rgba(36,87,214,.12)}
.plan h3{margin:0;font-size:18px}.price{font-size:36px;font-weight:900;margin:8px 0}.price small{font-size:15px;font-weight:600;color:#6b7690}
.plan ul{list-style:none;padding:0;margin:12px 0 18px;color:#3d4659;font-size:15px}.plan li{padding:4px 0}
.center{text-align:center}.small-note{font-size:14px;color:#6b7690;text-align:center;margin-top:14px}
ol.steps{counter-reset:s;list-style:none;padding:0;max-width:640px;margin:0 auto}
ol.steps li{counter-increment:s;display:flex;gap:14px;align-items:center;padding:12px 0;font-size:17px}
ol.steps li::before{content:counter(s);flex:0 0 36px;height:36px;border-radius:50%;background:#2457d6;color:#fff;font-weight:800;display:flex;align-items:center;justify-content:center}
.faq{max-width:760px;margin:0 auto}.faq details{border:1px solid #e2e7f0;border-radius:12px;padding:14px 18px;margin:10px 0;background:#fff}
.faq summary{cursor:pointer;font-weight:700}.faq p{margin:10px 0 0;color:#4a5568}
.final{background:#1d2a5c;color:#fff;text-align:center;border-radius:20px;padding:46px 22px}.final p{color:#cdd6f4;font-size:18px;margin:0 0 22px}
footer{border-top:1px solid #eceff5;padding:30px 0;font-size:14px;color:#6b7690}
footer .langs{display:flex;flex-wrap:wrap;gap:6px 14px;margin:10px 0 16px}footer .langs a{color:#4a5568;text-decoration:none}
.suggest{display:none;background:#fff8e6;border-bottom:1px solid #ffe2a8;text-align:center;padding:8px;font-size:14px}
"""

ICONS = ["▲", "✉", "▶", "⚙", "✎", "%"]

def page(code, L):
    a = aff(L)
    link = f'href="{E(a)}" rel="sponsored nofollow noopener" target="_blank"'
    alts = "\n".join(f'<link rel="alternate" hreflang="{M["hl"]}" href="{url(M)}">' for M in LANGS.values())
    alts += f'\n<link rel="alternate" hreflang="x-default" href="{BASE}">'
    depth = "../" if L["path"] else ""
    rel = lambda M: depth + (M["path"] + "/" if M["path"] else "")
    menu = "".join(f'<a href="{rel(M)}" hreflang="{M["hl"]}" lang="{M["hl"]}">{E(M["name"])}</a>' for M in LANGS.values())
    feats = "".join(f'<div class="card"><div class="ico">{ICONS[i]}</div><h3>{E(t)}</h3><p>{E(d)}</p></div>' for i, (t, d) in enumerate(L["f"]))
    n = lambda x: num(x, code)
    plans = [
        (L["free"], 0, [f"{n(2000)} {L['contacts']}", f"3 {L['funnels']}", f"1 {L['courses']}"], False),
        ("Startup", 17, [f"{n(5000)} {L['contacts']}", f"10 {L['funnels']}", f"5 {L['courses']}"], True),
        ("Webinar", 47, [f"{n(10000)} {L['contacts']}", f"50 {L['funnels']}", f"20 {L['courses']}", L["webinars"]], False),
        ("Unlimited", 97, [L["unl_line"]], False),
    ]
    plan_html = "".join(
        f'<div class="plan{" hl" if hl else ""}"><h3>{E(nm)}</h3><div class="price">${p}<small>{E(L["month"])}</small></div>'
        f'<ul>{"".join(f"<li>{E(x)}</li>" for x in items)}</ul><a class="btn small" {link}>{E(L["cta"])}</a></div>'
        for nm, p, items, hl in plans)
    steps = "".join(f"<li>{E(s)}</li>" for s in L["s"])
    faq = "".join(f"<details><summary>{E(q)}</summary><p>{E(r)}</p></details>" for q, r in L["q"])
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": L["hl"],
          "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": r}} for q, r in L["q"]]}
    # suggestion de langue (seulement sur la page anglaise)
    sug = ""
    if not L["path"]:
        m = {M["hl"].split("-")[0].lower() + ("-br" if M["hl"] == "pt-BR" else ""): (rel(M), M["name"]) for M in LANGS.values() if M["path"]}
        sug = ("<script>(function(){try{var l=(navigator.language||'').toLowerCase(),m=" + json.dumps(m, ensure_ascii=False) +
               ",k=l.indexOf('pt-br')===0?'pt-br':l.split('-')[0];if(k==='no'||k==='nn')k='nb';var t=m[k];if(t){var b=document.getElementById('sg');"
               "b.innerHTML='<a href=\"'+t[0]+'\">'+t[1]+' &rarr;</a>';b.style.display='block'}}catch(e){}})();</script>")
    return f"""<!doctype html>
<html lang="{L['hl']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(L['title'])}</title>
<meta name="description" content="{E(L['desc'])}">
<link rel="canonical" href="{url(L)}">
{alts}
<meta property="og:title" content="{E(L['title'])}">
<meta property="og:description" content="{E(L['desc'])}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url(L)}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%232457d6'/%3E%3Cpath d='M18 40l10-10 8 8 12-14' stroke='white' stroke-width='6' fill='none' stroke-linecap='round'/%3E%3C/svg%3E">
<style>{CSS}</style>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<div class="suggest" id="sg"></div>
<header><div class="wrap">
<a class="logo" href="{rel(L)}">Systeme<span>.io</span> Guide</a>
<details class="lang"><summary>🌐 {E(L['name'])}</summary><div>{menu}</div></details>
</div></header>
<main>
<div class="hero"><div class="wrap">
<h1>{E(L['h1'])}</h1>
<p class="sub">{E(L['sub'])}</p>
<a class="btn" {link}>{E(L['cta'])}</a>
<p class="note">{E(L['nocard'])}</p>
</div></div>
<section><div class="wrap"><h2>{E(L['what_h'])}</h2><p class="lead">{E(L['what_p'])}</p></div></section>
<section class="alt"><div class="wrap"><h2>{E(L['feat_h'])}</h2><div class="grid">{feats}</div></div></section>
<section id="pricing"><div class="wrap"><h2>{E(L['price_h'])}</h2><div class="plans">{plan_html}</div>
<p class="small-note">{E(L['price_note'])} {E(L['all_inc'])}</p></div></section>
<section class="alt"><div class="wrap"><h2>{E(L['steps_h'])}</h2><ol class="steps">{steps}</ol>
<p class="center" style="margin-top:20px"><a class="btn" {link}>{E(L['cta'])}</a></p></div></section>
<section><div class="wrap"><h2>{E(L['faq_h'])}</h2><div class="faq">{faq}</div></div></section>
<section><div class="wrap"><div class="final"><h2>{E(L['final_h'])}</h2><p>{E(L['final_p'])}</p><a class="btn" {link}>{E(L['cta'])}</a></div></div></section>
</main>
<footer><div class="wrap">
<p>{E(L['disc'])}</p>
<strong>{E(L['other'])}</strong>
<div class="langs">{menu}</div>
<p>© <span id="y"></span> Systeme.io Guide</p>
</div></footer>
<script>document.getElementById('y').textContent=new Date().getFullYear();</script>
{sug}
</body>
</html>
"""

os.makedirs(OUT, exist_ok=True)
for code, L in LANGS.items():
    d = os.path.join(OUT, L["path"]) if L["path"] else OUT
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(page(code, L))

# sitemap avec hreflang
items = []
for L in LANGS.values():
    alt = "".join(f'<xhtml:link rel="alternate" hreflang="{M["hl"]}" href="{url(M)}"/>' for M in LANGS.values())
    items.append(f"<url><loc>{url(L)}</loc>{alt}</url>")
with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">'
            + "".join(items) + "</urlset>\n")
with open(os.path.join(OUT, "robots.txt"), "w") as f:
    f.write(f"User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n")
open(os.path.join(OUT, ".nojekyll"), "w").close()
print("ok", len(LANGS), "langues")
