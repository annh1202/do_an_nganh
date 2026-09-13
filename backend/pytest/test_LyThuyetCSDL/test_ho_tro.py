from backend.app.modules.LyThuyetCSDL.bai_giai.ho_tro import (
    tach_phu_thuoc_ham_ve_phai,
    co_phai_phu_thuoc_ham_du_thua,
    loai_bo_phu_thuoc_ham_du_thua,
    co_phai_sieu_khoa,
    cac_thuoc_tinh_trong_khoa_ung_vien,
    loc_phu_thuoc_ham,
    tim_phu_thuoc_ham_vong,
    gom_phu_thuoc_ham_vi_pham,
    gom_phu_thuoc_ham_theo_ve_trai,
    tim_phu_thuoc_bo_phan_voi_khoa,
    tim_phu_thuoc_ham_vi_pham_dang_chuan_2,
    tim_phu_thuoc_ham_vi_pham_dang_chuan_3,
    tim_phu_thuoc_ham_vi_pham_bcnf
)

def test_tach_phu_thuoc_ham_ve_phai():
    assert tach_phu_thuoc_ham_ve_phai([('A', 'BC')]) == [({'A'}, {'B'}), ({'A'}, {'C'})]
    assert tach_phu_thuoc_ham_ve_phai([('AC', 'BD')]) == [({'A', 'C'}, {'B'}), ({'A', 'C'}, {'D'})]
    assert tach_phu_thuoc_ham_ve_phai([('A', 'BC'), ('A', 'CD')]) == [
        ({'A'}, {'B'}), ({'A'}, {'C'}), ({'A'}, {'C'}), ({'A'}, {'D'})
    ]


def test_co_phai_phu_thuoc_ham_du_thua():
    tap_phu_thuoc_ham = [({'A'}, {'B'}), ({'B'}, {'C'})]
    assert co_phai_phu_thuoc_ham_du_thua(({'A'}, {'C'}), tap_phu_thuoc_ham) == True
    assert co_phai_phu_thuoc_ham_du_thua(({'C'}, {'A'}), tap_phu_thuoc_ham) == False
    assert co_phai_phu_thuoc_ham_du_thua(({'C'}, {'C'}), tap_phu_thuoc_ham) == True


def test_loai_bo_phu_thuoc_ham_du_thua():
    tap_phu_thuoc_ham = [({'A'}, {'B'}), ({'B'}, {'C'}), ({'A'}, {'C'}), ({'A'}, {'A'})]
    assert loai_bo_phu_thuoc_ham_du_thua(tap_phu_thuoc_ham) == [({'A'}, {'B'}), ({'B'}, {'C'})]


def test_co_phai_sieu_khoa():
    tap_thuoc_tinh = ['A', 'B', 'C']
    tap_phu_thuoc_ham = ['A → B', 'B → C']
    assert co_phai_sieu_khoa(['A'], tap_thuoc_tinh, tap_phu_thuoc_ham) == True
    assert co_phai_sieu_khoa(['B'], tap_thuoc_tinh, tap_phu_thuoc_ham) == False
    assert co_phai_sieu_khoa(['A'], ['A', 'B'], tap_phu_thuoc_ham) == True
    assert co_phai_sieu_khoa(['B'], ['A', 'B'], tap_phu_thuoc_ham) == False


def test_cac_thuoc_tinh_trong_khoa_ung_vien():
    assert cac_thuoc_tinh_trong_khoa_ung_vien(['AB']) == {'A', 'B'}
    assert cac_thuoc_tinh_trong_khoa_ung_vien(['AB', 'DC']) == {'A', 'B', 'C', 'D'}
    assert cac_thuoc_tinh_trong_khoa_ung_vien(['AB', 'AC', 'DC']) == {'A', 'B', 'C', 'D'}


def test_loc_phu_thuoc_ham():
    tap_phu_thuoc_ham = ['A → B', 'DB → C', 'A → D', 'D → C']
    assert loc_phu_thuoc_ham(['A', 'B'], tap_phu_thuoc_ham) == [({'A'}, {'B'})]
    assert loc_phu_thuoc_ham(['B', 'C', 'D'], tap_phu_thuoc_ham) == [
        ({'B', 'D'}, {'C'}), ({'D'}, {'C'})
    ]

