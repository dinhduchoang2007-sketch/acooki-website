# -*- coding: utf-8 -*-
"""Dữ liệu sản phẩm Acooki — giá KHÔNG chiết khấu (cột "Bảng báo giá nhà phân phối", đã gồm VAT).
Sửa giá / ảnh / mô tả tại đây rồi chạy lại build.py."""

CATS = [
    # id, tên, eyebrow, ảnh đại diện, mô tả nhóm
    ("nuoc-mam", "Nước chấm Vị Ngư", "Nước mắm", "vi-ngu-03",
     "Nước mắm chế biến từ cá cơm tươi, lên men tự nhiên theo phương pháp truyền thống kết hợp công nghệ hiện đại. Đủ quy cách từ chai 500ml đến can 4,8 lít."),
    ("hat-nem", "Hạt nêm Acook", "Hạt nêm", "hat-nem-02",
     "Hạt nêm 3 trong 1 từ thịt thăn, rau củ và xương ống, bổ sung Betacarotene, đậm đà cho mọi món canh, kho, xào."),
    ("hat-nem-chay", "Hạt nêm chay nấm", "Hạt nêm chay", "hat-nem-chay-01",
     "Hạt nêm chay hương nấm organic, ngọt thanh tự nhiên, dùng được cho cả bữa chay và bữa mặn."),
    ("bao-lon", "Hạt nêm bao lớn", "Hạt nêm bao lớn", "bao-lon-01",
     "Bao 5kg và 10kg dành cho quán ăn, bếp ăn tập thể: dùng bền, tiết kiệm chi phí."),
    ("nuoc-tuong", "Nước tương Soya", "Nước tương", "nuoc-tuong-03",
     "Nước tương làm từ đậu nành tuyển chọn, lên men tự nhiên, đậm đà cho mọi bữa cơm."),
    ("sa-te", "Sa tế Acook", "Sa tế", "sa-te-01",
     "Sa tế cay đậm chuẩn vị quán và sa tế tôm chua cay dậy mùi, dùng cho lẩu, mì, bún, xào, ướp."),
    ("tuong", "Tương ớt & tương xay", "Tương", "tuong-ot-03",
     "Tương ớt cay sánh ngon và tương xay đậm vị quen, ngon bữa cơm nhà."),
    ("nuoc-giat", "Nước giặt Amatic", "Hóa phẩm gia dụng", "nuoc-giat-03",
     "Nước giặt xả 6 trong 1 Amatic hương thơm lâu, sạch sâu, bảo vệ sợi vải. Sản phẩm của TB Foods."),
    ("rua-chen", "Nước rửa chén Chanh", "Hóa phẩm gia dụng", "rua-chen-04",
     "Nước rửa chén hương chanh 3 in 1: sạch dầu mỡ, khử mùi, dịu nhẹ da tay. Sản phẩm của TB Foods."),
]

