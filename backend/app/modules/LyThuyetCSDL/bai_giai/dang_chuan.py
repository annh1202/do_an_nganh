from backend.app.modules.LyThuyetCSDL.bai_giai.bao_dong_tap_thuoc_tinh import tinh_bao_dong_tap_thuoc_tinh
from backend.app.modules.LyThuyetCSDL.bai_giai.ho_tro import loai_bo_phu_thuoc_ham_du_thua
from backend.app.modules.LyThuyetCSDL.bai_giai.khoa_ung_vien import tim_khoa_ung_vien
from backend.app.modules.LyThuyetCSDL.utils.chuan_hoa import chuan_hoa_tap_thuoc_tinh, \
    chuan_hoa_tap_phu_thuoc_ham_sang_tuple
from backend.app.modules.LyThuyetCSDL.utils.dinh_dang import dinh_dang_tap_thuoc_tinh, dinh_dang_chuoi_tap_thuoc_tinh, \
    dinh_dang_phu_thuoc_ham, dinh_dang_tap_phu_thuoc_ham_tuple


# ============================================
# CÁC HÀM HỖ TRỢ
# ============================================
def co_phai_sieu_khoa(tap_thuoc_tinh_can_tim, tap_thuoc_tinh, tap_phu_thuoc_ham):
    bao_dong, _ = tinh_bao_dong_tap_thuoc_tinh(tap_thuoc_tinh_can_tim, tap_phu_thuoc_ham)

    return bao_dong == chuan_hoa_tap_thuoc_tinh(tap_thuoc_tinh)


def cac_thuoc_tinh_trong_khoa_ung_vien(cac_khoa_ung_vien):
    cac_thuoc_tinh_trong_khoa_ung_vien = set()

    for khoa in cac_khoa_ung_vien:
        cac_thuoc_tinh_trong_khoa_ung_vien.update(set(khoa))

    return cac_thuoc_tinh_trong_khoa_ung_vien


def loc_phu_thuoc_ham(tap_thuoc_tinh, tap_phu_thuoc_ham):
    tap_thuoc_tinh = chuan_hoa_tap_thuoc_tinh(tap_thuoc_tinh)
    danh_sach_pth = chuan_hoa_tap_phu_thuoc_ham_sang_tuple(tap_phu_thuoc_ham)

    phu_thuoc_ham_duoc_loc_lai = []

    for ve_trai, ve_phai in danh_sach_pth:
        # 1. Vế trái phải nằm hoàn toàn trong tập thuộc tính
        if not ve_trai.issubset(tap_thuoc_tinh):
            continue

        # 2. Bỏ các thuộc tính ở vế phải không nằm trong tập thuộc tính
        giao = ve_phai & tap_thuoc_tinh

        # 3. Bỏ các thuộc tính ở vế phải đã có ở vế trái
        ve_phai_moi = giao - ve_trai

        if ve_phai_moi:
            phu_thuoc_ham_duoc_loc_lai.append((ve_trai, ve_phai_moi))

    return phu_thuoc_ham_duoc_loc_lai


def tim_khoa_co_phu_thuoc_bo_phan(ve_trai, ve_phai, danh_sach_khoa_ung_vien, tap_thuoc_tinh_khoa):
    ve_trai = chuan_hoa_tap_thuoc_tinh(ve_trai)

    if ve_phai in tap_thuoc_tinh_khoa:
        return None

    for khoa in danh_sach_khoa_ung_vien:
        cac_thuoc_tinh_trong_khoa = set(khoa)

        if ve_trai < cac_thuoc_tinh_trong_khoa:
            return khoa

    return None


# ============================================
# NÂNG DẠNG CHUẨN 2
# ============================================
def tim_phu_thuoc_ham_vi_pham_dang_chuan_2(tap_phu_thuoc_ham, cac_khoa_ung_vien):
    danh_sach_vi_pham = []

    cac_thuoc_tinh_khoa = (
        cac_thuoc_tinh_trong_khoa_ung_vien(
            cac_khoa_ung_vien
        )
    )

    danh_sach_phu_thuoc_ham = (
        chuan_hoa_tap_phu_thuoc_ham_sang_tuple(
            tap_phu_thuoc_ham
        )
    )

    for ve_trai, ve_phai in danh_sach_phu_thuoc_ham:

        for thuoc_tinh in ve_phai:

            if thuoc_tinh in cac_thuoc_tinh_khoa:
                continue

            khoa_vi_pham = tim_khoa_co_phu_thuoc_bo_phan(
                ve_trai,
                thuoc_tinh,
                cac_khoa_ung_vien,
                cac_thuoc_tinh_khoa
            )

            if khoa_vi_pham is not None:
                danh_sach_vi_pham.append({
                    "ve_trai": ve_trai,
                    "ve_phai": thuoc_tinh,
                    "khoa": khoa_vi_pham
                })

    return danh_sach_vi_pham