def test_tim_phu_thuoc_ham_vong():
    tap_phu_thuoc_ham = [({'A'}, {'B'}), ({'B'}, {'C'}), ({'A'}, {'C'}), ({'D'}, {'A'})]
    assert tim_phu_thuoc_ham_vong(tap_phu_thuoc_ham) == {}

    tap_phu_thuoc_ham = [({'A'}, {'B'}), ({'B'}, {'C'}), ({'C'}, {'A'}), ({'D'}, {'A'})]
    assert tim_phu_thuoc_ham_vong(tap_phu_thuoc_ham) == {
        ('A', 'B', 'C'): [({'A'}, {'B'}), ({'B'}, {'C'}), ({'C'}, {'A'})]
    }

    tap_phu_thuoc_ham = [({'A'}, {'B'}), ({'B'}, {'C'}), ({'A'}, {'C'}), ({'C'}, {'A'})]
    assert tim_phu_thuoc_ham_vong(tap_phu_thuoc_ham) == {
        ('A', 'B', 'C'): [({'A'}, {'B'}), ({'B'}, {'C'}), ({'C'}, {'A'})],
        ('A', 'C'): [({'A'}, {'C'}), ({'C'}, {'A'})]
    }


def test_gom_phu_thuoc_ham_vi_pham():
    assert gom_phu_thuoc_ham_vi_pham([], [], []) == []

    danh_sach_vi_pham = [('A', 'B')]
    tap_phu_thuoc_ham = ['A → B']
    thuoc_tinh_khong_khoa = ['B']
    ket_qua = gom_phu_thuoc_ham_vi_pham(danh_sach_vi_pham, tap_phu_thuoc_ham, thuoc_tinh_khong_khoa)
    assert ket_qua == [({'A', 'B'}, [({'A'}, {'B'})])]

    danh_sach_vi_pham = [('A', 'B'), ('A', 'C')]
    tap_phu_thuoc_ham = ['A → B', 'A → C']
    thuoc_tinh_khong_khoa = ['B', 'C']
    ket_qua = gom_phu_thuoc_ham_vi_pham(danh_sach_vi_pham,tap_phu_thuoc_ham,thuoc_tinh_khong_khoa)
    assert ket_qua == [({'A', 'B', 'C'}, [({'A'}, {'B'}), ({'A'}, {'C'})])]

    danh_sach_vi_pham = [('A', 'B'), ('C', 'D')]
    tap_phu_thuoc_ham = ['A → B', 'C → D']
    thuoc_tinh_khong_khoa = ['B', 'D']
    ket_qua = gom_phu_thuoc_ham_vi_pham(danh_sach_vi_pham, tap_phu_thuoc_ham, thuoc_tinh_khong_khoa)
    assert ket_qua == [({'B', 'A'}, [({'A'}, {'B'})]), ({'D', 'C'}, [({'C'}, {'D'})])]


def test_gom_phu_thuoc_ham_theo_ve_trai():
    tap_phu_thuoc_ham = []
    ket_qua = gom_phu_thuoc_ham_theo_ve_trai(tap_phu_thuoc_ham)
    assert ket_qua == []

    tap_phu_thuoc_ham = [({'A'}, {'B'}), ({'B'}, {'C'}), ({'C'}, {'A'})]
    ket_qua = gom_phu_thuoc_ham_theo_ve_trai(tap_phu_thuoc_ham)
    assert ket_qua == [
        ({'A'}, [({'A'}, {'B'})]),
        ({'B'}, [({'B'}, {'C'})]),
        ({'C'}, [({'C'}, {'A'})])
    ]

    tap_phu_thuoc_ham = [({'A'}, {'B'}), ({'B'}, {'C'}), ({'A'}, {'C'}), ({'C'}, {'A'})]
    ket_qua = gom_phu_thuoc_ham_theo_ve_trai(tap_phu_thuoc_ham)
    assert ket_qua == [
        ({'A'}, [({'A'}, {'B'}), ({'A'}, {'C'})]),
        ({'B'}, [({'B'}, {'C'})]),
        ({'C'}, [({'C'}, {'A'})])
    ]


def test_tim_phu_thuoc_bo_phan_voi_khoa():
    ket_qua = tim_phu_thuoc_bo_phan_voi_khoa('A', 'CD', ['BC'])
    assert ket_qua == []

    ket_qua = tim_phu_thuoc_bo_phan_voi_khoa('A', 'CD', ['AB'])
    assert ket_qua == ['AB']

    ket_qua = tim_phu_thuoc_bo_phan_voi_khoa('C', 'D', ['BC', 'AC'])
    assert ket_qua == ['BC', 'AC']

    ket_qua = tim_phu_thuoc_bo_phan_voi_khoa('A', 'CD', ['A'])
    assert ket_qua == []


