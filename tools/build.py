#!/usr/bin/env python3
# Genere le site statique multilingue dans le dossier passe en argument.
import os, sys, json, html
sys.path.insert(0, os.path.dirname(__file__))
from i18n import LANGS
from articles import ARTICLES, BLOGTXT
from pages_i18n import P
from long_i18n import LONG
from long_es import LONG_ES
from long_br import LONG_BR
from long_de import LONG_DE
for _x in (LONG_ES, LONG_BR, LONG_DE): LONG.update(_x)

OUT = sys.argv[1]
BASE = "https://jeremstyke.github.io/systeme-guide/"
SA = "saf63423d0e3bb82b406a7beae792cc107"
E = html.escape

SEP = {"en": ",", "jp": ",", "id": ".", "de": ".", "es": ".", "it": ".", "pt": ".", "br": ".", "ro": ".", "sq": "."}
def num(n, code):
    s = f"{n:,}"
    sep = SEP.get(code, " ")  # espace insecable par defaut (fr, pl, ru, sv, no, sk)
    return s.replace(",", sep)

EURO = {"fr", "de", "es", "it", "pt", "pl", "ro", "sv", "no", "sk", "sq"}
EURO_BEFORE = {"sq"}
def money(p, code):
    # Europe : euros, symbole apres le montant (usage local) ; ailleurs : dollars
    if code in EURO:
        return f"€{p}" if code in EURO_BEFORE else f"{p}\u00a0€"
    return f"${p}"

def aff(L):
    return f"https://systeme.io/{L['sio']}?sa={SA}" if L["sio"] else f"https://systeme.io/?sa={SA}"

def url(L):
    return BASE + (L["path"] + "/" if L["path"] else "")

