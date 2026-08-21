from backend.app.modules.LyThuyetCSDL.bai_giai.bao_dong_tap_thuoc_tinh import tinh_bao_dong_tap_thuoc_tinh
from backend.app.modules.LyThuyetCSDL.bai_giai.ho_tro import loai_bo_phu_thuoc_ham_du_thua, \
    cac_thuoc_tinh_trong_khoa_ung_vien, loc_phu_thuoc_ham, tim_phu_thuoc_ham_vi_pham_dang_chuan_2, \
    tim_phu_thuoc_ham_vi_pham_dang_chuan_3, \
    gom_phu_thuoc_ham_theo_ve_trai, gom_phu_thuoc_ham_vi_pham
from backend.app.modules.LyThuyetCSDL.bai_giai.khoa_ung_vien import tim_khoa_ung_vien
from backend.app.modules.LyThuyetCSDL.utils.chuan_hoa import chuan_hoa_tap_thuoc_tinh, \
    chuan_hoa_tap_phu_thuoc_ham_sang_tuple
from backend.app.modules.LyThuyetCSDL.utils.dinh_dang import dinh_dang_phu_thuoc_ham, dinh_dang_tap_phu_thuoc_ham_tuple


# ============================================
# NÂNG DẠNG CHUẨN 2
# ============================================
def nang_dang_chuan_2(tap_thuoc_tinh, tap_phu_thuoc_ham):
    tap_phu_thuoc_ham_dang_tuple = chuan_hoa_tap_phu_thuoc_ham_sang_tuple(tap_phu_thuoc_ham)
    tap_phu_thuoc_ham_con_lai = loai_bo_phu_thuoc_ham_du_thua(tap_phu_thuoc_ham_dang_tuple)
    tap_phu_thuoc_ham_con_lai_dang_chuoi = dinh_dang_tap_phu_thuoc_ham_tuple(tap_phu_thuoc_ham_con_lai)

    khoa_ung_vien, _ = tim_khoa_ung_vien(tap_thuoc_tinh, tap_phu_thuoc_ham_con_lai_dang_chuoi)
    cac_thuoc_tinh_khoa = set(cac_thuoc_tinh_trong_khoa_ung_vien(khoa_ung_vien))

    tap_thuoc_tinh_goc = set(chuan_hoa_tap_thuoc_tinh(tap_thuoc_tinh))
    cac_thuoc_tinh_khong_khoa = tap_thuoc_tinh_goc - cac_thuoc_tinh_khoa

    danh_sach_phu_thuoc_ham_vi_pham = tim_phu_thuoc_ham_vi_pham_dang_chuan_2(
        tap_phu_thuoc_ham_con_lai_dang_chuoi,
        khoa_ung_vien
    )

    tap_thuoc_tinh_con_lai = tap_thuoc_tinh_goc.copy()
    cac_bang_duoc_tach = []
    cac_buoc_giai = []
    danh_sach_bang_da_xet = []

    dinh_dang_tap_phu_thuoc_ham_con_lai = ", ".join(
        dinh_dang_tap_phu_thuoc_ham_tuple(tap_phu_thuoc_ham_con_lai)
    )
    dinh_dang_khoa_ung_vien = ", ".join(sorted(khoa_ung_vien))

    if danh_sach_phu_thuoc_ham_vi_pham:
        dinh_dang_tap_phu_thuoc_ham_vi_pham = ", ".join(
            sorted({dinh_dang_phu_thuoc_ham(ve_trai, ve_phai)
                    for ve_trai, ve_phai, _ in danh_sach_phu_thuoc_ham_vi_pham})
        )
    else:
        dinh_dang_tap_phu_thuoc_ham_vi_pham = "Không có"

    cac_buoc_giai.append(
        f"Tập phụ thuộc hàm sau khi tách vế phải và bỏ phụ thuộc hàm dư thừa: {dinh_dang_tap_phu_thuoc_ham_con_lai}"
    )
    cac_buoc_giai.append(f"Khóa ứng viên: {dinh_dang_khoa_ung_vien}")
    cac_buoc_giai.append(f"Các thuộc tính khóa: {', '.join(sorted(cac_thuoc_tinh_khoa))}")
    cac_buoc_giai.append(
        f"Tìm các phụ thuộc hàm có thuộc tính không khóa phụ thuộc 1 phần vào khóa ứng viên: "
        f"{dinh_dang_tap_phu_thuoc_ham_vi_pham}"
    )

    # TRƯỜNG HỢP 1: Đã đạt 2NF
    if not danh_sach_phu_thuoc_ham_vi_pham:
        dinh_dang_tap_thuoc_tinh = ", ".join(sorted(tap_thuoc_tinh_con_lai))
        tap_phu_thuoc_ham_trong_bang = loc_phu_thuoc_ham(
            tap_thuoc_tinh_con_lai,
            tap_phu_thuoc_ham_con_lai_dang_chuoi
        )

        dinh_dang_phu_thuoc_ham_trong_bang = ", ".join(
            dinh_dang_tap_phu_thuoc_ham_tuple(tap_phu_thuoc_ham_trong_bang)
        )

        cac_bang_duoc_tach.append(
            f"R({dinh_dang_tap_thuoc_tinh}) với {{ {dinh_dang_phu_thuoc_ham_trong_bang} }}"
        )
        cac_buoc_giai.append(
            f"Quan hệ R({dinh_dang_tap_thuoc_tinh}) đã đạt dạng chuẩn 2."
        )

        return "\n".join(cac_bang_duoc_tach), cac_buoc_giai

    # TRƯỜNG HỢP 2: Phân rã 2NF
    danh_sach_pth_vi_pham = [
        (set(ve_trai), set(ve_phai))
        for ve_trai, ve_phai, _ in danh_sach_phu_thuoc_ham_vi_pham
    ]

    danh_sach_nhom_vi_pham = gom_phu_thuoc_ham_vi_pham(
        danh_sach_pth_vi_pham,
        tap_phu_thuoc_ham_con_lai_dang_chuoi,
        cac_thuoc_tinh_khong_khoa
    )

    cac_buoc_giai.append(
        "Gom nhóm các phụ thuộc hàm vi phạm theo vế trái "
        "và các thuộc tính được suy ra để tạo các bảng con tương ứng"
    )

    # Tách bảng cho các nhóm vi phạm 2NF
    for i, (thuoc_tinh_trong_bang_moi, danh_sach_pth) in enumerate(danh_sach_nhom_vi_pham, start=1):
        tap_thuoc_tinh_con_lai -= (thuoc_tinh_trong_bang_moi & cac_thuoc_tinh_khong_khoa)

        danh_sach_bang_da_xet.append(thuoc_tinh_trong_bang_moi)

        dinh_dang_tap_thuoc_tinh_trong_bang_moi = ", ".join(sorted(thuoc_tinh_trong_bang_moi))

        danh_sach_pth = list({
            (frozenset(ve_trai), frozenset(ve_phai))
            for ve_trai, ve_phai in danh_sach_pth
        })
        dinh_dang_tap_phu_thuoc_ham_trong_bang_moi = ", ".join(
            dinh_dang_tap_phu_thuoc_ham_tuple(danh_sach_pth)
        ) if danh_sach_pth else "không có phụ thuộc hàm nào"

        cac_bang_duoc_tach.append(
            f"R{i}({dinh_dang_tap_thuoc_tinh_trong_bang_moi}) "
            f"với {{ {dinh_dang_tap_phu_thuoc_ham_trong_bang_moi} }}"
        )

        chuoi_danh_sach_pth = ", ".join(
            sorted({dinh_dang_phu_thuoc_ham(vt, vp) for vt, vp in danh_sach_pth})
        )
        cac_buoc_giai.append(
            f"Từ {chuoi_danh_sach_pth} tạo bảng R{i}({dinh_dang_tap_thuoc_tinh_trong_bang_moi}) "
            f"do vi phạm phụ thuộc bộ phận vào khóa."
        )


    # Tạo bảng còn lại chứa khóa + thuộc tính chưa tách
    danh_sach_bang_da_xet.append(tap_thuoc_tinh_con_lai)
    dinh_dang_tap_thuoc_tinh_con_lai = ", ".join(sorted(tap_thuoc_tinh_con_lai))
    tap_phu_thuoc_ham_trong_bang_cuoi = loc_phu_thuoc_ham(
        tap_thuoc_tinh_con_lai,
        tap_phu_thuoc_ham_con_lai_dang_chuoi
    )

    so_thu_tu_bang = len(cac_bang_duoc_tach) + 1

    if tap_phu_thuoc_ham_trong_bang_cuoi:
        dinh_dang_tap_phu_thuoc_ham_trong_bang_cuoi = ", ".join(
            dinh_dang_tap_phu_thuoc_ham_tuple(tap_phu_thuoc_ham_trong_bang_cuoi)
        )
        cac_bang_duoc_tach.append(
            f"R{so_thu_tu_bang}({dinh_dang_tap_thuoc_tinh_con_lai}) "
            f"với {{ {dinh_dang_tap_phu_thuoc_ham_trong_bang_cuoi} }}"
        )
    else:
        cac_bang_duoc_tach.append(
            f"R{so_thu_tu_bang}({dinh_dang_tap_thuoc_tinh_con_lai}) "
            f"không có phụ thuộc hàm nào"
        )

    cac_buoc_giai.append(
        f"Còn lại R{so_thu_tu_bang}({dinh_dang_tap_thuoc_tinh_con_lai}) "
        f"chứa khóa ứng viên {dinh_dang_khoa_ung_vien} "
        f"và các thuộc tính còn lại."
    )

    # Kiểm tra phụ thuộc hàm nào chưa có
    pth_chua_co = []
    for ve_trai, ve_phai in tap_phu_thuoc_ham_con_lai:
        tap_phu_thuoc = set(ve_trai) | set(ve_phai)
        # Kiểm tra xem có bảng nào chứa trọn vẹn cả vế trái và vế phải không
        da_co = any(tap_phu_thuoc.issubset(bang) for bang in danh_sach_bang_da_xet)

        if not da_co:
            pth_chua_co.append((set(ve_trai), set(ve_phai)))

    if pth_chua_co:
        for vt_pth, vp_pth in pth_chua_co:
            so_thu_tu_bang += 1
            tap_pth_moi = vt_pth | vp_pth
            danh_sach_bang_da_xet.append(tap_pth_moi)

            dinh_dang_tap_thuoc_tinh_moi = ", ".join(sorted(tap_pth_moi))
            dinh_dang_pth = dinh_dang_phu_thuoc_ham(vt_pth, vp_pth)

            cac_bang_duoc_tach.append(
                f"R{so_thu_tu_bang}({dinh_dang_tap_thuoc_tinh_moi}) với {{ {dinh_dang_pth} }}"
            )
            cac_buoc_giai.append(
                f"Tạo thêm bảng R{so_thu_tu_bang}({dinh_dang_tap_thuoc_tinh_moi}) "
                f"để bảo toàn phụ thuộc hàm {dinh_dang_pth}."
            )

    return "\n".join(cac_bang_duoc_tach), cac_buoc_giai


