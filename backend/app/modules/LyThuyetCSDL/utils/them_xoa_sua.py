from backend.app.modules.LyThuyetCSDL.config import LoaiThongBao
from backend.app.modules.LyThuyetCSDL.utils.dinh_dang import dinh_dang_phu_thuoc_ham
from backend.app.modules.LyThuyetCSDL.utils.chuan_hoa import chuan_hoa_thuoc_tinh, chuan_hoa_tap_phu_thuoc_ham_sang_tuple, chuan_hoa_mot_ve_phu_thuoc_ham
from backend.app.modules.LyThuyetCSDL.utils.kiem_tra_hop_le import co_phai_thuoc_tinh_hop_le, thuoc_tinh_co_trong_phu_thuoc_ham, co_phai_phu_thuoc_ham_hop_le, \
    co_phai_phu_thuoc_ham_hien_nhien


# ====================<< ATTRIBUTE >>====================
def them_thuoc_tinh(thuoc_tinh, tap_thuoc_tinh):
    thuoc_tinh = chuan_hoa_thuoc_tinh(thuoc_tinh)

    if not co_phai_thuoc_tinh_hop_le(thuoc_tinh):
        return False, LoaiThongBao.NGUY_HIEM, "Thuộc tính phải là một chữ cái tiếng Anh"

    if thuoc_tinh in tap_thuoc_tinh:
        return False, LoaiThongBao.CANH_BAO, "Thuộc tính đã tồn tại"

    tap_thuoc_tinh.append(thuoc_tinh)
    tap_thuoc_tinh.sort()

    return True, LoaiThongBao.THANH_CONG, f"Đã thêm thuộc tính {thuoc_tinh}"


def xoa_thuoc_tinh(thuoc_tinh, tap_thuoc_tinh, tap_phu_thuoc_ham, tap_thuoc_tinh_muc_tieu=None):
    thuoc_tinh = chuan_hoa_thuoc_tinh(thuoc_tinh)

    if not co_phai_thuoc_tinh_hop_le(thuoc_tinh):
        return False, LoaiThongBao.NGUY_HIEM, "Thuộc tính phải là một chữ cái tiếng Anh"

    if thuoc_tinh not in tap_thuoc_tinh:
        return False, LoaiThongBao.CANH_BAO, "Thuộc tính không tồn tại"

    if thuoc_tinh_co_trong_phu_thuoc_ham(thuoc_tinh, chuan_hoa_tap_phu_thuoc_ham_sang_tuple(tap_phu_thuoc_ham)):
        return False, LoaiThongBao.CANH_BAO, f"Không thể xoá vì thuộc tính {thuoc_tinh} xuất hiện trong F"

    if tap_thuoc_tinh_muc_tieu is not None:
        if thuoc_tinh in tap_thuoc_tinh_muc_tieu:
            return False, LoaiThongBao.CANH_BAO, f"Không thể xoá vì thuộc tính {thuoc_tinh} xuất hiện trong X"

    tap_thuoc_tinh.remove(thuoc_tinh)

    return True, LoaiThongBao.THANH_CONG, f"Đã xoá thuộc tính {thuoc_tinh}"


def xoa_trong_tap_thuoc_tinh(tap_thuoc_tinh, tap_phu_thuoc_ham, tap_thuoc_tinh_muc_tieu=None):
    if tap_thuoc_tinh_muc_tieu is not None:
        if tap_phu_thuoc_ham or tap_thuoc_tinh_muc_tieu:
            return (
                False,
                LoaiThongBao.CANH_BAO,
                "Không thể xoá toàn bộ tập thuộc tính khi F hoặc X chưa rỗng"
            )
    else:
        if tap_phu_thuoc_ham:
            return (
                False,
                LoaiThongBao.CANH_BAO,
                "Không thể xoá toàn bộ tập thuộc tính khi F chưa rỗng"
            )
    tap_thuoc_tinh.clear()

    return True, LoaiThongBao.THANH_CONG, "Đã xoá toàn bộ tập thuộc tính"


