# -*- coding: utf-8 -*-
"""Vá chung cho mọi trang: logo chữ Acooki, menu sản phẩm mới, favicon, shop.css. Chạy 1 lần trên bản gốc."""
import sys, os, re, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import CATS
ROOT = sys.argv[1]

DROP = '<svg class="wm-d" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.5c-3.6 4.6-6.5 8.2-6.5 12a6.5 6.5 0 0 0 13 0c0-3.8-2.9-7.400-6.500-12z"/></svg>'
WM = f'<span class="wm" aria-hidden="true">{DROP}<span class="wm-t">Acook<i>i</i></span></span><span class="sr">Acooki</span>'
WM_L = f'<span class="wm light" aria-hidden="true">{DROP}<span class="wm-t">Acook<i>i</i></span></span><span class="sr">Acooki</span>'
sub = '<ul class="sub">\n                ' + "".join(f'<li><a href="san-pham.html#{c[0]}">{c[1].replace("&", "&amp;")}</a></li>' for c in CATS) + "\n              </ul>"
foot = "<h4>Sản phẩm</h4>\n            <ul>\n              " + "".join(f'<li><a href="san-pham.html#{c[0]}">{c[1].replace("&", "&amp;")}</a></li>' for c in CATS) + "\n            </ul>"
HEART = '<symbol id="i-heart" viewBox="0 0 24 24"><path d="M12 20.500s-8-4.800-8-10.800A4.500 4.500 0 0 1 12 7a4.500 4.500 0 0 1 8 2.700c0 6-8 10.800-8 10.800z" /></symbol>'

for f in glob.glob(os.path.join(ROOT, "*.html")):
    s = open(f, encoding="utf-8").read()
    s = re.sub(r'(<a class="brand"[^>]*>)\s*<img[^>]*>\s*</a>', lambda m: m.group(1) + WM + "</a>", s, flags=re.S)
    s = re.sub(r'<img\s+class="logo"[^>]*>', '<a class="foot-brand" href="index.html" aria-label="Acooki - Trang chủ">' + WM_L + "</a>", s, flags=re.S)
    s = re.sub(r'<ul class="sub">.*?</ul>', lambda m: sub, s, flags=re.S)
    s = re.sub(r"<h4>Sản phẩm</h4>\s*<ul>.*?</ul>", lambda m: foot, s, flags=re.S)
    s = re.sub(r'<link rel="icon" href="[^"]*" />', '<link rel="icon" type="image/svg+xml" href="assets/favicon.svg" />', s)
    s = s.replace('<link rel="stylesheet" href="assets/vip.css" />', '<link rel="stylesheet" href="assets/vip.css" />\n    <link rel="stylesheet" href="assets/shop.css" />', 1)
    if "i-heart" not in s: s = s.replace("<defs>", "<defs>\n        " + HEART, 1)
    open(f, "w", encoding="utf-8").write(s)
    print(os.path.basename(f), "logo:", s.count('class="wm'), "css:", "shop.css" in s)
