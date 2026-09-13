from collections import defaultdict
from itertools import combinations

from backend.app.modules.LyThuyetCSDL.bai_giai.bao_dong_tap_thuoc_tinh import tinh_bao_dong_tap_thuoc_tinh
from backend.app.modules.LyThuyetCSDL.utils.chuan_hoa import chuan_hoa_tap_phu_thuoc_ham_sang_tuple, \
    chuan_hoa_tap_thuoc_tinh
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

    tap_phu_thuoc_ham_con_lai = [fd for fd in tap_phu_thuoc_ham_hien_tai if fd != phu_thuoc_ham_can_xet]

    bao_dong, _ = tinh_bao_dong_tap_thuoc_tinh(
        list(ve_trai),
        dinh_dang_tap_phu_thuoc_ham_tuple(tap_phu_thuoc_ham_con_lai)
    )

    bao_dong = set(bao_dong)

    return ve_phai.issubset(bao_dong)


def loai_bo_phu_thuoc_ham_du_thua(tap_pth):
    if not tap_pth:
        return []

    # Phân rã vế phải thành các thuộc tính đơn
    pth_don = []
    for vt, vp in tap_pth:
        vt_set = set(vt) if isinstance(vt, (list, tuple, set)) else {vt}
        vp_set = set(vp) if isinstance(vp, (list, tuple, set)) else {vp}
        for v in vp_set:
            pth_don.append((vt_set, {v}))

    pth_toi_uu_vt = []
    for vt, vp in pth_don:
        vt_moi = set(vt)
        vp_char = list(vp)[0]
        for z in list(vt):
            if len(vt_moi) > 1:
                vt_thu = vt_moi - {z}
                pth_thu_chuoi = dinh_dang_tap_phu_thuoc_ham_tuple([(vt_moi, vp)])
                bao_dong, _ = tinh_bao_dong_tap_thuoc_tinh(vt_thu, pth_thu_chuoi)
                if vp_char in bao_dong:
                    vt_moi.remove(z)
        pth_toi_uu_vt.append((vt_moi, vp))

    pth_ket_qua = []
    for i in range(len(pth_toi_uu_vt)):
        vt_hien_tai, vp_hien_tai = pth_toi_uu_vt[i]
        vp_char = list(vp_hien_tai)[0]

        tap_con_lai = pth_toi_uu_vt[:i] + pth_toi_uu_vt[i + 1:]
        tap_con_lai_chuoi = dinh_dang_tap_phu_thuoc_ham_tuple(tap_con_lai)

        bao_dong, _ = tinh_bao_dong_tap_thuoc_tinh(vt_hien_tai, tap_con_lai_chuoi)

        if vp_char not in bao_dong:
            pth_ket_qua.append((vt_hien_tai, vp_hien_tai))

    return pth_ket_qua


def co_phai_sieu_khoa(tap_thuoc_tinh_can_tim, tap_thuoc_tinh, tap_phu_thuoc_ham):
    tap_thuoc_tinh = set(
        chuan_hoa_tap_thuoc_tinh(tap_thuoc_tinh)
    )

    bao_dong, _ = tinh_bao_dong_tap_thuoc_tinh(
        tap_thuoc_tinh_can_tim,
        tap_phu_thuoc_ham
    )

    bao_dong = set(bao_dong)

    return tap_thuoc_tinh.issubset(bao_dong)


def cac_thuoc_tinh_trong_khoa_ung_vien(cac_khoa_ung_vien):
    cac_thuoc_tinh_trong_khoa_ung_vien = set()

    for khoa in cac_khoa_ung_vien:
        cac_thuoc_tinh_trong_khoa_ung_vien.update(set(khoa))

    return cac_thuoc_tinh_trong_khoa_ung_vien


def loc_phu_thuoc_ham(tap_thuoc_tinh, tap_phu_thuoc_ham):
    tap_thuoc_tinh = chuan_hoa_tap_thuoc_tinh(tap_thuoc_tinh)
    danh_sach_pth = chuan_hoa_tap_phu_thuoc_ham_sang_tuple(tap_phu_thuoc_ham)

    phu_thuoc_ham_duoc_loc_lai = []

    for ve_trai, ve_phai in danh_sach_pth:
        # 1. Vế trái phải nằm hoàn toàn trong tập thuộc tính
        if not ve_trai.issubset(tap_thuoc_tinh):
            continue

        # 2. Bỏ các thuộc tính ở vế phải không nằm trong tập thuộc tính
        giao = ve_phai & tap_thuoc_tinh

        # 3. Bỏ các thuộc tính ở vế phải đã có ở vế trái
        ve_phai_moi = giao - ve_trai

        if ve_phai_moi:
            phu_thuoc_ham_duoc_loc_lai.append((ve_trai, ve_phai_moi))

    return phu_thuoc_ham_duoc_loc_lai


