from backend.app.modules.LyThuyetCSDL.bai_giai.bao_dong_tap_thuoc_tinh import tinh_bao_dong_tap_thuoc_tinh
from backend.app.modules.LyThuyetCSDL.bai_giai.bao_dong_tap_phu_thuoc_ham import (
    tinh_bao_dong_tap_phu_thuoc_ham
)
from backend.app.modules.LyThuyetCSDL.bai_giai.khoa_ung_vien import (
    phan_loai_thuoc_tinh,
    kiem_tra_tinh_toi_thieu,
    tim_khoa_ung_vien
)


def test_tinh_bao_dong_tap_thuoc_tinh():
    # Các phụ thuộc hàm đều đã thỏa sẵn
    tap_thuoc_tinh = ['A', 'B', 'C']
    tap_phu_thuoc_ham = ['A → B', 'B → C']
    tap_thuoc_tinh_can_tim = ['A', 'B']
    bao_dong, _ = tinh_bao_dong_tap_thuoc_tinh(tap_thuoc_tinh_can_tim, tap_phu_thuoc_ham, tap_thuoc_tinh)
    assert bao_dong == {'A', 'B', 'C'}

    # Không kích hoạt được PTH nào
    tap_thuoc_tinh = ['A', 'B', 'C', 'D']
    tap_phu_thuoc_ham = ['B → C', 'CD → A']
    tap_thuoc_tinh_can_tim = ['A']
    bao_dong, _ = tinh_bao_dong_tap_thuoc_tinh(tap_thuoc_tinh_can_tim, tap_phu_thuoc_ham, tap_thuoc_tinh)
    assert bao_dong == {'A'}

    # Có phụ thuộc hàm chưa thỏa sẵn 'BC → D', 'D → E'
    tap_thuoc_tinh = ['A', 'B', 'C', 'D', 'E']
    tap_phu_thuoc_ham = ['A → B', 'BC → D', 'D → E']
    tap_thuoc_tinh_can_tim = ['A', 'C']
    bao_dong, _ = tinh_bao_dong_tap_thuoc_tinh(tap_thuoc_tinh_can_tim, tap_phu_thuoc_ham, tap_thuoc_tinh)
    assert bao_dong == {'A', 'B', 'C', 'D', 'E'}

    # Có phụ thuộc hàm dạng vòng
    tap_thuoc_tinh = ['A', 'B', 'C', 'D']
    tap_phu_thuoc_ham = ['A → B', 'B → C', 'C → A']
    tap_thuoc_tinh_can_tim = ['B']
    bao_dong, _ = tinh_bao_dong_tap_thuoc_tinh(tap_thuoc_tinh_can_tim, tap_phu_thuoc_ham, tap_thuoc_tinh)
    assert bao_dong == {'A', 'B', 'C'}

    # Tập thuộc tính cần tìm là tập rỗng
    tap_thuoc_tinh = ['A', 'B', 'C']
    tap_phu_thuoc_ham = ['A → B', 'B → C']
    tap_thuoc_tinh_can_tim = []
    bao_dong, _ = tinh_bao_dong_tap_thuoc_tinh(tap_thuoc_tinh_can_tim, tap_phu_thuoc_ham, tap_thuoc_tinh)
    assert bao_dong == set()

    # Tập phụ thuộc hàm rỗng
    tap_thuoc_tinh = ['A', 'B', 'C']
    tap_phu_thuoc_ham = []
    tap_thuoc_tinh_can_tim = ['A', 'B']
    bao_dong, _ = tinh_bao_dong_tap_thuoc_tinh(tap_thuoc_tinh_can_tim, tap_phu_thuoc_ham, tap_thuoc_tinh)
    assert bao_dong == {'A', 'B'}


def test_tinh_bao_dong_tap_phu_thuoc_ham():
    # Tập phụ thuộc hàm rỗng
    tap_phu_thuoc_ham = []
    bao_dong, _ = tinh_bao_dong_tap_phu_thuoc_ham(tap_phu_thuoc_ham)
    assert bao_dong == set()

    # Phụ thuộc hàm đơn lẻ
    tap_phu_thuoc_ham = ['A → B']
    bao_dong, _ = tinh_bao_dong_tap_phu_thuoc_ham(tap_phu_thuoc_ham)
    assert bao_dong == {'A → B'}

    # Phụ thuộc bắc cầu
    tap_phu_thuoc_ham = ['A → B', 'B → C']
    bao_dong, _ = tinh_bao_dong_tap_phu_thuoc_ham(tap_phu_thuoc_ham)
    assert bao_dong == {'A → B', 'B → C', 'A → C', 'AB → C', 'AC → B'}

    # Phụ thuộc hàm vòng
    tap_phu_thuoc_ham = ['A → B', 'B → C', 'C → A']
    bao_dong, _ = tinh_bao_dong_tap_phu_thuoc_ham(tap_phu_thuoc_ham)
    assert bao_dong == {'A → B', 'A → C', 'B → A', 'B → C', 'C → A', 'C → B', 'AB → C', 'AC → B', 'BC → A'}

    # Vế trái là tập gồm nhiều thuộc tính
    tap_phu_thuoc_ham = ['AB → C', 'D → C']
    bao_dong, _ = tinh_bao_dong_tap_phu_thuoc_ham(tap_phu_thuoc_ham)
    assert bao_dong == {'AB → C', 'D → C', 'BD → C', 'AD → C', 'ABD → C'}

    # Hai phụ thuộc hàm độc lập
    tap_phu_thuoc_ham = ['A → B', 'C → D']
    bao_dong, _ = tinh_bao_dong_tap_phu_thuoc_ham(tap_phu_thuoc_ham)
    assert bao_dong == {
        'A → B', 'C → D',
        'AC → B', 'AC → D',
        'AD → B', 'BC → D',
        'ACD → B', 'ABC → D'
    }


