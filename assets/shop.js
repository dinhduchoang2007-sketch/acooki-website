/* ACOOKI — yêu thích, lọc/tìm sản phẩm, điền sẵn form liên hệ */
(() => {
  const $ = (s, r = document) => r.querySelector(s),
    $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const PR = window.PRODUCTS || [];
  const norm = (s) => s.toLowerCase().replace(/đ/g, "d").normalize("NFD").replace(/[̀-ͯ]/g, "");
  const money = (n) => String(n).replace(/\B(?=(\d{3})+(?!\d))/g, ".") + "đ";
  const KEY = "acooki-fav";

  /* ---------- yêu thích ---------- */
  const rf = () => {
    try {
      const a = JSON.parse(localStorage.getItem(KEY) || "[]");
      return Array.isArray(a) ? a : [];
    } catch (e) {
      return [];
    }
  };
  const wf = (a) => {
    try {
      localStorage.setItem(KEY, JSON.stringify(a));
    } catch (e) {}
  };
  const sync = () => {
    const f = rf();
    $$(".pc-fav").forEach((b) => {
      const on = f.includes(b.dataset.s);
      b.setAttribute("aria-pressed", on);
      const sp = $("span", b);
      if (sp) sp.textContent = on ? "Đã lưu yêu thích" : "Yêu thích";
    });
  };
  const card = (p) => {
    const href = "sp-" + p.s + ".html",
      tag = p.t ? '<span class="pc-tag t-' + p.t + '">' + { best: "Bán chạy", feat: "Nổi bật", fav: "Yêu thích" }[p.t] + "</span>" : "";
    const cs = p.q > 1 ? 'Thùng ' + p.q + " " + p.u + ": <b>" + money(p.pc) + "</b>" : "Quy cách: 1 " + p.u;
    return (
      '<article class="pc" data-s="' + p.s + '"><a class="pc-pic' + (p.fit ? " fit" : "") + '" href="' + href + '" tabindex="-1" aria-hidden="true"><img src="' + p.img + '" alt="" loading="lazy" />' + tag + "</a>" +
      '<button type="button" class="pc-fav" data-s="' + p.s + '" aria-pressed="false" aria-label="Lưu ' + p.n + ' vào yêu thích"><svg class="ico" aria-hidden="true"><use href="#i-heart" /></svg></button>' +
      '<div class="pc-b"><span class="pc-cat">' + p.cn + '</span><h3><a href="' + href + '">' + p.n + "</a></h3>" +
      '<div class="pc-price"><b>' + money(p.p) + "</b><small>/" + p.u + '</small></div><span class="pc-case">' + cs + "</span>" +
      '<a class="pc-btn" href="' + href + '">Xem chi tiết</a></div></article>'
    );
  };
  const renderFavHome = () => {
    const box = $('[data-home="fav"]');
    if (!box) return;
    const f = rf().map((s) => PR.find((p) => p.s === s)).filter(Boolean);
    if (!f.length) return;
    box.innerHTML = f.slice(0, 8).map((p) => card({ ...p, t: "fav" })).join("");
    $("#fav-h").innerHTML = "Sản phẩm bạn <em>đã lưu</em>";
    $("#fav-sub").textContent = "Những sản phẩm bạn bấm trái tim. Danh sách được lưu ngay trên trình duyệt này.";
  };
  document.addEventListener("click", (e) => {
    const b = e.target.closest(".pc-fav");
    if (!b) return;
    e.preventDefault();
    let f = rf();
    const s = b.dataset.s,
      was = f.includes(s);
    f = was ? f.filter((x) => x !== s) : [s, ...f];
    wf(f.slice(0, 40));
    sync();
    // Trang chủ: đổi danh sách yêu thích sau khi người dùng chủ động lưu
    if (!was) renderFavHome();
  });
  renderFavHome();
  sync();

  /* ---------- trang danh sách: lọc nhóm + tìm kiếm ---------- */
  const secs = $$(".cat-sec");
  if (secs.length) {
    const chips = $$(".chip"),
      q = $("#pq"),
      none = $(".no-res");
    const apply = () => {
      const h = decodeURIComponent(location.hash.slice(1));
      const cat = secs.some((s) => s.id === h) ? h : "all";
      const kw = norm(q.value.trim());
      let shown = 0;
      secs.forEach((s) => {
        let any = false;
        $$(".pc", s).forEach((c) => {
          const hit = !kw || norm(c.dataset.k + " " + s.querySelector("h2").textContent).includes(kw);
          c.hidden = !hit;
          c.style.display = hit ? "" : "none";
          any = any || hit;
        });
        const vis = any && (cat === "all" || s.id === cat);
        s.hidden = !vis;
        if (vis) shown++;
      });
      chips.forEach((c) => c.classList.toggle("on", c.dataset.c === cat));
      none.hidden = shown > 0;
    };
    chips.forEach((c) =>
      c.addEventListener("click", (e) => {
        e.preventDefault();
        history.replaceState(null, "", c.dataset.c === "all" ? location.pathname : "#" + c.dataset.c);
        apply();
        scrollTo({ top: Math.max(0, $(".shop").offsetTop - 60), behavior: "smooth" });
      }),
    );
    q.addEventListener("input", apply);
    addEventListener("hashchange", apply);
    apply();
  }

  /* ---------- liên hệ: điền sẵn sản phẩm quan tâm ---------- */
  const m = $("#m"),
    sp = new URLSearchParams(location.search).get("sp");
  if (m && sp) {
    const p = PR.find((x) => x.s === sp);
    if (p) {
      m.value = "Tôi muốn nhận báo giá / đặt mua: " + p.n + " (quy cách " + p.q + " " + p.u + "/thùng).";
      const sel = $("#s");
      if (sel) sel.value = "Mua sản phẩm";
      setTimeout(() => $("#cf") && $("#cf").scrollIntoView({ behavior: "smooth", block: "center" }), 400);
    }
  }
})();
