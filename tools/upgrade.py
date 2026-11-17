# -*- coding: utf-8 -*-
"""Nâng cấp Acooki lên giao diện doanh nghiệp (chạy 1 lần): python3 upgrade.py <thư mục website>"""
import sys, os, re, glob
ROOT = sys.argv[1]

def rd(f): return open(f, encoding="utf-8").read()
def wr(f, s): open(f, "w", encoding="utf-8").write(s)

# ---------- 1. Áp dụng cho MỌI trang ----------
for f in glob.glob(os.path.join(ROOT, "*.html")):
    s = rd(f)
    # bỏ font serif Newsreader, chỉ giữ Be Vietnam Pro (đủ dấu tiếng Việt)
    s = re.sub(r"family=Be\+Vietnam\+Pro:wght@[0-9;]+&family=Newsreader:[^\"&]*&display=swap",
               "family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap", s)
    # nạp pro2.css sau cùng
    if "assets/pro2.css" not in s:
        s = s.replace("</head>", '    <link rel="stylesheet" href="assets/pro2.css" />\n  </head>', 1)
    # bỏ icon mũi tên (nếu còn trong nội dung)
    s = re.sub(r'<svg class="ico" aria-hidden="true">\s*<use href="#i-out"\s*/>\s*</svg>', "", s)
    s = re.sub(r'<symbol id="i-out".*?</symbol>', "", s, flags=re.S)
    s = re.sub(r'<symbol id="i-up".*?</symbol>', "", s, flags=re.S)
    # chữ nghiêng -> in thường (thẻ <em> đã được CSS xử lý, bỏ style inline cũ)
    s = s.replace('<em style="background:none;color:#fff;-webkit-text-fill-color:#fff">', "<em>")
    wr(f, s)

# ---------- 2. Lightbox: nút chữ thay mũi tên ‹ › ----------
p = os.path.join(ROOT, "assets", "vip.js")
j = rd(p)
j = j.replace('aria-label="Ảnh trước">‹</button>', 'aria-label="Ảnh trước">Trước</button>')
j = j.replace('aria-label="Ảnh sau">›</button>', 'aria-label="Ảnh sau">Sau</button>')
wr(p, j)

# ---------- 3. Trang chủ ----------
p = os.path.join(ROOT, "index.html")
s = rd(p)

s = s.replace("Chín nhóm sản phẩm cho", "Bảy nhóm sản phẩm cho")

# bỏ mục "Yêu thích" và "Gợi ý cho bạn" (kiểu cửa hàng online) khỏi trang chủ doanh nghiệp
s = re.sub(r'\s*<section class="sec" id="fav-sec">.*?</section>', "", s, flags=re.S)
s = re.sub(r'\s*<section class="sec rv-sec"[^>]*>.*?</section>', "", s, flags=re.S)

AUD = """
      <section class="sec" id="giai-phap">
        <div class="wrap">
          <div class="sec-head">
            <span class="eyebrow">Giải pháp theo nhu cầu</span>
            <h2>Acooki đồng hành cùng <em>từng mô hình kinh doanh</em></h2>
            <p class="lede">Dù bạn nấu cho gia đình, vận hành bếp quán, phân phối hàng tiêu dùng hay muốn có thương hiệu riêng, Acooki có quy cách và hình thức hợp tác phù hợp.</p>
          </div>
          <div class="aud">
            <article class="aud-c">
              <span class="aud-n">01</span>
              <h3>Gia đình &amp; bếp ăn</h3>
              <p>Nước chấm, hạt nêm, nước tương, sa tế đóng chai, đóng túi tiện dùng hằng ngày.</p>
              <ul><li>Chai 500ml đến 900ml</li><li>Hạt nêm gói 200g, 400g, 900g</li></ul>
              <a class="link" href="san-pham.html">Xem sản phẩm</a>
            </article>
            <article class="aud-c">
              <span class="aud-n">02</span>
              <h3>Nhà hàng, quán ăn, bếp tập thể</h3>
              <p>Quy cách lớn, giá theo thùng, đáp ứng nhu cầu dùng đều và số lượng nhiều.</p>
              <ul><li>Can nước chấm 4,8 lít</li><li>Hạt nêm bao 5kg, 10kg</li></ul>
              <a class="link" href="lien-he.html">Nhận báo giá</a>
            </article>
            <article class="aud-c">
              <span class="aud-n">03</span>
              <h3>Đại lý &amp; nhà phân phối</h3>
              <p>Chính sách ưu đãi riêng của Công ty Asian Việt Nam dành cho đối tác kinh doanh.</p>
              <ul><li>Danh mục 28 sản phẩm</li><li>Hồ sơ pháp lý công khai</li></ul>
              <a class="link" href="lien-he.html">Nhận chính sách đại lý</a>
            </article>
            <article class="aud-c">
              <span class="aud-n">04</span>
              <h3>Gia công thương hiệu riêng</h3>
              <p>Gia công nước mắm độc quyền cho doanh nghiệp, sản xuất tại nhà máy Acooki ở Củ Chi.</p>
              <ul><li>Nhà máy riêng tại Củ Chi</li><li>Quy trình ủ chượp truyền thống</li></ul>
              <a class="link" href="lien-he.html">Trao đổi về gia công</a>
            </article>
          </div>
        </div>
      </section>
"""

