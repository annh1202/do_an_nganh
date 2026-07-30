from backend.app.modules.LyThuyetCSDL.utils.chuan_hoa import chuan_hoa_tap_thuoc_tinh, chuan_hoa_thuoc_tinh


# ====================<< CHECK ATTRIBUTE >>====================
def co_phai_thuoc_tinh_hop_le(thuoc_tinh):
    if not thuoc_tinh:
        return False
    thuoc_tinh = thuoc_tinh.strip()
    return len(thuoc_tinh) == 1 and thuoc_tinh.isalpha() and thuoc_tinh.isascii()


def thuoc_tinh_co_trong_phu_thuoc_ham(thuoc_tinh, tap_phu_thuoc_ham):
    for ve_trai, ve_phai in tap_phu_thuoc_ham:
        if thuoc_tinh in ve_trai or thuoc_tinh in ve_phai:
            return True
    return False

# ====================<< CHECK FUNCTIONAL DEPENDENCY >>====================
def co_phai_phu_thuoc_ham_hien_nhien(thuoc_tinh_ve_trai, thuoc_tinh_ve_phai):
    ve_trai = chuan_hoa_tap_thuoc_tinh(thuoc_tinh_ve_trai)
    ve_phai = chuan_hoa_tap_thuoc_tinh(thuoc_tinh_ve_phai)

    return ve_phai.issubset(ve_trai)


def co_phai_phu_thuoc_ham_hop_le(ve_trai, ve_phai, tap_thuoc_tinh):
    tap_hop_thuoc_tinh = set(tap_thuoc_tinh)
    if ve_trai.issubset(tap_hop_thuoc_tinh) and ve_phai.issubset(tap_hop_thuoc_tinh):
        return True
    return False

# ====================<< VALIDATE COMMON STRUCTURE >>====================
def validate_common_fields(data):
    # attributes
    attributes = data.get("attributes")

    if not isinstance(attributes, list) or not attributes:
        return False, (
            "Field 'attributes' phải là list "
            "và không được rỗng"
        )

    # fds
    fds = data.get("fds")

    if not isinstance(fds, list):
        return False, "Field 'fds' phải là list"

    for i, fd in enumerate(fds):

        if not isinstance(fd, list) or len(fd) != 2:
            return False, (
                f"fds[{i}] phải có dạng "
                "[lhs, rhs]"
            )

        lhs, rhs = fd

        if not isinstance(lhs, list):
            return False, (
                f"fds[{i}][0] (lhs) "
                "phải là list"
            )

        if not isinstance(rhs, list):
            return False, (
                f"fds[{i}][1] (rhs) "
                "phải là list"
            )

    return True, "OK"


# ====================<< VALIDATE CLOSURE OF ATTRIBUTES >>====================
def validate_closure_of_attributes(data):
    """
    Kiểm tra tính hợp lệ toàn diện của tệp tin cấu hình dành cho bài toán "Tìm bao đóng của tập thuộc tính".
    Yêu cầu bổ sung trường mục tiêu 'target'.

    Args:
        data (dict): Dữ liệu phân tích từ file JSON.

    Returns:
        tuple: Bộ đôi (Trạng thái hợp lệ, Thông báo phản hồi kết quả).
    """
    # type
    if data.get("type") != "closure_of_attributes":
        return False, (
            "File không thuộc loại "
            "'closure_of_attributes'"
        )

    # common fields
    is_valid, message = validate_common_fields(data)

    if not is_valid:
        return False, message

    # target
    target = data.get("target")

    if target is None:
        return False, (
            "Type 'closure_of_attributes' "
            "phải có field 'target'"
        )

    if not isinstance(target, list):
        return False, (
            "Field 'target' phải là list"
        )

    return True, "File closure_of_attributes hợp lệ"


# ====================<< VALIDATE CLOSURE OF FUNCTIONAL DEPENDENCIES >>====================
def validate_closure_of_functional_dependencies(data):
    """
    Kiểm tra tính hợp lệ toàn diện của tệp tin cấu hình dành cho bài toán "Tìm bao đóng của tập phụ thuộc hàm".

    Args:
        data (dict): Dữ liệu phân tích từ file JSON.

    Returns:
        tuple: Bộ đôi (Trạng thái hợp lệ, Thông báo phản hồi kết quả).
    """
    # type
    if data.get("type") != (
            "closure_of_functional_dependencies"
    ):
        return False, (
            "File không thuộc loại "
            "'closure_of_functional_dependencies'"
        )

    # common fields
    is_valid, message = validate_common_fields(data)

    if not is_valid:
        return False, message

    return True, (
        "File closure_of_functional_dependencies hợp lệ"
    )


# ====================<< VALIDATE CANDIDATE KEYS >>====================
def validate_candidate_keys(data):
    """
    Kiểm tra tính hợp lệ toàn diện của tệp tin cấu hình dành cho bài toán "Tìm khóa ứng viên".

    Args:
        data (dict): Dữ liệu phân tích từ file JSON.

    Returns:
        tuple: Bộ đôi (Trạng thái hợp lệ, Thông báo phản hồi kết quả).
    """
    # type
    if data.get("type") != "candidate_keys":
        return False, (
            "File không thuộc loại "
            "'candidate_keys'"
        )

    # common fields
    is_valid, message = validate_common_fields(data)

    if not is_valid:
        return False, message

    return True, (
        "File candidate_keys hợp lệ"
    )


# ====================<< VALIDATE NORMAL FORM >>====================
def validate_normal_form(data):
    """
    Kiểm tra tính hợp lệ toàn diện của tệp tin cấu hình dành cho bài toán "Phân rã dạng chuẩn".
    Yêu cầu cấu hình phải tồn tại trường cấp độ đích 'target-level' thuộc danh sách (1NF, 2NF, 3NF, BCNF).

    Args:
        data (dict): Dữ liệu phân tích từ file JSON.

    Returns:
        tuple: Bộ đôi (Trạng thái hợp lệ, Thông báo phản hồi kết quả).
    """
    # type
    if data.get("type") != "normal_form":
        return False, (
            "File không thuộc loại "
            "'normal_form'"
        )

    # common fields
    is_valid, message = validate_common_fields(data)

    if not is_valid:
        return False, message

    # target-level
    level = data.get("target-level")

    valid_levels = {
        "1NF",
        "2NF",
        "3NF",
        "BCNF"
    }

    if level is None:
        return False, (
            "Type 'normal_form' "
            "phải có field 'target-level'"
        )

    if level not in valid_levels:
        return False, (
            "Field 'target-level' không hợp lệ. "
            "Phải là: 1NF, 2NF, 3NF hoặc BCNF"
        )

    return True, (
        "File normal_form hợp lệ"
    )