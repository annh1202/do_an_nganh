from backend.app.modules.LyThuyetCSDL.utils.normalizers import normalize_attrs, normalize_attr


# ====================<< CHECK ATTRIBUTE >>====================
def is_attribute(attribute):
    """
    Kiểm tra một chuỗi đầu vào có tuân thủ định dạng của một thuộc tính đơn lẻ hay không.
    Một thuộc tính hợp lệ phải là một ký tự chữ cái duy nhất thuộc bảng chữ cái tiếng Anh.

    Args:
        attribute (str): Chuỗi ký tự cần kiểm tra.

    Returns:
        bool: True nếu chuỗi là một thuộc tính hợp lệ, ngược lại trả về False.
    """
    if not attribute:
        return False
    attribute = attribute.strip()
    return len(attribute) == 1 and attribute.isalpha() and attribute.isascii()

def is_attribute_used(attribute, fds):
    """
    Kiểm tra xem một thuộc tính cụ thể có xuất hiện trong tập phụ thuộc hàm hay không.

    Args:
        attribute (str): Thuộc tính cần kiểm tra sự tồn tại.
        fds (list): Danh sách các phụ thuộc hàm đã chuẩn hóa dưới dạng cặp (lhs, rhs).

    Returns:
        bool: True nếu thuộc tính có tham gia vào ít nhất một phụ thuộc hàm, ngược lại trả về False.
    """
    for lhs, rhs in fds:
        if attribute in lhs or attribute in rhs:
            return True
    return False

# ====================<< CHECK FUNCTIONAL DEPENDENCY >>====================
def is_trivial_fd(left, right):
    """
    Kiểm tra một phụ thuộc hàm có phải là phụ thuộc hiển nhiên hay không.

    Một phụ thuộc hàm X → Y được gọi là hiển nhiên nếu: Y ⊆ X

    Args:
        left (iterable | str): Tập thuộc tính vế trái.
        right (iterable | str): Tập thuộc tính vế phải.

    Returns:
        bool:
            - True nếu là phụ thuộc hàm hiển nhiên.
            - False nếu không phải.
    """
    lhs = normalize_attrs(left)
    rhs = normalize_attrs(right)

    return rhs.issubset(lhs)

def is_valid_fd(left, right, attributes):
    """
    Kiểm tra phụ thuộc hàm có hợp lệ với tập thuộc tính của quan hệ hay không.

    Một phụ thuộc hàm X → Y hợp lệ nếu mọi thuộc tính trong X và Y
    đều thuộc tập thuộc tính R của quan hệ.

    Args:
        left (set): Tập thuộc tính vế trái.
        right (set): Tập thuộc tính vế phải.
        attributes (iterable): Tập thuộc tính của quan hệ.

    Returns:
        bool:
            - True nếu mọi thuộc tính trong phụ thuộc hàm đều thuộc R.
            - False nếu tồn tại thuộc tính không thuộc R.
    """
    attrs = set(attributes)
    if left.issubset(attrs) and right.issubset(attrs):
        return True
    return False

# ====================<< VALIDATE COMMON STRUCTURE >>====================
def validate_common_fields(data):
    """
    Kiểm tra các trường cấu trúc chung bắt buộc xuất hiện trong mọi tệp tin cấu hình bài toán
    bao gồm trường 'attributes' và trường 'fds'.

    Args:
        data (dict): Dữ liệu lược đồ đọc từ tệp tin JSON.

    Returns:
        tuple: Bộ đôi giá trị bao gồm:
            - bool: Trạng thái hợp lệ của cấu trúc chung (True/False).
            - str: Thông báo lỗi chi tiết nếu phát hiện sai sót, hoặc "OK" nếu hợp lệ.
    """
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