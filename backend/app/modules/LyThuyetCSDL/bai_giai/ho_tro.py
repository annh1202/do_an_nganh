from backend.app.modules.LyThuyetCSDL.bai_giai.bao_dong_tap_thuoc_tinh import tinh_bao_dong_tap_thuoc_tinh
from backend.app.modules.LyThuyetCSDL.utils.chuan_hoa import chuan_hoa_tap_phu_thuoc_ham_sang_tuple, \
    chuan_hoa_phu_thuoc_ham_sang_tuple
from backend.app.modules.LyThuyetCSDL.utils.dinh_dang import dinh_dang_tap_phu_thuoc_ham_tuple


def tach_phu_thuoc_ham_ve_phai(tap_phu_thuoc_ham):
    # danh_sach_phu_thuoc_ham = chuan_hoa_tap_phu_thuoc_ham_sang_tuple(tap_phu_thuoc_ham)

    tap_phu_thuoc_ham_moi = []

    for ve_trai, ve_phai in tap_phu_thuoc_ham:
        for thuoc_tinh in ve_phai:
            tap_phu_thuoc_ham_moi.append((set(ve_trai), {thuoc_tinh}))

    return tap_phu_thuoc_ham_moi


def co_phu_thuoc_ham_du_thua(phu_thuoc_ham_can_xet, tap_phu_thuoc_ham_hien_tai):
    ve_trai, ve_phai = phu_thuoc_ham_can_xet

    # Tạo tập PTH mới bỏ đi PTH đang xét
    tap_phu_thuoc_ham_con_lai = [
        fd for fd in tap_phu_thuoc_ham_hien_tai
        if fd != phu_thuoc_ham_can_xet
    ]

    # Tính bao đóng vế trái trên tập các PTH còn lại
    bao_dong, _ = tinh_bao_dong_tap_thuoc_tinh(
        list(ve_trai),
        dinh_dang_tap_phu_thuoc_ham_tuple(tap_phu_thuoc_ham_con_lai)
    )

    bao_dong = set(bao_dong)

    # Nếu vế phải vẫn nằm trong bao đóng -> PTH đang xét bị dư thừa
    return ve_phai.issubset(bao_dong)


def loai_phu_thuoc_ham_du_thua(tap_phu_thuoc_ham):
    # Nên tách vế phải về dạng đơn trước khi xét dư thừa
    tap_phu_thuoc_ham_hien_tai = tach_phu_thuoc_ham_ve_phai(tap_phu_thuoc_ham)

    i = 0
    # Dùng while thay cho for để quản lý chỉ số i chính xác khi pop phần tử
    while i < len(tap_phu_thuoc_ham_hien_tai):
        phu_thuoc_ham = tap_phu_thuoc_ham_hien_tai[i]

        # Kiểm tra dư thừa dựa trên danh sách ĐÃ ĐƯỢC CẬP NHẬT
        if co_phu_thuoc_ham_du_thua(phu_thuoc_ham, tap_phu_thuoc_ham_hien_tai):
            # Xóa PTH dư thừa khỏi danh sách hiện tại
            tap_phu_thuoc_ham_hien_tai.pop(i)
            # Không tăng i vì phần tử tiếp theo đã nhảy vào vị trí i
        else:
            # Không dư thừa thì giữ lại và xét tiếp phần tử kế bên
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
    print(co_phu_thuoc_ham_du_thua(({'A'}, {'F'}), tap_phu_thuoc_ham))
    print(co_phu_thuoc_ham_du_thua(({'B', 'A'}, {'F'}), tap_phu_thuoc_ham))
    print(co_phu_thuoc_ham_du_thua(({'D', 'B'}, {'C'}), tap_phu_thuoc_ham))
    print(loai_phu_thuoc_ham_du_thua(tap_phu_thuoc_ham))

    """
    [({'A'}, {'F'}), ({'B', 'A'}, {'F'}), ({'E'}, {'C'}), ({'F'}, {'D'}), ({'D'}, {'C'}), ({'B', 'D'}, {'C'}), ({'B'}, {'C'})]
    True
    True
    True
    [({'A'}, {'F'}), ({'B', 'A'}, {'F'}), ({'E'}, {'C'}), ({'F'}, {'D'}), ({'D'}, {'C'}), ({'B', 'D'}, {'C'}), ({'B'}, {'C'})]
    """

