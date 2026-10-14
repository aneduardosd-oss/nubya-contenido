"""NuByA carousel renderer (brandbook v1.4).
Usage: python3 render.py spec.json outdir
Spec: {"slug":..., "handle":"@nutritionbyannie", "cards":[{type, ...}]}
Card types: hook, list, statement, cta. Every card lists its doodles.
v1.1: avatar de Annie opcional (si no existe el archivo, se omite) y clase .tch (palabra tachada a mano).
"""
import json, sys, base64, pathlib, html
from playwright.sync_api import sync_playwright

import os
ROOT = pathlib.Path(__file__).parent
SK = pathlib.Path(os.environ.get('NUBYA_ASSETS', '/mnt/skills/plugins/nubya-brand-identity/assets'))
FS = ROOT / 'node_modules/@fontsource'
GF = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&family=Playfair+Display:wght@600;700&family=Poppins:wght@400;500;600&display=block">'

def b64(p): return base64.b64encode(pathlib.Path(p).read_bytes()).decode()
def font(fam, file, w):
    return f"@font-face{{font-family:'{fam}';font-weight:{w};src:url(data:font/woff2;base64,{b64(FS/file)}) format('woff2');}}"
FONTS = '' if not FS.exists() else ''.join([
    font('Playfair Display', 'playfair-display/files/playfair-display-latin-600-normal.woff2', 600),
    font('Playfair Display', 'playfair-display/files/playfair-display-latin-700-normal.woff2', 700),
    font('Caveat', 'caveat/files/caveat-latin-600-normal.woff2', 600),
    font('Caveat', 'caveat/files/caveat-latin-700-normal.woff2', 700),
    font('Poppins', 'poppins/files/poppins-latin-400-normal.woff2', 400),
    font('Poppins', 'poppins/files/poppins-latin-500-normal.woff2', 500),
    font('Poppins', 'poppins/files/poppins-latin-600-normal.woff2', 600),
])
LOGO = b64(SK / 'logo-nubya.jpg')
ANNIE = b64(SK / 'annie.webp') if (SK / 'annie.webp').exists() else None
U = '<svg class="uline" viewBox="0 0 300 16" preserveAspectRatio="none"><path d="M3 10 C60 4 110 13 160 8 S250 5 297 9" fill="none" stroke="#E2688C" stroke-width="4" stroke-linecap="round"/></svg>'
STRIKE = '<svg class="sline" viewBox="0 0 300 20" preserveAspectRatio="none"><path d="M2 12 C70 6 140 15 200 9 S270 7 298 10" fill="none" stroke="#E2688C" stroke-width="7" stroke-linecap="round"/></svg>'

def doodle(name, x, y, w, rot=0):
    svg = (SK / 'doodles/svg' / f'{name}.svg').read_text()
    svg = svg.replace('<svg', '<svg preserveAspectRatio="xMidYMid meet"', 1)
    return f'<span class="dd" style="left:{x}px;top:{y}px;width:{w}px;transform:rotate({rot}deg)">{svg}</span>'

def stain(color, pos):
    seed = abs(hash(pos + color)) % 97
    fill = {'rosa': '#F1C6D9', 'menta': '#C3E3D8'}[color]
    css = {'tr': 'top:-190px;right:-200px', 'bl': 'bottom:-230px;left:-230px',
           'tl': 'top:-190px;left:-210px', 'br': 'bottom:-230px;right:-220px'}[pos]
    return f'''<svg class="stain" style="{css}" viewBox="0 0 600 600"><defs><filter id="w{seed}{pos}" x="-20%" y="-20%" width="140%" height="140%">
<feTurbulence type="fractalNoise" baseFrequency=".012" numOctaves="3" seed="{seed}"/><feDisplacementMap in="SourceGraphic" scale="150"/><feGaussianBlur stdDeviation="6"/></filter></defs>
<g filter="url(#w{seed}{pos})" fill="{fill}"><circle cx="300" cy="300" r="190" opacity=".85"/><circle cx="360" cy="250" r="120" opacity=".7"/><circle cx="240" cy="360" r="110" opacity=".6"/></g></svg>'''