# ========================================
# NÂNG DẠNG CHUẨN 3
# ========================================
def nang_dang_chuan_3(tap_thuoc_tinh, tap_phu_thuoc_ham):
    tap_phu_thuoc_ham_dang_tuple = chuan_hoa_tap_phu_thuoc_ham_sang_tuple(tap_phu_thuoc_ham)
    tap_phu_thuoc_ham_con_lai = loai_bo_phu_thuoc_ham_du_thua(tap_phu_thuoc_ham_dang_tuple)
    tap_phu_thuoc_ham_con_lai_dang_chuoi = dinh_dang_tap_phu_thuoc_ham_tuple(tap_phu_thuoc_ham_con_lai)

    khoa_ung_vien, _ = tim_khoa_ung_vien(
        tap_thuoc_tinh, tap_phu_thuoc_ham_con_lai_dang_chuoi
    )
    cac_thuoc_tinh_khoa = set(cac_thuoc_tinh_trong_khoa_ung_vien(khoa_ung_vien))

    tap_thuoc_tinh_goc = set(chuan_hoa_tap_thuoc_tinh(tap_thuoc_tinh))

    danh_sach_phu_thuoc_ham_vi_pham = tim_phu_thuoc_ham_vi_pham_dang_chuan_3(
        tap_thuoc_tinh,
        tap_phu_thuoc_ham_con_lai_dang_chuoi,
        khoa_ung_vien,
    )

    cac_bang_duoc_tach = []
    cac_buoc_giai = []

    dinh_dang_tap_phu_thuoc_ham_con_lai = ", ".join(
        dinh_dang_tap_phu_thuoc_ham_tuple(tap_phu_thuoc_ham_con_lai)
    )

    cac_buoc_giai.append(
        f"Tách vế phải và bỏ phụ thuộc hàm dư thừa: {dinh_dang_tap_phu_thuoc_ham_con_lai}"
    )
    cac_buoc_giai.append(f"Khóa ứng viên: {', '.join(sorted(khoa_ung_vien))}")
    cac_buoc_giai.append(f"Tập thuộc tính khóa: {{ {', '.join(sorted(cac_thuoc_tinh_khoa))} }}")

    # TRƯỜNG HỢP 1: Đã đạt 3NF
    if not danh_sach_phu_thuoc_ham_vi_pham:
        dinh_dang_tap_thuoc_tinh = ", ".join(sorted(tap_thuoc_tinh_goc))
        tap_pth_trong_bang = loc_phu_thuoc_ham(
            tap_thuoc_tinh_goc, tap_phu_thuoc_ham_con_lai_dang_chuoi
        )

        dinh_dang_tap_pth = (
            ", ".join(dinh_dang_tap_phu_thuoc_ham_tuple(tap_pth_trong_bang))
            if tap_pth_trong_bang else "không có phụ thuộc hàm nào"
        )

        cac_bang_duoc_tach.append(f"R({dinh_dang_tap_thuoc_tinh}) với {{ {dinh_dang_tap_pth} }}")
        cac_buoc_giai.append(f"Quan hệ R({dinh_dang_tap_thuoc_tinh}) đã đạt dạng chuẩn 3.")

        return "\n".join(cac_bang_duoc_tach), cac_buoc_giai


    # TRƯỜNG HỢP 2: Phân rã 3NF
    dinh_dang_tap_phu_thuoc_ham_vi_pham = ", ".join(
        dinh_dang_phu_thuoc_ham(ve_trai, ve_phai)
        for ve_trai, ve_phai in danh_sach_phu_thuoc_ham_vi_pham
    )

    cac_buoc_giai.append(
        f"Tìm các phụ thuộc hàm có vế trái không phải siêu khóa "
        f"và vế phải không phải thuộc tính khóa: {dinh_dang_tap_phu_thuoc_ham_vi_pham}"
    )

    # 1. Gom nhóm tất cả PTH trong F_c theo vế trái để tạo các bảng con
    nhom_theo_ve_trai = gom_phu_thuoc_ham_theo_ve_trai(tap_phu_thuoc_ham_con_lai)

    danh_sach_bang_tam = []
    for ve_trai, danh_sach_pth in nhom_theo_ve_trai:
        tap_tt_bang = set(ve_trai)
        for _, ve_phai in danh_sach_pth:
            tap_tt_bang.update(ve_phai)

        danh_sach_bang_tam.append(tap_tt_bang)


    # 2. Loại bỏ các bảng bị bao hàm hoàn toàn
    danh_sach_bang = []
    for i, tap_thuoc_tinh_1 in enumerate(danh_sach_bang_tam):
        la_bang_con = False
        for j, tap_thuoc_tinh_2 in enumerate(danh_sach_bang_tam):
            if i != j and tap_thuoc_tinh_1 < tap_thuoc_tinh_2:
                la_bang_con = True
                break
            elif i != j and tap_thuoc_tinh_1 == tap_thuoc_tinh_2 and i > j:
                la_bang_con = True
                break
        if not la_bang_con:
            danh_sach_bang.append(tap_thuoc_tinh_1)

    # Kiểm tra xem có bảng nào chứa khóa chưa
    danh_sach_khoa = [set(kv) for kv in khoa_ung_vien]

    da_chua_khoa = False
    for bang_tt in danh_sach_bang:
        for tap_khoa in danh_sach_khoa:
            if tap_khoa.issubset(bang_tt):
                da_chua_khoa = True
                break
        if da_chua_khoa:
            break

    if not da_chua_khoa and danh_sach_khoa:
        tap_khoa_chon = danh_sach_khoa[0]
        danh_sach_bang.append(tap_khoa_chon)
        cac_buoc_giai.append(
            f"Tạo thêm bảng chứa khóa ứng viên {''.join(sorted(tap_khoa_chon))} để bảo toàn thông tin."
        )

    # 4. Xuất kết quả các bảng con
    for i, tap_tt_bang in enumerate(danh_sach_bang, start=1):
        dinh_dang_thuoc_tinh_bang = ", ".join(sorted(tap_tt_bang))
        tap_pth_trong_bang = loc_phu_thuoc_ham(
            tap_tt_bang, tap_phu_thuoc_ham_con_lai_dang_chuoi
        )

        if tap_pth_trong_bang:
            dinh_dang_pth_bang = (
                ", ".join(dinh_dang_tap_phu_thuoc_ham_tuple(tap_pth_trong_bang))
            )

            cac_bang_duoc_tach.append(
                f"R{i}({dinh_dang_thuoc_tinh_bang}) với {{ {dinh_dang_pth_bang} }}"
            )
            cac_buoc_giai.append(
                f"Tạo bảng R{i}({dinh_dang_thuoc_tinh_bang}) với các phụ thuộc hàm {{ {dinh_dang_pth_bang} }}"
            )
        else:
            cac_bang_duoc_tach.append(
                f"R{i}({dinh_dang_thuoc_tinh_bang}) không có phụ thuộc hàm nào"
            )
            cac_buoc_giai.append(
                f"Tạo bảng R{i}({dinh_dang_thuoc_tinh_bang}) không có phụ thuộc hàm nào"
            )

    return "\n".join(cac_bang_duoc_tach), cac_buoc_giai