CSS = """
:root{--blue:#00A0FF;--blue2:#0086d6;--deep:#0B3B66;--ink:#19191B;--mute:#7B7E85;--soft:#F2F2F3;--sky:#E8F6FF;--line:#E4E6EA}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;font-family:Inter,system-ui,-apple-system,'Segoe UI',Roboto,'Noto Sans','Noto Sans JP',sans-serif;color:var(--ink);background:#fff;line-height:1.6;-webkit-font-smoothing:antialiased}
a{color:var(--blue2)}.wrap{max-width:1100px;margin:0 auto;padding:0 20px}
header{position:sticky;top:0;z-index:5;background:rgba(255,255,255,.92);backdrop-filter:saturate(180%) blur(10px);border-bottom:1px solid var(--line)}
header .wrap{display:flex;align-items:center;justify-content:space-between;gap:12px;height:64px}
.logo{display:flex;align-items:center;gap:9px;font-weight:800;font-size:18px;color:var(--ink);text-decoration:none;letter-spacing:-.3px}
.logo i{width:30px;height:30px;border-radius:9px;background:var(--blue);display:inline-flex;align-items:center;justify-content:center}
.logo strong{font-weight:800}.logo span{color:var(--blue)}.logo em{font-style:normal;font-size:11px;font-weight:700;color:var(--mute);border:1px solid var(--line);border-radius:999px;padding:2px 8px;margin-left:4px}
.hdr-r{display:flex;align-items:center;gap:10px}
details.lang{position:relative}details.lang summary{cursor:pointer;list-style:none;font-size:14px;font-weight:600;padding:7px 12px;border:1px solid var(--line);border-radius:10px;background:#fff}
details.lang summary::-webkit-details-marker{display:none}
details.lang>div{position:absolute;right:0;top:44px;background:#fff;border:1px solid var(--line);border-radius:14px;box-shadow:0 18px 40px rgba(11,59,102,.14);padding:8px;display:grid;grid-template-columns:1fr 1fr;gap:2px;min-width:290px;max-height:70vh;overflow:auto}
details.lang a{display:block;padding:7px 10px;border-radius:8px;text-decoration:none;color:var(--ink);font-size:14px}details.lang a:hover{background:var(--sky);color:var(--blue2)}
.btn{display:inline-flex;align-items:center;gap:8px;background:var(--blue);color:#fff;font-weight:700;text-decoration:none;padding:16px 28px;border-radius:12px;font-size:17px;box-shadow:0 10px 24px rgba(0,160,255,.32);transition:transform .15s,background .15s}
.btn:hover{background:var(--blue2);transform:translateY(-1px);color:#fff}.btn:focus-visible{outline:3px solid #9bd8ff;outline-offset:3px}
.btn::after{content:"→"}.btn.small{padding:10px 18px;font-size:15px;box-shadow:none}.btn.small::after{content:none}
.btn.hdr{padding:9px 16px;font-size:14px;box-shadow:none}.btn.hdr::after{content:none}
.hero{background:radial-gradient(900px 420px at 85% -10%,#c9ecff 0,rgba(201,236,255,0) 70%),linear-gradient(180deg,var(--sky),#fff 85%);padding:64px 0 40px;overflow:hidden}
.hero .wrap{display:grid;grid-template-columns:1.05fr .95fr;gap:44px;align-items:center}
.pill{display:inline-flex;align-items:center;gap:8px;background:#fff;border:1px solid #cfeaff;color:var(--deep);font-size:13px;font-weight:700;border-radius:999px;padding:6px 12px;margin-bottom:18px}
.pill b{background:var(--blue);color:#fff;border-radius:999px;padding:1px 8px;font-size:11px}
.hero h1{font-size:clamp(32px,5vw,52px);line-height:1.08;margin:0 0 18px;letter-spacing:-1.2px;font-weight:800;color:var(--ink)}
.hero p.sub{font-size:19px;color:#454850;margin:0 0 28px;max-width:560px}
.note{font-size:14px;color:var(--mute);margin-top:14px;display:flex;align-items:center;gap:6px}.note::before{content:"✓";color:#16a34a;font-weight:800}
.mock{background:#fff;border:1px solid #d8ecfb;border-radius:18px;box-shadow:0 30px 60px rgba(11,59,102,.16);overflow:hidden;transform:rotate(1deg)}
.mock .bar{display:flex;gap:6px;padding:12px 14px;background:var(--soft);border-bottom:1px solid var(--line)}.mock .bar i{width:10px;height:10px;border-radius:50%;background:#d4d6db}
.mock .bar i:first-child{background:#ff6159}.mock .bar i:nth-child(2){background:#ffbd2e}.mock .bar i:nth-child(3){background:#28c941}
.mock .in{padding:18px;display:grid;gap:12px}
.mrow{display:flex;align-items:center;justify-content:space-between;border:1px solid var(--line);border-radius:12px;padding:12px 14px;font-weight:600;font-size:15px}
.mrow span{color:var(--mute);font-weight:500;font-size:13px}.mrow b{font-size:20px;color:var(--deep)}
.mfun{display:flex;align-items:flex-end;gap:8px}.mfun div{flex:1;height:54px;border-radius:10px;background:linear-gradient(180deg,#bfe7ff,#7fcfff)}
.mfun div:nth-child(2){height:42px;opacity:.85}.mfun div:nth-child(3){height:30px;opacity:.7}.mfun div:nth-child(4){height:20px;opacity:.55}
.mchart{height:70px;border-radius:12px;background:linear-gradient(180deg,rgba(0,160,255,.18),rgba(0,160,255,0)),url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 300 70' preserveAspectRatio='none'%3E%3Cpath d='M0 60 C40 55 60 40 100 42 S170 20 210 24 S270 6 300 8' fill='none' stroke='%2300A0FF' stroke-width='3'/%3E%3C/svg%3E") center/100% 100% no-repeat}
section{padding:72px 0}section h2{font-size:clamp(26px,3.6vw,38px);text-align:center;margin:0 0 14px;letter-spacing:-.6px;line-height:1.15}
.kicker{display:block;text-align:center;color:var(--blue2);font-weight:700;font-size:14px;margin-bottom:8px}
.lead{max-width:740px;margin:0 auto;font-size:18px;color:#454850;text-align:center}
.alt{background:var(--soft)}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:34px}
.card{border:1px solid var(--line);border-radius:18px;padding:26px;background:#fff;transition:box-shadow .2s,border-color .2s}
.card:hover{border-color:#bfe5ff;box-shadow:0 14px 34px rgba(11,59,102,.08)}
.card h3{margin:0 0 6px;font-size:18px;letter-spacing:-.2px}.card p{margin:0;color:#55585f;font-size:15.5px}
.ico{width:46px;height:46px;border-radius:13px;background:var(--sky);display:flex;align-items:center;justify-content:center;margin-bottom:16px}
.ico svg{width:24px;height:24px;stroke:var(--blue);fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.plans{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:34px;align-items:stretch}
.plan{border:1px solid var(--line);border-radius:18px;padding:26px 22px;background:#fff;display:flex;flex-direction:column}
.plan.hl{border:2px solid var(--blue);box-shadow:0 20px 44px rgba(0,160,255,.18);position:relative}
.plan.hl::before{content:"★";position:absolute;top:-14px;left:50%;transform:translateX(-50%);background:var(--blue);color:#fff;width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:14px}
.plan h3{margin:0;font-size:17px;color:var(--mute);font-weight:700}.price{font-size:40px;font-weight:800;margin:6px 0 4px;letter-spacing:-1px}.price small{font-size:15px;font-weight:600;color:var(--mute);letter-spacing:0}
.plan ul{list-style:none;padding:0;margin:12px 0 22px;color:#3c3f45;font-size:15px;flex:1}.plan li{padding:6px 0 6px 26px;position:relative}
.plan li::before{content:"";position:absolute;left:0;top:10px;width:16px;height:16px;border-radius:50%;background:var(--sky) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='M4 8.5l2.5 2.5L12 5.5' fill='none' stroke='%2300A0FF' stroke-width='2' stroke-linecap='round'/%3E%3C/svg%3E") center/16px no-repeat}
.plan .btn{justify-content:center}.plan:not(.hl) .btn{background:#fff;color:var(--blue2);border:1.5px solid var(--blue)}.plan:not(.hl) .btn:hover{background:var(--sky)}
.center{text-align:center}.small-note{font-size:14px;color:var(--mute);text-align:center;margin-top:18px}
ol.steps{list-style:none;padding:0;margin:34px auto 0;max-width:900px;display:grid;grid-template-columns:repeat(3,1fr);gap:18px;counter-reset:s}
ol.steps li{counter-increment:s;background:#fff;border:1px solid var(--line);border-radius:18px;padding:24px;font-size:16.5px;font-weight:600}
ol.steps li::before{content:counter(s);display:flex;width:38px;height:38px;border-radius:12px;background:var(--blue);color:#fff;font-weight:800;align-items:center;justify-content:center;margin-bottom:12px}
.faq{max-width:780px;margin:30px auto 0}.faq details{border:1px solid var(--line);border-radius:14px;padding:16px 20px;margin-bottom:10px;background:#fff}
.faq summary{cursor:pointer;font-weight:700;list-style:none;display:flex;justify-content:space-between;gap:12px}.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";color:var(--blue);font-size:22px;line-height:1}.faq details[open] summary::after{content:"−"}
.faq p{margin:10px 0 0;color:#55585f}
.final{background:linear-gradient(135deg,var(--blue),#0070c9);color:#fff;text-align:center;border-radius:24px;padding:56px 24px;box-shadow:0 30px 60px rgba(0,112,201,.25)}
.final h2{color:#fff}.final p{color:#e3f4ff;font-size:18px;margin:0 auto 26px;max-width:620px}
.final .btn{background:#fff;color:var(--blue2);box-shadow:0 10px 24px rgba(0,0,0,.15)}.final .btn:hover{background:#f0f9ff;color:var(--blue2)}
footer{border-top:1px solid var(--line);padding:34px 0;font-size:14px;color:var(--mute)}
.langs{display:flex;flex-wrap:wrap;gap:6px 14px;margin:8px 0 16px}.langs a{color:var(--mute);text-decoration:none}.langs a:hover{color:var(--blue2)}
.suggest{display:none;background:var(--sky);border-bottom:1px solid #cfeaff;text-align:center;padding:9px;font-size:14px;font-weight:600}
.nav-g{font-size:14px;font-weight:600;color:var(--ink);text-decoration:none;padding:7px 4px}.nav-g:hover{color:var(--blue2)}
.posts{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:30px}
.post{display:block;border:1px solid var(--line);border-radius:18px;padding:24px;background:#fff;text-decoration:none;color:var(--ink);transition:box-shadow .2s,border-color .2s}
.post:hover{border-color:#bfe5ff;box-shadow:0 14px 34px rgba(11,59,102,.08)}.post h3{margin:0 0 8px;font-size:18px;line-height:1.3}.post p{margin:0;color:#55585f;font-size:15px}
.post span{display:inline-block;margin-top:12px;color:var(--blue2);font-weight:700;font-size:14px}
.art{max-width:760px;margin:0 auto;padding:48px 20px 20px}.crumbs{font-size:14px;color:var(--mute);margin-bottom:14px}.crumbs a{color:var(--mute)}
.art h1{font-size:clamp(30px,4.6vw,44px);line-height:1.12;letter-spacing:-1px;margin:0 0 14px}.meta{color:var(--mute);font-size:14px;margin-bottom:28px}
.art h2{font-size:clamp(22px,3vw,28px);margin:40px 0 12px;letter-spacing:-.4px;line-height:1.2}.art h3{font-size:19px;margin:26px 0 8px}
.art p,.art li{font-size:17.5px;color:#2b2d31}.art ul,.art ol{padding-left:22px}.art li{margin:6px 0}
.art table{width:100%;border-collapse:collapse;margin:20px 0;font-size:15.5px}.art th,.art td{border:1px solid var(--line);padding:10px 12px;text-align:left;vertical-align:top}.art th{background:var(--sky)}
.tbl{overflow-x:auto}
.cta-box{background:linear-gradient(135deg,var(--sky),#fff);border:1px solid #cfeaff;border-radius:18px;padding:24px;margin:32px 0;text-align:center}
.cta-box p{margin:0 0 16px;font-weight:600}
.tip{border-left:4px solid var(--blue);background:var(--soft);border-radius:0 12px 12px 0;padding:14px 18px;margin:22px 0}
@media(max-width:900px){.posts{grid-template-columns:1fr 1fr}}@media(max-width:600px){.posts{grid-template-columns:1fr}.nav-g{display:none}}
@media(max-width:900px){.hero .wrap{grid-template-columns:1fr}.mock{transform:none;max-width:460px}.grid,.plans{grid-template-columns:1fr 1fr}ol.steps{grid-template-columns:1fr}}
@media(max-width:600px){.grid,.plans{grid-template-columns:1fr}.hero{padding:40px 0 24px}section{padding:52px 0}.logo em,.btn.hdr{display:none}.hero p.sub{font-size:17px}}
.pc{list-style:none;padding:0!important;margin:0}.pc li{padding:9px 0 9px 32px!important;position:relative;border-bottom:1px solid var(--line);margin:0!important}
.pc.good li::before{content:"✓";position:absolute;left:6px;color:#16a34a;font-weight:800}.pc.bad li::before{content:"✕";position:absolute;left:6px;color:#dc2626;font-weight:800}
.two{display:grid;grid-template-columns:1fr 1fr;gap:26px}@media(max-width:700px){.two{grid-template-columns:1fr}}
.art td.win{background:#ecfdf3;font-weight:600}.glinks{display:flex;flex-wrap:wrap;gap:8px 16px;margin-bottom:14px}.glinks a{color:var(--ink);font-weight:600;text-decoration:none}.glinks a:hover{color:var(--blue2)}
.cmp{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:30px}@media(max-width:800px){.cmp{grid-template-columns:1fr}}
@media(prefers-reduced-motion:reduce){*{transition:none!important;scroll-behavior:auto!important}}
"""

