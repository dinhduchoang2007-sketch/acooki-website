# -*- coding: utf-8 -*-
"""Dựng trang sản phẩm / chi tiết sản phẩm / trang chủ cho website Acooki.
Chạy:  python3 build.py <thư mục website>   (thư mục chứa index.html)"""
import sys, os, re, json, html as H
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import *

ROOT = sys.argv[1]
SIZES = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "sizes.json")))
def rd(f): return open(os.path.join(ROOT, f), encoding="utf-8").read()
def wr(f, s): open(os.path.join(ROOT, f), "w", encoding="utf-8").write(s)
esc = H.escape

CAT = {c[0]: c for c in CATS}
HOME = {  # 4 sản phẩm mỗi mục trang chủ
    "best": ["vi-ngu-900ml", "hat-nem-900g", "vi-ngu-750ml", "sa-te-cay-100g"],
    "feat": ["vi-ngu-4-8l", "hat-nem-chay-200g", "sa-te-tom-100g", "nuoc-giat-can-comfor"],
    "fav": ["vi-ngu-500ml", "hat-nem-chay-900g", "tuong-xay-850g", "nuoc-giat-can-downy"],
}
TAGNAME = {"best": "Bán chạy", "feat": "Nổi bật", "fav": "Yêu thích"}
TAGOF = {s: t for t, l in HOME.items() for s in l}

prods = []
for (slug, cat, name, qty, unit, p1, pc, img, grp, short, _t, promo) in P:
    w, h = SIZES[img]
    prods.append(dict(s=slug, c=cat, n=name, q=qty, u=unit, p=p1, pc=pc, img=img, fit=w >= h, grp=grp,
                      short=short, promo=promo, t=TAGOF.get(slug, "")))
BY = {p["s"]: p for p in prods}
def money(n): return f"{n:,}".replace(",", ".") + "đ"
def imgp(i): return f"assets/img/sp/{i}.webp"
def brand(p): return "TB Foods" if p["c"] in ("nuoc-giat", "rua-chen") else "Acook"
def cat_images(c):
    prefix = {"nuoc-mam": "vi-ngu", "hat-nem": "hat-nem", "hat-nem-chay": "hat-nem-chay", "bao-lon": "bao-lon", "nuoc-tuong": "nuoc-tuong",
              "sa-te": "sa-te", "tuong": "tuong-ot", "nuoc-giat": "nuoc-giat", "rua-chen": "rua-chen"}[c]
    return sorted(k for k in SIZES if re.fullmatch(prefix + r"-\d\d", k))
def gallery(p):
    own = [p["img"]] + [i for i in cat_images(p["c"]) if i != p["img"]]
    if p["c"] == "hat-nem": own = [p["img"]] + [i for i in cat_images("hat-nem") if i != p["img"]]
    return own[:8]

# ---------- thẻ sản phẩm ----------
def card(p, tag=None):
    t = tag or p["t"]
    href = f"sp-{p['s']}.html"
    case = f'<span class="pc-case">Thùng {p["q"]} {p["u"]}: <b>{money(p["pc"])}</b></span>' if p["q"] > 1 else f'<span class="pc-case">Quy cách: 1 {p["u"]}</span>'
    tg = f'<span class="pc-tag t-{t}">{TAGNAME[t]}</span>' if t else ""
    return (f'<article class="pc" data-s="{p["s"]}" data-k="{esc(p["n"].lower())}">'
            f'<a class="pc-pic{" fit" if p["fit"] else ""}" href="{href}" tabindex="-1" aria-hidden="true"><img src="{imgp(p["img"])}" alt="" loading="lazy" width="{SIZES[p["img"]][0]}" height="{SIZES[p["img"]][1]}" />{tg}</a>'
            f'<button type="button" class="pc-fav" data-s="{p["s"]}" aria-pressed="false" aria-label="Lưu {esc(p["n"])} vào yêu thích"><svg class="ico" aria-hidden="true"><use href="#i-heart" /></svg></button>'
            f'<div class="pc-b"><span class="pc-cat">{esc(CAT[p["c"]][2])}</span>'
            f'<h3><a href="{href}">{esc(p["n"])}</a></h3>'
            f'<div class="pc-price"><b>{money(p["p"])}</b><small>/{p["u"]}</small></div>{case}'
            f'<a class="pc-btn" href="{href}">Xem chi tiết<svg class="ico" aria-hidden="true"><use href="#i-out" /></svg></a></div></article>')

