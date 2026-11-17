# Acooki Website

Website tĩnh (HTML/CSS/JS) của Acooki. Toàn bộ site nằm ở **thư mục gốc** của repo, nên có thể deploy trực tiếp bằng GitHub Pages.

## Cấu trúc

```
/                       <- root repo
├── index.html          trang chủ
├── san-pham.html       danh sách sản phẩm
├── sp-*.html           trang chi tiết sản phẩm
├── bai-viet-*.html     bài viết
├── tin-tuc.html, gioi-thieu.html, chung-nhan.html, lien-he.html
├── assets/             css, js, favicon, hình ảnh (assets/img)
├── tools/              script Python dùng để tạo/cập nhật trang (không bắt buộc khi deploy)
├── chay-thu-tren-may.bat   chạy thử website trên Windows (http://localhost:8080)
└── .nojekyll           báo GitHub Pages không xử lý bằng Jekyll
```

## Đưa lên GitHub (main / root)

1. Tạo repo mới trên GitHub, nhánh mặc định `main`.
2. Giải nén file zip, upload **toàn bộ nội dung bên trong thư mục** `acooki-website` lên repo (kéo thả vào trang repo, hoặc dùng git).
   Nhớ bật hiện file ẩn để upload cả `.nojekyll`.
3. Vào **Settings → Pages → Build and deployment → Source: Deploy from a branch**, chọn **Branch: main**, thư mục **/ (root)**, bấm Save.
4. Chờ 1–2 phút, site chạy tại `https://<tên-tài-khoản>.github.io/<tên-repo>/`.

Dùng git:

```bash
git init
git add .
git commit -m "Acooki website"
git branch -M main
git remote add origin https://github.com/<tên-tài-khoản>/<tên-repo>.git
git push -u origin main
```

## Chạy thử trên máy

- Windows: bấm đúp `chay-thu-tren-may.bat`.
- Hoặc: `python -m http.server 8080` rồi mở http://localhost:8080

## Dùng script trong tools/

Các script nhận đường dẫn thư mục site làm tham số. Vì site giờ nằm ở root, chạy từ thư mục gốc:

```bash
python tools/build.py .
python tools/upgrade.py .
python tools/patch.py .
```