ICONS = [
 '<svg viewBox="0 0 24 24"><path d="M3 4h18l-7 8v6l-4 2v-8z"/></svg>',
 '<svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>',
 '<svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="13" rx="2"/><path d="M10 8.5v5l4.5-2.5z"/><path d="M8 21h8"/></svg>',
 '<svg viewBox="0 0 24 24"><path d="M13 2L4 14h7l-1 8 9-12h-7z"/></svg>',
 '<svg viewBox="0 0 24 24"><path d="M4 20h4L19 9l-4-4L4 16z"/><path d="M13 7l4 4"/></svg>',
 '<svg viewBox="0 0 24 24"><circle cx="9" cy="8" r="3"/><circle cx="17" cy="10" r="2.5"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6M14.5 20c.3-2.5 2-4 4-4s3 1 3.5 2.5"/></svg>',
]

def bt(code, k):
    return BLOGTXT.get(code, BLOGTXT["en"])[k]

MOIS = {"fr": ["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"],
        "en": ["January","February","March","April","May","June","July","August","September","October","November","December"]}
def fdate(d, code):
    y, m, j = d.split("-")
    if code == "fr": return f"{int(j)} {MOIS['fr'][int(m)-1]} {y}"
    if code == "en": return f"{MOIS['en'][int(m)-1]} {int(j)}, {y}"
    return d