# ---------- cắt khuôn trang từ san-pham.html cũ (đã vá logo/menu) ----------
base = rd("san-pham.html")
M0 = base.index('<main id="main">'); M1 = base.index("</main>") + len("</main>")
HEAD, TAIL = base[:M0], base[M1:]
CTA = re.search(r'<section class="cta">.*?</section>', base, re.S).group(0)

def set_head(head, title, desc, extra=""):
    head = re.sub(r"<title>.*?</title>", f"<title>{esc(title)}</title>", head, flags=re.S)
    head = re.sub(r'(<meta\s+name="description"\s+content=")[^"]*(")', lambda m: m.group(1) + esc(desc, True) + m.group(2), head, flags=re.S)
    head = re.sub(r'(<meta property="og:title" content=")[^"]*(")', lambda m: m.group(1) + esc(title, True) + m.group(2), head)
    head = re.sub(r'(<meta\s+property="og:description"\s+content=")[^"]*(")', lambda m: m.group(1) + esc(desc, True) + m.group(2), head, flags=re.S)
    return head.replace("</head>", extra + "</head>")

def tail_scripts(tail):
    return tail.replace('<script src="assets/main.js"></script>', '<script src="assets/products.js"></script>\n    <script src="assets/main.js"></script>') \
               .replace('<script src="assets/pro.js" defer></script>', '<script src="assets/pro.js" defer></script>\n    <script src="assets/shop.js" defer></script>')
TAIL2 = tail_scripts(TAIL)

# ---------- products.js ----------
js = [dict(s=p["s"], c=p["c"], cn=CAT[p["c"]][2], n=p["n"], q=p["q"], u=p["u"], p=p["p"], pc=p["pc"], img=imgp(p["img"]), fit=p["fit"], t=p["t"]) for p in prods]
wr("assets/products.js", "/* Tạo tự động bởi build.py - sửa giá/ảnh trong data.py */\nwindow.PRODUCTS=" + json.dumps(js, ensure_ascii=False) + ";\nwindow.CATS=" +
   json.dumps([dict(id=c[0], n=c[1]) for c in CATS], ensure_ascii=False) + ";\n")

# ---------- trang danh sách ----------
chips = '<a class="chip on" href="san-pham.html" data-c="all">Tất cả <i>32</i></a>' + "".join(
    f'<a class="chip" href="san-pham.html#{c[0]}" data-c="{c[0]}">{esc(c[1])} <i>{sum(1 for p in prods if p["c"] == c[0])}</i></a>' for c in CATS)
secs = []
for c in CATS:
    ps = [p for p in prods if p["c"] == c[0]]
    secs.append(f'<section class="cat-sec" id="{c[0]}" data-cat="{c[0]}"><div class="cat-head"><div><span class="eyebrow">{esc(c[2])}</span><h2>{esc(c[1])}</h2><p>{esc(c[4])}</p></div>'
                f'<span class="cat-n">{len(ps)} sản phẩm</span></div><div class="pgrid">' + "".join(card(p) for p in ps) + "</div></section>")
list_main = f'''<main id="main">
      <section class="ph">
        <div class="wrap">
          <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Trang chủ</a><span>/</span><span>Sản phẩm</span></nav>
          <h1>Sản phẩm</h1>
          <p>Nước mắm, hạt nêm, nước tương, sa tế, tương ớt và hóa phẩm gia dụng: 32 sản phẩm đủ quy cách cho gia đình, quán ăn và bếp lớn.</p>
        </div>
      </section>
      <section class="sec shop">
        <div class="wrap">
          <div class="shop-bar">
            <nav class="chips" aria-label="Nhóm sản phẩm">{chips}</nav>
            <label class="shop-search"><svg class="ico" aria-hidden="true"><use href="#i-search" /></svg><input type="search" id="pq" placeholder="Tìm sản phẩm..." aria-label="Tìm sản phẩm" autocomplete="off" /></label>
          </div>
          <div class="rv-sec compact" data-rv="list" hidden></div>
          {"".join(secs)}
          <p class="no-res" hidden>Không tìm thấy sản phẩm phù hợp. Hãy thử từ khóa khác hoặc gọi hotline <a class="link" href="tel:0966220012">0966220012</a>.</p>
          <aside class="price-note"><b>Lưu ý về giá</b><ul>
            <li>Giá hiển thị là giá nhà phân phối <b>chưa chiết khấu</b>, đã gồm VAT.</li>
            <li>Đơn hàng dưới 30 triệu đồng, công ty hỗ trợ giao tới chành xe.</li>
            <li>Muốn nhận chính sách chiết khấu cho đại lý / nhà phân phối? <a class="link" href="lien-he.html">Liên hệ Acooki</a>.</li>
          </ul></aside>
        </div>
      </section>
      {CTA}
    </main>'''