def tim_phu_thuoc_ham_vong(tap_phu_thuoc_ham):
    phu_thuoc_ham_vong = {}

    for ve_trai, ve_phai in tap_phu_thuoc_ham:
        tap_phu_thuoc_ham_tam = []

        tap_thuoc_tinh_bat_dau = ve_trai
        tap_thuoc_tinh_dang_xet = ve_phai

        tap_phu_thuoc_ham_tam.append(
            (tap_thuoc_tinh_bat_dau, tap_thuoc_tinh_dang_xet)
        )

        for ve_trai_moi, ve_phai_moi in tap_phu_thuoc_ham:
            if tap_thuoc_tinh_dang_xet == ve_trai_moi:
                tap_thuoc_tinh_dang_xet = ve_phai_moi

                tap_phu_thuoc_ham_tam.append(
                    (ve_trai_moi, ve_phai_moi)
                )

        if tap_thuoc_tinh_dang_xet == tap_thuoc_tinh_bat_dau:

            tap_thuoc_tinh_trong_phu_thuoc_ham_vong = set()

            for ve_trai_moi, ve_phai_moi in tap_phu_thuoc_ham_tam:
                tap_thuoc_tinh_trong_phu_thuoc_ham_vong.update(
                    ve_trai_moi
                )
                tap_thuoc_tinh_trong_phu_thuoc_ham_vong.update(
                    ve_phai_moi
                )

            if tap_thuoc_tinh_trong_phu_thuoc_ham_vong:
                khoa_nhom = tuple(
                    sorted(tap_thuoc_tinh_trong_phu_thuoc_ham_vong)
                )

                if khoa_nhom not in phu_thuoc_ham_vong:
                    phu_thuoc_ham_vong[khoa_nhom] = tap_phu_thuoc_ham_tam

    return phu_thuoc_ham_vong


def gom_phu_thuoc_ham_vi_pham(danh_sach_vi_pham, tap_phu_thuoc_ham, thuoc_tinh_khong_khoa):
    if not danh_sach_vi_pham:
        return []

    # Tính bao đóng từng vế trái trong tập phụ thuộc hàm
    tap_khong_khoa = set(thuoc_tinh_khong_khoa)
    danh_sach_bao_dong = {}

    for ve_trai, ve_phai in danh_sach_vi_pham:
        tap_ve_trai = set(ve_trai)
        if frozenset(tap_ve_trai) not in danh_sach_bao_dong:
            bao_dong_day_du, _ = tinh_bao_dong_tap_thuoc_tinh(tap_ve_trai, tap_phu_thuoc_ham)

            # Chỉ giữ lại vế trái và các thuộc tính không khóa trong bao đóng
            thuoc_tinh_trong_bang_moi = (bao_dong_day_du & tap_khong_khoa) | tap_ve_trai
            danh_sach_bao_dong[frozenset(tap_ve_trai)] = thuoc_tinh_trong_bang_moi

    # Loại bỏ vế trái có bao đóng bị bao hàm hoàn toàn bởi bao đóng khác
    danh_sach_ve_trai = list(danh_sach_bao_dong.keys())
    danh_sach_ve_trai_dai_dien = []

    for vi_tri_1, ve_trai_1 in enumerate(danh_sach_ve_trai):
        bao_dong_1 = danh_sach_bao_dong[ve_trai_1]
        la_bao_dong_con = False
        for vi_tri_2, ve_trai_2 in enumerate(danh_sach_ve_trai):
            # 2 phụ thuộc hàm khác nhau mới xét
            if vi_tri_1 != vi_tri_2:
                bao_dong_2 = danh_sach_bao_dong[ve_trai_2]
                # Nếu bao_dong_1 là tập con thực sự của bao_dong_2
                if bao_dong_1 < bao_dong_2:
                    la_bao_dong_con = True
                    break
                # Nếu 2 bao đóng bằng nhau, giữ lại vế trái có kích thước nhỏ hơn (hoặc xuất hiện trước)
                elif bao_dong_1 == bao_dong_2 and len(ve_trai_1) > len(ve_trai_2):
                    la_bao_dong_con = True
                    break
        if not la_bao_dong_con:
            danh_sach_ve_trai_dai_dien.append(ve_trai_1)

    # Gom các PTH vi phạm vào nhóm đại diện tương ứng
    nhom_phu_thuoc_ham = defaultdict(list)
    for ve_trai in danh_sach_ve_trai_dai_dien:
        thuoc_tinh_trong_bang_moi = danh_sach_bao_dong[ve_trai]
        for ve_trai_pth, ve_phai_pth in danh_sach_vi_pham:
            ve_trai_pth = set(ve_trai_pth)
            ve_phai_pth = set(ve_phai_pth)
            # PTH thuộc nhóm nếu cả vế trái và vế phải nằm trong bao đóng đại diện
            if ve_trai_pth.issubset(thuoc_tinh_trong_bang_moi) and ve_phai_pth.issubset(thuoc_tinh_trong_bang_moi):
                nhom_phu_thuoc_ham[frozenset(thuoc_tinh_trong_bang_moi)].append((ve_trai_pth, ve_phai_pth))

    # Chuyển đổi kết quả về dạng danh sách tuple (set(ve_trai_dai_dien), danh_sach_pth)
    ket_qua = []
    for ve_trai, danh_sach_pth in nhom_phu_thuoc_ham.items():
        ket_qua.append((set(ve_trai), danh_sach_pth))

    return ket_qua