def arts(code):
    return sorted([a for a in ARTICLES if a["lang"] == code], key=lambda a: a["date"], reverse=True)

def blog_link(code, base):
    return f'<a class="nav-g" href="{base}blog/">{E(bt(code, "blog"))}</a>' if arts(code) else ""

def cards(code, base, items):
    return "".join(f'<a class="post" href="{base}blog/{a["slug"]}/"><h3>{E(a["h1"])}</h3><p>{E(a["desc"])}</p><span>{E(bt(code, "read"))} →</span></a>' for a in items)

def posts_section(code, base):
    A = arts(code)
    if not A:
        return ""
    return f'<section class="alt"><div class="wrap"><h2>{E(bt(code, "guides_h"))}</h2><div class="posts">{cards(code, base, A[:3])}</div><p class="center" style="margin-top:22px"><a href="{base}blog/">{E(bt(code, "all"))} →</a></p></div></section>'


SLUGS = ["review", "vs-clickfunnels", "vs-kajabi"]

def guide_links(code, base):
    T = P[code]
    return f'<a class="nav-g" href="{base}review/">{E(T["nav_review"])}</a><a class="nav-g" href="{base}vs-clickfunnels/">{E(T["nav_vs"])}</a>'

def pt(code, s):
    return s.replace("{P0}", money(0, code)).replace("{P17}", money(17, code)).replace("{P97}", money(97, code))

