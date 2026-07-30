from backend.app.modules.LyThuyetCSDL.schemas import PhuThuocHam


# ====================<< NORMALIZE ATTRIBUTES >>====================
def chuan_hoa_thuoc_tinh(thuoc_tinh_tho):
    return thuoc_tinh_tho.strip().upper()


def chuan_hoa_tap_thuoc_tinh(tap_thuoc_tinh_tho):
    return set(chuan_hoa_thuoc_tinh(thuoc_tinh_tho) for thuoc_tinh_tho in tap_thuoc_tinh_tho)


# ====================<< NORMALIZE FDS >>====================
def chuyen_tap_phu_thuoc_ham_sang_dang_class(tap_phu_thuoc_ham):
    ket_qua = []

    for phu_thuoc_ham in tap_phu_thuoc_ham:
        ve_trai, ve_phai = map(str.strip, phu_thuoc_ham.split("→"))
        ket_qua.append(
            PhuThuocHam(
                ve_trai=ve_trai,
                ve_phai=ve_phai
            )
        )

    return ket_qua

def chuan_hoa_phu_thuoc_ham_sang_tuple(phu_thuoc_ham_dang_string):
    if "→" in phu_thuoc_ham_dang_string:
        ve_trai, ve_phai = phu_thuoc_ham_dang_string.split("→")
    elif "->" in phu_thuoc_ham_dang_string:
        ve_trai, ve_phai = phu_thuoc_ham_dang_string.split("->")
    else:
        return None

    tap_hop_thuoc_tinh_ve_trai = frozenset(ve_trai.replace(" ", "").upper())
    tap_hop_thuoc_tinh_ve_phai = frozenset(ve_phai.replace(" ", "").upper())

    return tap_hop_thuoc_tinh_ve_trai, tap_hop_thuoc_tinh_ve_phai


def chuan_hoa_tap_phu_thuoc_ham_sang_tuple(tap_phu_thuoc_ham_tho):
    return [
        da_chuan_hoa
        for phu_thuoc_ham in tap_phu_thuoc_ham_tho
        if (da_chuan_hoa := chuan_hoa_phu_thuoc_ham_sang_tuple(phu_thuoc_ham))
    ]


def chuan_hoa_mot_ve_phu_thuoc_ham(cac_thuoc_tinh):
    return frozenset(chuan_hoa_thuoc_tinh(thuoc_tinh) for thuoc_tinh in cac_thuoc_tinh)