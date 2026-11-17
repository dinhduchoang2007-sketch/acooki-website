/* ACOOKI PRO — video phát tại chỗ, "sản phẩm vừa xem" */
(() => {
  const $ = (s, r = document) => r.querySelector(s),
    $$ = (s, r = document) => [...r.querySelectorAll(s)];

  /* ---------- 1. Video: bấm là phát ngay trên trang chủ ---------- */
  $$(".yt").forEach((box) => {
    const id = box.dataset.id,
      btn = $(".yt-play", box),
      img = $("img", box);
    if (img) {
      img.addEventListener("error", () => {
        if (!img.dataset.fb) {
          img.dataset.fb = "1";
          img.src = "https://i.ytimg.com/vi/" + id + "/hqdefault.jpg";
        }
      });
    }
    const play = () => {
      // Mở file trực tiếp từ máy (file://): YouTube chặn nhúng (lỗi 153) -> mở YouTube ở tab mới
      if (location.protocol === "file:") {
        window.open("https://www.youtube.com/watch?v=" + id, "_blank", "noopener");
        return;
      }
      const f = document.createElement("iframe");
      f.src =
        "https://www.youtube.com/embed/" +
        id +
        "?autoplay=1&rel=0&modestbranding=1&playsinline=1";
      f.title = box.dataset.title || "Video Acooki";
      f.allow =
        "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; fullscreen";
      f.allowFullscreen = true;
      f.referrerPolicy = "strict-origin-when-cross-origin";
      box.classList.add("on");
      box.appendChild(f);
    };
    btn && btn.addEventListener("click", play);
  });

  /* ---------- 2. Sản phẩm vừa xem ---------- */
  const KEY = "acooki-rv";
  const PR = window.PRODUCTS || [];
  const P = {};
  PR.forEach((p) => (P[p.s] = [p.n, p.cn, p.img, p.fit]));
  const read = () => {
    try {
      const a = JSON.parse(localStorage.getItem(KEY) || "[]");
      return Array.isArray(a) ? a.filter((k) => P[k]) : [];
    } catch (e) {
      return [];
    }
  };
  const write = (a) => {
    try {
      localStorage.setItem(KEY, JSON.stringify(a.slice(0, 8)));
    } catch (e) {}
  };
  const push = (id) => {
    if (!P[id]) return;
    const a = read().filter((k) => k !== id);
    a.unshift(id);
    write(a);
  };

  // trang chi tiết: ghi nhận sau khi xem 1,5 giây (không tính sản phẩm đang mở trong danh sách gợi ý)
  const cur = (document.querySelector("main[data-slug]") || {}).dataset;
  const curSlug = cur && cur.slug;
  if (curSlug) setTimeout(() => { push(curSlug); }, 1500);

  const card = (id) => {
    const [name, cat, img, fit] = P[id];
    return (
      '<a class="rv-card" href="sp-' + id + '.html"><span class="rv-pic"><img src="' + img + '" alt="" loading="lazy"' +
      (fit ? ' style="object-fit:contain"' : "") + " /></span><span class=\"rv-cat\">" + cat + '</span><span class="rv-name">' + name + "</span></a>"
    );
  };

  function renderAll() {
    $$("[data-rv]").forEach((slot) => {
      const mode = slot.dataset.rv; // "home" | "list"
      const seen = read().filter((k) => k !== curSlug);
      let ids = seen,
        title = "Sản phẩm bạn vừa xem",
        sub = "Xem lại nhanh những sản phẩm bạn đã mở trên trang này.",
        clear = true;
      if (!seen.length) {
        if (mode === "list") {
          slot.hidden = true;
          return;
        }
        ids = ["vi-ngu-900ml", "hat-nem-900g", "nuoc-tuong-soya-700ml", "sa-te-cay-100g"].filter((k) => P[k]);
        title = "Gợi ý cho bạn";
        sub = "Những sản phẩm quen thuộc trong gian bếp Việt. Sản phẩm bạn xem sẽ hiện ở đây.";
        clear = false;
      }
      slot.hidden = false;
      slot.innerHTML =
        '<div class="rv-head"><div><h2>' + title + '</h2><p class="rv-sub">' + sub + "</p></div>" +
        (clear ? '<button type="button" class="rv-clear">Xóa lịch sử</button>' : "") +
        '</div><div class="rv-rail">' + ids.map(card).join("") + "</div>";
      const c = $(".rv-clear", slot);
      c &&
        c.addEventListener("click", () => {
          write([]);
          renderAll();
        });
    });
  }
  renderAll();
})();