# Mô tả dùng chung theo nhóm (thu thập & chỉnh lại từ acooki.com và ảnh sản phẩm)
CATINFO = {
    "nuoc-mam": dict(
        desc=["Nước chấm Vị Ngư được chế biến từ cá cơm tươi ngon, chọn lọc kỹ lưỡng, áp dụng phương pháp lên men tự nhiên truyền thống kết hợp công nghệ hiện đại.",
              "Nước mắm có màu cánh gián óng ánh tự nhiên, không pha chế màu; độ đạm cao, độ mặn cân bằng và độ chua nhẹ. Có thể dùng để chấm, kho, nấu và tẩm ướp nhiều món ăn."],
        ticks=["Cá cơm tươi, lên men tự nhiên theo quy trình truyền thống", "Màu cánh gián óng ánh, không pha chế màu", "Dùng để chấm, kho, nấu, tẩm ướp"],
        use="Dùng làm nước chấm, nêm nếm, kho, nấu, tẩm ướp.",
        store="Bảo quản nơi khô ráo, thoáng mát, tránh ánh nắng trực tiếp.", cert="nuoc-cham"),
    "hat-nem": dict(
        desc=["Hạt nêm Acook 3 trong 1 từ thịt thăn, rau củ và xương ống, đậm đà hương vị cho mọi món ăn, bổ sung Betacarotene.",
              "Thành phần tự nhiên, tan nhanh trong nước và thực phẩm, giúp tiết kiệm thời gian nấu nướng. Dùng cho các món canh, súp, xào, kho, nướng."],
        ticks=["3 trong 1: thịt thăn, rau củ, xương ống", "Bổ sung Betacarotene", "Tan nhanh, nêm canh, kho, xào, nướng đều ngon"],
        use="Nêm trực tiếp vào món canh, súp, xào, kho, nướng; nêm từ từ và nếm lại cho vừa khẩu vị.",
        store="Bảo quản nơi khô ráo, thoáng mát; đậy kín bao bì sau khi mở.", cert=None),
    "hat-nem-chay": dict(
        desc=["Hạt nêm chay Acook hương nấm hương organic, vị ngọt thanh tự nhiên, dùng cho cả nhà và nêm được nhiều món.",
              "Phù hợp bữa chay lẫn bữa mặn; dễ nêm, dễ tan, giữ vị ngọt lành cho nồi canh, món xào và món kho."],
        ticks=["Hương nấm hương organic, ngọt thanh tự nhiên", "Chay, dễ nêm, nêm món nào cũng hợp", "Dùng được cho cả bữa chay và bữa mặn"],
        use="Nêm vào canh, xào, kho, lẩu chay; nêm từ từ và nếm lại cho vừa khẩu vị.",
        store="Bảo quản nơi khô ráo, thoáng mát; đậy kín bao bì sau khi mở.", cert=None),
    "bao-lon": dict(
        desc=["Hạt nêm Acook quy cách bao lớn dành cho quán ăn, bếp ăn tập thể và nhà hàng: dùng bền, tiết kiệm chi phí.",
              "Hương vị đậm đà từ thịt và nước cốt xương hầm, chuẩn bếp quán, bếp ăn công nghiệp."],
        ticks=["Bao lớn - dùng bền - tiết kiệm", "Chuẩn quán ăn, bếp lớn, nhà hàng", "Có chính sách ưu đãi cho đại lý và nhà phân phối"],
        use="Nêm trực tiếp vào nồi canh, nước dùng, món xào, kho cho bếp quy mô lớn.",
        store="Bảo quản nơi khô ráo, thoáng mát; buộc kín miệng bao sau khi dùng.", cert=None),
    "nuoc-tuong": dict(
        desc=["Nước tương Soya Acook được chế biến từ những hạt đậu nành tuyển chọn kỹ lưỡng, non hạt, giàu dinh dưỡng; lên men tự nhiên truyền thống kết hợp công nghệ hiện đại.",
              "Hương vị đậm đà, hài hòa giữa vị ngọt dịu của đậu nành và vị mặn nhẹ của muối; màu nâu cánh gián tự nhiên, trong suốt, không dùng chất tạo màu."],
        ticks=["Đậu nành tuyển chọn, lên men tự nhiên", "Độ mặn vừa phải, không quá gắt", "Chấm, kho, nấu, ướp, xào, làm nước sốt"],
        use="Dùng để chấm, kho, nấu, ướp, xào và làm nước sốt.",
        store="Bảo quản nơi khô ráo, thoáng mát, tránh ánh nắng trực tiếp.", cert="nuoc-tuong-soya"),
    "sa-te": dict(
        desc=[],
        ticks=[],
        use="Dùng cho món xào, nướng, lẩu, bún, phở; làm nước chấm hải sản, thịt nướng hoặc sốt ướp món chiên, nướng.",
        store="Bảo quản nơi khô ráo, thoáng mát; đậy kín nắp và dùng muỗng sạch sau khi mở.", cert=None),
    "tuong": dict(
        desc=[],
        ticks=[],
        use="Dùng làm nước chấm, chan, trộn gỏi, ăn kèm bún, phở, bánh, món chiên.",
        store="Bảo quản nơi khô ráo, thoáng mát; đậy kín nắp sau khi mở.", cert=None),
    "nuoc-giat": dict(
        desc=["Nước giặt xả Amatic 6 trong 1: sạch sâu, thơm lâu, bảo vệ sợi vải, công nghệ đậm đặc, an toàn và tiết kiệm.",
              "Dòng sản phẩm của TB Foods với nhiều hương: hương hoa Bulgaria, hương tím Huế, hương nắng mai, hương thiên nhiên; có can 3,8L và túi tiết kiệm 2L."],
        ticks=["6 trong 1: giặt và xả trong một lần", "Sạch sâu, thơm lâu, bảo vệ sợi vải", "Công nghệ đậm đặc, tiết kiệm hơn"],
        use="Dùng cho giặt tay và giặt máy; xem liều lượng khuyến nghị trên bao bì.",
        store="Bảo quản nơi khô ráo, thoáng mát, tránh ánh nắng trực tiếp; để xa tầm tay trẻ em.", cert="nuoc-giat-444"),
    "rua-chen": dict(
        desc=["Nước rửa chén Chanh 3 in 1 sạch sáng bóng, thơm mát tự nhiên: sạch dầu mỡ, khử mùi tanh, dịu nhẹ với da tay.",
              "Nhiều quy cách từ chai 400ml đến can 5L, phù hợp cho gia đình, quán ăn và bếp ăn. Sản phẩm của TB Foods."],
        ticks=["Chanh 3 in 1: sạch dầu mỡ, khử mùi, dịu nhẹ da tay", "Sạch sáng bóng, thơm mát tự nhiên", "Nhiều quy cách cho gia đình lẫn bếp ăn"],
        use="Cho một lượng vừa đủ lên miếng rửa, tạo bọt, rửa sạch và xả lại bằng nước.",
        store="Bảo quản nơi khô ráo, thoáng mát, tránh ánh nắng trực tiếp; để xa tầm tay trẻ em.", cert="nuoc-rua-chen-777"),
}

