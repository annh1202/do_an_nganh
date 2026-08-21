# ==================================
# TÌM KHÓA ỨNG VIÊN
# ==================================
from itertools import combinations

from backend.app.modules.LyThuyetCSDL.bai_giai.bao_dong_tap_thuoc_tinh import tinh_bao_dong_tap_thuoc_tinh
from backend.app.modules.LyThuyetCSDL.bai_giai.ho_tro import loc_phu_thuoc_ham, loai_bo_phu_thuoc_ham_du_thua
from backend.app.modules.LyThuyetCSDL.utils.chuan_hoa import chuan_hoa_tap_phu_thuoc_ham_sang_tuple
from backend.app.modules.LyThuyetCSDL.utils.dinh_dang import dinh_dang_tap_thuoc_tinh, dinh_dang_chuoi_tap_thuoc_tinh


def phan_loai_thuoc_tinh(tap_thuoc_tinh, tap_phu_thuoc_ham):
    tap_thuoc_tinh = set(tap_thuoc_tinh)

    thuoc_tinh_o_ve_trai = set()
    thuoc_tinh_o_ve_phai = set()

    for ve_trai, ve_phai in tap_phu_thuoc_ham:
        thuoc_tinh_o_ve_trai.update(ve_trai)
        thuoc_tinh_o_ve_phai.update(ve_phai)

    # Tập nguồn: Không xuất hiện ở vế phải
    tap_nguon = tap_thuoc_tinh - thuoc_tinh_o_ve_phai

    # Tập đích: Chỉ xuất hiện ở vế phải
    tap_dich = thuoc_tinh_o_ve_phai - thuoc_tinh_o_ve_trai

    # Tập trung gian: Xuất hiện cả ở vế trái và vế phải
    tap_trung_gian = tap_thuoc_tinh - tap_nguon - tap_dich

    return set(sorted(tap_nguon)), set(sorted(tap_trung_gian)), set(sorted(tap_dich))


def kiem_tra_tinh_toi_thieu(
    cac_khoa_ung_vien,
    tap_thuoc_tinh_dang_xet,
    cac_tap_thuoc_tinh_bo_qua
):
    for khoa_ung_vien in cac_khoa_ung_vien:
        if set(khoa_ung_vien).issubset(tap_thuoc_tinh_dang_xet):
            if khoa_ung_vien not in cac_tap_thuoc_tinh_bo_qua:
                cac_tap_thuoc_tinh_bo_qua[khoa_ung_vien] = []

            cac_tap_thuoc_tinh_bo_qua[khoa_ung_vien].append(
                dinh_dang_chuoi_tap_thuoc_tinh(tap_thuoc_tinh_dang_xet)
            )

            return False

    return True


def kiem_tra_sieu_khoa(tap_thuoc_tinh_dang_xet, bao_dong, tap_thuoc_tinh_goc):
    if bao_dong == tap_thuoc_tinh_goc:

        noi_dung = (
            f"→ {tap_thuoc_tinh_dang_xet} là siêu khóa"
            f"\n→ {tap_thuoc_tinh_dang_xet} là khóa ứng viên vì tối thiểu"
        )

        return True, noi_dung

    cac_thuoc_tinh_con_thieu = tap_thuoc_tinh_goc - bao_dong

    noi_dung = (
        f"→ {tap_thuoc_tinh_dang_xet} không phải siêu khóa "
        f"vì thiếu "
        f"{dinh_dang_tap_thuoc_tinh(cac_thuoc_tinh_con_thieu)}"
    )

    return False, noi_dung