def test_tim_phu_thuoc_ham_vi_pham_dang_chuan_2():
    # phụ thuộc bộ phận bình thường
    tap_phu_thuoc_ham = ['A → B', 'C → D', 'B → D']
    khoa_ung_vien = ['AC']
    ket_qua = tim_phu_thuoc_ham_vi_pham_dang_chuan_2(tap_phu_thuoc_ham, khoa_ung_vien)
    assert ket_qua == [
        ({'A'}, {'B'}, 'AC'),
        ({'C'}, {'D'}, 'AC')
    ]

    # phụ thuộc toán bộ khóa
    tap_phu_thuoc_ham = ['AC → B', 'AC → D']
    khoa_ung_vien = ['AC']
    ket_qua = tim_phu_thuoc_ham_vi_pham_dang_chuan_2(tap_phu_thuoc_ham, khoa_ung_vien)
    assert ket_qua == []

    # vế trái là thuộc tính khóa
    tap_phu_thuoc_ham = ['A → C']
    khoa_ung_vien = ['AC']
    ket_qua = tim_phu_thuoc_ham_vi_pham_dang_chuan_2(tap_phu_thuoc_ham, khoa_ung_vien)
    assert ket_qua == []

    # không phụ thuộc bộ phận
    tap_phu_thuoc_ham = ['B → D']
    khoa_ung_vien = ['AC']
    ket_qua = tim_phu_thuoc_ham_vi_pham_dang_chuan_2(tap_phu_thuoc_ham, khoa_ung_vien)
    assert ket_qua == []

    # 1 phụ thuộc hàm vi phạm nhiều khóa
    tap_phu_thuoc_ham = ['A → D', 'C → E', 'B → F']
    khoa_ung_vien = ['AB', 'BC']
    ket_qua = tim_phu_thuoc_ham_vi_pham_dang_chuan_2(tap_phu_thuoc_ham, khoa_ung_vien)
    assert ket_qua == [
        ({'A'}, {'D'}, 'AB'),
        ({'C'}, {'E'}, 'BC'),
        ({'B'}, {'F'}, 'AB'),
        ({'B'}, {'F'}, 'BC')
    ]


def test_tim_phu_thuoc_ham_vi_pham_dang_chuan_3():
    # Quan hệ đã đạt 3NF
    tap_thuoc_tinh = ['A', 'B', 'C']
    tap_phu_thuoc_ham = ['AB → C']
    khoa_ung_vien = ['AB']
    ket_qua = tim_phu_thuoc_ham_vi_pham_dang_chuan_3(tap_thuoc_tinh, tap_phu_thuoc_ham, khoa_ung_vien)
    assert ket_qua == []

    #  Vi phạm phụ thuộc bắc cầu
    tap_thuoc_tinh = ['A', 'B', 'C', 'D']
    tap_phu_thuoc_ham = ['AB → C', 'C → D']
    khoa_ung_vien = ['AB']
    ket_qua = tim_phu_thuoc_ham_vi_pham_dang_chuan_3(tap_thuoc_tinh, tap_phu_thuoc_ham, khoa_ung_vien)
    assert ket_qua == [({'C'}, {'D'})]

    # Vi phạm phụ thuộc bộ phận
    tap_thuoc_tinh = ['A', 'B', 'C', 'D']
    tap_phu_thuoc_ham = ['AB → C', 'A → D']
    khoa_ung_vien = ['AB']
    ket_qua = tim_phu_thuoc_ham_vi_pham_dang_chuan_3(tap_thuoc_tinh, tap_phu_thuoc_ham, khoa_ung_vien)
    assert ket_qua == [({'A'}, {'D'})]

    # Vế phải là thuộc tính khóa
    tap_thuoc_tinh = ['A', 'B', 'C']
    tap_phu_thuoc_ham = ['AB → C', 'C → B']
    khoa_ung_vien = ['AB', 'AC']
    ket_qua = tim_phu_thuoc_ham_vi_pham_dang_chuan_3(tap_thuoc_tinh, tap_phu_thuoc_ham, khoa_ung_vien)
    assert ket_qua == []

    # Nhiều khóa ứng viên và vế phải là thuộc tính khóa
    tap_thuoc_tinh = ['A', 'B', 'C', 'D', 'E']
    tap_phu_thuoc_ham = ['AB → CD', 'C → E', 'D → B']
    khoa_ung_vien = ['AB', 'AD']
    ket_qua = tim_phu_thuoc_ham_vi_pham_dang_chuan_3(tap_thuoc_tinh, tap_phu_thuoc_ham, khoa_ung_vien)
    assert ket_qua == [({'C'}, {'E'})]

    # Phụ thuộc hàm hiển nhiên
    tap_thuoc_tinh = ['A', 'B', 'C']
    tap_phu_thuoc_ham = ['A → A', 'AB → A']
    khoa_ung_vien = ['AB']
    ket_qua = tim_phu_thuoc_ham_vi_pham_dang_chuan_3(tap_thuoc_tinh, tap_phu_thuoc_ham, khoa_ung_vien)
    assert ket_qua == []

    # Vế trái và vế phải đều gồm nhiều thuộc tính vi phạm
    tap_thuoc_tinh = ['A', 'B', 'C', 'D', 'E', 'F']
    tap_phu_thuoc_ham = ['ABC → DE', 'D → EF']
    khoa_ung_vien = ['ABC']
    ket_qua = tim_phu_thuoc_ham_vi_pham_dang_chuan_3(tap_thuoc_tinh, tap_phu_thuoc_ham, khoa_ung_vien)
    assert ket_qua == [({'D'}, {'E', 'F'})]


