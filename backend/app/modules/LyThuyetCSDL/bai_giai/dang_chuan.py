from backend.app.modules.LyThuyetCSDL.bai_giai.bao_dong_tap_thuoc_tinh import tinh_bao_dong_tap_thuoc_tinh
from backend.app.modules.LyThuyetCSDL.bai_giai.khoa_ung_vien import tim_khoa_ung_vien
from backend.app.modules.LyThuyetCSDL.utils.chuan_hoa import chuan_hoa_tap_thuoc_tinh, \
    chuan_hoa_tap_phu_thuoc_ham_sang_tuple
from backend.app.modules.LyThuyetCSDL.utils.dinh_dang import dinh_dang_tap_thuoc_tinh, dinh_dang_chuoi_tap_thuoc_tinh, \
    dinh_dang_phu_thuoc_ham


# ========================================
# CÁC HÀM HỖ TRỢ
# ========================================
def co_phai_sieu_khoa(tap_thuoc_tinh_can_tim, tap_thuoc_tinh, tap_phu_thuoc_ham):
    bao_dong, _ = tinh_bao_dong_tap_thuoc_tinh(tap_thuoc_tinh_can_tim, tap_phu_thuoc_ham)

    return bao_dong == chuan_hoa_tap_thuoc_tinh(tap_thuoc_tinh)


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


def co_phai_phu_thuoc_bo_phan_voi_khoa(ve_trai, ve_phai, danh_sach_khoa_ung_vien, tap_thuoc_tinh_khoa):
    ve_trai = chuan_hoa_tap_thuoc_tinh(ve_trai)

    # Chỉ quan tâm phụ thuộc hàm của thuộc tính không phải khóa vào khóa.
    if ve_phai in tap_thuoc_tinh_khoa:
        return False

    for khoa in danh_sach_khoa_ung_vien:
        cac_thuoc_tinh_trong_khoa = set(khoa)

        if ve_trai < cac_thuoc_tinh_trong_khoa:
            return True

    return False


def tim_phu_thuoc_ham_vi_pham_dang_chuan_2(tap_phu_thuoc_ham, cac_khoa_ung_vien):
    danh_sach_vi_pham = []

    cac_thuoc_tinh_khoa = cac_thuoc_tinh_trong_khoa_ung_vien(cac_khoa_ung_vien)
    danh_sach_phu_thuoc_ham = chuan_hoa_tap_phu_thuoc_ham_sang_tuple(tap_phu_thuoc_ham)

    for ve_trai, ve_phai in danh_sach_phu_thuoc_ham:
        # cần biết từng thuộc tính không phải khóa có phụ thuộc bộ phận hay không
        for thuoc_tinh in ve_phai:
            if thuoc_tinh in cac_thuoc_tinh_khoa:
                continue

            if co_phai_phu_thuoc_bo_phan_voi_khoa(
                    ve_trai,
                    thuoc_tinh,
                    cac_khoa_ung_vien,
                    cac_thuoc_tinh_khoa
            ):
                danh_sach_vi_pham.append({
                    "ve_trai": ve_trai,
                    "ve_phai": thuoc_tinh,
                    "ly_do": (
                        f"{dinh_dang_phu_thuoc_ham(ve_trai, thuoc_tinh)} "
                        f"là phụ thuộc bộ phận với khóa"
                    )
                })

    return danh_sach_vi_pham


