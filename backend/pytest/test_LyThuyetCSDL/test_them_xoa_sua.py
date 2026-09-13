from backend.app.modules.LyThuyetCSDL.utils.them_xoa_sua import (
    them_thuoc_tinh,
    xoa_thuoc_tinh,
    xoa_trong_tap_thuoc_tinh,
    them_phu_thuoc_ham,
    xoa_phu_thuoc_ham,
    xoa_trong_tap_phu_thuoc_ham,
    them_thuoc_tinh_can_tim,
    xoa_thuoc_tinh_can_tim,
    xoa_trong_tap_thuoc_tinh_can_tim
)


# ==============================================
# TEST THÊM XÓA TRONG TẬP THUỘC TÍNH
# ==============================================
def test_them_thuoc_tinh():
    tap_thuoc_tinh = []
    assert them_thuoc_tinh('1', tap_thuoc_tinh) == (
        False,  'danger', 'Thuộc tính phải là một chữ cái tiếng Anh'
    )
    assert tap_thuoc_tinh == []

    assert them_thuoc_tinh('A', tap_thuoc_tinh) == (
        True, 'success', 'Đã thêm thuộc tính A'
    )
    assert tap_thuoc_tinh == ['A']

    assert them_thuoc_tinh('A', tap_thuoc_tinh) == (
        False, 'warning', 'Thuộc tính đã tồn tại'
    )
    assert tap_thuoc_tinh == ['A']


def test_xoa_thuoc_tinh():
    tap_thuoc_tinh = []
    tap_phu_thuoc_ham = ['A → B']
    tap_thuoc_tinh_muc_tieu = ['A']
    assert xoa_thuoc_tinh("1", tap_thuoc_tinh,[],[]) == (
        False, 'danger', 'Thuộc tính phải là một chữ cái tiếng Anh'
    )
    assert tap_thuoc_tinh == []

    assert xoa_thuoc_tinh("A", [], [], []) == (
        False, 'warning', 'Thuộc tính không tồn tại'
    )
    assert tap_thuoc_tinh == []

    tap_thuoc_tinh = ['A', 'B']
    assert xoa_thuoc_tinh("A", tap_thuoc_tinh, tap_phu_thuoc_ham, []) == (
        False, 'warning', 'Không thể xoá vì thuộc tính A xuất hiện trong F'
    )
    assert tap_thuoc_tinh == ['A', 'B']

    assert xoa_thuoc_tinh("A", tap_thuoc_tinh, [], tap_thuoc_tinh_muc_tieu) == (
        False, 'warning', 'Không thể xoá vì thuộc tính A xuất hiện trong X'
    )
    assert tap_thuoc_tinh == ['A', 'B']

    assert xoa_thuoc_tinh("A", tap_thuoc_tinh, tap_phu_thuoc_ham, tap_thuoc_tinh_muc_tieu) == (
        False, 'warning', 'Không thể xoá vì thuộc tính A xuất hiện trong F và X'
    )
    assert tap_thuoc_tinh == ['A', 'B']

    assert xoa_thuoc_tinh("A", tap_thuoc_tinh, [], []) == (
        True, 'success', 'Đã xoá thuộc tính A'
    )
    assert tap_thuoc_tinh == ['B']


def test_xoa_trong_tap_thuoc_tinh():
    tap_thuoc_tinh = ['A', 'B']

    assert xoa_trong_tap_thuoc_tinh(tap_thuoc_tinh, ['A → B'], None) == (
        False, 'warning', 'Không thể xoá toàn bộ tập thuộc tính khi F chưa rỗng'
    )
    assert tap_thuoc_tinh == ['A', 'B']

    assert xoa_trong_tap_thuoc_tinh(tap_thuoc_tinh, [], ['A']) == (
        False, 'warning', 'Không thể xoá toàn bộ tập thuộc tính khi F hoặc X chưa rỗng'
    )
    assert tap_thuoc_tinh == ['A', 'B']

    assert xoa_trong_tap_thuoc_tinh(tap_thuoc_tinh, [], []) == (
        True, 'success', 'Đã xoá toàn bộ tập thuộc tính'
    )
    assert tap_thuoc_tinh == []

    tap_thuoc_tinh = ['A', 'B']
    assert xoa_trong_tap_thuoc_tinh(tap_thuoc_tinh, [], None) == (
        True, 'success', 'Đã xoá toàn bộ tập thuộc tính'
    )
    assert tap_thuoc_tinh == []

