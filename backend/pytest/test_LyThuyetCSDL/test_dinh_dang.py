from backend.app.modules.LyThuyetCSDL.schemas import PhuThuocHam
from backend.app.modules.LyThuyetCSDL.utils.dinh_dang import (
    dinh_dang_tap_thuoc_tinh,
    dinh_dang_chuoi_tap_thuoc_tinh,
    dinh_dang_phu_thuoc_ham,
    dinh_dang_tap_phu_thuoc_ham_tuple,
    dinh_dang_tap_phu_thuoc_ham_object
)


def test_dinh_dang_tap_thuoc_tinh():
    assert dinh_dang_tap_thuoc_tinh(['A', 'B', 'C']) == 'A, B, C'
    assert dinh_dang_tap_thuoc_tinh(['Aa', 'Bb', 'Cc']) == 'Aa, Bb, Cc'


def test_dinh_dang_chuoi_tap_thuoc_tinh():
    assert dinh_dang_chuoi_tap_thuoc_tinh({}) == ''
    assert dinh_dang_chuoi_tap_thuoc_tinh({'A', 'B'}) == 'AB'
    assert dinh_dang_chuoi_tap_thuoc_tinh(['A', 'B', 'C']) == 'ABC'
    assert dinh_dang_chuoi_tap_thuoc_tinh(['A', 'B', 'C', 'C']) == 'ABCC'
    assert dinh_dang_chuoi_tap_thuoc_tinh([]) == ''


def test_dinh_dang_phu_thuoc_ham():
    assert dinh_dang_phu_thuoc_ham({'A'}, ['B']) == 'A → B'
    assert dinh_dang_phu_thuoc_ham(['A'], {'B'}) == 'A → B'
    assert dinh_dang_phu_thuoc_ham(['A'], ['B']) == 'A → B'
    assert dinh_dang_phu_thuoc_ham(['A'], ['BC']) == 'A → BC'
    assert dinh_dang_phu_thuoc_ham(['A', 'D'], ['BC']) == 'AD → BC'


def test_dinh_dang_tap_phu_thuoc_ham_tuple():
    assert dinh_dang_tap_phu_thuoc_ham_tuple([('A', 'B')]) == ['A → B']
    assert dinh_dang_tap_phu_thuoc_ham_tuple([('A', 'B'), ('B', 'C')]) == ['A → B', 'B → C']


def test_dinh_dang_tap_phu_thuoc_ham_object():
    assert dinh_dang_tap_phu_thuoc_ham_object([PhuThuocHam(ve_trai='AB', ve_phai='C')]) == ['AB → C']


def main():
    tests = [
        test_dinh_dang_tap_thuoc_tinh,
        test_dinh_dang_chuoi_tap_thuoc_tinh,
        test_dinh_dang_phu_thuoc_ham,
        test_dinh_dang_tap_phu_thuoc_ham_tuple,
        test_dinh_dang_tap_phu_thuoc_ham_object
    ]
    print(f"Chạy {len(tests)} bài kiểm thử...\n")
    for t in tests:
        t()
    print("\nALL TESTS PASSED")


if __name__ == "__main__":
    main()