# ========================================
# NÂNG DẠNG CHUẨN 2
# ========================================
def phan_ra_sang_dang_chuan_2(tap_thuoc_tinh, tap_phu_thuoc_ham):
    # 1. Tìm khóa ứng viên & kiểm tra vi phạm
    danh_sach_khoa_ung_vien, _ = tim_khoa_ung_vien(tap_thuoc_tinh, tap_phu_thuoc_ham)
    if not danh_sach_khoa_ung_vien:
        return "Không tìm thấy khóa ứng viên.", ["Lỗi: Không tìm thấy khóa ứng viên cho tập thuộc tính này."]

    danh_sach_vi_pham = tim_phu_thuoc_ham_vi_pham_dang_chuan_2(tap_phu_thuoc_ham, danh_sach_khoa_ung_vien)

    # 2. Phân loại thuộc tính
    cac_thuoc_tinh_khoa = cac_thuoc_tinh_trong_khoa_ung_vien(danh_sach_khoa_ung_vien)
    tap_thuoc_tinh_chuan = set(chuan_hoa_tap_thuoc_tinh(tap_thuoc_tinh))
    cac_thuoc_tinh_khong_khoa = tap_thuoc_tinh_chuan - set(cac_thuoc_tinh_khoa)

    # 3. Lọc các vế trái tối thiểu vi phạm
    cac_ve_trai_vi_pham = []
    for vp in danh_sach_vi_pham:
        vt = set(vp["ve_trai"])
        if vt not in cac_ve_trai_vi_pham:
            cac_ve_trai_vi_pham.append(vt)

    cac_ve_trai_toi_thieu = [
        vt for vt in cac_ve_trai_vi_pham
        if not any(v_khac != vt and v_khac < vt for v_khac in cac_ve_trai_vi_pham)
    ]

    # 4. Khởi tạo dữ liệu phân rã
    danh_sach_bang_dict = []
    danh_sach_chuoi_bang = []
    cac_buoc_giai = []
    tap_thuoc_tinh_con_lai = set(tap_thuoc_tinh_chuan)

    cac_khoa_str = ", ".join(dinh_dang_chuoi_tap_thuoc_tinh(k) for k in danh_sach_khoa_ung_vien)
    danh_sach_chuoi_bang.append(f"Các khóa ứng viên: {cac_khoa_str}")

    # 5. Phân rã các phụ thuộc bộ phận
    for ve_trai in cac_ve_trai_toi_thieu:
        bao_dong, _ = tinh_bao_dong_tap_thuoc_tinh(list(ve_trai), tap_phu_thuoc_ham)
        tt_phu_thuoc = set(bao_dong) & cac_thuoc_tinh_khong_khoa

        if not tt_phu_thuoc:
            continue

        tt_bang_moi = ve_trai | tt_phu_thuoc
        if any(b["thuoc_tinh"] == tt_bang_moi for b in danh_sach_bang_dict):
            continue

        so_quan_he = len(danh_sach_bang_dict) + 1
        ten_quan_he = f"R{so_quan_he}"

        pth_loc = loc_phu_thuoc_ham(tt_bang_moi, tap_phu_thuoc_ham)
        pth_str = ", ".join([dinh_dang_phu_thuoc_ham(vt, vp) for vt, vp in pth_loc]) if pth_loc else "Không có"
        tt_bang_moi_str = dinh_dang_tap_thuoc_tinh(tt_bang_moi)

        danh_sach_bang_dict.append({"ten": ten_quan_he, "thuoc_tinh": tt_bang_moi})
        danh_sach_chuoi_bang.append(f"{ten_quan_he}({tt_bang_moi_str}) với F_{ten_quan_he} = {{ {pth_str} }}")

        # Tạo giải thích
        khoa_lien_quan = [k for k in danh_sach_khoa_ung_vien if ve_trai < set(k)]
        khoa_str = dinh_dang_chuoi_tap_thuoc_tinh(khoa_lien_quan[0]) if khoa_lien_quan else ""

        cac_buoc_giai.append(
            f"Tạo {ten_quan_he}({tt_bang_moi_str}) "
            f"do {dinh_dang_phu_thuoc_ham(ve_trai, tt_phu_thuoc)} phụ thuộc bộ phận với khóa {khoa_str}"
        )

        tap_thuoc_tinh_con_lai -= tt_phu_thuoc

    # 6. Đảm bảo bảo toàn khóa và thuộc tính còn lại
    khoa_dai_nhat = set(max(danh_sach_khoa_ung_vien, key=len))
    co_quan_he_chua_khoa = any(khoa_dai_nhat.issubset(b["thuoc_tinh"]) for b in danh_sach_bang_dict)

    if not co_quan_he_chua_khoa:
        so_quan_he = len(danh_sach_bang_dict) + 1
        ten_quan_he = f"R{so_quan_he}"
        tt_quan_he_cuoi = tap_thuoc_tinh_con_lai | khoa_dai_nhat

        pth_cuoi = loc_phu_thuoc_ham(tt_quan_he_cuoi, tap_phu_thuoc_ham)
        pth_cuoi_str = ", ".join([dinh_dang_phu_thuoc_ham(vt, vp) for vt, vp in pth_cuoi]) if pth_cuoi else "Không có"
        tt_cuoi_str = dinh_dang_tap_thuoc_tinh(tt_quan_he_cuoi)

        danh_sach_chuoi_bang.append(f"{ten_quan_he}({tt_cuoi_str}) với F_{ten_quan_he} = {{ {pth_cuoi_str} }}")
        cac_buoc_giai.append(
            f"Tạo {ten_quan_he}({tt_cuoi_str}) chứa các thuộc tính còn lại và khóa ứng viên {dinh_dang_chuoi_tap_thuoc_tinh(khoa_dai_nhat)}."
        )

    return "\n".join(danh_sach_chuoi_bang), cac_buoc_giai