# ========================================
# NÂNG DẠNG CHUẨN BOYCE-CODD
# ========================================
def nang_dang_chuan_bcnf(tap_thuoc_tinh, tap_phu_thuoc_ham):
    tap_thuoc_tinh_goc = set(chuan_hoa_tap_thuoc_tinh(tap_thuoc_tinh))
    tap_pth_tuple = chuan_hoa_tap_phu_thuoc_ham_sang_tuple(tap_phu_thuoc_ham)
    tap_pth_toi_thieu = loai_bo_phu_thuoc_ham_du_thua(tap_pth_tuple)
    tap_pth_dang_chuoi = dinh_dang_tap_phu_thuoc_ham_tuple(tap_pth_toi_thieu)

    khoa_ung_vien, _ = tim_khoa_ung_vien(tap_thuoc_tinh_goc, tap_pth_dang_chuoi)

    cac_buoc_giai = [f"Khóa ứng viên ban đầu: {', '.join(sorted(khoa_ung_vien))}"]
    quan_he_can_xet = [tap_thuoc_tinh_goc]
    cac_bang_bcnf_ket_qua = []

    while quan_he_can_xet:
        tap_thuoc_tinh_hien_tai = set(quan_he_can_xet.pop(0))

        # 1. Tính chiếu PTH lên quan hệ hiện tại (Sửa lại ở đây)
        tap_pth_hien_tai = loc_phu_thuoc_ham(tap_thuoc_tinh_hien_tai, tap_pth_dang_chuoi)
        tap_pth_hien_tai_dang_chuoi = dinh_dang_tap_phu_thuoc_ham_tuple(tap_pth_hien_tai)

        khoa_ung_vien_hien_tai, _ = tim_khoa_ung_vien(
            tap_thuoc_tinh_hien_tai, tap_pth_hien_tai_dang_chuoi
        )

        cac_nhom_phu_thuoc_ham = gom_phu_thuoc_ham_theo_ve_trai(tap_pth_hien_tai)
        cac_nhom_vi_pham = []

        # 2. Kiểm tra điều kiện BCNF
        for ve_trai, danh_sach_pth in cac_nhom_phu_thuoc_ham:
            ve_trai_set = set(ve_trai)
            la_sieu_khoa = False
            for khoa in khoa_ung_vien_hien_tai:
                khoa_set = set(khoa)
                if khoa_set.issubset(ve_trai_set):
                    la_sieu_khoa = True
                    break

            if not la_sieu_khoa:
                cac_nhom_vi_pham.append((ve_trai_set, danh_sach_pth))

        if not cac_nhom_vi_pham:
            cac_bang_bcnf_ket_qua.append((tap_thuoc_tinh_hien_tai, tap_pth_hien_tai))
            continue

        # 3. Chọn phụ thuộc hàm vi phạm đầu tiên để tách
        ve_trai_vi_pham, danh_sach_pth_vi_pham = cac_nhom_vi_pham[0]

        bao_dong, _ = tinh_bao_dong_tap_thuoc_tinh(
            ve_trai_vi_pham, tap_pth_hien_tai_dang_chuoi
        )
        bao_dong_trong_quan_he = set(bao_dong) & tap_thuoc_tinh_hien_tai

        bang1 = bao_dong_trong_quan_he
        bang2 = (tap_thuoc_tinh_hien_tai - bang1) | ve_trai_vi_pham

        bang_dang_xet_dang_chuoi = ", ".join(sorted(tap_thuoc_tinh_hien_tai))
        str_pth_vi_pham = ", ".join(
            sorted(dinh_dang_phu_thuoc_ham(vt, vp) for vt, vp in danh_sach_pth_vi_pham)
        )
        bang1_dang_chuoi = ", ".join(sorted(bang1))
        bang2_dang_chuoi = ", ".join(sorted(bang2))

        cac_buoc_giai.append(
            f"Quan hệ R({bang_dang_xet_dang_chuoi}) vi phạm BCNF do {str_pth_vi_pham} "
            f"(vế trái {', '.join(sorted(ve_trai_vi_pham))} không phải siêu khóa)."
        )
        cac_buoc_giai.append(
            f"Tách R({bang_dang_xet_dang_chuoi}) thành R'({bang1_dang_chuoi}) và R''({bang2_dang_chuoi})."
        )

        if bang1 != tap_thuoc_tinh_hien_tai and bang1 not in quan_he_can_xet:
            quan_he_can_xet.append(bang1)
        if bang2 != tap_thuoc_tinh_hien_tai and bang2 not in quan_he_can_xet:
            quan_he_can_xet.append(bang2)

    # 4. Loại bỏ các bảng bị bao hàm hoàn toàn (R_i ⊂ R_j)
    danh_sach_bang = []
    for i, (tt_i, pth_i) in enumerate(cac_bang_bcnf_ket_qua):
        la_con = False
        for j, (tt_j, _) in enumerate(cac_bang_bcnf_ket_qua):
            if i != j and tt_i < tt_j:
                la_con = True
                break
            elif i != j and tt_i == tt_j and i > j:
                la_con = True
                break
        if not la_con:
            danh_sach_bang.append((tt_i, pth_i))

    # 5. Định dạng đầu ra cuối cùng (Lấy pth_i được lưu từ lúc phân rã, không dùng tap_pth_dang_chuoi nữa)
    cac_bang_duoc_tach = []
    for i, (tap_tt, tap_pth_trong_bang) in enumerate(danh_sach_bang, start=1):
        tap_tt_trong_bang = ", ".join(sorted(tap_tt))

        if tap_pth_trong_bang:
            str_pth = ", ".join(dinh_dang_tap_phu_thuoc_ham_tuple(tap_pth_trong_bang))
            cac_bang_duoc_tach.append(f"R{i}({tap_tt_trong_bang}) với {{ {str_pth} }}")
        else:
            cac_bang_duoc_tach.append(
                f"R{i}({tap_tt_trong_bang}) với không có phụ thuộc hàm nào"
            )

    return "\n".join(cac_bang_duoc_tach), cac_buoc_giai


