from backend.app.modules.LyThuyetCSDL.config import DANH_SACH_DANG_CHUAN
from backend.app.modules.LyThuyetCSDL.utils.chuan_hoa import chuan_hoa_tap_thuoc_tinh, chuan_hoa_thuoc_tinh


# ====================================
# KIỂM TRA THUỘC TÍNH
# ====================================
def co_phai_thuoc_tinh_hop_le(thuoc_tinh):
    if not thuoc_tinh:
        return False
    thuoc_tinh = thuoc_tinh.strip()
    return len(thuoc_tinh) == 1 and thuoc_tinh.isalpha() and thuoc_tinh.isascii()


def thuoc_tinh_co_trong_phu_thuoc_ham(thuoc_tinh, tap_phu_thuoc_ham):
    for ve_trai, ve_phai in tap_phu_thuoc_ham:
        if thuoc_tinh in ve_trai or thuoc_tinh in ve_phai:
            return True
    return False

# ====================================
# KIỂM TRA PHỤ THUỘC HÀM
# ====================================
def co_phai_phu_thuoc_ham_hien_nhien(thuoc_tinh_ve_trai, thuoc_tinh_ve_phai):
    ve_trai = chuan_hoa_tap_thuoc_tinh(thuoc_tinh_ve_trai)
    ve_phai = chuan_hoa_tap_thuoc_tinh(thuoc_tinh_ve_phai)

    return ve_phai.issubset(ve_trai)


def co_phai_phu_thuoc_ham_hop_le(ve_trai, ve_phai, tap_thuoc_tinh):
    tap_hop_thuoc_tinh = set(tap_thuoc_tinh)
    if ve_trai.issubset(tap_hop_thuoc_tinh) and ve_phai.issubset(tap_hop_thuoc_tinh):
        return True
    return False

# ====================================
# KIỂM TRA TẬP THUỘC TÍNH
# ====================================
def kiem_tra_tap_thuoc_tinh(tap_thuoc_tinh):
    if not isinstance(tap_thuoc_tinh, list):
        return False, "Tập thuộc tính phải là list"

    if not tap_thuoc_tinh:
        return False, "Tập thuộc tính không được rỗng"

    tap_thuoc_tinh_da_gap = set()

    for thuoc_tinh in tap_thuoc_tinh:

        if not isinstance(thuoc_tinh, str):
            return False, "Mỗi thuộc tính phải là chuỗi"

        if not co_phai_thuoc_tinh_hop_le(thuoc_tinh):
            return False, (
                f"Thuộc tính '{thuoc_tinh}' không hợp lệ"
            )

        thuoc_tinh = thuoc_tinh.strip().upper()

        if thuoc_tinh in tap_thuoc_tinh_da_gap:
            return False, (
                f"Thuộc tính '{thuoc_tinh}' bị trùng"
            )

        tap_thuoc_tinh_da_gap.add(thuoc_tinh)

    return True, "Tập thuộc tính hợp lệ"


# ====================================
# KIỂM TRA PHỤ PHỤ THUỘC HÀM
# ====================================
def kiem_tra_tap_phu_thuoc_ham(tap_phu_thuoc_ham, tap_thuoc_tinh=None):
    if not isinstance(tap_phu_thuoc_ham, list):
        return False, "Tập phụ thuộc hàm phải là list"

    if not tap_phu_thuoc_ham:
        return False, "Tập phụ thuộc hàm không được rỗng"

    if tap_thuoc_tinh is None:
        tap_thuoc_tinh = set()
    else:
        tap_thuoc_tinh = set(chuan_hoa_tap_thuoc_tinh(tap_thuoc_tinh))

    cac_phu_thuoc_ham_da_co = set()

    for i, phu_thuoc_ham in enumerate(tap_phu_thuoc_ham):
        if not isinstance(phu_thuoc_ham, dict):
            return False, f"Phụ thuộc hàm thứ {i + 1} phải là object"

        if set(phu_thuoc_ham.keys()) != {"ve_trai", "ve_phai"}:
            return False, f"Phụ thuộc hàm thứ {i + 1} phải có 've_trai' và 've_phai'"

        ve_trai = phu_thuoc_ham["ve_trai"]
        ve_phai = phu_thuoc_ham["ve_phai"]

        if not isinstance(ve_trai, str):
            return False, f"Vế trái của phụ thuộc hàm thứ {i + 1} phải là chuỗi"

        if not isinstance(ve_phai, str):
            return False, f"Vế phải của phụ thuộc hàm thứ {i + 1} phải là chuỗi"

        ve_trai = ve_trai.strip().upper()
        ve_phai = ve_phai.strip().upper()

        if not ve_trai or not ve_phai:
            return False, f"Phụ thuộc hàm thứ {i + 1} không được có vế rỗng"

        # Kiểm tra từng thuộc tính trong FD
        for thuoc_tinh in ve_trai + ve_phai:
            if not co_phai_thuoc_tinh_hop_le(thuoc_tinh):
                return False, (
                    f"Thuộc tính '{thuoc_tinh}' trong phụ thuộc hàm thứ {i + 1} không hợp lệ"
                )
            if tap_thuoc_tinh and thuoc_tinh not in tap_thuoc_tinh:
                return False, (
                    f"Thuộc tính '{thuoc_tinh}' "
                    "trong phụ thuộc hàm không tồn tại trong tập thuộc tính"
                )

        # Không cho phép phụ thuộc hàm hiển nhiên
        if co_phai_phu_thuoc_ham_hien_nhien(ve_trai, ve_phai):
            return False, (
                f"Phụ thuộc hàm '{ve_trai} → {ve_phai}' là phụ thuộc hàm hiển nhiên"
            )

        # Kiểm tra phụ thuộc hàm bị trùng
        phu_thuoc_ham_hien_tai = (ve_trai, ve_phai)

        if phu_thuoc_ham_hien_tai in cac_phu_thuoc_ham_da_co:
            return False, (
                f"Phụ thuộc hàm '{ve_trai} → {ve_phai}' bị trùng"
            )

        cac_phu_thuoc_ham_da_co.add(phu_thuoc_ham_hien_tai)

    return True, "Tập phụ thuộc hàm hợp lệ"


