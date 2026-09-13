from dns.rdtypes.svcbbase import key_to_text

from backend.app.modules.LyThuyetCSDL.utils.kiem_tra_hop_le import (
    co_phai_thuoc_tinh_hop_le,
    co_phai_phu_thuoc_ham_hop_le,
    co_phai_phu_thuoc_ham_hien_nhien,
    thuoc_tinh_co_trong_phu_thuoc_ham,
    kiem_tra_tap_thuoc_tinh,
    kiem_tra_tap_phu_thuoc_ham,
    kiem_tra_tap_thuoc_tinh_can_tim,
    kiem_tra_dang_chuan
)


def test_co_phai_thuoc_tinh_hop_le():
    assert co_phai_thuoc_tinh_hop_le('') == False
    assert co_phai_thuoc_tinh_hop_le('1') == False
    assert co_phai_thuoc_tinh_hop_le('Â') == False
    assert co_phai_thuoc_tinh_hop_le('aa') == False
    assert co_phai_thuoc_tinh_hop_le('a') == True
    assert co_phai_thuoc_tinh_hop_le('A') == True


def test_co_phai_phu_thuoc_ham_hop_le():
    tap_thuoc_tinh = {'A', 'B', 'C'}
    assert co_phai_phu_thuoc_ham_hop_le({'D'}, {'C'}, {}) == False
    assert co_phai_phu_thuoc_ham_hop_le({'D'}, {'C'}, tap_thuoc_tinh) == False
    assert co_phai_phu_thuoc_ham_hop_le({'A'}, {'D'}, tap_thuoc_tinh) == False
    assert co_phai_phu_thuoc_ham_hop_le({'A'}, {'b'}, tap_thuoc_tinh) == False
    assert co_phai_phu_thuoc_ham_hop_le({'a'}, {'C'}, tap_thuoc_tinh) == False
    assert co_phai_phu_thuoc_ham_hop_le({'A', 'B'}, {'C'}, tap_thuoc_tinh) == True


def test_co_phai_phu_thuoc_ham_hien_nhien():
    assert co_phai_phu_thuoc_ham_hien_nhien({'A', 'B'}, {'C'}) == False
    assert co_phai_phu_thuoc_ham_hien_nhien({'A'}, {'a'}) == True
    assert co_phai_phu_thuoc_ham_hien_nhien({'A'}, {'A'}) == True
    assert co_phai_phu_thuoc_ham_hien_nhien({'a', 'B'}, {'A'}) == True
    assert co_phai_phu_thuoc_ham_hien_nhien({'A', 'B'}, {'A'}) == True


def test_thuoc_tinh_co_trong_phu_thuoc_ham():
    tap_phu_thuoc_ham = [({'A'}, {'B'}), ({'B'}, {'C'})]
    assert thuoc_tinh_co_trong_phu_thuoc_ham('D', tap_phu_thuoc_ham) == False
    assert thuoc_tinh_co_trong_phu_thuoc_ham('a', tap_phu_thuoc_ham) == False
    assert thuoc_tinh_co_trong_phu_thuoc_ham('A', tap_phu_thuoc_ham) == True


def test_kiem_tra_tap_thuoc_tinh():
    assert kiem_tra_tap_thuoc_tinh({'A', 'B', 'C'}) == (False, 'Tập thuộc tính phải là list')
    assert kiem_tra_tap_thuoc_tinh([]) == (False, 'Tập thuộc tính không được rỗng')
    assert kiem_tra_tap_thuoc_tinh(['A', 'B', 1]) == (False, 'Mỗi thuộc tính phải là chuỗi')
    assert kiem_tra_tap_thuoc_tinh(['A', 'B', '1']) == (False, "Thuộc tính '1' không hợp lệ")
    assert kiem_tra_tap_thuoc_tinh(['A', '1', '2']) == (False, "Thuộc tính '1' không hợp lệ")
    assert kiem_tra_tap_thuoc_tinh(['A', 'B', 'A']) == (False, "Thuộc tính 'A' bị trùng")
    assert kiem_tra_tap_thuoc_tinh(['A', 'B', 'A', 'B']) == (False, "Thuộc tính 'A' bị trùng")
    assert kiem_tra_tap_thuoc_tinh(['A', 'B', 'C']) == (True, 'Tập thuộc tính hợp lệ')