def nang_dang_chuan_2(tap_thuoc_tinh, tap_phu_thuoc_ham):
    tap_phu_thuoc_ham_dang_tuple = chuan_hoa_tap_phu_thuoc_ham_sang_tuple(tap_phu_thuoc_ham)
    tap_phu_thuoc_ham_con_lai = loai_bo_phu_thuoc_ham_du_thua(tap_phu_thuoc_ham_dang_tuple)
    tap_phu_thuoc_ham_con_lai_dang_chuoi = dinh_dang_tap_phu_thuoc_ham_tuple(tap_phu_thuoc_ham_con_lai)

    khoa_ung_vien, _ = tim_khoa_ung_vien(tap_thuoc_tinh, tap_phu_thuoc_ham_con_lai_dang_chuoi)

    danh_sach_vi_pham = (
        tim_phu_thuoc_ham_vi_pham_dang_chuan_2(
            tap_phu_thuoc_ham_con_lai_dang_chuoi,
            khoa_ung_vien
        )
    )

    # Các thuộc tính nằm trong khóa ứng viên
    cac_thuoc_tinh_khoa = cac_thuoc_tinh_trong_khoa_ung_vien(khoa_ung_vien)

    # Gom các phụ thuộc bộ phận có cùng vế trái
    cac_nhom_phu_thuoc_ham_vi_pham = {}

    for vi_pham in danh_sach_vi_pham:
        ve_trai = frozenset(chuan_hoa_tap_thuoc_tinh(vi_pham["ve_trai"]))
        ve_phai = chuan_hoa_tap_thuoc_tinh(vi_pham["ve_phai"])

        khoa_vi_pham = frozenset(chuan_hoa_tap_thuoc_tinh(vi_pham["khoa"]))

        if ve_trai not in cac_nhom_phu_thuoc_ham_vi_pham:
            cac_nhom_phu_thuoc_ham_vi_pham[ve_trai] = {
                "ve_phai": set(),
                "cac_khoa": set()
            }

        cac_nhom_phu_thuoc_ham_vi_pham[ve_trai]["ve_phai"].update(ve_phai)
        cac_nhom_phu_thuoc_ham_vi_pham[ve_trai]["cac_khoa"].add(khoa_vi_pham)

    tap_thuoc_tinh_con_lai = chuan_hoa_tap_thuoc_tinh(tap_thuoc_tinh)

    cac_bang_duoc_tach = []
    cac_buoc_giai = []

    cac_buoc_giai.append(f"Khóa ứng viên: {", ".join(khoa_ung_vien)}")

    # Tách từng nhóm phụ thuộc bộ phận
    for i, (ve_trai, thong_tin) in enumerate(cac_nhom_phu_thuoc_ham_vi_pham.items(), bat_dau=1):
        bao_dong, _ = tinh_bao_dong_tap_thuoc_tinh(
            set(ve_trai), tap_phu_thuoc_ham_con_lai_dang_chuoi
        )

        bao_dong = set(bao_dong)

        cac_thuoc_tinh_khong_nam_trong_khoa = bao_dong - cac_thuoc_tinh_khoa

        tap_thuoc_tinh_con_lai -= cac_thuoc_tinh_khong_nam_trong_khoa

        tap_thuoc_tinh_trong_bang_moi = set(ve_trai) | cac_thuoc_tinh_khong_nam_trong_khoa

        dinh_dang_tap_thuoc_tinh_trong_bang_moi = ", ".join(sorted(tap_thuoc_tinh_trong_bang_moi))

        tap_phu_thuoc_ham_trong_bang_moi = (
            loc_phu_thuoc_ham(
                tap_thuoc_tinh_trong_bang_moi,
                tap_phu_thuoc_ham_con_lai_dang_chuoi
            )
        )

        if tap_phu_thuoc_ham_trong_bang_moi:
            dinh_dang_tap_phu_thuoc_ham_trong_bang_moi = (
                ", ".join(
                    dinh_dang_phu_thuoc_ham(ve_trai_pth, ve_phai_pth)
                    for ve_trai_pth, ve_phai_pth in tap_phu_thuoc_ham_trong_bang_moi
                )
            )
        else:
            dinh_dang_tap_phu_thuoc_ham_trong_bang_moi = "không có phụ thuộc hàm nào"



        cac_bang_duoc_tach.append(
            f"R{i}({dinh_dang_tap_thuoc_tinh_trong_bang_moi}) "
            f"với {{ {dinh_dang_tap_phu_thuoc_ham_trong_bang_moi} }}"
        )

        # Các PTH vi phạm trong nhóm
        cac_pth_vi_pham = ", ".join(
            sorted(dinh_dang_phu_thuoc_ham(ve_trai, {thuoc_tinh})
                for thuoc_tinh in thong_tin["ve_phai"]
            )
        )

        # Các khóa gây ra phụ thuộc bộ phận
        cac_khoa_vi_pham = ", ".join(
            sorted("".join(sorted(khoa))
                for khoa in thong_tin["cac_khoa"]
            )
        )

        cac_buoc_giai.append(
            f"Tách R{i}({dinh_dang_tap_thuoc_tinh_trong_bang_moi}) "
            f"vì {cac_pth_vi_pham} là phụ thuộc bộ phận với khóa {cac_khoa_vi_pham}."
        )

    # Tạo bảng còn lại
    dinh_dang_tap_thuoc_tinh_trong_bang_cuoi = ", ".join(sorted(tap_thuoc_tinh_con_lai))

    tap_phu_thuoc_ham_trong_bang_cuoi = (
        loc_phu_thuoc_ham(tap_thuoc_tinh_con_lai, tap_phu_thuoc_ham_con_lai_dang_chuoi
        )
    )

    if tap_phu_thuoc_ham_trong_bang_cuoi:
        dinh_dang_tap_phu_thuoc_ham_trong_bang_cuoi = (
            ", ".join(
                dinh_dang_phu_thuoc_ham(ve_trai, ve_phai
                )
                for ve_trai, ve_phai in tap_phu_thuoc_ham_trong_bang_cuoi
            )
        )
    else:
        dinh_dang_tap_phu_thuoc_ham_trong_bang_cuoi = "không có phụ thuộc hàm nào"

    so_thu_tu_bang_cuoi = len(cac_bang_duoc_tach) + 1

    cac_bang_duoc_tach.append(
        f"R{so_thu_tu_bang_cuoi}({dinh_dang_tap_thuoc_tinh_trong_bang_cuoi}) "
        f"với {{ {dinh_dang_tap_phu_thuoc_ham_trong_bang_cuoi} }}"
    )

    cac_buoc_giai.append(
        f"Còn lại R{so_thu_tu_bang_cuoi}({dinh_dang_tap_thuoc_tinh_trong_bang_cuoi}) "
        f"là các thuộc tính còn lại và trong khóa ứng viên."
    )

    return "\n".join(cac_bang_duoc_tach), cac_buoc_giai