def compare_section(code, base):
    T = P[code]
    items = [("review/", T["read_review"], T["rev_desc"]),
             ("vs-clickfunnels/", "Systeme.io vs ClickFunnels", T["vs_desc"].format(x="ClickFunnels")),
             ("vs-kajabi/", "Systeme.io vs Kajabi", T["vs_desc"].format(x="Kajabi"))]
    cards_ = "".join(f'<a class="post" href="{base}{h}"><h3>{E(t)}</h3><p>{E(d)}</p><span>{E(T["nav_review"] if h == "review/" else T["nav_vs"])} →</span></a>' for h, t, d in items)
    return f'<section><div class="wrap"><h2>{E(T["compare_h"])}</h2><div class="cmp">{cards_}</div></div></section>'

def alt_links(slug):
    s = "\n".join(f'<link rel="alternate" hreflang="{M["hl"]}" href="{url(M)}{slug}/">' for M in LANGS.values())
    return s + f'\n<link rel="alternate" hreflang="x-default" href="{BASE}{slug}/">'

def review_main(code, L):
    T = P[code]
    li = lambda xs: "".join(f"<li>{E(pt(code, x))}</li>" for x in xs)
    n = lambda v: num(v, code)
    cta = f'<div class="cta-box"><p>{E(L["nocard"])}</p><a class="btn" {{AFF}}>{E(T["try_free"])}</a></div>'
    rows = [(L["free"], 0, n(2000), "3", "1"), ("Startup", 17, n(5000), "10", "5"), ("Webinar", 47, n(10000), "50", "20"), ("Unlimited", 97, L["unl"], L["unl"], L["unl"])]
    tbl = "".join(f"<tr><td><b>{E(a)}</b></td><td>{money(p, code)}{E(L['month'])}</td><td>{E(c)}</td><td>{E(f)}</td><td>{E(k)}</td></tr>" for a, p, c, f, k in rows)
    return f"""<article class="art"><div class="crumbs"><a href="../">Systeme.io Guide</a> › {E(T['nav_review'])}</div>
<h1>{E(T['rev_h1'])}</h1><p>{E(T['rev_intro'])}</p>{cta}
<div class="two"><div><h2>{E(T['pros_h'])}</h2><ul class="pc good">{li(T['pros'])}</ul></div><div><h2>{E(T['cons_h'])}</h2><ul class="pc bad">{li(T['cons'])}</ul></div></div>
<h2>{E(L['price_h'])}</h2><div class="tbl"><table><thead><tr><th></th><th>{E(L['price_h'])}</th><th>{E(L['contacts'])}</th><th>{E(L['funnels'])}</th><th>{E(L['courses'])}</th></tr></thead><tbody>{tbl}</tbody></table></div>
<p style="font-size:15px;color:var(--mute)">{E(L['price_note'])} {E(L['all_inc'])}</p>
<h2>{E(T['who_h'])}</h2><ul class="pc good">{li(T['who'])}</ul>
<h2>{E(T['verdict_h'])}</h2><div class="tip">{E(pt(code, T['rev_verdict']))}</div>
{cta}
<h2>{E(T['compare_h'])}</h2><div class="posts" style="grid-template-columns:1fr 1fr"><a class="post" href="../vs-clickfunnels/"><h3>Systeme.io vs ClickFunnels</h3><span>{E(T['nav_vs'])} →</span></a><a class="post" href="../vs-kajabi/"><h3>Systeme.io vs Kajabi</h3><span>{E(T['nav_vs'])} →</span></a></div>
<p style="font-size:14px;color:var(--mute)">{E(T['checked'])}</p></article>"""