# ========================================
# NÂNG DẠNG CHUẨN 3
# ========================================


# ========================================
# NÂNG DẠNG CHUẨN BOYCE-CODD
# ========================================



# def find_cyclic_fd(fds):
#     cyclic_groups = []
#     cyclic_fds_map = {}
#
#     for l, r in fds:
#         fds_temp = []
#         start = l
#         run = r
#         fds_temp.append((start, run))
#
#         for lhs, rhs in fds:
#             if run == lhs:
#                 run = rhs
#                 fds_temp.append((lhs, rhs))
#
#         if run == start:
#             # 1. Gom thuộc tính của chu trình
#             cycle_attrs = set()
#             for lhs, rhs in fds_temp:
#                 cycle_attrs.update(lhs)
#                 cycle_attrs.update(rhs)
#
#             if len(cycle_attrs) > 0:
#                 group_key = tuple(sorted(list(cycle_attrs)))
#
#                 # 2. Nếu nhóm này chưa tồn tại, lưu cả nhóm lẫn tập PTH tạo nên nó
#                 if cycle_attrs not in cyclic_groups:
#                     cyclic_groups.append(cycle_attrs)
#                     cyclic_fds_map[group_key] = fds_temp
#
#     return cyclic_groups, cyclic_fds_map
#
# # Decompose to 3NF
# def decompose_to_3nf(all_attrs, fds_raw):
#     steps = []
#
#     # 1. Chuẩn hóa dữ liệu đầu vào và tìm các khóa ứng viên
#     all_attrs_set = normalize_attrs(all_attrs)
#     candidate_keys, _ = find_candidate_keys(all_attrs, fds_raw)
#     fds = normalize_fds_to_tuple(fds_raw)
#
#     # steps.append(f"-> Khóa ứng viên tìm được từ lược đồ gốc: {format_attrs(candidate_keys)} {candidate_keys}")
#
#     # 2. Phát hiện các nhóm tuần hoàn (Chu trình bắc cầu khép kín)
#     cyclic_groups, cyclic_fds_map = find_cyclic_fd(fds)
#
#     if cyclic_groups:
#         steps.append(f"Tìm các nhóm phụ thuộc tuần hoàn: {[format_fds(f) for f in list(cyclic_fds_map.values())]}")
#
#     relations_accumulator = []  # Lưu trữ các tập thuộc tính bảng con tạm thời
#     used_fds = set()  # Đánh dấu các PTH đã được xử lý xong
#
#     # BƯỚC 1: Ưu tiên xây dựng các lược đồ con từ nhóm phụ thuộc tuần hoàn trước
#     for group in cyclic_groups:
#         relations_accumulator.append(group)
#         group_key = tuple(sorted(list(group)))
#
#         # Đánh dấu các PTH tạo nên chu trình này là đã dùng để tránh tách rời ở bước sau
#         if group_key in cyclic_fds_map:
#             for lhs, rhs in cyclic_fds_map[group_key]:
#                 used_fds.add((lhs, rhs))
#         steps.append(f"- Tạo lược đồ con {{ {format_attrs(group)} }} từ nhóm phụ thuộc tuần hoàn.")
#
#     # BƯỚC 2: Duyệt các PTH còn lại (không nằm trong chu trình) để tạo bảng con
#     for lhs, rhs in fds:
#         if (lhs, rhs) in used_fds:
#             continue
#
#         relation = set(lhs) | set(rhs)
#
#         # Nếu PTH này nằm lọt thỏm trong một nhóm tuần hoàn đã tạo -> Bỏ qua luôn
#         is_sub_group = any(relation.issubset(group) for group in cyclic_groups)
#         if is_sub_group:
#             continue
#
#         # Kiểm tra điều kiện phủ thông minh: Thuộc tính của PTH này đã xuất hiện rải rác
#         # và được liên kết hoàn toàn ở các bảng tuần hoàn / bảng trước đó chưa?
#         all_discovered_attrs = set().union(*relations_accumulator) if relations_accumulator else set()
#         if relation.issubset(all_discovered_attrs):
#             # Nếu đã phủ hoàn toàn, bỏ qua không tạo bảng dư thừa (Tránh tạo các bảng như R(A,C,G))
#             lhs_str = "".join(sorted(list(lhs)))
#             rhs_str = "".join(sorted(list(rhs)))
#             steps.append(
#                 f"- Không tạo bảng với phụ thuộc hàm {lhs_str}→{rhs_str} vì các thuộc tính đã được bảo toàn liên kết.")
#             continue
#
#         # Nếu chưa được phủ, tiến hành tách bảng mới bình thường
#         relations_accumulator.append(relation)
#         lhs_str = "".join(sorted(list(lhs)))
#         rhs_str = "".join(sorted(list(rhs)))
#         steps.append(f"- Tạo lược đồ con {{ {format_attrs(relation)} }} từ phụ thuộc hàm: {lhs_str} → {rhs_str}")
#
#     # BƯỚC 3: Loại bỏ các lược đồ con bị bao hàm lẫn nhau (Dư thừa thuộc tính)
#     final_sets = []
#     for r in relations_accumulator:
#         if not any(r < other for other in relations_accumulator):
#             if r not in final_sets:
#                 final_sets.append(r)
#         else:
#             steps.append(f"- Bỏ lược đồ {format_attrs(r)} do bị bao hàm hoàn toàn bởi lược đồ lớn hơn.")
#
#     # BƯỚC 4: Đảm bảo tính bảo toàn khóa ứng viên (Quy tắc bổ sung của Synthesis Approach)
#     has_key = False
#     for r in final_sets:
#         for key in candidate_keys:
#             if set(key).issubset(r):
#                 has_key = True
#                 break
#         if has_key:
#             break
#
#     # Nếu chưa có bất kỳ bảng con nào ôm trọn vẹn một khóa ứng viên -> Bù thêm bảng chứa khóa đại diện
#     if not has_key:
#         chosen_key = set(candidate_keys[0])
#         final_sets.append(chosen_key)
#         steps.append(
#             f"- Chưa có lược đồ con nào chứa trọn vẹn một khóa gốc. Thêm quan hệ bù: {format_attrs(chosen_key)}")
#
#     # BƯỚC 5: Đóng gói dữ liệu đầu ra và gán phụ thuộc hàm cục bộ siêu sạch
#     final_relations = []
#     steps.append("\n=> Các lược đồ con có được sau khi phân tách:")
#
#     for idx, r_set in enumerate(final_sets, start=1):
#         r_key = tuple(sorted(list(r_set)))
#
#         # Nếu bảng con này là kết quả của một nhóm tuần hoàn, gán luôn tập PTH chu trình cốt lõi
#         if r_key in cyclic_fds_map:
#             projected_local_fds = cyclic_fds_map[r_key]
#         else:
#             # Nếu là bảng bình thường, tính phép chiếu project_fds như cũ
#             projected_local_fds = project_fds(r_set, fds_raw)
#
#         final_relations.append({
#             "name": f"R{idx}",
#             "attrs": r_set,
#             "fds": projected_local_fds
#         })
#
#         steps.append(f"+ R{idx} {{ {format_attrs(r_set)} }} có tập phụ thuộc hàm: {format_fds([x for x in projected_local_fds])}")
#
#     return final_relations, steps
#
# # Project fds
# def project_fds(attrs, fds_raw):
#     attrs = normalize_attrs(attrs)
#     fds = normalize_fds_to_tuple(fds_raw)
#
#     projected = []
#
#     for lhs, rhs in fds:
#
#         if not lhs.issubset(attrs):
#             continue
#
#         rhs_in = rhs & attrs
#
#         if not rhs_in:
#             continue
#
#         # bỏ FD tầm thường
#         rhs_in -= lhs
#
#         if rhs_in:
#             projected.append((lhs, rhs_in))
#
#     return projected
#
# def powerset(s):
#     s = list(s)
#
#     for r in range(1, len(s) + 1):
#         for combo in combinations(s, r):
#             yield set(combo)
#
# def project_fds_full(attrs, fds_raw):
#     attrs = normalize_attrs(attrs)
#
#     projected = []
#
#     for lhs in powerset(attrs):
#
#         closure, _ = compute_closure_of_attrs(lhs, fds_raw)
#
#         closure &= attrs
#
#         for attr in (closure - lhs):
#             projected.append((lhs, {attr}))
#
#     return projected
#
# # Decompose to BCNF
# def decompose_to_bcnf(all_attrs, fds_raw):
#     result = []
#     steps = []
#     counter = 1
#
#     def rec(attrs):
#         nonlocal counter
#         attrs = normalize_attrs(attrs)
#
#         if len(attrs) <= 1:
#             result.append({
#                 "name": f"R{counter}",
#                 "attrs": attrs,
#                 "fds": []
#             })
#             counter += 1
#             return
#
#         local_fds = project_fds_full(attrs, fds_raw)
#         violation = None
#
#         for lhs, rhs in local_fds:
#             closure, _ = compute_closure_of_attrs(lhs, fds_raw)
#             local_closure = closure & attrs
#
#             if local_closure != attrs:
#                 actual_rhs = rhs & attrs - lhs
#                 if actual_rhs:
#                     violation = (lhs, actual_rhs)
#                     break
#
#         if violation is None:
#             result.append({
#                 "name": f"R{counter}",
#                 "attrs": attrs,
#                 "fds": local_fds
#             })
#             counter += 1
#             return
#
#         lhs, rhs = violation
#         closure_lhs, _ = compute_closure_of_attrs(lhs, fds_raw)
#         r1 = (closure_lhs & attrs)
#         r2 = (attrs - r1) | lhs
#
#         if r1 == attrs or r2 == attrs:
#             r1 = lhs | rhs
#             r2 = attrs - rhs
#
#         steps.append(
#             f"Tách R({format_attrs(attrs)}) thành "
#             f"R({format_attrs(r1)}) và R({format_attrs(r2)}) "
#             f"do vi phạm bởi PTH: {format_fd(lhs, rhs)}"
#         )
#
#         rec(r1)
#         rec(r2)
#
#     rec(set(all_attrs))
#     return result, steps


if __name__ == '__main__':
    tap_thuoc_tinh = ["A", "B", "C", "D", "E", "G"]

    tap_phu_thuoc_ham = [
        "AB → C",
        "A → D",
        "B → E",
        "C → G"
    ]

    kq, bc = tim_khoa_ung_vien(tap_thuoc_tinh, tap_phu_thuoc_ham)

    # print(cac_thuoc_tinh_trong_khoa_ung_vien(kq))
    # print(loc_phu_thuoc_ham(["A", "B", "C"], tap_phu_thuoc_ham))
    # print(tim_vi_pham_dang_chuan_2(tap_phu_thuoc_ham, kq))
    r, s = phan_ra_sang_dang_chuan_2(tap_thuoc_tinh, tap_phu_thuoc_ham)
    print(r)
    for b in s:
        print(b)