# ========================================
# NÂNG DẠNG CHUẨN 3
# ========================================
def tim_phu_thuoc_ham_vong(tap_phu_thuoc_ham):
    cac_tap_thuoc_tinh_trong_phu_thuoc_ham_vong = []
    phu_thuoc_ham_vong = {}

    for ve_trai, ve_phai in tap_phu_thuoc_ham:
        tap_phu_thuoc_ham_tam = []

        tap_thuoc_tinh_bat_dau = ve_trai
        tap_thuoc_tinh_dang_xet = ve_phai

        tap_phu_thuoc_ham_tam.append((tap_thuoc_tinh_bat_dau, tap_thuoc_tinh_dang_xet))

        for ve_trai_moi, ve_phai_moi in tap_phu_thuoc_ham:
            if tap_thuoc_tinh_dang_xet == ve_trai_moi:
                tap_thuoc_tinh_dang_xet = ve_phai_moi

                tap_phu_thuoc_ham_tam.append((ve_trai_moi, ve_phai_moi))

        if tap_thuoc_tinh_dang_xet == tap_thuoc_tinh_bat_dau:

            # 1. Gom các thuộc tính của chu trình
            tap_thuoc_tinh_trong_phu_thuoc_ham_vong = set()

            for ve_trai_moi, ve_phai_moi in tap_phu_thuoc_ham_tam:
                tap_thuoc_tinh_trong_phu_thuoc_ham_vong.update(ve_trai_moi)
                tap_thuoc_tinh_trong_phu_thuoc_ham_vong.update(ve_phai_moi)

            if len(tap_thuoc_tinh_trong_phu_thuoc_ham_vong) > 0:
                khoa_nhom = tuple(sorted(list(tap_thuoc_tinh_trong_phu_thuoc_ham_vong)))

                # 2. Nếu nhóm chưa tồn tại thì lưu lại
                #    cả nhóm thuộc tính và các PTH tạo nên nhóm
                if (
                    tap_thuoc_tinh_trong_phu_thuoc_ham_vong
                    not in cac_tap_thuoc_tinh_trong_phu_thuoc_ham_vong
                ):
                    cac_tap_thuoc_tinh_trong_phu_thuoc_ham_vong.append(
                        tap_thuoc_tinh_trong_phu_thuoc_ham_vong
                    )

                    phu_thuoc_ham_vong[khoa_nhom] = tap_phu_thuoc_ham_tam


    return cac_tap_thuoc_tinh_trong_phu_thuoc_ham_vong, phu_thuoc_ham_vong