COMP = {
 "vs-clickfunnels": dict(x="ClickFunnels", price=97, yearly=81, trial="q", contacts=10000, emails=50000, courses="3", fees="fees_cf", verdict="cf_verdict"),
 "vs-kajabi": dict(x="Kajabi", price=179, yearly=143, trial=14, contacts=2500, emails=None, courses="5", fees="fees_kj", verdict="kj_verdict"),
}

def vs_main(code, L, slug):
    T = P[code]; C = COMP[slug]; x = C["x"]
    n = lambda v: num(v, code)
    trial = T["trial_q"] if C["trial"] == "q" else T["trial_n"].format(n=C["trial"])
    emails = f"{n(C['emails'])} {T['per_month']}" if C["emails"] else "-"
    courses = C["courses"] if slug == "vs-clickfunnels" else f"{C['courses']} {T['products']}"
    rows = [
        (T["r_price"], f"{money(0, code)} / {money(17, code)}{T['mo']}", f"${C['price']}{T['mo']} ({T['yearly'].format(p='$' + str(C['yearly']))})", 1),
        (T["r_free"], T["yes"], T["no"], 1),
        (T["r_trial"], T["trial_none"], trial, 0),
        (T["r_contacts"], pt(code, T["sio_contacts"]), n(C["contacts"]), 0),
        (T["r_emails"], T["unl"], emails, 1),
        (T["r_courses"], pt(code, T["sio_courses"]), courses, 0),
        (T["r_fees"], T["fees_sio"], T[C["fees"]], 0),
    ]
    body = "".join(f'<tr><th>{E(a)}</th><td class="{"win" if w else ""}">{E(b)}</td><td>{E(c)}</td></tr>' for a, b, c, w in rows)
    other = "vs-kajabi" if slug == "vs-clickfunnels" else "vs-clickfunnels"
    cta = f'<div class="cta-box"><p>{E(L["nocard"])}</p><a class="btn" {{AFF}}>{E(T["try_free"])}</a></div>'
    return f"""<article class="art"><div class="crumbs"><a href="../">Systeme.io Guide</a> › {E(T['nav_vs'])}</div>
<h1>{E(T['vs_h1'].format(x=x))}</h1><p>{E(T['vs_intro'].format(x=x))}</p>
<div class="tbl"><table><thead><tr><th>{E(T['c_feat'])}</th><th>Systeme.io</th><th>{E(x)}</th></tr></thead><tbody>{body}</tbody></table></div>
<p style="font-size:14px;color:var(--mute)">{E(T['checked'])}</p>
<h2>{E(T['verdict_vs'])}</h2><div class="tip">{E(pt(code, T[C['verdict']]))}</div>
{cta}
<h2>{E(T['compare_h'])}</h2><div class="posts" style="grid-template-columns:1fr 1fr"><a class="post" href="../review/"><h3>{E(T['read_review'])}</h3><span>{E(T['nav_review'])} →</span></a><a class="post" href="../{other}/"><h3>Systeme.io vs {COMP[other]['x']}</h3><span>{E(T['nav_vs'])} →</span></a></div></article>"""

def long_main(code, L, slug):
    T = P[code]; X = LONG[(code, slug)]
    h1 = T["rev_h1"] if slug == "review" else T["vs_h1"].format(x=COMP[slug]["x"])
    crumb = T["nav_review"] if slug == "review" else T["nav_vs"]
    faq = "".join(f"<details><summary>{E(q)}</summary><p>{E(r)}</p></details>" for q, r in X["faq"])
    rel = [("review/", T["read_review"]), ("vs-clickfunnels/", "Systeme.io vs ClickFunnels"), ("vs-kajabi/", "Systeme.io vs Kajabi")]
    rel_html = "".join(f'<a class="post" href="../{h}"><h3>{E(t)}</h3><span>{E(T["nav_review"] if h == "review/" else T["nav_vs"])} →</span></a>' for h, t in rel if h != slug + "/")
    main = (f'<article class="art"><div class="crumbs"><a href="../">Systeme.io Guide</a> › {E(crumb)}</div><h1>{E(h1)}</h1>'
            f'<div class="meta">{E(T["checked"])}</div>{X["body"]}'
            f'<h2>{E(L["faq_h"])}</h2><div class="faq" style="margin-top:12px">{faq}</div>'
            f'<h2>{E(T["compare_h"])}</h2><div class="posts" style="grid-template-columns:1fr 1fr">{rel_html}</div></article>')
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": L["hl"],
          "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": r}} for q, r in X["faq"]]}
    return main, ld