def gom_phu_thuoc_ham_theo_ve_trai(tap_phu_thuoc_ham):
    nhom_pth = {}
    for pth in tap_phu_thuoc_ham:
        ve_trai, ve_phai = pth
        ve_trai = tuple(sorted(list(ve_trai)))
        if ve_trai not in nhom_pth:
            nhom_pth[ve_trai] = []
        nhom_pth[ve_trai].append(pth)

    return [(set(vt), ds) for vt, ds in nhom_pth.items()]


# ==================================================
# Hỗ trợ nâng dạng chuẩn 2
# ==================================================
def tim_phu_thuoc_bo_phan_voi_khoa(ve_trai, ve_phai, danh_sach_khoa_ung_vien):
    ve_trai = set(chuan_hoa_tap_thuoc_tinh(ve_trai))
    ve_phai = set(chuan_hoa_tap_thuoc_tinh(ve_phai))

    tap_thuoc_tinh_khoa = cac_thuoc_tinh_trong_khoa_ung_vien(danh_sach_khoa_ung_vien)

    if not ve_phai.isdisjoint(tap_thuoc_tinh_khoa):
        return []

    cac_khoa_vi_pham = []

    for khoa in danh_sach_khoa_ung_vien:
        cac_thuoc_tinh_trong_khoa = set(khoa)

        if ve_trai < cac_thuoc_tinh_trong_khoa:
            cac_khoa_vi_pham.append(khoa)

    return cac_khoa_vi_pham


def tim_phu_thuoc_ham_vi_pham_dang_chuan_2(tap_phu_thuoc_ham, cac_khoa_ung_vien):
    """
    Tìm phụ thuộc hàm có thuộc tính không khóa phụ thuộc bộ phận vào khóa
    """
    danh_sach_pth_vi_pham = []

    danh_sach_phu_thuoc_ham = chuan_hoa_tap_phu_thuoc_ham_sang_tuple(tap_phu_thuoc_ham)

    for ve_trai, ve_phai in danh_sach_phu_thuoc_ham:

        cac_khoa_vi_pham = tim_phu_thuoc_bo_phan_voi_khoa(
            ve_trai,
            ve_phai,
            cac_khoa_ung_vien
        )

        for khoa_vi_pham in cac_khoa_vi_pham:
            danh_sach_pth_vi_pham.append((ve_trai, ve_phai, khoa_vi_pham))

    return danh_sach_pth_vi_pham