if __name__ == '__main__':
    # Test dạng chuẩn 2
    # tap_thuoc_tinh = [
    #     ["A", "B", "C", "D"],  # Bài 11
    #     ["A", "B", "C", "D"],  # Bài 12
    #     ["A", "B", "C", "D", "E"],  # Bài 13
    #     ["A", "B", "C", "D", "E"],  # Bài 14
    #     ["A", "B", "C", "D", "E", "F"],  # Bài 15
    #     ["A", "B", "C", "D", "E"],  # Bài 16
    #     ["A", "B", "C", "D", "E", "F"],  # Bài 17
    #     ["A", "B", "C", "D", "E"],  # Bài 18
    #     ["A", "B", "C", "D", "E", "F"],  # Bài 19
    #     ["A", "B", "C", "D", "E", "F"]  # Bài 20
    # ]
    #
    # tap_phu_thuoc_ham = [
    #     # Bài 11: AB → C, B → D, AB → D (Dư thừa AB → D)
    #     ["AB → C", "B → D", "AB → D"],
    #
    #     # Bài 12: A → B, B → C, C → D, A → C (Dư thừa A → C)
    #     ["A → B", "B → C", "C → D", "A → C"],
    #
    #     # Bài 13: AB → C, A → D, D → E, B → C (B → C làm dư thừa AB → C)
    #     ["AB → C", "A → D", "D → E", "B → C"],
    #
    #     # Bài 14: AB → C, C → D, D → A, B → E (Nhiều khóa, kiểm tra thuộc tính khóa)
    #     ["AB → C", "C → D", "D → A", "B → E"],
    #
    #     # Bài 15: A → BC, B → C, D → E, A → C (Tách vế phải + lọc dư thừa)
    #     ["A → B", "A → C", "B → C", "D → E"],
    #
    #     # Bài 16: AB → CD, A → C, B → D (Tách vế phải, cả 2 vế trái đều vi phạm 2NF)
    #     ["AB → C", "AB → D", "A → C", "B → D"],
    #
    #     # Bài 17: AB → C, C → D, DE → F, B → D (Dư thừa B → D qua C)
    #     ["AB → C", "C → D", "DE → F", "B → D"],
    #
    #     # Bài 18: AB → C, B → D, D → E, A → E (Vi phạm 2NF từ B → D)
    #     ["AB → C", "B → D", "D → E", "A → E"],
    #
    #     # Bài 19: ABC → D, A → D, B → E, E → F (ABC → D bị thừa vế trái BC)
    #     ["ABC → D", "A → D", "B → E", "E → F"],
    #
    #     # Bài 20: AB → C, C → B, A → D, D → E, E → F, A → E (Dư thừa A → E)
    #     ["AB → C", "C → B", "A → D", "D → E", "E → F", "A → E"]
    # ]

    # test dạng chuẩn 3
    # tap_thuoc_tinh = [
    #     ["A", "B", "C"],
    #     ["A", "B", "C"],
    #     ["A", "B", "C"],
    #     ["A", "B", "C", "D"],
    #     ["A", "B", "C", "D", "E"],
    #     ["A", "B", "C", "D"],
    #     ["A", "B", "C", "D", "E"],
    #     ["A", "B", "C", "D"],
    #     ["A", "B", "C", "D", "E", "F"],
    #     ["A", "B", "C", "D", "E", "F", "G"]
    # ]
    #
    # tap_phu_thuoc_ham = [
    #     ["A → B", "B → C"],
    #     ["AB → C"],
    #     ["A → B", "B → A", "A → C"],
    #     ["A → B", "B → C", "C → D"],
    #     ["A → B", "A → C", "B → D", "C → E"],
    #     ["A → B", "B → A", "A → C", "B → D"],
    #     ["A → B", "B → A", "A → C", "B → D", "C → E"],
    #     ["A → B", "B → C", "C → A", "A → D"],
    #     ["AB → C", "C → D", "D → E", "AB → F"],
    #     ["AB → C", "AC → B", "A → D", "B → E", "C → F", "D → G"]
    # ]

    # test dạng chuẩn boyce-codd
    tap_thuoc_tinh = [
        ["A", "B", "C", "D"],
        ["A", "B", "C", "D"],
        ["A", "B", "C", "D", "E"],
        ["A", "B", "C"],
        ["A", "B", "C", "D"],
        ["A", "B", "C", "D", "E"],
        ["A", "B", "C", "D"],
        ["A", "B", "C", "D", "E"],
        ["A", "B", "C", "D"],
        ["A", "B", "C", "D", "E", "F"]
    ]

    tap_phu_thuoc_ham = [
        ["A → B", "B → C", "B → D"],
        ["AB → C", "C → D", "D → A"],
        ["A → B", "BC → D", "D → E"],
        ["A → B", "A → C", "B → C"],
        ["AB → C", "AB → D"],
        ["A → B", "A → C", "C → D", "D → E"],
        ["A → B", "B → C", "A → D"],
        ["AB → C", "C → D", "C → E", "E → A"],
        ["A → B", "C → D"],
        ["A → B", "A → C", "D → E", "D → F"]
    ]

    i = 1
    for ttt, tpth in zip(tap_thuoc_tinh, tap_phu_thuoc_ham):
        print(f"Bài {i}")
        i += 1
        print(f"Tập thuộc tính R = {{ {", ".join(ttt)} }}")
        print(f"Tập phụ thuộc hàm F = {{ {", ".join(tpth)} }}")

        result, steps = nang_dang_chuan_bcnf(ttt, tpth)
        print(result)
        for step in steps:
            print(step)

        print("-"*50)