wr("san-pham.html", set_head(HEAD, "Sản phẩm | Acooki - Nước mắm Việt",
   "32 sản phẩm Acooki: nước chấm Vị Ngư, hạt nêm Acook, nước tương Soya, sa tế, tương ớt, nước giặt Amatic, nước rửa chén Chanh. Xem giá và quy cách từng sản phẩm.") + list_main + TAIL2)

# ---------- trang chi tiết ----------
def related(p):
    same = [q for q in prods if q["c"] == p["c"] and q["s"] != p["s"]]
    rest = [q for q in prods if q["c"] != p["c"]]
    return (same + rest)[:4]

for p in prods:
    c = CAT[p["c"]]; info = CATINFO[p["c"]]
    desc = EXTRA_DESC.get(p["s"]) or info["desc"]
    ticks = info["ticks"]
    if p["c"] == "sa-te":
        ticks = (["Cay đậm, chuẩn vị quán"] if "cay" in p["s"] else ["Đặc biệt chua cay, dậy mùi, đậm vị"]) + ["Làm từ ớt, tỏi và nguyên liệu tự nhiên", "Dùng cho lẩu, mì, bún, xào, ướp"]
    if p["c"] == "tuong":
        ticks = (["Tương ớt: cay - sánh - ngon"] if "ot" in p["s"] else ["Tương xay: sánh mịn, dễ chấm"]) + ["Hợp món chay lẫn món mặn", "Đậm vị quen, ngon bữa cơm nhà"]
    gal = gallery(p)
    gm = f'<button type="button" class="gal-main fit" aria-label="Phóng to ảnh {esc(p["n"])}"><img src="{imgp(gal[0])}" alt="{esc(p["n"])}" width="{SIZES[gal[0]][0]}" height="{SIZES[gal[0]][1]}" /><span class="zoom" aria-hidden="true">Phóng to</span></button>'
    gts = "".join(f'<button type="button" class="gt{" on" if i == 0 else ""}" aria-label="Xem ảnh {i+1}"><img src="{imgp(g)}" alt="" loading="lazy" width="{SIZES[g][0]}" height="{SIZES[g][1]}" /></button>' for i, g in enumerate(gal))
    case_row = f'<div class="pd-row"><span>Giá nguyên thùng ({p["q"]} {p["u"]})</span><b>{money(p["pc"])}</b></div>' if p["q"] > 1 else ""
    cert = CERT_OVERRIDE.get(p["s"]) or info["cert"]
    cert_li = f'<li><svg class="ico" aria-hidden="true"><use href="#i-doc" /></svg><a href="chung-nhan.html#{cert}">Xem hồ sơ công bố sản phẩm</a></li>' if cert else ""
    promo = f'<p class="pd-promo">{esc(p["promo"])}</p>' if p["promo"] else ""
    nt = f'<p class="pd-ill">Hình ảnh mang tính minh họa theo nhóm sản phẩm.</p>' if p["s"] in ("hat-nem-400g", "tuong-ot-4-5kg", "tuong-xay-4-5kg", "nuoc-giat-can-comfor", "nuoc-giat-can-downy", "nuoc-giat-tui-comfor", "nuoc-giat-tui-downy") else ""
    jsonld = {"@context": "https://schema.org", "@type": "Product", "name": p["n"], "brand": {"@type": "Brand", "name": brand(p)},
              "category": c[1], "description": p["short"], "image": [imgp(gal[0])],
              "offers": {"@type": "Offer", "priceCurrency": "VND", "price": p["p"], "availability": "https://schema.org/InStock"}}
    body = f'''<main id="main" data-slug="{p["s"]}">
      <section class="ph ph-s">
        <div class="wrap">
          <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Trang chủ</a><span>/</span><a href="san-pham.html">Sản phẩm</a><span>/</span><a href="san-pham.html#{c[0]}">{esc(c[1])}</a><span>/</span><span>{esc(p["n"])}</span></nav>
        </div>
      </section>
      <section class="sec pd">
        <div class="wrap pd-grid">
          <div class="gal"><div class="pd-gal">{gm}<div class="gts">{gts}</div></div>{nt}</div>
          <div class="pd-info">
            <span class="eyebrow">{esc(c[2])}</span>
            <h1>{esc(p["n"])}</h1>
            <p class="pd-short">{esc(p["short"])}</p>
            <div class="pd-price">
              <span class="pd-lab">Giá chưa chiết khấu · đã gồm VAT</span>
              <div class="pd-big"><b>{money(p["p"])}</b><small>/ {p["u"]}</small></div>
              {case_row}
            </div>
            {promo}
            <dl class="pd-spec">
              <div><dt>Quy cách</dt><dd>{p["q"]} {p["u"]} / thùng</dd></div>
              <div><dt>Đơn vị tính</dt><dd>{p["u"].capitalize()}</dd></div>
              <div><dt>Thương hiệu</dt><dd>{brand(p)}</dd></div>
              <div><dt>Nhóm</dt><dd><a class="link" href="san-pham.html#{c[0]}">{esc(c[1])}</a></dd></div>
            </dl>
            <div class="actions">
              <a class="btn" href="lien-he.html?sp={p["s"]}">Đặt mua / nhận báo giá</a>
              <a class="btn btn-line" href="tel:0966220012"><svg class="ico" aria-hidden="true"><use href="#i-phone" /></svg>0966220012</a>
              <button type="button" class="btn btn-line pd-fav pc-fav" data-s="{p["s"]}" aria-pressed="false"><svg class="ico" aria-hidden="true"><use href="#i-heart" /></svg><span>Yêu thích</span></button>
            </div>
            <p class="pd-note">Đơn hàng dưới 30 triệu đồng, công ty hỗ trợ giao tới chành xe.</p>
          </div>
        </div>
      </section>
      <section class="sec sec-salt pd-more">
        <div class="wrap pd-cols">
          <div>
            <h2>Mô tả sản phẩm</h2>
            {"".join(f"<p>{esc(d)}</p>" for d in desc)}
            <ul class="ticks">{"".join(f'<li><svg class="ico" aria-hidden="true"><use href="#i-check" /></svg><span>{esc(t)}</span></li>' for t in ticks)}</ul>
          </div>
          <div class="pd-box">
            <h3>Thông tin sản phẩm</h3>
            <table class="pd-tbl">
              <tr><th>Tên sản phẩm</th><td>{esc(p["n"])}</td></tr>
              <tr><th>Quy cách đóng gói</th><td>{p["q"]} {p["u"]} / thùng</td></tr>
              <tr><th>Giá / {p["u"]}</th><td>{money(p["p"])}</td></tr>
              <tr><th>Giá / thùng</th><td>{money(p["pc"])}</td></tr>
              <tr><th>Hướng dẫn sử dụng</th><td>{esc(info["use"])}</td></tr>
              <tr><th>Bảo quản</th><td>{esc(info["store"])}</td></tr>
            </table>
            <ul class="pd-links">{cert_li}<li><svg class="ico" aria-hidden="true"><use href="#i-phone" /></svg><a href="lien-he.html">Nhận chính sách chiết khấu đại lý / NPP</a></li></ul>
          </div>
        </div>
      </section>
      <section class="sec">
        <div class="wrap">
          <div class="sec-head row"><div><span class="eyebrow">Gợi ý</span><h2>Sản phẩm liên quan</h2></div><a class="btn btn-line" href="san-pham.html">Xem tất cả sản phẩm</a></div>
          <div class="pgrid">{"".join(card(q) for q in related(p))}</div>
          <div class="rv-sec compact" data-rv="list" hidden style="margin-top:48px"></div>
        </div>
      </section>
      {CTA}
    </main>'''
    wr(f"sp-{p['s']}.html", set_head(HEAD, f"{p['n']} | Acooki", f"{p['n']} - {p['short']} Giá {money(p['p'])}/{p['u']}, quy cách {p['q']} {p['u']}/thùng.",
       f'<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>\n') + body + TAIL2)