def tim_phu_thuoc_ham_vi_pham_dang_chuan_3(tap_thuoc_tinh, tap_phu_thuoc_ham, cac_khoa_ung_vien):
    danh_sach_vi_pham = []

    cac_thuoc_tinh_khoa = cac_thuoc_tinh_trong_khoa_ung_vien(cac_khoa_ung_vien)

    danh_sach_phu_thuoc_ham = chuan_hoa_tap_phu_thuoc_ham_sang_tuple(tap_phu_thuoc_ham)

    for ve_trai, ve_phai in danh_sach_phu_thuoc_ham:

        # Kiểm tra vế trái có phải siêu khóa hay không
        la_sieu_khoa = co_phai_sieu_khoa(ve_trai, tap_thuoc_tinh, tap_phu_thuoc_ham)

        # Nếu vế trái là siêu khóa thì PTH không vi phạm 3NF
        if la_sieu_khoa:
            continue

        for thuoc_tinh in ve_phai:

            # Thuộc tính khóa ở vế phải → không vi phạm 3NF
            if thuoc_tinh in cac_thuoc_tinh_khoa:
                continue

            danh_sach_vi_pham.append({
                "ve_trai": ve_trai,
                "ve_phai": thuoc_tinh
            })

    return danh_sach_vi_pham