# ==================================================
# Hỗ trợ nâng dạng chuẩn 3
# ==================================================
def tim_phu_thuoc_ham_vi_pham_dang_chuan_3(tap_thuoc_tinh, tap_phu_thuoc_ham, cac_khoa_ung_vien):
    danh_sach_pth_vi_pham = []
    cac_thuoc_tinh_khoa = cac_thuoc_tinh_trong_khoa_ung_vien(cac_khoa_ung_vien)
    danh_sach_phu_thuoc_ham = chuan_hoa_tap_phu_thuoc_ham_sang_tuple(tap_phu_thuoc_ham)

    for ve_trai, ve_phai in danh_sach_phu_thuoc_ham:
        # 1. Kiểm tra vế trái có phải siêu khóa không
        la_sieu_khoa = co_phai_sieu_khoa(ve_trai, tap_thuoc_tinh, tap_phu_thuoc_ham)
        if la_sieu_khoa:
            continue

        # 2. Tìm các thuộc tính ở vế phải KHÔNG nằm trong thuộc tính khóa
        ve_phai_khong_khoa = {tt for tt in ve_phai if tt not in cac_thuoc_tinh_khoa}

        # Nếu tồn tại thuộc tính không khóa phụ thuộc vào X -> Vi phạm 3NF
        if ve_phai_khong_khoa:
            phu_thuoc_ham = (set(ve_trai), set(ve_phai))
            if phu_thuoc_ham not in danh_sach_pth_vi_pham:
                danh_sach_pth_vi_pham.append(phu_thuoc_ham)

    return danh_sach_pth_vi_pham


# ==================================================
# Hỗ trợ nâng dạng chuẩn Boyce-Codd
# ==================================================
def tim_phu_thuoc_ham_vi_pham_bcnf(tap_thuoc_tinh, tap_phu_thuoc_ham):
    tap_thuoc_tinh = set(chuan_hoa_tap_thuoc_tinh(tap_thuoc_tinh))
    tap_phu_thuoc_ham_tuple = chuan_hoa_tap_phu_thuoc_ham_sang_tuple(tap_phu_thuoc_ham)
    danh_sach_pth_str = dinh_dang_tap_phu_thuoc_ham_tuple(tap_phu_thuoc_ham_tuple)

    danh_sach_pth_vi_pham = []

    for ve_trai, ve_phai in tap_phu_thuoc_ham_tuple:
        ve_trai_set = set(ve_trai)
        ve_phai_set = set(ve_phai)

        # 1. Chỉ xét PTH có cả 2 vế thuộc quan hệ hiện tại
        if not ve_trai_set.issubset(tap_thuoc_tinh):
            continue

        ve_phai_trong_R = ve_phai_set & tap_thuoc_tinh
        if not ve_phai_trong_R:
            continue

        # 2. Bỏ qua PTH hiển nhiên
        if ve_phai_trong_R.issubset(ve_trai_set):
            continue

        # 3. Tính bao đóng của vế trái trong quan hệ hiện tại
        bao_dong, _ = tinh_bao_dong_tap_thuoc_tinh(list(ve_trai_set), danh_sach_pth_str)
        bao_dong_trong_R = set(bao_dong) & tap_thuoc_tinh

        # Nếu bao đóng trong R không phủ hết R -> vế trái không phải Siêu khóa -> VI PHẠM BCNF
        if not tap_thuoc_tinh.issubset(bao_dong_trong_R):
            danh_sach_pth_vi_pham.append((ve_trai_set, ve_phai_trong_R))

    return danh_sach_pth_vi_pham

if __name__ == '__main__':
    tap_thuoc_tinh = [
        ["A", "B", "C"],
        ["A", "B", "C"],
        ["A", "B", "C", "D"],
        ["A", "B", "C", "D"],
        ["A", "B", "C"],
        ["A", "B", "C"],
        ["A", "B", "C", "D"],
        ["A", "B", "C", "D", "E"],
        ["A", "B", "C", "D", "E"],
        ["A", "B", "C", "D", "E", "F"]
    ]

    tap_phu_thuoc_ham = [
        ["A → B", "B → C"],
        ["AB → C"],
        ["A → B", "B → C", "C → D"],
        ["A → B", "A → C", "B → D"],
        ["A → B", "B → A", "A → C"],
        ["AB → C", "C → B"],
        ["A → B", "B → C", "C → A", "A → D"],
        ["A → B", "B → C", "D → E"],
        ["AB → C", "C → D", "D → E"],
        ["AB → C", "C → A", "C → D", "D → E", "E → F"]
    ]