# ---------- trang chủ ----------
idx = rd("index.html")
def home_sec(kind, cls, eyebrow, title, lede):
    return (f'<section class="sec {cls}" id="{kind}-sec"><div class="wrap"><div class="sec-head row"><div><span class="eyebrow">{eyebrow}</span><h2>{title}</h2><p class="lede">{lede}</p></div>'
            f'<a class="btn btn-line" href="san-pham.html">Xem tất cả sản phẩm</a></div><div class="pgrid" data-home="{kind}">' + "".join(card(BY[s], kind) for s in HOME[kind]) + "</div></div></section>")
best = home_sec("best", "sec-salt", "Bán chạy", "Sản phẩm <em>bán chạy</em>", "Những quy cách được khách hàng chọn nhiều nhất: nước chấm Vị Ngư, hạt nêm Acook và sa tế cay.")
feat = home_sec("feat", "", "Nổi bật", "Sản phẩm <em>nổi bật</em>", "Gợi ý của Acooki cho bếp nhà, bếp quán và gian hàng của bạn.")
tiles_data = [("nuoc-mam", "vi-ngu-01", "Nước chấm Vị Ngư", "Nguyên vị, nguyên chất, đậm đà. 6 quy cách từ chai 500ml đến can 4,8 lít."),
              ("hat-nem", "hat-nem-02", "Hạt nêm Acook", "3 trong 1 thịt thăn, rau củ, xương ống; bổ sung Betacarotene."),
              ("hat-nem-chay", "hat-nem-chay-01", "Hạt nêm chay nấm", "Hương nấm organic, ngọt thanh tự nhiên. Gói 200g và 900g."),
              ("bao-lon", "bao-lon-01", "Hạt nêm bao lớn", "Bao 5kg, 10kg dành cho quán ăn và bếp ăn tập thể."),
              ("nuoc-tuong", "nuoc-tuong-03", "Nước tương Soya", "Từ đậu nành tuyển chọn, đậm đà cho mọi bữa cơm."),
              ("sa-te", "sa-te-01", "Sa tế Acook", "Sa tế cay chuẩn vị quán và sa tế tôm chua cay dậy mùi."),
              ("tuong", "tuong-ot-03", "Tương ớt & tương xay", "Cay sánh ngon, đậm vị quen cho bữa cơm nhà."),
              ("nuoc-giat", "nuoc-giat-03", "Nước giặt Amatic", "6 trong 1, thơm lâu, sạch sâu. Can 3,8L và túi 2L."),
              ("rua-chen", "rua-chen-04", "Nước rửa chén Chanh", "Chanh 3 in 1 sạch dầu mỡ, thơm mát, dịu nhẹ da tay.")]
