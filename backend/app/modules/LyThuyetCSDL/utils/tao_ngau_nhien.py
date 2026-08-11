import random
import string


def tao_tap_thuoc_tinh_ngau_nhien(so_thuoc_tinh_toi_thieu=5, so_thuoc_tinh_toi_da=7):
    kich_thuoc = random.randint(so_thuoc_tinh_toi_thieu, so_thuoc_tinh_toi_da)
    return list(string.ascii_uppercase[:kich_thuoc])


def tao_tap_phu_thuoc_ham_ngau_nhien(tap_thuoc_tinh=None, so_luong_phu_thuoc_ham=None):
    if so_luong_phu_thuoc_ham is None:
        so_luong_phu_thuoc_ham = random.randint(len(tap_thuoc_tinh),len(tap_thuoc_tinh) + 2)

    tap_phu_thuoc_ham = []

    while len(tap_phu_thuoc_ham) < so_luong_phu_thuoc_ham:
        so_luong_thuoc_tinh_o_ve_trai = 1 if random.random() < 0.7 else 2

        ve_trai = sorted(random.sample(tap_thuoc_tinh, so_luong_thuoc_tinh_o_ve_trai))

        thuoc_tinh_co_the_o_ve_phai = [
            attr for attr in tap_thuoc_tinh
            if attr not in ve_trai
        ]

        if not thuoc_tinh_co_the_o_ve_phai:
            continue

        ve_phai = random.sample(thuoc_tinh_co_the_o_ve_phai, 1)

        if (ve_trai, ve_phai) in tap_phu_thuoc_ham:
            continue

        tap_phu_thuoc_ham.append((ve_trai, ve_phai))

    return tap_phu_thuoc_ham


def tao_tap_thuoc_tinh_can_tim_ngau_nhien(tap_thuoc_tinh, so_thuoc_tinh_toi_thieu=1, so_thuoc_tinh_toi_da=2):
    kich_thuoc = random.randint(so_thuoc_tinh_toi_thieu, so_thuoc_tinh_toi_da)
    return sorted(random.sample(tap_thuoc_tinh, kich_thuoc))


def tao_dang_dang_chuan_ngau_nhien():
    return random.choice(["2NF", "3NF", "BCNF"])

if __name__ == "__main__":
    print(tao_tap_phu_thuoc_ham_ngau_nhien(
        tap_thuoc_tinh=tao_tap_thuoc_tinh_ngau_nhien(),
        so_luong_phu_thuoc_ham=None
    ))