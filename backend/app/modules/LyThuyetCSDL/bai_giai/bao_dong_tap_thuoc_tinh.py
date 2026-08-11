from backend.app.modules.LyThuyetCSDL.utils.chuan_hoa import chuan_hoa_tap_phu_thuoc_ham_sang_tuple, \
    chuan_hoa_tap_thuoc_tinh
from backend.app.modules.LyThuyetCSDL.utils.dinh_dang import dinh_dang_phu_thuoc_ham, dinh_dang_tap_thuoc_tinh, \
    dinh_dang_chuoi_tap_thuoc_tinh


# ================================
# TÍNH BAO ĐÓNG TẬP THUỘC TÍNH
# ================================
def tinh_bao_dong_tap_thuoc_tinh(tap_thuoc_tinh_can_tim, tap_phu_thuoc_ham_dau_vao):
    tap_phu_thuoc_ham = chuan_hoa_tap_phu_thuoc_ham_sang_tuple(tap_phu_thuoc_ham_dau_vao)

    bao_dong = set(chuan_hoa_tap_thuoc_tinh(tap_thuoc_tinh_can_tim))

    cac_buoc_giai = []
    so_cac_buoc_giai = 1

    while True:
        co_thay_doi = False

        for ve_trai, ve_phai in tap_phu_thuoc_ham:

            # ve_trai ⊆ bao_dong
            # ve_phai chưa nằm hoàn toàn trong bao_dong
            if ve_trai.issubset(bao_dong) and not ve_phai.issubset(bao_dong):

                bao_dong_chua_them = bao_dong.copy()

                # Chỉ lấy thuộc tính mới
                cac_thuoc_tinh_moi = ve_phai - bao_dong

                if not cac_thuoc_tinh_moi:
                    continue

                bao_dong.update(cac_thuoc_tinh_moi)

                co_thay_doi = True

                cac_buoc_giai.append(
                    f"Bước {so_cac_buoc_giai}: "
                    f"Xét phụ thuộc hàm {dinh_dang_phu_thuoc_ham(ve_trai, ve_phai)}\n"
                    f"Vì {{ {dinh_dang_tap_thuoc_tinh(ve_trai)} }} "
                    f"⊆ X = {{ {dinh_dang_tap_thuoc_tinh(bao_dong_chua_them)} }}, "
                    f"nên áp dụng {dinh_dang_phu_thuoc_ham(ve_trai, ve_phai)}, "
                    f"thêm {dinh_dang_chuoi_tap_thuoc_tinh(cac_thuoc_tinh_moi)} "
                    f"vào X⁺ do đó X⁺ = {{ {dinh_dang_tap_thuoc_tinh(bao_dong)} }}"
                )

                so_cac_buoc_giai += 1

        if not co_thay_doi:
            break

    cac_buoc_giai.append(f"Vậy bao đóng tập thuộc tính là X⁺ = {{ {dinh_dang_tap_thuoc_tinh(bao_dong)} }}")

    return bao_dong, cac_buoc_giai


if __name__ == '__main__':
    tap_thuoc_tinh = ["A", "B", "C", "D"]
    tap_phu_thuoc_ham = ["A → B", "B → C", "AC → D"]
    tap_thuoc_tinh_can_tim = ["A", "B"]

    bao_dong, cac_buoc_giai = tinh_bao_dong_tap_thuoc_tinh(tap_thuoc_tinh_can_tim, tap_phu_thuoc_ham)
    print(bao_dong)
    for b in cac_buoc_giai:
        print(b)