# ====================================================
# TEST THÊM XÓA TRONG TẬP PHỤ THUỘC HÀM
# ====================================================
def test_them_phu_thuoc_ham():
    tap_thuoc_tinh = ['A', 'B']
    tap_phu_thuoc_ham = []

    assert them_phu_thuoc_ham('', '', tap_thuoc_tinh, tap_phu_thuoc_ham) == (
        False, 'danger', 'Hai vế của phụ thuộc hàm không được rỗng'
    )
    assert tap_phu_thuoc_ham == []

    assert them_phu_thuoc_ham('', 'B', tap_thuoc_tinh, tap_phu_thuoc_ham) == (
        False, 'danger', 'Hai vế của phụ thuộc hàm không được rỗng'
    )
    assert tap_phu_thuoc_ham == []

    assert them_phu_thuoc_ham('A', '', tap_thuoc_tinh, tap_phu_thuoc_ham) == (
        False, 'danger', 'Hai vế của phụ thuộc hàm không được rỗng'
    )
    assert tap_phu_thuoc_ham == []

    assert them_phu_thuoc_ham('A', 'F', tap_thuoc_tinh, tap_phu_thuoc_ham) == (
        False, 'warning', 'Mọi thuộc tính trong F phải thuộc tập R'
    )
    assert tap_phu_thuoc_ham == []

    assert them_phu_thuoc_ham('1', '2', tap_thuoc_tinh, tap_phu_thuoc_ham) == (
        False, 'warning', 'Mọi thuộc tính trong F phải thuộc tập R'
    )
    assert tap_phu_thuoc_ham == []

    assert them_phu_thuoc_ham('A', 'A', tap_thuoc_tinh, tap_phu_thuoc_ham) == (
        False, 'warning', 'Phụ thuộc hàm hiển nhiên'
    )
    assert tap_phu_thuoc_ham == []

    assert them_phu_thuoc_ham('A', 'B', tap_thuoc_tinh, tap_phu_thuoc_ham) == (
        True, 'success', 'Đã thêm phụ thuộc hàm A → B'
    )
    assert tap_phu_thuoc_ham == ['A → B']

    assert them_phu_thuoc_ham('A', 'B', tap_thuoc_tinh, tap_phu_thuoc_ham) == (
        False, 'warning', 'Phụ thuộc hàm đã tồn tại'
    )
    assert tap_phu_thuoc_ham == ['A → B']


def test_xoa_phu_thuoc_ham():
    tap_phu_thuoc_ham = ['A → B']

    assert xoa_phu_thuoc_ham('', '', tap_phu_thuoc_ham) == (
        False, 'danger', 'Hai vế của phụ thuộc hàm không được rỗng'
    )
    assert tap_phu_thuoc_ham == ['A → B']

    assert xoa_phu_thuoc_ham('A', '', tap_phu_thuoc_ham) == (
        False, 'danger', 'Hai vế của phụ thuộc hàm không được rỗng'
    )
    assert tap_phu_thuoc_ham == ['A → B']

    assert xoa_phu_thuoc_ham('', 'B', tap_phu_thuoc_ham) == (
        False, 'danger', 'Hai vế của phụ thuộc hàm không được rỗng'
    )
    assert tap_phu_thuoc_ham == ['A → B']

    assert xoa_phu_thuoc_ham('A', 'C', tap_phu_thuoc_ham) == (
        False, 'warning', 'Phụ thuộc hàm không tồn tại'
    )
    assert tap_phu_thuoc_ham == ['A → B']

    assert xoa_phu_thuoc_ham('A', 'B', tap_phu_thuoc_ham) == (
        True, 'success', 'Đã xoá phụ thuộc hàm A → B'
    )
    assert tap_phu_thuoc_ham == []


