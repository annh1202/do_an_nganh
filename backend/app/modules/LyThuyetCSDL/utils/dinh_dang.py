# ==================================
# ĐỊNH DẠNG TẬP THUỘC TÍNH
# ==================================

def dinh_dang_tap_thuoc_tinh(tap_thuoc_tinh):
    return ", ".join(sorted(set(tap_thuoc_tinh)))

# ==================================
# ĐỊNH DẠNG TẬP PHỤ THUỘC HÀM
# ==================================

def dinh_dang_chuoi_tap_thuoc_tinh(mot_ve_phu_thuoc_ham):
    return "".join(sorted(mot_ve_phu_thuoc_ham))


def dinh_dang_phu_thuoc_ham(ve_trai, ve_phai):
    return f"{dinh_dang_chuoi_tap_thuoc_tinh(ve_trai)} → {dinh_dang_chuoi_tap_thuoc_tinh(ve_phai)}"


def dinh_dang_tap_phu_thuoc_ham_object(tap_phu_thuoc_ham):
    return [
        dinh_dang_phu_thuoc_ham(
            phu_thuoc_ham.ve_trai,
            phu_thuoc_ham.ve_phai
        )
        for phu_thuoc_ham in tap_phu_thuoc_ham
        if phu_thuoc_ham.ve_trai and phu_thuoc_ham.ve_phai
    ]


def dinh_dang_tap_phu_thuoc_ham_tuple(tap_phu_thuoc_ham):
    return [
        dinh_dang_phu_thuoc_ham(ve_trai, ve_phai)
        for ve_trai, ve_phai in tap_phu_thuoc_ham
        if ve_trai and ve_phai
    ]