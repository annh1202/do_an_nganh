import random
import string
from itertools import chain, combinations

from backend.app.modules.LyThuyetCSDL.bai_giai.bao_dong_tap_thuoc_tinh import tinh_bao_dong_tap_thuoc_tinh
from backend.app.modules.LyThuyetCSDL.utils.chuan_hoa import chuan_hoa_thuoc_tinh, \
    chuan_hoa_tap_phu_thuoc_ham_sang_tuple
from backend.app.modules.LyThuyetCSDL.utils.dinh_dang import dinh_dang_tap_thuoc_tinh, dinh_dang_phu_thuoc_ham


# ==================================
# TÍNH BAO ĐÓNG TẬP PHỤ THUỘC HÀM
# ==================================
def tinh_bao_dong_tap_phu_thuoc_ham(tap_phu_thuoc_ham):
    # Lấy tất cả thuộc tính xuất hiện trong các phụ thuộc hàm
    tap_thuoc_tinh = set()

    for ve_trai, ve_phai in chuan_hoa_tap_phu_thuoc_ham_sang_tuple(tap_phu_thuoc_ham):
        tap_thuoc_tinh.update(ve_trai)
        tap_thuoc_tinh.update(ve_phai)

    tap_thuoc_tinh_sap_xep = sorted(
        chuan_hoa_thuoc_tinh(thuoctinh)
        for thuoctinh in tap_thuoc_tinh
    )

    bao_dong_tap_phu_thuoc_ham = set()
    cac_buoc_giai = []

    # chain.from_iterable() -> nối các nhóm kết quả thành 1 chuỗi
    # combinations(R, n) -> lấy tập con có độ dài n
    cac_tap_con = chain.from_iterable(
        combinations(tap_thuoc_tinh_sap_xep, do_dai)
        for do_dai in range(1, len(tap_thuoc_tinh_sap_xep) + 1)
    )

    for so_buoc, tap_con in enumerate(cac_tap_con, start=1):
        tap_con_dang_chuoi = "".join(tap_con)

        bao_dong_tap_thuoc_tinh, _ = tinh_bao_dong_tap_thuoc_tinh(
            tap_con_dang_chuoi,
            tap_phu_thuoc_ham
        )

        tap_thuoc_tinh_moi = set(bao_dong_tap_thuoc_tinh) - set(tap_con)

        noi_dung_tung_buoc = (
            f"Bước {so_buoc}: Xét tập thuộc tính {tap_con_dang_chuoi}\n"
            f"Ta tính được {tap_con_dang_chuoi}⁺ = "
            f"{{ {dinh_dang_tap_thuoc_tinh(bao_dong_tap_thuoc_tinh)} }}"
        )

        if tap_thuoc_tinh_moi:
            for thuoctinh in sorted(tap_thuoc_tinh_moi):

                phu_thuoc_ham = dinh_dang_phu_thuoc_ham(tap_con_dang_chuoi, thuoctinh)

                bao_dong_tap_phu_thuoc_ham.add(phu_thuoc_ham)

                noi_dung_tung_buoc += (
                    f"\nVì {thuoctinh} ∈ {tap_con_dang_chuoi}⁺ "
                    f"nên suy ra {phu_thuoc_ham}"
                )

        else:

            noi_dung_tung_buoc += (
                f"\nKhông suy ra thêm thuộc tính nào mới "
                f"từ {tap_con_dang_chuoi}"
            )

        cac_buoc_giai.append(noi_dung_tung_buoc)

    return bao_dong_tap_phu_thuoc_ham, cac_buoc_giai


if __name__ == '__main__':
    tap_thuoc_tinh = ["A", "B", "C", "D"]
    tap_phu_thuoc_ham = ["A → B", "B → C", "AC → D"]
    tap_thuoc_tinh_can_tim = ["A"]

    bao_dong, cac_buoc_giai = tinh_bao_dong_tap_phu_thuoc_ham(tap_phu_thuoc_ham)
    print(bao_dong)
    for b in cac_buoc_giai:
        print(b)