CSS = FONTS + '''
*{box-sizing:border-box;margin:0;padding:0}
body{width:1080px;height:1350px;background:#FCFBF7}
.card{position:relative;width:1080px;height:1350px;overflow:hidden;background:#FCFBF7;color:#26241F;font-family:Poppins}
.card::after{content:"";position:absolute;inset:0;opacity:.06;pointer-events:none;z-index:5;
 background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='260' height='260'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 .2 0 0 0 0 .2 0 0 0 0 .19 0 0 0 .6 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
.stain{position:absolute;width:620px;height:620px;opacity:.62;z-index:0}
.dd{position:absolute;z-index:3;line-height:0}.dd svg{width:100%;height:auto;display:block;overflow:visible}
.inner{position:absolute;inset:0;padding:130px 100px 150px;display:flex;flex-direction:column;justify-content:center;z-index:2}
h1,h2{font-family:'Playfair Display';font-weight:600;letter-spacing:-.01em;text-wrap:balance}
h1{font-size:98px;line-height:1.07}
.hook h1{font-size:128px;line-height:1.02}
.hook .whisper{font-size:80px;margin-top:56px}
h2{font-size:84px;line-height:1.1}
.whisper{text-wrap:balance;font-family:Caveat;font-weight:700;color:#E2688C;font-size:74px;line-height:1.02;margin-top:44px;transform:rotate(-2deg);transform-origin:left}
.u{position:relative;display:inline-block}.u .uline{position:absolute;left:0;bottom:-14px;width:100%;height:18px;overflow:visible}
.tch{position:relative;display:inline-block;color:#6B675F}.tch .sline{position:absolute;left:-8px;top:46%;width:calc(100% + 16px);height:24px;overflow:visible;transform:rotate(-3deg)}
.body{font-size:44px;line-height:1.42;margin-top:40px;text-wrap:pretty}
.paren{font-size:40px;line-height:1.4;color:#6B675F;margin-top:34px;text-wrap:balance}
.panel{background:#F3F0E9;border-radius:26px;padding:60px 64px 56px;position:relative;margin-top:50px}
.panel.salvia{background:#E9F0E7}
.washi{position:absolute;width:170px;height:54px;top:-24px;left:70px;transform:rotate(-6deg);opacity:.9;
 background:repeating-linear-gradient(45deg,#F1C6D9,#F1C6D9 10px,rgba(255,255,255,.6) 10px,rgba(255,255,255,.6) 20px)}
.washi.mint{background:repeating-linear-gradient(45deg,#7AC9B5,#7AC9B5 10px,rgba(255,255,255,.55) 10px,rgba(255,255,255,.55) 20px)}
.lbl{font:600 26px Poppins;letter-spacing:.2em;text-transform:uppercase;color:#0B5D46;margin-bottom:26px}
ul.mk{list-style:none;display:flex;flex-direction:column;gap:26px}
ul.mk li{font:500 44px Poppins;display:inline-block;align-self:flex-start;padding:2px 20px;transform:rotate(-1deg)}
ul.mk li:nth-child(odd){background:linear-gradient(transparent 16%,#F1C6D9 16%,#F1C6D9 90%,transparent 90%)}
ul.mk li:nth-child(even){background:linear-gradient(transparent 16%,#7AC9B5 16%,#7AC9B5 90%,transparent 90%)}
.mark{padding:0 14px;background:linear-gradient(transparent 20%,#7AC9B5 20%,#7AC9B5 90%,transparent 90%)}
.mark.rosa{background:linear-gradient(transparent 20%,#F1C6D9 20%,#F1C6D9 90%,transparent 90%)}
.foot{position:absolute;bottom:52px;left:64px;right:64px;display:flex;justify-content:space-between;font:400 25px Poppins;color:#6B675F;letter-spacing:.03em;z-index:4}
.swipe{position:absolute;right:100px;bottom:120px;font:600 48px Caveat;color:#E2688C;z-index:4}
.annie{position:absolute;right:-40px;bottom:0;width:560px;z-index:3}
.logo{position:absolute;left:64px;bottom:40px;width:250px;mix-blend-mode:multiply;z-index:4}
.offer .inner{justify-content:center;padding-top:110px}
.intro{font:400 38px/1.35 Poppins;color:#26241F}
.intro b{font-weight:600}
.creds{font:400 29px/1.4 Poppins;color:#6B675F;margin-top:10px}
.offer h2{font-size:78px;margin-top:44px}
.stack{background:#E9F0E7;border-radius:26px;padding:48px 56px 44px;margin-top:40px;position:relative}
.stack .lbl{margin-bottom:22px}
.stack li{list-style:none;display:flex;align-items:center;gap:22px;font:500 40px/1.25 Poppins;margin-top:20px}
.stack li:first-of-type{margin-top:0}
.stack li .ck{width:46px;flex:none;line-height:0}.stack li .ck svg{width:100%;height:auto}
.pricebar{display:flex;align-items:center;gap:30px;margin-top:40px}
.pricebar .big{font:700 104px/1 'Playfair Display'}
.pricebar .big small{font:600 40px Poppins;margin-left:6px}
.pricebar .meta{font:500 30px/1.35 Poppins;color:#0B5D46;border-left:3px solid #E3DFD6;padding-left:28px}
.offer .whisper{font-size:64px;margin-top:30px}
.cta .kicker{font:600 28px Poppins;letter-spacing:.2em;text-transform:uppercase;color:#0B5D46;margin-bottom:28px}
.price{display:inline-block;margin-top:40px;font:600 40px Poppins;color:#26241F;background:#F3F0E9;border-radius:20px;padding:22px 34px;align-self:flex-start;transform:rotate(-1deg)}
.price b{font-family:'Playfair Display';font-size:64px;font-weight:700;margin-left:8px}
'''

