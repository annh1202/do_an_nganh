# ====================<< FORMAT ATTRIBUTE >>====================
def dinh_dang_tap_thuoc_tinh(s):
    return ", ".join(sorted(set(s)))


# ====================<< FORMAT FD >>====================
def dinh_dang_mot_ve_phu_thuoc_ham(fd_side):
    return "".join(sorted(fd_side))


def dinh_dang_phu_thuoc_ham(ve_trai, ve_phai):
    return f"{dinh_dang_mot_ve_phu_thuoc_ham(ve_trai)} → {dinh_dang_mot_ve_phu_thuoc_ham(ve_phai)}"


def dinh_dang_tap_phu_thuoc_ham(fds_raw):
    return [
        dinh_dang_phu_thuoc_ham(lhs, rhs)
        for lhs, rhs in fds_raw
        if lhs and rhs
    ]