def test_xoa_trong_tap_phu_thuoc_ham():
    tap_phu_thuoc_ham = ['A → B']
    assert xoa_trong_tap_phu_thuoc_ham(tap_phu_thuoc_ham)
    assert tap_phu_thuoc_ham == []

# =======================================================
# TEST THÊM XÓA TRONG TẬP THUỘC TÍNH CẦN TÌM BAO ĐÓNG
# =======================================================
def test_them_thuoc_tinh_can_tim():
    tap_thuoc_tinh = ['A']
    tap_thuoc_muc_tieu = []

    assert them_thuoc_tinh_can_tim('', tap_thuoc_tinh, tap_thuoc_muc_tieu) == (
        False, 'danger', 'Thuộc tính phải là một chữ cái tiếng Anh'
    )
    assert tap_thuoc_muc_tieu == []

    assert them_thuoc_tinh_can_tim('1', tap_thuoc_tinh, tap_thuoc_muc_tieu) == (
        False, 'danger', 'Thuộc tính phải là một chữ cái tiếng Anh'
    )
    assert tap_thuoc_muc_tieu == []

    assert them_thuoc_tinh_can_tim('F', tap_thuoc_tinh, tap_thuoc_muc_tieu) == (
        False, 'warning', 'Thuộc tính F không thuộc tập R'
    )
    assert tap_thuoc_muc_tieu == []

    assert them_thuoc_tinh_can_tim('A', tap_thuoc_tinh, tap_thuoc_muc_tieu) == (
        True, 'success', 'Đã thêm thuộc tính'
    )
    assert tap_thuoc_muc_tieu == ['A']

    assert them_thuoc_tinh_can_tim('A', tap_thuoc_tinh, tap_thuoc_muc_tieu) == (
        False, 'warning', 'Thuộc tính A đã tồn tại trong X'
    )
    assert tap_thuoc_muc_tieu == ['A']


def test_xoa_thuoc_tinh_can_tim():
    tap_thuoc_tinh_muc_tieu = ['A']

    assert xoa_thuoc_tinh_can_tim('', tap_thuoc_tinh_muc_tieu) == (
        False, 'danger', 'Thuộc tính phải là một chữ cái tiếng Anh'
    )
    assert tap_thuoc_tinh_muc_tieu == ['A']

    assert xoa_thuoc_tinh_can_tim('1', tap_thuoc_tinh_muc_tieu) == (
        False, 'danger', 'Thuộc tính phải là một chữ cái tiếng Anh'
    )
    assert tap_thuoc_tinh_muc_tieu == ['A']

    assert xoa_thuoc_tinh_can_tim('B', tap_thuoc_tinh_muc_tieu) == (
        False, 'warning', 'Thuộc tính B không tồn tại trong X'
    )
    assert tap_thuoc_tinh_muc_tieu == ['A']

    assert xoa_thuoc_tinh_can_tim('A', tap_thuoc_tinh_muc_tieu) == (
        True, 'success', 'Đã xoá thuộc tính A khỏi X'
    )
    assert tap_thuoc_tinh_muc_tieu == []


def test_xoa_trong_tap_thuoc_tinh_can_tim():
    tap_thuoc_tinh_muc_tieu = ['A', 'B']
    assert xoa_trong_tap_thuoc_tinh_can_tim(tap_thuoc_tinh_muc_tieu) == (
        True, 'success', 'Đã xoá toàn bộ tập X'
    )
    assert tap_thuoc_tinh_muc_tieu == []


def main():
    tests = [
        test_them_thuoc_tinh,
        test_xoa_thuoc_tinh,
        test_xoa_trong_tap_thuoc_tinh,
        test_them_phu_thuoc_ham,
        test_xoa_phu_thuoc_ham,
        test_xoa_trong_tap_phu_thuoc_ham,
        test_them_thuoc_tinh_can_tim,
        test_xoa_thuoc_tinh_can_tim,
        test_xoa_trong_tap_thuoc_tinh_can_tim
    ]
    print(f"Chạy {len(tests)} bài kiểm thử...\n")
    for t in tests:
        t()
    print("\nALL TESTS PASSED")


if __name__ == "__main__":
    main()