def tim_khoa_ung_vien(tap_thuoc_tinh, tap_phu_thuoc_ham):
    tap_thuoc_tinh = set(tap_thuoc_tinh)

    tap_phu_thuoc_ham_dang_tuple = (
        loai_bo_phu_thuoc_ham_du_thua(
            chuan_hoa_tap_phu_thuoc_ham_sang_tuple(tap_phu_thuoc_ham)
        )
    )

    # Phân loại thuộc tính
    tap_nguon, tap_trung_gian, tap_dich = phan_loai_thuoc_tinh(
        tap_thuoc_tinh,
        tap_phu_thuoc_ham_dang_tuple
    )

    # Lưu các tập bị bỏ qua theo từng khóa ứng viên
    cac_tap_thuoc_tinh_bo_qua = {}

    cac_khoa_ung_vien = []
    cac_buoc_giai = []

    # PHÂN LOẠI THUỘC TÍNH

    noi_dung_tung_buoc = "Phân loại thuộc tính:"

    noi_dung_tung_buoc += (
        f"\nTập nguồn: "
        f"{{ {dinh_dang_tap_thuoc_tinh(tap_nguon) if tap_nguon else '∅'} }}"
        f"\nTập trung gian: "
        f"{{ {dinh_dang_tap_thuoc_tinh(tap_trung_gian) if tap_trung_gian else '∅'} }}"
        f"\nTập đích: "
        f"{{ {dinh_dang_tap_thuoc_tinh(tap_dich) if tap_dich else '∅'} }}"
    )

    cac_buoc_giai.append(noi_dung_tung_buoc)

    so_buoc = 1

    # Chỉ sinh tổ hợp trên tập trung gian
    for do_dai in range(len(tap_trung_gian) + 1):
        for tap_con in combinations(tap_trung_gian, do_dai):

            tap_thuoc_tinh_dang_xet = tap_nguon | set(tap_con)

            tap_thuoc_tinh_dang_chuoi = dinh_dang_chuoi_tap_thuoc_tinh(tap_thuoc_tinh_dang_xet)

            # KIỂM TRA TÍNH TỐI THIỂU
            if not kiem_tra_tinh_toi_thieu(
                cac_khoa_ung_vien,
                tap_thuoc_tinh_dang_xet,
                cac_tap_thuoc_tinh_bo_qua
            ):
                continue

            # ========================================================
            # TÍNH BAO ĐÓNG
            # ========================================================

            bao_dong, _ = (
                tinh_bao_dong_tap_thuoc_tinh(tap_thuoc_tinh_dang_chuoi, tap_phu_thuoc_ham)
            )

            tap_bao_dong = set(bao_dong)

            noi_dung_tung_buoc = (
                f"Bước {so_buoc}: "
                f"{tap_thuoc_tinh_dang_chuoi}⁺ = "
                f"{{ "
                f"{dinh_dang_tap_thuoc_tinh(bao_dong) if bao_dong else '∅'} "
                f"}}\n"
            )

            so_buoc += 1

            # ========================================================
            # KIỂM TRA SIÊU KHÓA
            # ========================================================
            la_sieu_khoa, noi_dung_kiem_tra_sieu_khoa = kiem_tra_sieu_khoa(
                tap_thuoc_tinh_dang_chuoi,
                tap_bao_dong,
                tap_thuoc_tinh
            )

            if la_sieu_khoa:
                cac_khoa_ung_vien.append(tap_thuoc_tinh_dang_chuoi)

            noi_dung_tung_buoc += noi_dung_kiem_tra_sieu_khoa

            cac_buoc_giai.append(noi_dung_tung_buoc)

    # ============================================================
    # GOM CÁC TẬP BỊ BỎ QUA THEO TỪNG KHÓA ỨNG VIÊN
    # ============================================================

    for khoa_ung_vien, cac_tap_bo_qua in cac_tap_thuoc_tinh_bo_qua.items():

        if cac_tap_bo_qua:
            noi_dung_tung_buoc = (
                f"Các tập thuộc tính bị bỏ qua vì chứa khóa ứng viên {khoa_ung_vien}:"
                f"\n{{ {', '.join(cac_tap_bo_qua)} }}"
            )

            cac_buoc_giai.append(noi_dung_tung_buoc)

    return cac_khoa_ung_vien, cac_buoc_giai



if __name__ == '__main__':
    tap_thuoc_tinh = ["A", "B", "C", "D", "E", "G"]

    tap_phu_thuoc_ham = [
        "A → BC",
        "C → D",
        "BD → E",
        "E → G"
    ]

    khoa_ung_vien, cac_buoc_giai = tim_khoa_ung_vien(tap_thuoc_tinh, tap_phu_thuoc_ham)
    print(khoa_ung_vien)
    for b in cac_buoc_giai:
        print(b)