def test_phan_loai_thuoc_tinh():
    # Tập phụ thuộc hàm rỗng -> Tất cả thuộc tính thuộc tập Nguồn
    tap_thuoc_tinh = ['A', 'B', 'C']
    tap_phu_thuoc_ham = []
    ket_qua = phan_loai_thuoc_tinh(tap_thuoc_tinh, tap_phu_thuoc_ham)
    assert ket_qua == ({'A', 'B', 'C'}, set(), set())

    # Tất cả thuộc tính đều thuộc tập Trung gian
    tap_thuoc_tinh = ['A', 'B', 'C']
    tap_phu_thuoc_ham = [({'A'}, {'B'}), ({'B'}, {'C'}), ({'C'}, {'A'})]
    ket_qua = phan_loai_thuoc_tinh(tap_thuoc_tinh, tap_phu_thuoc_ham)
    assert ket_qua == (set(), {'A', 'B', 'C'}, set())

    # Chỉ có tập Nguồn và tập Đích
    tap_thuoc_tinh = ['A', 'B']
    tap_phu_thuoc_ham = [({'A'}, {'B'})]
    ket_qua = phan_loai_thuoc_tinh(tap_thuoc_tinh, tap_phu_thuoc_ham)
    assert ket_qua == ({'A'}, set(), {'B'})

    # Đầy đủ 3 tập (Nguồn, Trung gian, Đích)
    tap_thuoc_tinh = ['A', 'B', 'C', 'D', 'E']
    tap_phu_thuoc_ham = [({'A'}, {'B'}), ({'B'}, {'C'}), ({'D'}, {'E'})]
    ket_qua = phan_loai_thuoc_tinh(tap_thuoc_tinh, tap_phu_thuoc_ham)
    assert ket_qua == ({'A', 'D'}, {'B'}, {'C', 'E'})

    # Thuộc tính không xuất hiện trong PTH -> Thuộc tập Nguồn
    tap_thuoc_tinh = ['A', 'B', 'C', 'X']
    tap_phu_thuoc_ham = [({'A'}, {'B'}), ({'B'}, {'C'})]
    ket_qua = phan_loai_thuoc_tinh(tap_thuoc_tinh, tap_phu_thuoc_ham)
    assert ket_qua == ({'A', 'X'}, {'B'}, {'C'})

    # Vế trái và vế phải chứa nhiều thuộc tính (Tập thuộc tính hợp)
    tap_thuoc_tinh = ['A', 'B', 'C', 'D', 'E']
    tap_phu_thuoc_ham = [({'A', 'B'}, {'C', 'D'}), ({'C'}, {'E'})]
    ket_qua = phan_loai_thuoc_tinh(tap_thuoc_tinh, tap_phu_thuoc_ham)
    assert ket_qua == ({'A', 'B'}, {'C'}, {'D', 'E'})


