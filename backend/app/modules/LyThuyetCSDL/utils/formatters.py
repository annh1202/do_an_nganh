# ====================<< FORMAT ATTRIBUTE >>====================
def format_attrs(s):
    """
    Định dạng một tập hợp các thuộc tính thành một chuỗi ký tự được sắp xếp
    và phân tách bằng dấu phẩy (ví dụ: từ {'C', 'A', 'B'} thành "A, B, C").
    Dùng để hiển thị danh sách thuộc tính của một lược đồ quan hệ con hoặc tập bao đóng.

    Args:
        s (iterable): Tập hợp hoặc danh sách các thuộc tính thô.

    Returns:
        str: Chuỗi ký tự các thuộc tính đã sắp xếp và định dạng đẹp mắt.
    """
    return ", ".join(sorted(set(s)))


# ====================<< FORMAT FD >>====================
def format_fd_side(fd_side):
    """
    Định dạng một vế (trái hoặc phải) của phụ thuộc hàm bằng cách sắp xếp
    và viết liền các thuộc tính lại với nhau (ví dụ: từ {'B', 'A'} thành "AB").

    Args:
        fd_side (iterable): Tập hợp các thuộc tính thuộc một vế của phụ thuộc hàm.

    Returns:
        str: Chuỗi ký tự viết liền các thuộc tính đã sắp xếp.
    """
    return "".join(sorted(fd_side))


def format_fd(left, right):
    """
    Định dạng một cặp vế trái và vế phải thành một chuỗi biểu diễn phụ thuộc hàm hoàn chỉnh
    sử dụng ký tự mũi tên tiêu chuẩn (ví dụ: "AB → C").

    Args:
        left (iterable): Tập thuộc tính vế trái (LHS).
        right (iterable): Tập thuộc tính vế phải (RHS).

    Returns:
        str: Chuỗi ký tự biểu diễn phụ thuộc hàm dạng hoàn chỉnh.
    """
    return f"{format_fd_side(left)} → {format_fd_side(right)}"


def format_fds(fds_raw):
    """
    Chuyển đổi toàn bộ danh sách các cặp phụ thuộc hàm thô đầu vào thành một mảng
    các chuỗi phụ thuộc hàm đã định dạng sẵn sàng để hiển thị lên giao diện (UI).

    Args:
        fds_raw (list): Danh sách các phụ thuộc hàm thô dưới dạng [(lhs, rhs), ...].

    Returns:
        list: Danh sách các chuỗi phụ thuộc hàm đã định dạng hoàn chỉnh (ví dụ: ["A → B", "AB → CD"]).
    """
    return [
        format_fd(lhs, rhs)
        for lhs, rhs in fds_raw
        if lhs and rhs
    ]