# ====================<< FUNCTIONAL DEPENDENCY >>====================
def them_phu_thuoc_ham(thuoc_tinh_ve_trai, thuoc_tinh_ve_phai, tap_thuoc_tinh, tap_phu_thuoc_ham):
    ve_trai = chuan_hoa_mot_ve_phu_thuoc_ham(thuoc_tinh_ve_trai)
    ve_phai = chuan_hoa_mot_ve_phu_thuoc_ham(thuoc_tinh_ve_phai)

    if not ve_trai or not ve_phai:
        return False, LoaiThongBao.NGUY_HIEM, "Hai vế của phụ thuộc hàm không được rỗng"

    if tap_thuoc_tinh is not None and not co_phai_phu_thuoc_ham_hop_le(ve_trai, ve_phai, tap_thuoc_tinh):
        return False, LoaiThongBao.CANH_BAO, "Mọi thuộc tính trong F phải thuộc tập R"

    if co_phai_phu_thuoc_ham_hien_nhien(thuoc_tinh_ve_trai, thuoc_tinh_ve_phai):
        return False, LoaiThongBao.CANH_BAO, "Phụ thuộc hàm hiển nhiên"

    fd_string = dinh_dang_phu_thuoc_ham(ve_trai, ve_phai)
    if fd_string in tap_phu_thuoc_ham:
        return False, LoaiThongBao.CANH_BAO, "Phụ thuộc hàm đã tồn tại"

    tap_phu_thuoc_ham.append(fd_string)

    return True, LoaiThongBao.THANH_CONG, f"Đã thêm phụ thuộc hàm {fd_string}"


def xoa_phu_thuoc_ham(thuoc_tinh_ve_trai, thuoc_tinh_ve_phai, tap_phu_thuoc_ham):
    ve_trai = chuan_hoa_mot_ve_phu_thuoc_ham(thuoc_tinh_ve_trai)
    ve_phai = chuan_hoa_mot_ve_phu_thuoc_ham(thuoc_tinh_ve_phai)

    fd_string = dinh_dang_phu_thuoc_ham(ve_trai, ve_phai)

    if fd_string not in tap_phu_thuoc_ham:
        return False, LoaiThongBao.CANH_BAO, "Phụ thuộc hàm không tồn tại"

    tap_phu_thuoc_ham.remove(fd_string)

    return True, LoaiThongBao.THANH_CONG, f"Đã xoá phụ thuộc hàm {fd_string}"


def xoa_trong_tap_phu_thuoc_ham(tap_phu_thuoc_ham):
    tap_phu_thuoc_ham.clear()
    return True, LoaiThongBao.THANH_CONG, "Đã xoá toàn bộ tập phụ thuộc hàm"


# ====================<< TARGET ATTRIBUTE >>====================
def them_thuoc_tinh_can_tim(thuoc_tinh, tap_thuoc_tinh, tap_thuoc_tinh_muc_tieu):
    thuoc_tinh = chuan_hoa_thuoc_tinh(thuoc_tinh)

    if not co_phai_thuoc_tinh_hop_le(thuoc_tinh):
        return False, LoaiThongBao.NGUY_HIEM, "Thuộc tính phải là một chữ cái tiếng Anh"

    if thuoc_tinh not in tap_thuoc_tinh:
        return False, LoaiThongBao.CANH_BAO, f"Thuộc tính {thuoc_tinh} không thuộc tập R"

    if thuoc_tinh in tap_thuoc_tinh_muc_tieu:
        return False, LoaiThongBao.CANH_BAO, f"Thuộc tính {thuoc_tinh} đã tồn tại trong X"

    tap_thuoc_tinh_muc_tieu.append(thuoc_tinh)
    tap_thuoc_tinh_muc_tieu.sort()

    return True, LoaiThongBao.THANH_CONG, f"Đã thêm thuộc tính"


def xoa_thuoc_tinh_can_tim(thuoc_tinh, tap_thuoc_tinh_muc_tieu):
    thuoc_tinh = chuan_hoa_thuoc_tinh(thuoc_tinh)

    if not co_phai_thuoc_tinh_hop_le(thuoc_tinh):
        return False, LoaiThongBao.NGUY_HIEM, "Thuộc tính phải là một chữ cái tiếng Anh"

    if thuoc_tinh not in tap_thuoc_tinh_muc_tieu:
        return False, LoaiThongBao.CANH_BAO, f"Thuộc tính {thuoc_tinh} không tồn tại trong X"

    tap_thuoc_tinh_muc_tieu.remove(thuoc_tinh)

    return True, LoaiThongBao.THANH_CONG, f"Đã xoá thuộc tính {thuoc_tinh} khỏi X"


def xoa_trong_tap_thuoc_tinh_can_tim(tap_thuoc_tinh_muc_tieu):
    tap_thuoc_tinh_muc_tieu.clear()
    return True, LoaiThongBao.THANH_CONG, "Đã xoá toàn bộ tập X"