# slug, cat, tên, quy cách (số/thùng), ĐVT, giá/đơn vị, giá/thùng, ảnh chính, nhóm giá, mô tả riêng, tags, ghi chú ưu đãi
# tags: best = bán chạy, feat = nổi bật, fav = yêu thích (mặc định)
P = [
 ("vi-ngu-500ml","nuoc-mam","Nước chấm Vị Ngư 500ml (chai vuông)",24,"chai",10400,249600,"vi-ngu-05","KPI",
  "Chai vuông 500ml gọn nhẹ, tiện cho bếp gia đình dùng hằng ngày.","fav",""),
 ("vi-ngu-750ml","nuoc-mam","Nước chấm Vị Ngư 750ml (chai vuông)",20,"chai",11960,239200,"vi-ngu-06","KPI",
  "Chai vuông 750ml là quy cách phổ biến cho bữa cơm gia đình.","best",""),
 ("vi-ngu-800ml","nuoc-mam","Nước chấm Vị Ngư 800ml (chai vuông)",15,"chai",11648,174720,"vi-ngu-04","KPI",
  "Chai vuông 800ml dòng siêu tiết kiệm, dùng được lâu hơn cho gia đình đông người.","",""),
 ("vi-ngu-900ml","nuoc-mam","Nước chấm Vị Ngư 900ml (chai vuông)",15,"chai",13520,202800,"vi-ngu-03","KPI",
  "Chai vuông 900ml cao đạm, lựa chọn vì sức khỏe, được nhiều gia đình tin dùng.","best",""),
 ("vi-ngu-1-8l","nuoc-mam","Nước chấm Vị Ngư 1,8 lít (chai vuông)",8,"chai",23920,191360,"vi-ngu-01","KPI",
  "Chai lớn 1,8 lít: dùng lâu, tiết kiệm, phù hợp gia đình và quán ăn.","",""),
 ("vi-ngu-4-8l","nuoc-mam","Nước chấm Vị Ngư 4,8 lít (can)",4,"can",52000,208000,"vi-ngu-02","KPI",
  "Can 4,8 lít siêu tiết kiệm, chuyên cho bếp quán và bếp ăn lớn.","feat",""),

 ("hat-nem-400g","hat-nem","Hạt nêm Acook 400g",40,"túi",20800,832000,"hat-nem-01","KPI",
  "Gói 400g vừa dùng cho gia đình nhỏ.","fav",""),
 ("hat-nem-900g","hat-nem","Hạt nêm Acook 900g",20,"túi",41600,832000,"hat-nem-02","KPI",
  "Gói 900g tiện lợi, thích hợp cho nhu cầu dùng hằng ngày.","best",""),

 ("hat-nem-chay-200g","hat-nem-chay","Hạt nêm chay Acook 200g",80,"túi",10400,832000,"hat-nem-chay-02","KPI",
  "Gói nhỏ 200g tiện lợi, ngọt thanh tự nhiên, lựa chọn vì sức khỏe.","feat",""),
 ("hat-nem-chay-900g","hat-nem-chay","Hạt nêm chay Acook 900g",20,"túi",44720,894400,"hat-nem-chay-01","KPI",
  "Gói 900g ngọt thanh tự nhiên, dùng cho cả nhà.","fav",""),

 ("hat-nem-5kg","bao-lon","Hạt nêm Acook 5kg",4,"túi",96200,384800,"bao-lon-01","Ngoài KPI",
  "Bao lớn 5kg dùng bền, tiết kiệm, lựa chọn cho quán ăn và bếp lớn.","",""),
 ("hat-nem-10kg","bao-lon","Hạt nêm Acook 10kg",2,"túi",192400,384800,"bao-lon-02","Ngoài KPI",
  "Bao đại 10kg dùng lâu, tiết kiệm chi phí, chuẩn quán ăn - bếp lớn - nhà hàng.","",""),

 ("nuoc-tuong-soya-700ml","nuoc-tuong","Nước tương Soya Acook 700ml",20,"chai",5616,112320,"nuoc-tuong-03","Ngoài KPI",
  "Chai Soya đậm đà cho mọi bữa cơm, gia vị quen thuộc nhà nào cũng có.","best",""),
 ("nuoc-tuong-soya-4-8l","nuoc-tuong","Nước tương Soya Acook 4,8 lít",4,"can",32396,129584,"nuoc-tuong-02","Ngoài KPI",
  "Can 4,8 lít tiết kiệm, dùng lâu hơn cho bếp quán.","",""),

 ("sa-te-cay-100g","sa-te","Sa tế cay Acook 100g",96,"chai",7280,698880,"sa-te-01","KPI",
  "Sa tế cay đậm, chuẩn vị quán. Làm từ ớt đỏ, tỏi và các nguyên liệu tự nhiên.","best",""),
 ("sa-te-tom-100g","sa-te","Sa tế tôm Acook 100g",96,"chai",7280,698880,"sa-te-02","KPI",
  "Sa tế tôm đặc biệt chua cay, dậy mùi, đậm vị.","feat",""),

 ("tuong-ot-850g","tuong","Tương ớt Acook 850g",12,"chai",9360,112320,"tuong-ot-01","Ngoài KPI",
  "Tương ớt cay, sánh, ngon.","feat","Ưu đãi: hỗ trợ 1 thùng tặng 3 chai nước chấm 800ml."),
 ("tuong-ot-4-5kg","tuong","Tương ớt Acook 4,5kg",4,"can",41600,166400,"tuong-ot-03","Ngoài KPI",
  "Can 4,5kg dành cho quán ăn và bếp lớn.","","Ưu đãi: hỗ trợ 1 thùng tặng 1 chai nước chấm 4,8 lít."),
 ("tuong-xay-850g","tuong","Tương xay (tương đen) Acook 850g",12,"chai",9360,112320,"tuong-ot-02","Ngoài KPI",
  "Tương xay sánh mịn, dễ chấm; đậm vị quen, ngon bữa cơm nhà.","fav","Ưu đãi: hỗ trợ 1 thùng tặng 3 chai nước chấm 800ml."),

 ("nuoc-giat-can-comfor","nuoc-giat","Nước giặt Amatic can 3,8L hương Comfor",4,"can",99840,399360,"nuoc-giat-03","KPI",
  "Can 3,8L hương hoa thơm ngát dài lâu, tinh dầu thơm hoa hồng Bulgaria.","feat",""),
 ("nuoc-giat-can-downy","nuoc-giat","Nước giặt Amatic can 3,8L hương Downy",4,"can",99840,399360,"nuoc-giat-06","KPI",
  "Can 3,8L hương tím Huế thơm lâu tinh tế, tinh dầu lavender & orchid.","fav",""),
 ("nuoc-giat-tui-comfor","nuoc-giat","Nước giặt Amatic túi 2L hương Comfor",6,"túi",46800,280800,"nuoc-giat-05","KPI",
  "Túi 2L tiết kiệm, hương nắng mai thơm mát dịu nhẹ.","best",""),
 ("nuoc-giat-tui-downy","nuoc-giat","Nước giặt Amatic túi 2L hương Downy",6,"túi",46800,280800,"nuoc-giat-04","KPI",
  "Túi 2L tiết kiệm, hương thiên nhiên an lành, đánh bay mọi vết bẩn.","",""),

 ("rua-chen-4l","rua-chen","Nước rửa chén Chanh can 4L hương chanh",4,"can",62400,249600,"rua-chen-04","KPI",
  "Can 4L sạch sáng bóng, thơm mát tự nhiên, dùng cho gia đình và quán ăn.","",""),
 ("rua-chen-1-5l","rua-chen","Nước rửa chén Chanh chai 1,5L hương chanh",8,"chai",29120,232960,"rua-chen-01","KPI",
  "Chai 1,5L tiện dùng, sạch dầu mỡ, dịu nhẹ da tay.","",""),
 ("rua-chen-770ml","rua-chen","Nước rửa chén Chanh chai 770ml hương chanh",20,"chai",15600,312000,"rua-chen-02","KPI",
  "Chai 770ml cho nhu cầu dùng hằng ngày.","",""),
 ("rua-chen-400ml","rua-chen","Nước rửa chén Chanh chai 400ml hương chanh",24,"chai",8320,199680,"rua-chen-05","KPI",
  "Chai 400ml nhỏ gọn, sạch sáng bóng, thơm mát hương chanh.","feat",""),
 ("rua-chen-5l","rua-chen","Nước rửa chén Chanh can 5L hương chanh",4,"can",69680,278720,"rua-chen-03","KPI",
  "Can 5L dung tích lớn, tiết kiệm cho bếp ăn và quán ăn.","",""),
]

