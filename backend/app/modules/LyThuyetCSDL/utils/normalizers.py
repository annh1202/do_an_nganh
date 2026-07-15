# ====================<< NORMALIZE ATTRIBUTES >>====================
def normalize_attr(attr):
    """
    Chuẩn hóa một thuộc tính đơn lẻ bằng cách loại bỏ khoảng trắng thừa
    và chuyển đổi thành chữ hoa.

    Args:
        attr (str): Chuỗi ký tự của thuộc tính cần chuẩn hóa.

    Returns:
        str: Thuộc tính đã được xử lý (viết hoa và cắt khoảng trắng).
    """
    return attr.strip().upper()


def normalize_attrs(attrs):
    """
    Chuẩn hóa một tập hợp các thuộc tính đầu vào thành một set chứa các thuộc tính
    đã viết hoa và loại bỏ khoảng trắng, giúp loại bỏ các phần tử trùng lặp.

    Args:
        attrs (iterable): Danh sách hoặc tập hợp các thuộc tính thô.

    Returns:
        set: Tập hợp các thuộc tính duy nhất đã được chuẩn hóa.
    """
    return set(normalize_attr(attr) for attr in attrs)


# ====================<< NORMALIZE FDS >>====================
def normalize_fd_to_tuple(fd_str):
    """
    Phân tích và chuẩn hóa một chuỗi phụ thuộc hàm thô (dạng "A -> B" hoặc "A → B")
    thành một cặp tuple chứa vế trái (LHS) và vế phải (RHS) dưới dạng frozenset.

    Args:
        fd_str (str): Chuỗi ký tự đại diện cho phụ thuộc hàm.

    Returns:
        tuple: Bộ đôi (lhs, rhs) trong đó mỗi vế là một frozenset các thuộc tính,
               hoặc None nếu chuỗi không đúng định dạng phụ thuộc hàm.
    """
    if "→" in fd_str:
        left, right = fd_str.split("→")
    elif "->" in fd_str:
        left, right = fd_str.split("->")
    else:
        return None

    lhs = frozenset(left.replace(" ", "").upper())
    rhs = frozenset(right.replace(" ", "").upper())

    return lhs, rhs


def normalize_fds_to_tuple(fds_raw):
    """
    Chuẩn hóa toàn bộ danh sách các chuỗi phụ thuộc hàm thô đầu vào thành một
    danh sách các cặp tuple (lhs, rhs) hợp lệ, tự động loại bỏ các chuỗi lỗi.

    Args:
        fds_raw (list): Danh sách các chuỗi phụ thuộc hàm thô chưa qua xử lý.

    Returns:
        list: Danh sách các phụ thuộc hàm đã được cấu trúc lại thành dạng [(lhs, rhs), ...].
    """
    return [parsed for fd in fds_raw if (parsed := normalize_fd_to_tuple(fd))]


def normalize_fd_side(attrs):
    """
    Chuẩn hóa một vế của phụ thuộc hàm (tập hợp các thuộc tính vế trái hoặc vế phải)
    thành định dạng bất biến frozenset để phục vụ cho các phép toán tập hợp nâng cao.

    Args:
        attrs (iterable): Tập hợp các thuộc tính thuộc một vế của phụ thuộc hàm.

    Returns:
        frozenset: Tập hợp bất biến chứa các thuộc tính đã được chuẩn hóa.
    """
    return frozenset(normalize_attr(attr) for attr in attrs)