def test_kiem_tra_tap_phu_thuoc_ham():
    tap_thuoc_tinh = ['A', 'B', 'C']
    ket_qua = kiem_tra_tap_phu_thuoc_ham({}, tap_thuoc_tinh)
    assert ket_qua == (False, 'Tập phụ thuộc hàm phải là list')

    ket_qua = kiem_tra_tap_phu_thuoc_ham([], tap_thuoc_tinh)
    assert ket_qua == (False, 'Tập phụ thuộc hàm không được rỗng')

    ket_qua = kiem_tra_tap_phu_thuoc_ham(['A → B'], tap_thuoc_tinh)
    assert ket_qua == (False, 'Phụ thuộc hàm thứ 1 phải là object')

    ket_qua = kiem_tra_tap_phu_thuoc_ham([{'trai': [], 'phai': []}], tap_thuoc_tinh)
    assert ket_qua == (False, "Phụ thuộc hàm thứ 1 phải có 've_trai' và 've_phai'")

    ket_qua = kiem_tra_tap_phu_thuoc_ham([{'ve_trai': [], 've_phai': "B"}], tap_thuoc_tinh)
    assert ket_qua == (False, 'Vế trái của phụ thuộc hàm thứ 1 phải là chuỗi')

    ket_qua = kiem_tra_tap_phu_thuoc_ham([{'ve_trai': "A", 've_phai': []}], tap_thuoc_tinh)
    assert ket_qua == (False, 'Vế phải của phụ thuộc hàm thứ 1 phải là chuỗi')

    ket_qua = kiem_tra_tap_phu_thuoc_ham([{'ve_trai': "A", 've_phai': "D"}], tap_thuoc_tinh)
    assert ket_qua == (False, "Thuộc tính 'D' trong phụ thuộc hàm không tồn tại trong tập thuộc tính")

    ket_qua = kiem_tra_tap_phu_thuoc_ham([{'ve_trai': "AB", 've_phai': "A"}], tap_thuoc_tinh)
    assert ket_qua == (False, "Phụ thuộc hàm 'AB → A' là phụ thuộc hàm hiển nhiên")

    ket_qua = kiem_tra_tap_phu_thuoc_ham(
        [{'ve_trai': "AB", 've_phai': "C"}, {'ve_trai': "AB", 've_phai': "C"}],
        tap_thuoc_tinh
    )
    assert ket_qua == (False, "Phụ thuộc hàm 'AB → C' bị trùng")

    ket_qua = kiem_tra_tap_phu_thuoc_ham(
        [{'ve_trai': "AB", 've_phai': "C"}],
        tap_thuoc_tinh
    )
    assert ket_qua == (True, 'Tập phụ thuộc hàm hợp lệ')


def test_kiem_tra_tap_thuoc_tinh_can_tim():
    tap_thuoc_tinh = ['A', 'B', 'C']

    ket_qua = kiem_tra_tap_thuoc_tinh_can_tim({}, tap_thuoc_tinh)
    assert ket_qua == (False, 'Tập thuộc tính cần tìm phải là list')

    ket_qua = kiem_tra_tap_thuoc_tinh_can_tim([], tap_thuoc_tinh)
    assert ket_qua == (False, 'Tập thuộc tính cần tìm không được rỗng')

    ket_qua = kiem_tra_tap_thuoc_tinh_can_tim([1], tap_thuoc_tinh)
    assert ket_qua == (False, 'Mỗi thuộc tính cần tìm phải là chuỗi')

    ket_qua = kiem_tra_tap_thuoc_tinh_can_tim(['1'], tap_thuoc_tinh)
    assert ket_qua == (False, "Thuộc tính '1' trong tập cần tìm không hợp lệ")

    ket_qua = kiem_tra_tap_thuoc_tinh_can_tim(['â'], tap_thuoc_tinh)
    assert ket_qua == (False, "Thuộc tính 'â' trong tập cần tìm không hợp lệ")

    ket_qua = kiem_tra_tap_thuoc_tinh_can_tim(['ab'], tap_thuoc_tinh)
    assert ket_qua == (False, "Thuộc tính 'ab' trong tập cần tìm không hợp lệ")

    ket_qua = kiem_tra_tap_thuoc_tinh_can_tim(['F'], tap_thuoc_tinh)
    assert ket_qua == (False, "Thuộc tính 'F' không tồn tại trong tập thuộc tính")

    ket_qua = kiem_tra_tap_thuoc_tinh_can_tim(['a'], tap_thuoc_tinh)
    assert ket_qua == (True, 'Tập thuộc tính cần tìm hợp lệ')

    ket_qua = kiem_tra_tap_thuoc_tinh_can_tim(['A'], tap_thuoc_tinh)
    assert ket_qua == (True, 'Tập thuộc tính cần tìm hợp lệ')


def test_kiem_tra_dang_chuan():
    assert kiem_tra_dang_chuan(2) == (False, 'Dạng chuẩn phải là chuỗi')
    assert kiem_tra_dang_chuan("dang chuan 2") == (
        False, "Dạng chuẩn 'DANG CHUAN 2' không hợp lệ, phải là 2NF, 3NF hoặc BCNF"
    )
    assert kiem_tra_dang_chuan("2nf") == (True, 'Dạng chuẩn hợp lệ')
    assert kiem_tra_dang_chuan("bCnF") == (True, 'Dạng chuẩn hợp lệ')
    assert kiem_tra_dang_chuan("BCNF") == (True, 'Dạng chuẩn hợp lệ')


def main():
    tests = [
        test_co_phai_thuoc_tinh_hop_le,
        test_co_phai_phu_thuoc_ham_hop_le,
        test_co_phai_phu_thuoc_ham_hien_nhien,
        test_thuoc_tinh_co_trong_phu_thuoc_ham,
        test_kiem_tra_tap_thuoc_tinh,
        test_kiem_tra_tap_phu_thuoc_ham,
        test_kiem_tra_tap_thuoc_tinh_can_tim,
        test_kiem_tra_dang_chuan
    ]
    print(f"Chạy {len(tests)} bài kiểm thử...\n")
    for t in tests:
        t()
    print("\nALL TESTS PASSED")


if __name__ == "__main__":
    main()