def nang_dang_chuan_3(
    tap_thuoc_tinh,
    tap_phu_thuoc_ham
):
    # =========================================================
    # 1. Chuẩn hóa PTH
    # =========================================================

    tap_phu_thuoc_ham_dang_tuple = (
        chuan_hoa_tap_phu_thuoc_ham_sang_tuple(
            tap_phu_thuoc_ham
        )
    )

    # =========================================================
    # 2. Loại bỏ PTH dư thừa
    # =========================================================

    tap_phu_thuoc_ham_con_lai = (
        loai_bo_phu_thuoc_ham_du_thua(
            tap_phu_thuoc_ham_dang_tuple
        )
    )

    tap_phu_thuoc_ham_con_lai_dang_chuoi = (
        dinh_dang_tap_phu_thuoc_ham_tuple(
            tap_phu_thuoc_ham_con_lai
        )
    )

    # =========================================================
    # 3. Tìm khóa ứng viên
    # =========================================================

    khoa_ung_vien, _ = tim_khoa_ung_vien(
        tap_thuoc_tinh,
        tap_phu_thuoc_ham_con_lai_dang_chuoi
    )

    # =========================================================
    # 4. Tìm PTH vi phạm 3NF
    # =========================================================

    danh_sach_vi_pham = (
        tim_phu_thuoc_ham_vi_pham_dang_chuan_3(
            tap_thuoc_tinh,
            tap_phu_thuoc_ham_con_lai_dang_chuoi,
            khoa_ung_vien
        )
    )

    # =========================================================
    # 5. Tìm PTH vòng
    # =========================================================

    cac_tap_thuoc_tinh_vong, phu_thuoc_ham_vong = (
        tim_phu_thuoc_ham_vong(
            tap_phu_thuoc_ham_con_lai
        )
    )

    # =========================================================
    # 6. Các thuộc tính khóa
    # =========================================================

    cac_thuoc_tinh_khoa = (
        cac_thuoc_tinh_trong_khoa_ung_vien(
            khoa_ung_vien
        )
    )

    # =========================================================
    # 7. Gom các PTH vi phạm theo cùng vế trái
    # =========================================================
    #
    # Ví dụ:
    #
    # C → B
    # C → D
    #
    # sẽ gom thành:
    #
    # C → {B, D}
    #
    # để chỉ tạo một quan hệ R(C, B, D).
    # =========================================================

    cac_vi_pham_theo_ve_trai = {}

    for vi_pham in danh_sach_vi_pham:

        ve_trai = frozenset(
            chuan_hoa_tap_thuoc_tinh(
                vi_pham["ve_trai"]
            )
        )

        ve_phai = chuan_hoa_tap_thuoc_tinh(
            vi_pham["ve_phai"]
        )

        if ve_trai not in cac_vi_pham_theo_ve_trai:
            cac_vi_pham_theo_ve_trai[ve_trai] = {
                "ve_phai": set()
            }

        cac_vi_pham_theo_ve_trai[ve_trai][
            "ve_phai"
        ].update(ve_phai)

    # =========================================================
    # 8. Chuẩn bị kết quả
    # =========================================================

    tap_thuoc_tinh_con_lai = (
        chuan_hoa_tap_thuoc_tinh(
            tap_thuoc_tinh
        )
    )

    cac_bang_duoc_tach = []
    cac_buoc_giai = []

    # =========================================================
    # 9. Phân rã các PTH vi phạm 3NF
    # =========================================================

    for i, (ve_trai, thong_tin) in enumerate(
        cac_vi_pham_theo_ve_trai.items(),
        start=1
    ):

        # -----------------------------------------------------
        # 9.1. Tạo tập thuộc tính của quan hệ mới
        # -----------------------------------------------------

        tap_thuoc_tinh_trong_bang_moi = (
            set(ve_trai)
            | thong_tin["ve_phai"]
        )

        # -----------------------------------------------------
        # 9.2. Chỉ loại các thuộc tính không phải thuộc tính khóa
        # khỏi quan hệ ban đầu
        # -----------------------------------------------------

        tap_thuoc_tinh_khong_khoa = (
            thong_tin["ve_phai"]
            - cac_thuoc_tinh_khoa
        )

        tap_thuoc_tinh_con_lai -= (
            tap_thuoc_tinh_khong_khoa
        )

        # -----------------------------------------------------
        # 9.3. Định dạng tập thuộc tính
        # -----------------------------------------------------

        dinh_dang_tap_thuoc_tinh_trong_bang_moi = (
            ", ".join(
                sorted(
                    tap_thuoc_tinh_trong_bang_moi
                )
            )
        )

        # -----------------------------------------------------
        # 9.4. Lọc PTH trong quan hệ mới
        # -----------------------------------------------------

        tap_phu_thuoc_ham_trong_bang_moi = (
            loc_phu_thuoc_ham(
                tap_thuoc_tinh_trong_bang_moi,
                tap_phu_thuoc_ham_con_lai_dang_chuoi
            )
        )

        if tap_phu_thuoc_ham_trong_bang_moi:

            dinh_dang_tap_phu_thuoc_ham_trong_bang_moi = (
                ", ".join(
                    dinh_dang_phu_thuoc_ham(
                        ve_trai_pth,
                        ve_phai_pth
                    )
                    for ve_trai_pth, ve_phai_pth
                    in tap_phu_thuoc_ham_trong_bang_moi
                )
            )

        else:

            dinh_dang_tap_phu_thuoc_ham_trong_bang_moi = (
                "không có phụ thuộc hàm nào"
            )

        # -----------------------------------------------------
        # 9.5. Lưu quan hệ
        # -----------------------------------------------------

        cac_bang_duoc_tach.append(
            f"R{i}("
            f"{dinh_dang_tap_thuoc_tinh_trong_bang_moi}"
            f") với {{ "
            f"{dinh_dang_tap_phu_thuoc_ham_trong_bang_moi}"
            f" }}"
        )

        # -----------------------------------------------------
        # 9.6. Tạo lời giải
        # -----------------------------------------------------

        cac_pth_vi_pham = ", ".join(
            sorted(
                dinh_dang_phu_thuoc_ham(
                    ve_trai,
                    {thuoc_tinh}
                )
                for thuoc_tinh
                in thong_tin["ve_phai"]
            )
        )

        cac_buoc_giai.append(
            f"Tách R{i}("
            f"{dinh_dang_tap_thuoc_tinh_trong_bang_moi}"
            f") vì {cac_pth_vi_pham} "
            f"vi phạm dạng chuẩn 3: "
            f"vế trái không phải siêu khóa và "
            f"vế phải không phải thuộc tính khóa."
        )

    # =========================================================
    # 10. Ghi nhận các phụ thuộc hàm vòng
    # =========================================================

    for tap_thuoc_tinh_vong in cac_tap_thuoc_tinh_vong:

        chuoi_thuoc_tinh_vong = ", ".join(
            sorted(tap_thuoc_tinh_vong)
        )

        khoa_nhom = tuple(
            sorted(tap_thuoc_tinh_vong)
        )

        tap_phu_thuoc_ham_trong_vong = (
            phu_thuoc_ham_vong.get(
                khoa_nhom,
                []
            )
        )

        if tap_phu_thuoc_ham_trong_vong:

            chuoi_phu_thuoc_ham_vong = ", ".join(
                dinh_dang_phu_thuoc_ham(
                    ve_trai,
                    ve_phai
                )
                for ve_trai, ve_phai
                in tap_phu_thuoc_ham_trong_vong
            )

            cac_buoc_giai.append(
                f"Phát hiện phụ thuộc hàm vòng "
                f"trên tập thuộc tính "
                f"{{ {chuoi_thuoc_tinh_vong} }}: "
                f"{chuoi_phu_thuoc_ham_vong}."
            )

    # =========================================================
    # 11. Tạo quan hệ còn lại
    # =========================================================

    dinh_dang_tap_thuoc_tinh_trong_bang_cuoi = (
        ", ".join(
            sorted(
                tap_thuoc_tinh_con_lai
            )
        )
    )

    tap_phu_thuoc_ham_trong_bang_cuoi = (
        loc_phu_thuoc_ham(
            tap_thuoc_tinh_con_lai,
            tap_phu_thuoc_ham_con_lai_dang_chuoi
        )
    )

    if tap_phu_thuoc_ham_trong_bang_cuoi:

        dinh_dang_tap_phu_thuoc_ham_trong_bang_cuoi = (
            ", ".join(
                dinh_dang_phu_thuoc_ham(
                    ve_trai,
                    ve_phai
                )
                for ve_trai, ve_phai
                in tap_phu_thuoc_ham_trong_bang_cuoi
            )
        )

    else:

        dinh_dang_tap_phu_thuoc_ham_trong_bang_cuoi = (
            "không có phụ thuộc hàm nào"
        )

    so_thu_tu_bang_cuoi = (
        len(cac_bang_duoc_tach) + 1
    )

    cac_bang_duoc_tach.append(
        f"R{so_thu_tu_bang_cuoi}("
        f"{dinh_dang_tap_thuoc_tinh_trong_bang_cuoi}"
        f") với {{ "
        f"{dinh_dang_tap_phu_thuoc_ham_trong_bang_cuoi}"
        f" }}"
    )

    cac_buoc_giai.append(
        f"Còn lại R{so_thu_tu_bang_cuoi}("
        f"{dinh_dang_tap_thuoc_tinh_trong_bang_cuoi}"
        f") là các thuộc tính còn lại và "
        f"chứa các thuộc tính của khóa ứng viên."
    )

    # =========================================================
    # 12. Trả kết quả
    # =========================================================

    return (
        "\n".join(cac_bang_duoc_tach),
        cac_buoc_giai
    )

# ========================================
# NÂNG DẠNG CHUẨN BOYCE-CODD
# ========================================



if __name__ == '__main__':
    tap_thuoc_tinh = ["A", "B", "C", "D", "E", "G"]

    tap_phu_thuoc_ham = [
        "A → BC",
        "C → D",
        "BD → E",
        "E → G"
    ]

    kq, bc = tim_khoa_ung_vien(tap_thuoc_tinh, tap_phu_thuoc_ham)

    # print(cac_thuoc_tinh_trong_khoa_ung_vien(kq))
    # print(loc_phu_thuoc_ham(["A", "B", "C"], tap_phu_thuoc_ham))
    # print(tim_vi_pham_dang_chuan_2(tap_phu_thuoc_ham, kq))

    # a, b = tim_phu_thuoc_ham_vong(chuan_hoa_tap_phu_thuoc_ham_sang_tuple(tap_phu_thuoc_ham))
    # print(a)
    # print(b)

    r, s = nang_dang_chuan_3(tap_thuoc_tinh, tap_phu_thuoc_ham)
    print(r)
    for b in s:
        print(b)