tiles = "".join(f'<a class="tile" href="san-pham.html#{c}"><span class="bgi" style="--bg:url(../{imgp(i)})"></span><h3>{esc(t)}</h3><p>{esc(d)}</p><span class="link">Xem sản phẩm</span></a>' for c, i, t, d in tiles_data)
cats = f'''<section class="sec sec-salt"><div class="wrap"><div class="sec-head row"><div><span class="eyebrow">Nhóm sản phẩm</span><h2>Chín nhóm sản phẩm cho <em>mọi gian bếp</em></h2>
<p class="lede">Từ nước mắm nguyên chất đến hạt nêm, nước tương, sa tế, tương ớt và hóa phẩm gia dụng, đủ quy cách cho gia đình lẫn bếp lớn.</p></div><a class="btn btn-line" href="san-pham.html">Xem tất cả sản phẩm</a></div><div class="tiles">{tiles}</div></div></section>'''
fav = (f'<section class="sec" id="fav-sec"><div class="wrap"><div class="sec-head row"><div><span class="eyebrow">Yêu thích</span><h2 id="fav-h">Sản phẩm <em>yêu thích</em></h2>'
       f'<p class="lede" id="fav-sub">Được nhiều khách hàng ưa chuộng. Bấm biểu tượng trái tim trên mỗi sản phẩm để lưu những món bạn thích vào đây.</p></div>'
       f'<a class="btn btn-line" href="san-pham.html">Xem tất cả sản phẩm</a></div><div class="pgrid" data-home="fav">' + "".join(card(BY[s], "fav") for s in HOME["fav"]) + "</div></div></section>")

