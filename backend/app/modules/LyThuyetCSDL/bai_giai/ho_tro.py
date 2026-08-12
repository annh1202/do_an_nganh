from backend.app.modules.LyThuyetCSDL.bai_giai.bao_dong_tap_thuoc_tinh import tinh_bao_dong_tap_thuoc_tinh
from backend.app.modules.LyThuyetCSDL.utils.chuan_hoa import chuan_hoa_tap_phu_thuoc_ham_sang_tuple
from backend.app.modules.LyThuyetCSDL.utils.dinh_dang import dinh_dang_tap_phu_thuoc_ham_tuple


def tach_phu_thuoc_ham_ve_phai(tap_phu_thuoc_ham):
    """
    A -> BC sẽ thành A -> B và A -> C
    """
    tap_phu_thuoc_ham_moi = []

    for ve_trai, ve_phai in tap_phu_thuoc_ham:
        for thuoc_tinh in ve_phai:
            tap_phu_thuoc_ham_moi.append((set(ve_trai), {thuoc_tinh}))

    return tap_phu_thuoc_ham_moi


def co_phai_phu_thuoc_ham_du_thua(phu_thuoc_ham_can_xet, tap_phu_thuoc_ham_hien_tai):
    """
    Phụ thuộc hàm X -> Y gọi là dư thừa khi có thể từ X suy ra Y mà không dùng X -> Y
    """
    ve_trai, ve_phai = phu_thuoc_ham_can_xet

    tap_phu_thuoc_ham_con_lai = [
        fd for fd in tap_phu_thuoc_ham_hien_tai
        if fd != phu_thuoc_ham_can_xet
    ]

    bao_dong, _ = tinh_bao_dong_tap_thuoc_tinh(
        list(ve_trai),
        dinh_dang_tap_phu_thuoc_ham_tuple(tap_phu_thuoc_ham_con_lai)
    )

    bao_dong = set(bao_dong)

    return ve_phai.issubset(bao_dong)


def loai_bo_phu_thuoc_ham_du_thua(tap_phu_thuoc_ham):
    tap_phu_thuoc_ham_hien_tai = tach_phu_thuoc_ham_ve_phai(tap_phu_thuoc_ham)

    i = 0

    while i < len(tap_phu_thuoc_ham_hien_tai):
        phu_thuoc_ham = tap_phu_thuoc_ham_hien_tai[i]

        if co_phai_phu_thuoc_ham_du_thua(phu_thuoc_ham, tap_phu_thuoc_ham_hien_tai):
            tap_phu_thuoc_ham_hien_tai.pop(i)

        else:
            i += 1

    return tap_phu_thuoc_ham_hien_tai

if __name__ == '__main__':
    tap_phu_thuoc_ham = [
        "A → F",
        "AB → F",
        "E → C",
        "F → D",
        "D → C",
        "BD → C",
        "B → C"
    ]

    tap_phu_thuoc_ham = chuan_hoa_tap_phu_thuoc_ham_sang_tuple(tap_phu_thuoc_ham)


    # print(tach_phu_thuoc_ham_ve_phai(tap_phu_thuoc_ham))
    print(co_phai_phu_thuoc_ham_du_thua(({'A'}, {'F'}), tap_phu_thuoc_ham))
    print(co_phai_phu_thuoc_ham_du_thua(({'B', 'A'}, {'F'}), tap_phu_thuoc_ham))
    print(co_phai_phu_thuoc_ham_du_thua(({'D', 'B'}, {'C'}), tap_phu_thuoc_ham))
    print(loai_bo_phu_thuoc_ham_du_thua(tap_phu_thuoc_ham))