def ul(t):
    t = t.replace('[[u]]','<span class="u">').replace('[[/u]]',U+'</span>')
    return t.replace('[[x]]','<span class="tch">').replace('[[/x]]',STRIKE+'</span>')

def card_html(c, i, n, handle):
    c={k:(ul(v) if isinstance(v,str) else v) for k,v in c.items()}
    k = c['type']; parts = [stain(*s) for s in c.get('stains', [])]
    parts += [doodle(*d) for d in c.get('doodles', [])]
    if k == 'hook':
        body = f'<h1>{c["title"]}</h1><p class="whisper">{c["whisper"]}</p>'
    elif k == 'list':
        items = ''.join(f'<li>{x}</li>' for x in c['items'])
        body = (f'<h2>{c["title"]}</h2><p class="body">{c["body"]}</p>'
                f'<div class="panel {c.get("panel","")}"><span class="washi {c.get("washi","")}"></span>'
                f'<p class="lbl">{c["label"]}</p><ul class="mk">{items}</ul></div>' + (f'<p class="paren">{c["paren"]}</p>' if c.get('paren') else ''))
    elif k == 'statement':
        body = f'<h2>{c["title"]}</h2>' + (f'<p class="whisper">{c["whisper"]}</p>' if c.get('whisper') else '') \
             + (f'<div class="price">{c["price"]}</div>' if c.get('price') else '') \
             + (f'<p class="paren">{c["paren"]}</p>' if c.get('paren') else '') \
             + (f'<p class="whisper">{c["closer"]}</p>' if c.get('closer') else '')
    elif k == 'offer':
        ck = (SK / 'doodles/svg/check.svg').read_text()
        items = ''.join(f'<li><span class="ck">{ck}</span>{x}</li>' for x in c['items'])
        body = (f'<p class="intro">{c["intro"]}</p>' + (f'<p class="creds">{c["creds"]}</p>' if c.get('creds') else '') +
                f'<h2>{c["title"]}</h2>'
                f'<div class="stack"><span class="washi {c.get("washi","")}"></span><p class="lbl">{c["label"]}</p><ul>{items}</ul></div>'
                f'<div class="pricebar"><span class="big">{c["price"]}</span><span class="meta">{c["meta"]}</span></div>'
                + (f'<p class="whisper">{c["closer"]}</p>' if c.get('closer') else ''))
    elif k == 'cta':
        body = (f'<p class="kicker">{c["kicker"]}</p><h2>{c["title"]}</h2>'
                f'<p class="whisper">{c["whisper"]}</p>')
    foot = '' if k == 'cta' else f'<div class="foot"><span>{handle}</span><span>{i}/{n}</span></div>'
    extra = ''
    if k == 'cta':
        extra = f'<img class="logo" src="data:image/jpeg;base64,{LOGO}">'
        if ANNIE: extra += f'<img class="annie" src="data:image/webp;base64,{ANNIE}">'
    extra += f'<span class="swipe">{c["swipe"]}</span>' if c.get('swipe') else ''
    style = f' style="{c["inner_style"]}"' if c.get('inner_style') else ''
    return f'<div class="card {k}">{"".join(parts)}<div class="inner"{style}>{body}</div>{extra}{foot}</div>'

def render(spec_path, outdir):
    spec = json.loads(pathlib.Path(spec_path).read_text())
    out = pathlib.Path(outdir); out.mkdir(parents=True, exist_ok=True)
    n = len(spec['cards']); files = []
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1350})
        for i, c in enumerate(spec['cards'], 1):
            doc = f'<!doctype html><html><head><meta charset="utf-8">{"" if FONTS else GF}<style>{CSS}</style></head><body>{card_html(c,i,n,spec["handle"])}</body></html>'
            (out / f'{i:02d}.html').write_text(doc)
            pg.set_content(doc, wait_until='networkidle'); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(300)
            f = out / f'{spec["slug"]}-{i:02d}.jpg'
            pg.screenshot(path=str(f), type='jpeg', quality=92); files.append(str(f))
        b.close()
    print('\n'.join(files))

if __name__ == '__main__':
    render(sys.argv[1], sys.argv[2])