def write_guides():
    urls = []
    for code, L in LANGS.items():
        T = P[code]
        base = os.path.join(OUT, L["path"]) if L["path"] else OUT
        depth = "../../" if L["path"] else "../"
        pages = {"review": (T["rev_title"], T["rev_desc"], review_main(code, L)),
                 "vs-clickfunnels": (T["vs_title"].format(x="ClickFunnels"), T["vs_desc"].format(x="ClickFunnels"), vs_main(code, L, "vs-clickfunnels")),
                 "vs-kajabi": (T["vs_title"].format(x="Kajabi"), T["vs_desc"].format(x="Kajabi"), vs_main(code, L, "vs-kajabi"))}
        for slug, (title, desc, main) in pages.items():
            ld = None
            if (code, slug) in LONG:
                main, ld = long_main(code, L, slug)
            d = os.path.join(base, slug)
            os.makedirs(d, exist_ok=True)
            open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(shell(code, L, title, desc, url(L) + slug + "/", main, ld, depth, alt_links(slug)))
    for slug in SLUGS:
        for L in LANGS.values():
            alt = "".join(f'<xhtml:link rel="alternate" hreflang="{M["hl"]}" href="{url(M)}{slug}/"/>' for M in LANGS.values())
            urls.append(f"<url><loc>{url(L)}{slug}/</loc>{alt}</url>")
    return urls


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
        f'<div class="plan{" hl" if hl else ""}"><h3>{E(nm)}</h3><div class="price">{money(p, code)}<small>{E(L["month"])}</small></div>'
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
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%2300A0FF'/%3E%3Cpath d='M18 40l10-10 8 8 12-14' stroke='white' stroke-width='6' fill='none' stroke-linecap='round'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<div class="suggest" id="sg"></div>
<header><div class="wrap">
<a class="logo" href="{rel(L)}"><i><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"><path d="M4 16l5-5 4 4 7-8"/></svg></i><strong>Systeme<span>.io</span> Guide</strong></a>
<div class="hdr-r">{guide_links(code, rel(L))}{blog_link(code, rel(L))}<details class="lang"><summary>🌐 {E(L['name'])}</summary><div>{menu}</div></details><a class="btn hdr" {link}>{E(L['cta'])}</a></div>
</div></header>
<main>
<div class="hero"><div class="wrap">
<div>
<div class="pill"><b>{E(L['free'])}</b> {E(L['nocard'])}</div>
<h1>{E(L['h1'])}</h1>
<p class="sub">{E(L['sub'])}</p>
<a class="btn" {link}>{E(L['cta'])}</a>
<p class="note">{E(L['all_inc'])}</p>
</div>
<div class="mock" aria-hidden="true"><div class="bar"><i></i><i></i><i></i></div><div class="in">
<div class="mfun"><div></div><div></div><div></div><div></div></div>
<div class="mrow"><span>{E(L['contacts'])}</span><b>{n(2000)}</b></div>
<div class="mrow"><span>{E(L['funnels'])}</span><b>3</b></div>
<div class="mchart"></div>
</div></div>
</div></div>
<section><div class="wrap"><h2>{E(L['what_h'])}</h2><p class="lead">{E(L['what_p'])}</p></div></section>
<section class="alt"><div class="wrap"><h2>{E(L['feat_h'])}</h2><div class="grid">{feats}</div></div></section>
<section id="pricing"><div class="wrap"><h2>{E(L['price_h'])}</h2><div class="plans">{plan_html}</div>
<p class="small-note">{E(L['price_note'])} {E(L['all_inc'])}</p></div></section>
<section class="alt"><div class="wrap"><h2>{E(L['steps_h'])}</h2><ol class="steps">{steps}</ol>
<p class="center" style="margin-top:20px"><a class="btn" {link}>{E(L['cta'])}</a></p></div></section>
{compare_section(code, rel(L))}
{posts_section(code, rel(L))}
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

FAV = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%2300A0FF'/%3E%3Cpath d='M18 40l10-10 8 8 12-14' stroke='white' stroke-width='6' fill='none' stroke-linecap='round'/%3E%3C/svg%3E"