a = idx.index('<section class="sec vsec" id="video">'); b = idx.index('<section class="sec sec-salt">', a)
c0 = b; c1 = idx.index("</section>", c0) + len("</section>")
idx = idx[:a] + best + "\n      " + feat + "\n      " + cats + "\n      " + fav + idx[c1:]
idx = re.sub(r'\s*<script type="application/ld\+json">\s*\{"@context":"https://schema.org","@type":"VideoObject".*?</script>', "", idx, flags=re.S)
idx = idx.replace('href="san-pham.html#nhi-ngu">Xem sản phẩm', 'href="san-pham.html#nuoc-mam">Xem sản phẩm')
idx = idx.replace("<dt>6</dt>", "<dt>32</dt>").replace("nhóm sản phẩm: nước mắm, hạt nêm, nước tương, sa tế, tương ớt, hóa phẩm", "sản phẩm: nước mắm, hạt nêm, nước tương, sa tế, tương, hóa phẩm")
idx = tail_scripts(idx)
wr("index.html", idx)

# ---------- liên hệ: chuyển video sang đây ----------
lh = rd("lien-he.html")
video = '''<section class="sec vsec" id="video">
        <div class="wrap vsec-grid">
          <div>
            <h2>Nhìn tận nơi cách Acooki làm nước mắm</h2>
            <p class="lede" style="margin-top: 14px">Video thực tế và chính sách ưu đãi dành cho quý đối tác đại lý, nhà phân phối của Công ty Asian Việt Nam.</p>
            <div class="vsec-note">
              <a href="https://www.youtube.com/watch?v=qzu580S23bo" target="_blank" rel="noopener">Mở trên YouTube</a>
              <a href="#cf">Gửi yêu cầu nhận chính sách đại lý</a>
            </div>
          </div>
          <div class="yt" data-id="qzu580S23bo" data-title="Video thực tế Acooki">
            <img src="https://i.ytimg.com/vi/qzu580S23bo/maxresdefault.jpg" alt="" loading="lazy" />
            <button type="button" class="yt-play" aria-label="Phát video: Nhìn tận nơi cách Acooki làm nước mắm"><i><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 4.5v15l13-7.5z"/></svg></i></button>
            <span class="yt-cap">Video thực tế Acooki</span>
          </div>
        </div>
      </section>
      '''
vld = '<script type="application/ld+json">{"@context":"https://schema.org","@type":"VideoObject","name":"Video thực tế Acooki","description":"Nhìn tận nơi cách Acooki làm nước mắm.","thumbnailUrl":"https://i.ytimg.com/vi/qzu580S23bo/maxresdefault.jpg","embedUrl":"https://www.youtube.com/embed/qzu580S23bo","uploadDate":"2026-10-12"}</script>\n'
lh = lh.replace("</main>", video + "</main>", 1).replace("</head>", vld + "</head>", 1)
lh = tail_scripts(lh)
wr("lien-he.html", lh)

# ---------- tìm kiếm toàn site (vip.js) ----------
v = rd("assets/vip.js")
v = re.sub(r'\n    \["Sản phẩm", .*?\],(?=\n)', "", v)
ins = "\n".join(f'    ["Sản phẩm", {json.dumps(p["n"], ensure_ascii=False)}, "sp-{p["s"]}.html", {json.dumps(CAT[p["c"]][1] + " " + str(p["q"]) + " " + p["u"], ensure_ascii=False)}],' for p in prods)
v = v.replace('  const IDX = [\n', '  const IDX = [\n' + ins + '\n', 1)
v = v.replace('["Trang", "Giới thiệu Acooki"', '["Trang", "Tất cả sản phẩm", "san-pham.html", "bang gia san pham gia"],\n    ["Trang", "Giới thiệu Acooki"', 1)
wr("assets/vip.js", v)
print("OK", len(prods), "sản phẩm")