# Mô tả riêng cho sa tế / tương (không có mô tả nhóm dùng chung)
EXTRA_DESC = {
 "sa-te-cay-100g": ["Sa tế cay là gia vị cay đặc trưng, được làm từ ớt đỏ, tỏi và các nguyên liệu tự nhiên, cay đậm chuẩn vị quán.",
                    "Dùng cho món xào, nướng, lẩu, bún, phở giúp món ăn thêm cay thơm, kích thích vị giác; cũng dùng làm nước chấm hải sản, thịt nướng hoặc sốt ướp món chiên, nướng."],
 "sa-te-tom-100g": ["Sa tế tôm Acook đặc biệt chua cay, dậy mùi, đậm vị.",
                    "Dùng cho lẩu, mì, bún, xào, ướp; phù hợp làm nước chấm hoặc nêm nếm thêm hương vị cho món ăn."],
 "tuong-ot-850g": ["Tương ớt Acook cay, sánh, ngon, dùng làm nước chấm, ăn kèm bún, phở, bánh và các món chiên.",
                   "Quy cách chai 850g tiện cho quán ăn và gia đình dùng nhiều."],
 "tuong-ot-4-5kg": ["Tương ớt Acook cay, sánh, ngon trong quy cách can 4,5kg, dành cho quán ăn và bếp lớn.",
                    "Cay nóng đậm vị, dễ chan, dễ pha chế sốt chấm."],
 "tuong-xay-850g": ["Tương xay Acook sánh mịn, dễ chấm, đậm vị quen - ngon bữa cơm nhà.",
                    "Hợp cả món chay lẫn món mặn: chấm đậu hũ, rau luộc, gỏi cuốn, bún, phở."],
 "tuong-xay-4-5kg": ["Tương xay Acook sánh mịn, dễ chấm trong quy cách can 4,5kg, dành cho quán ăn và bếp lớn.",
                     "Hợp cả món chay lẫn món mặn, tiết kiệm chi phí cho nơi dùng nhiều."],
}
EXTRA_TICKS = {
 "sa-te": ["Sa tế cay: cay đậm, chuẩn vị quán  |  Sa tế tôm: chua cay, dậy mùi, đậm vị", "Làm từ ớt, tỏi và nguyên liệu tự nhiên", "Dùng cho lẩu, mì, bún, xào, ướp"],
 "tuong": ["Tương ớt: cay - sánh - ngon", "Tương xay: sánh mịn, dễ chấm", "Hợp món chay lẫn món mặn"],
}
# Hồ sơ công bố riêng
CERT_OVERRIDE = {"sa-te-cay-100g": "sa-te-cay", "sa-te-tom-100g": "sa-te-tom", "tuong-ot-850g": "tuong-ot", "tuong-ot-4-5kg": "tuong-ot",
                 "tuong-xay-850g": "tuong-xay", "tuong-xay-4-5kg": "tuong-xay"}