def test_kiem_tra_tinh_toi_thieu():
    # Tập đang xét tối thiểu
    cac_khoa_ung_vien = ['A', 'BC']
    tap_thuoc_tinh_dang_xet = {'B', 'D'}
    cac_tap_thuoc_tinh_bo_qua = {}
    ket_qua = kiem_tra_tinh_toi_thieu(cac_khoa_ung_vien, tap_thuoc_tinh_dang_xet, cac_tap_thuoc_tinh_bo_qua)
    assert ket_qua is True
    assert cac_tap_thuoc_tinh_bo_qua == {}

    # Không tối thiểu (Chứa khóa 'A')
    cac_khoa_ung_vien = ['A']
    tap_thuoc_tinh_dang_xet = {'A', 'B'}
    cac_tap_thuoc_tinh_bo_qua = {}
    ket_qua = kiem_tra_tinh_toi_thieu(cac_khoa_ung_vien, tap_thuoc_tinh_dang_xet, cac_tap_thuoc_tinh_bo_qua)
    assert ket_qua is False
    assert cac_tap_thuoc_tinh_bo_qua == {'A': ['AB']}

    # Khóa đã tồn tại trong dictionary
    cac_khoa_ung_vien = ['A']
    tap_thuoc_tinh_dang_xet = {'A', 'B', 'C'}
    cac_tap_thuoc_tinh_bo_qua = {'A': ['AB']}
    ket_qua = kiem_tra_tinh_toi_thieu(cac_khoa_ung_vien, tap_thuoc_tinh_dang_xet, cac_tap_thuoc_tinh_bo_qua)
    assert ket_qua is False
    assert cac_tap_thuoc_tinh_bo_qua == {'A': ['AB', 'ABC']}

    # Chưa có khóa ứng viên -> Mặc định thỏa mãn tính tối thiểu
    cac_khoa_ung_vien = []
    tap_thuoc_tinh_dang_xet = {'A', 'B'}
    cac_tap_thuoc_tinh_bo_qua = {}
    ket_qua = kiem_tra_tinh_toi_thieu(cac_khoa_ung_vien, tap_thuoc_tinh_dang_xet, cac_tap_thuoc_tinh_bo_qua)
    assert ket_qua is True
    assert cac_tap_thuoc_tinh_bo_qua == {}

    # Tập đang xét bằng với khóa ứng viên đã có
    cac_khoa_ung_vien = ['AB']
    tap_thuoc_tinh_dang_xet = {'A', 'B'}
    cac_tap_thuoc_tinh_bo_qua = {}
    ket_qua = kiem_tra_tinh_toi_thieu(cac_khoa_ung_vien, tap_thuoc_tinh_dang_xet, cac_tap_thuoc_tinh_bo_qua)
    assert ket_qua is False
    assert cac_tap_thuoc_tinh_bo_qua == {'AB': ['AB']}

    # Tập đang xét chứa nhiều khóa -> Chỉ lấy khóa đầu tiên là đủ
    cac_khoa_ung_vien = ['A', 'B']
    tap_thuoc_tinh_dang_xet = {'A', 'B', 'C'}
    cac_tap_thuoc_tinh_bo_qua = {}
    ket_qua = kiem_tra_tinh_toi_thieu(cac_khoa_ung_vien, tap_thuoc_tinh_dang_xet, cac_tap_thuoc_tinh_bo_qua)
    assert ket_qua is False
    assert cac_tap_thuoc_tinh_bo_qua == {'A': ['ABC']}


def test_tim_khoa_ung_vien():
    # 1 khóa duy nhất
    tap_thuoc_tinh = ['A', 'B', 'C', 'D']
    tap_phu_thuoc_ham = ['A → B', 'B → C', 'C → D']
    khoa_ung_vien, _ = tim_khoa_ung_vien(tap_thuoc_tinh, tap_phu_thuoc_ham)
    assert khoa_ung_vien == ['A']

    # Khóa gồm nhiều thuộc tính
    tap_thuoc_tinh = ['A', 'B', 'C', 'D']
    tap_phu_thuoc_ham = ['AB → C', 'C → D']
    khoa_ung_vien, _ = tim_khoa_ung_vien(tap_thuoc_tinh, tap_phu_thuoc_ham)
    assert khoa_ung_vien == ['AB']

    # Nhiều khóa ứng viên (A → B, B → A)
    tap_thuoc_tinh = ['A', 'B', 'C']
    tap_phu_thuoc_ham = ['A → B', 'B → A', 'A → C']
    khoa_ung_vien, _ = tim_khoa_ung_vien(tap_thuoc_tinh, tap_phu_thuoc_ham)
    assert khoa_ung_vien == ['A', 'B']

    # Tập phụ thuộc hàm rỗng
    tap_thuoc_tinh = ['A', 'B', 'C']
    tap_phu_thuoc_ham = []
    khoa_ung_vien, _ = tim_khoa_ung_vien(tap_thuoc_tinh, tap_phu_thuoc_ham)
    assert khoa_ung_vien == ['ABC']

    # Phụ thuộc hàm vòng
    tap_thuoc_tinh = ['A', 'B', 'C']
    tap_phu_thuoc_ham = ['A → B', 'B → C', 'C → A']
    khoa_ung_vien, _ = tim_khoa_ung_vien(tap_thuoc_tinh, tap_phu_thuoc_ham)
    assert khoa_ung_vien == ['A', 'B', 'C']



def main():
    tests = [
        test_tinh_bao_dong_tap_thuoc_tinh,
        test_tinh_bao_dong_tap_phu_thuoc_ham,
        test_phan_loai_thuoc_tinh,
        test_kiem_tra_tinh_toi_thieu,
        test_tim_khoa_ung_vien,
    ]
    print(f'Chạy {len(tests)} bài kiểm thử...\n')
    for t in tests:
        t()
    print('\nALL TESTS PASSED')


if __name__ == '__main__':
    main()