def test_tim_phu_thuoc_ham_vi_pham_bcnf():
    # B không phải siêu khóa
    tap_thuoc_tinh = ['A', 'B', 'C', 'D']
    tap_phu_thuoc_ham = ['A → B', 'B → C', 'B → D']
    ket_qua = tim_phu_thuoc_ham_vi_pham_bcnf(tap_thuoc_tinh, tap_phu_thuoc_ham)
    assert ket_qua == [({'B'}, {'C'}), ({'B'}, {'D'})]

    # Đạt chuẩn BCNF
    tap_thuoc_tinh = ['A', 'B', 'C']
    tap_phu_thuoc_ham = ['AB → C', 'A → BC']
    ket_qua = tim_phu_thuoc_ham_vi_pham_bcnf(tap_thuoc_tinh, tap_phu_thuoc_ham)
    assert ket_qua == []

    # Đạt 3NF nhưng vi phạm BCNF
    tap_thuoc_tinh = ['A', 'B', 'C']
    tap_phu_thuoc_ham = ['AB → C', 'C → B']
    ket_qua = tim_phu_thuoc_ham_vi_pham_bcnf(tap_thuoc_tinh, tap_phu_thuoc_ham)
    assert ket_qua == [({'C'}, {'B'})]

    # Phụ thuộc hàm hiển nhiên -> Không vi phạm BCNF
    tap_thuoc_tinh = ['A', 'B', 'C']
    tap_phu_thuoc_ham = ['A → A', 'AB → A']
    ket_qua = tim_phu_thuoc_ham_vi_pham_bcnf(tap_thuoc_tinh, tap_phu_thuoc_ham)
    assert ket_qua == []

    # Vi phạm phụ thuộc bộ phận -> vi phạm dạng chuẩn 2
    tap_thuoc_tinh = ['A', 'B', 'C', 'D']
    tap_phu_thuoc_ham = ['AB → CD', 'A → C']
    ket_qua = tim_phu_thuoc_ham_vi_pham_bcnf(tap_thuoc_tinh, tap_phu_thuoc_ham)
    assert ket_qua == [({'A'}, {'C'})]

    # Vế trái có nhiều thuộc tính nhưng không đủ để tạo thành siêu khóa
    tap_thuoc_tinh = ['A', 'B', 'C', 'D', 'E']
    tap_phu_thuoc_ham = ['ABC → D', 'BC → E']
    ket_qua = tim_phu_thuoc_ham_vi_pham_bcnf(tap_thuoc_tinh, tap_phu_thuoc_ham)
    assert ket_qua == [({'B', 'C'}, {'E'})]

    # Vế trái và vế phải gồm nhiều thuộc tính
    tap_thuoc_tinh = ['A', 'B', 'C', 'D', 'E']
    tap_phu_thuoc_ham = ['AB → CDE', 'CD → EB']
    ket_qua = tim_phu_thuoc_ham_vi_pham_bcnf(tap_thuoc_tinh, tap_phu_thuoc_ham)
    assert ket_qua == [({'C', 'D'}, {'E', 'B'})]



def main():
    tests = [
        test_tach_phu_thuoc_ham_ve_phai,
        test_co_phai_phu_thuoc_ham_du_thua,
        test_loai_bo_phu_thuoc_ham_du_thua,
        test_co_phai_sieu_khoa,
        test_cac_thuoc_tinh_trong_khoa_ung_vien,
        test_cac_thuoc_tinh_trong_khoa_ung_vien,
        test_tim_phu_thuoc_ham_vong,
        test_gom_phu_thuoc_ham_vi_pham,
        test_gom_phu_thuoc_ham_theo_ve_trai,
        test_tim_phu_thuoc_bo_phan_voi_khoa,
        test_tim_phu_thuoc_ham_vi_pham_dang_chuan_2,
        test_tim_phu_thuoc_ham_vi_pham_dang_chuan_3,
        test_tim_phu_thuoc_ham_vi_pham_bcnf,
    ]
    print(f'Chạy {len(tests)} bài kiểm thử...\n')
    for t in tests:
        t()
    print('\nALL TESTS PASSED')


if __name__ == '__main__':
    main()