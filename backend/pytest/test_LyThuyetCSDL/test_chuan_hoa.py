from backend.app.modules.LyThuyetCSDL.schemas import PhuThuocHam
from backend.app.modules.LyThuyetCSDL.utils.chuan_hoa import (
    chuan_hoa_thuoc_tinh,
    chuan_hoa_tap_thuoc_tinh,
    chuan_hoa_phu_thuoc_ham_sang_tuple,
    chuan_hoa_tap_phu_thuoc_ham_sang_tuple,
    chuan_hoa_tap_phu_thuoc_ham_sang_dang_class,
    chuan_hoa_mot_ve_phu_thuoc_ham
)


def test_chuan_hoa_thuoc_tinh():
    assert chuan_hoa_thuoc_tinh('') == ''
    assert chuan_hoa_thuoc_tinh('1') == '1'
    assert chuan_hoa_thuoc_tinh('a') == 'A'
    assert chuan_hoa_thuoc_tinh(' a ') == 'A'


def test_chuan_hoa_tap_thuoc_tinh():
    assert chuan_hoa_tap_thuoc_tinh(['a', ' b', 'c ', ' d ', 'a']) == {'A', 'B', 'C', 'D'}


def test_chuan_hoa_phu_thuoc_ham_sang_tuple():
    assert chuan_hoa_phu_thuoc_ham_sang_tuple('a → b') == ({'A'}, {'B'})
    assert chuan_hoa_phu_thuoc_ham_sang_tuple('aa → b') == ({'A'}, {'B'})
    assert chuan_hoa_phu_thuoc_ham_sang_tuple('Aa → BbC') == ({'A'}, {'B', 'C'})
    assert chuan_hoa_phu_thuoc_ham_sang_tuple('A → BC') == ({'A'}, {'B', 'C'})


def test_chuan_hoa_tap_phu_thuoc_ham_sang_tuple():
    assert chuan_hoa_tap_phu_thuoc_ham_sang_tuple(['A → b', 'AA → Bb', 'A → Bc']) == [
        ({'A'}, {'B'}), ({'A'}, {'B'}), ({'A'}, {'B', 'C'})
    ]


def test_chuan_hoa_tap_phu_thuoc_ham_sang_dang_class():
    assert chuan_hoa_tap_phu_thuoc_ham_sang_dang_class(['A → B', 'A → BC']) == [
        PhuThuocHam(ve_trai='A', ve_phai='B'),
        PhuThuocHam(ve_trai='A', ve_phai='BC')
    ]

def test_chuan_hoa_mot_ve_phu_thuoc_ham():
    assert chuan_hoa_mot_ve_phu_thuoc_ham(['A', 'B', 'A', 'C']) == frozenset({'A', 'B', 'C'})


def main():
    tests = [
        test_chuan_hoa_thuoc_tinh,
        test_chuan_hoa_tap_thuoc_tinh,
        test_chuan_hoa_phu_thuoc_ham_sang_tuple,
        test_chuan_hoa_tap_phu_thuoc_ham_sang_tuple,
        test_chuan_hoa_tap_phu_thuoc_ham_sang_dang_class,
        test_chuan_hoa_mot_ve_phu_thuoc_ham
    ]
    print(f"Chạy {len(tests)} bài kiểm thử...\n")
    for t in tests:
        t()
    print("\nALL TESTS PASSED")


if __name__ == "__main__":
    main()