WHY = """
      <section class="sec sec-salt">
        <div class="wrap why">
          <div class="why-img"><img src="assets/img/vi-ngu-7.webp" alt="Nước mắm Acooki và quy trình sản xuất" loading="lazy" /></div>
          <div>
            <span class="eyebrow">Vì sao chọn Acooki</span>
            <h2>Năng lực sản xuất <em>minh bạch, ổn định</em></h2>
            <div class="why-list">
              <div><b class="n">01</b><h3>Nhà máy trực tiếp sản xuất</h3><p>3 nhà máy tại huyện Củ Chi, TP.HCM, chủ động nguồn hàng và chất lượng.</p></div>
              <div><b class="n">02</b><h3>Quy trình ủ chượp 8 bước</h3><p>Từ chọn cá, chọn muối đến lọc mắm nhĩ và đóng chai theo quy trình truyền thống.</p></div>
              <div><b class="n">03</b><h3>Danh mục đầy đủ cho một gian bếp</h3><p>28 sản phẩm: nước mắm, hạt nêm, nước tương, sa tế, tương ớt và hóa phẩm gia dụng.</p></div>
              <div><b class="n">04</b><h3>Hồ sơ pháp lý rõ ràng</h3><p>Công bố sản phẩm và giấy tờ liên quan được đăng tại <a class="link" href="chung-nhan.html">trang Chứng nhận</a>.</p></div>
            </div>
          </div>
        </div>
      </section>
"""

FLOW = """
      <section class="sec">
        <div class="wrap">
          <div class="sec-head">
            <span class="eyebrow">Quy trình hợp tác</span>
            <h2>Bắt đầu hợp tác <em>trong bốn bước</em></h2>
            <p class="lede">Quy trình gọn, rõ ràng để đối tác nhanh chóng nhận được thông tin, báo giá và sản phẩm.</p>
          </div>
          <div class="flow">
            <div><h3>Gửi yêu cầu</h3><p>Liên hệ qua hotline, email hoặc biểu mẫu, cho biết nhu cầu và khu vực kinh doanh.</p></div>
            <div><h3>Tư vấn &amp; báo giá</h3><p>Acooki tư vấn quy cách phù hợp và gửi bảng giá, chính sách theo đối tượng.</p></div>
            <div><h3>Xác nhận đơn hàng</h3><p>Hai bên thống nhất số lượng, điều khoản thanh toán và lịch giao hàng.</p></div>
            <div><h3>Giao hàng &amp; đồng hành</h3><p>Nhận hàng và được hỗ trợ trong suốt quá trình kinh doanh cùng Acooki.</p></div>
          </div>
        </div>
      </section>
"""

REACH = """
      <section class="sec sec-salt">
        <div class="wrap">
          <div class="reach">
            <div class="reach-l">
              <span class="eyebrow">Liên hệ doanh nghiệp</span>
              <h2>Nhận bảng giá &amp; chính sách cho đối tác</h2>
              <p>Để lại nhu cầu của bạn, đội ngũ Acooki sẽ phản hồi sớm nhất có thể. Hỗ trợ đại lý, nhà phân phối, nhà hàng và gia công thương hiệu riêng.</p>
              <div class="actions">
                <a class="btn" href="lien-he.html">Gửi yêu cầu báo giá</a>
                <a class="btn btn-ghost" href="tel:0966220012">Gọi 0966220012</a>
              </div>
            </div>
            <div class="reach-r">
              <div><small>Hotline</small><a href="tel:0966220012">0966220012</a></div>
              <div><small>Email</small><a href="mailto:asianvietnam.tong@gmail.com">asianvietnam.tong@gmail.com</a></div>
              <div><small>Văn phòng</small><span>Đường N1, KDC Hiệp Thành City, Quận 12, TP.HCM</span></div>
            </div>
          </div>
        </div>
      </section>
"""

# chèn "Giải pháp theo nhu cầu" ngay sau phần Về Acooki (trước Bán chạy)
s = s.replace('      <section class="sec sec-salt" id="best-sec">', AUD + '      <section class="sec sec-salt" id="best-sec">', 1)
# bỏ khối "Hợp tác cùng Acooki" cũ (đã gộp vào giải pháp) và thay bằng Vì sao chọn + quy trình hợp tác
s = re.sub(r'\s*<section class="sec">\s*<div class="wrap">\s*<div class="sec-head">\s*<span class="eyebrow">Hợp tác</span>.*?</section>',
           WHY + FLOW, s, count=1, flags=re.S)
# chèn khối liên hệ doanh nghiệp trước khối đối tác (logos)
s = s.replace('      <section class="sec">\n        <div class="wrap">\n          <div class="logos">', REACH + '      <section class="sec">\n        <div class="wrap">\n          <div class="logos">', 1)
wr(p, s)
print("OK")