def shell(code, L, title, desc, canon, main, ld=None, depth="", alts=""):
    a = aff(L)
    link = f'href="{E(a)}" rel="sponsored nofollow noopener" target="_blank"'
    home = depth + (L["path"] + "/" if L["path"] else "")
    menu = "".join(f'<a href="{depth}{(M["path"] + "/") if M["path"] else ""}" hreflang="{M["hl"]}" lang="{M["hl"]}">{E(M["name"])}</a>' for M in LANGS.values())
    ldj = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>' if ld else ""
    return f"""<!doctype html>
<html lang="{L['hl']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{canon}">
{alts}
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:type" content="article">
<meta property="og:url" content="{canon}">
<link rel="icon" href="{FAV}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
{ldj}
</head>
<body>
<header><div class="wrap">
<a class="logo" href="{home}"><i><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"><path d="M4 16l5-5 4 4 7-8"/></svg></i><strong>Systeme<span>.io</span> Guide</strong></a>
<div class="hdr-r">{guide_links(code, home)}{blog_link(code, home)}<details class="lang"><summary>🌐 {E(L['name'])}</summary><div>{menu}</div></details><a class="btn hdr" {link}>{E(L['cta'])}</a></div>
</div></header>
<main>{main.replace("{AFF}", link).replace("{CTA}", E(L['cta']))}</main>
<footer><div class="wrap"><div class="glinks"><a href="{home}">Systeme.io Guide</a><a href="{home}review/">{E(P[code]["nav_review"])}</a><a href="{home}vs-clickfunnels/">Systeme.io vs ClickFunnels</a><a href="{home}vs-kajabi/">Systeme.io vs Kajabi</a></div><p>{E(L['disc'])}</p><p>© <span id="y"></span> Systeme.io Guide</p></div></footer>
<script>document.getElementById('y').textContent=new Date().getFullYear();</script>
</body>
</html>
"""

def article_url(L, a):
    return url(L) + "blog/" + a["slug"] + "/"

def write_articles():
    out_urls = []
    for code, L in LANGS.items():
        A = arts(code)
        if not A:
            continue
        base = os.path.join(OUT, L["path"]) if L["path"] else OUT
        depth_art = "../../../" if L["path"] else "../../"
        depth_blog = "../../" if L["path"] else "../"
        for a in A:
            ld = {"@context": "https://schema.org", "@type": "Article", "headline": a["h1"], "inLanguage": L["hl"],
                  "datePublished": a["date"], "dateModified": a.get("updated", a["date"]),
                  "author": {"@type": "Organization", "name": "Systeme.io Guide"}}
            cta = f'<div class="cta-box"><p>{E(bt(code, "cta_p"))}</p><a class="btn" {{AFF}}>{{CTA}}</a></div>'
            others = [x for x in A if x["slug"] != a["slug"]][:3]
            more = f'<h2>{E(bt(code, "more"))}</h2><div class="posts" style="grid-template-columns:1fr">{cards(code, depth_art + (L["path"] + "/" if L["path"] else ""), others)}</div>' if others else ""
            main = (f'<article class="art"><div class="crumbs"><a href="{depth_art}{(L["path"] + "/") if L["path"] else ""}">Systeme.io Guide</a> › <a href="../">{E(bt(code, "blog"))}</a></div>'
                    f'<h1>{E(a["h1"])}</h1><div class="meta">{E(bt(code, "upd"))} {fdate(a.get("updated", a["date"]), code)}</div>'
                    f'{a["body"].replace("[CTA]", cta)}{cta}{more}</article>')
            d = os.path.join(base, "blog", a["slug"])
            os.makedirs(d, exist_ok=True)
            open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(shell(code, L, a["title"], a["desc"], article_url(L, a), main, ld, depth_art))
            out_urls.append(article_url(L, a))
        main = (f'<section><div class="wrap"><h2>{E(bt(code, "guides_h"))}</h2><p class="lead">{E(bt(code, "blog_p"))}</p>'
                f'<div class="posts">{cards(code, depth_blog + (L["path"] + "/" if L["path"] else ""), A)}</div></div></section>')
        d = os.path.join(base, "blog")
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(shell(code, L, bt(code, "guides_h") + " | Systeme.io Guide", bt(code, "blog_p"), url(L) + "blog/", main, None, depth_blog))
        out_urls.append(url(L) + "blog/")
    return out_urls


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
items += [f"<url><loc>{u}</loc></url>" for u in write_articles()]
items += write_guides()
with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">'
            + "".join(items) + "</urlset>\n")
with open(os.path.join(OUT, "robots.txt"), "w") as f:
    f.write(f"User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n")
open(os.path.join(OUT, ".nojekyll"), "w").close()
print("ok", len(LANGS), "langues")