# ====================================
# KIỂM TRA TẬP THUỘC TÍNH CẦN TÌM
# ====================================
def kiem_tra_tap_thuoc_tinh_can_tim(tap_thuoc_tinh_can_tim, tap_thuoc_tinh):
    if not isinstance(tap_thuoc_tinh_can_tim, list):
        return False, "Tập thuộc tính cần tìm phải là list"

    if not tap_thuoc_tinh_can_tim:
        return False, "Tập thuộc tính cần tìm không được rỗng"

    tap_thuoc_tinh = set(tap_thuoc_tinh)
    tap_da_gap = set()

    for thuoc_tinh in tap_thuoc_tinh_can_tim:
        if not isinstance(thuoc_tinh, str):
            return False, "Mỗi thuộc tính cần tìm phải là chuỗi"

        if not co_phai_thuoc_tinh_hop_le(thuoc_tinh):
            return False, f"Thuộc tính '{thuoc_tinh}' trong tập cần tìm không hợp lệ"

        thuoc_tinh = thuoc_tinh.strip().upper()

        if thuoc_tinh not in tap_thuoc_tinh:
            return False, f"Thuộc tính '{thuoc_tinh}' không tồn tại trong tập thuộc tính"

        if thuoc_tinh in tap_da_gap:
            return False, f"Thuộc tính '{thuoc_tinh}' bị trùng trong tập cần tìm"

        tap_da_gap.add(thuoc_tinh)

    return True, "Tập thuộc tính cần tìm hợp lệ"


# ====================================
# KIỂM TRA DẠNG CHUẨN
# ====================================
dang_chuan_hop_le = {
    item["value"]
    for item in DANH_SACH_DANG_CHUAN
}

def kiem_tra_dang_chuan(dang_chuan):
    if not isinstance(dang_chuan, str):
        return False, "Dạng chuẩn phải là chuỗi"

    dang_chuan = dang_chuan.strip().upper()

    if dang_chuan not in dang_chuan_hop_le:
        return False, f"Dạng chuẩn '{dang_chuan}' không hợp lệ, phải là 2NF, 3NF hoặc BCNF"

    return True, "Dạng chuẩn hợp lệ"


# ===============================================
# KIỂM TRA FILE ĐƯỢC NẠP LÊN
# ===============================================
def kiem_tra_file_bao_dong_tap_thuoc_tinh(data):
    if not isinstance(data, dict):
        return False, "Dữ liệu file phải là object"

    # 1. Kiểm tra tập thuộc tính
    tap_thuoc_tinh = data.get("tap_thuoc_tinh")

    hop_le, thong_bao = kiem_tra_tap_thuoc_tinh(tap_thuoc_tinh)

    if not hop_le:
        return False, thong_bao

    # 2. Kiểm tra tập phụ thuộc hàm
    tap_phu_thuoc_ham = data.get("tap_phu_thuoc_ham")

    hop_le, thong_bao = kiem_tra_tap_phu_thuoc_ham(tap_phu_thuoc_ham, tap_thuoc_tinh)

    if not hop_le:
        return False, thong_bao

    # 3. Kiểm tra tập thuộc tính cần tìm
    tap_thuoc_tinh_can_tim = data.get("tap_thuoc_tinh_can_tim")

    hop_le, thong_bao = kiem_tra_tap_thuoc_tinh_can_tim(tap_thuoc_tinh_can_tim, tap_thuoc_tinh)

    if not hop_le:
        return False, thong_bao

    return True, "File dạng chuẩn hợp lệ"


def kiem_tra_file_bao_dong_tap_phu_thuoc_ham(data):
    if not isinstance(data, dict):
        return False, "Dữ liệu file phải là object"

    # Kiểm tra tập phụ thuộc hàm
    tap_phu_thuoc_ham = data.get("tap_phu_thuoc_ham")

    hop_le, thong_bao = kiem_tra_tap_phu_thuoc_ham(tap_phu_thuoc_ham, None)

    if not hop_le:
        return False, thong_bao

    return True, "File dạng chuẩn hợp lệ"


def kiem_tra_file_dang_chuan(data):
    if not isinstance(data, dict):
        return False, "Dữ liệu file phải là object"

    # 1. Kiểm tra tập thuộc tính
    tap_thuoc_tinh = data.get("tap_thuoc_tinh")

    hop_le, thong_bao = kiem_tra_tap_thuoc_tinh(tap_thuoc_tinh)

    if not hop_le:
        return False, thong_bao

    # 2. Kiểm tra tập phụ thuộc hàm
    tap_phu_thuoc_ham = data.get("tap_phu_thuoc_ham")

    hop_le, thong_bao = kiem_tra_tap_phu_thuoc_ham(tap_phu_thuoc_ham, tap_thuoc_tinh)

    if not hop_le:
        return False, thong_bao

    # 3. Kiểm tra dạng chuẩn
    dang_chuan = data.get("dang_chuan")

    hop_le, thong_bao = kiem_tra_dang_chuan(dang_chuan)

    if not hop_le:
        return False, thong_bao

    return True, "File dạng chuẩn hợp lệ"
