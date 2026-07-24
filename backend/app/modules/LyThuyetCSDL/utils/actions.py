from backend.app.modules.LyThuyetCSDL.config import LoaiThongBao
from backend.app.modules.LyThuyetCSDL.utils.formatters import format_fd
from backend.app.modules.LyThuyetCSDL.utils.normalizers import normalize_attr, normalize_fds_to_tuple, normalize_fd_side
from backend.app.modules.LyThuyetCSDL.utils.validators import is_attribute, is_attribute_used, is_valid_fd, \
    is_trivial_fd


# ====================<< ATTRIBUTE >>====================
def them_thuoc_tinh(attribute, attributes):
    """
    Chuẩn hóa và thêm một thuộc tính mới vào tập thuộc tính gốc của quan hệ (R).
    Đảm bảo tính hợp lệ của ký tự và kiểm tra trùng lặp trước khi thực hiện sắp xếp lại.

    Args:
        attribute (str): Thuộc tính thô nhận từ người dùng.
        attributes (list): Tập hợp các thuộc tính hiện tại của quan hệ.

    Returns:
        tuple: Bộ ba giá trị (Trạng thái thực thi bool, Phân loại thông báo UI, Nội dung thông báo).
    """
    attribute = normalize_attr(attribute)

    if not is_attribute(attribute):
        return False, LoaiThongBao.DANGER, "Thuộc tính phải là một chữ cái tiếng Anh"

    if attribute in attributes:
        return False, LoaiThongBao.WARNING, "Thuộc tính đã tồn tại"

    attributes.append(attribute)
    attributes.sort()

    return True, LoaiThongBao.SUCCESS, f"Đã thêm thuộc tính {attribute}"


def xoa_thuoc_tinh(attribute, attributes, fds, target_attrs=None):
    """
    Xóa một thuộc tính khỏi tập thuộc tính gốc của quan hệ (R).
    Ràng buộc: Thuộc tính muốn xóa không được phép xuất hiện trong tập phụ thuộc hàm (F)
    hoặc tập thuộc tính mục tiêu (X) hiện tại.

    Args:
        attribute (str): Thuộc tính cần xóa.
        attributes (list): Tập hợp các thuộc tính hiện tại của quan hệ.
        fds (list): Tập hợp các phụ thuộc hàm hiện tại của hệ thống.
        target_attrs (list, optional): Tập thuộc tính mục tiêu X (nếu có).

    Returns:
        tuple: Bộ ba giá trị phản hồi trạng thái thực thi nghiệp vụ và thông báo lỗi/thành công.
    """
    attribute = normalize_attr(attribute)

    if not is_attribute(attribute):
        return False, LoaiThongBao.DANGER, "Thuộc tính phải là một chữ cái tiếng Anh"

    if attribute not in attributes:
        return False, LoaiThongBao.WARNING, "Thuộc tính không tồn tại"

    if is_attribute_used(attribute, normalize_fds_to_tuple(fds)):
        return False, LoaiThongBao.WARNING, f"Không thể xoá vì thuộc tính {attribute} xuất hiện trong F"

    if target_attrs is not None:
        if attribute in target_attrs:
            return False, LoaiThongBao.WARNING, f"Không thể xoá vì thuộc tính {attribute} xuất hiện trong X"

    attributes.remove(attribute)

    return True, LoaiThongBao.SUCCESS, f"Đã xoá thuộc tính {attribute}"


def xoa_trong_tap_thuoc_tinh(attributes, fds, target_attrs=None):
    """
    Làm rỗng hoàn toàn tập thuộc tính gốc của quan hệ (R).
    Ràng buộc: Chỉ cho phép làm rỗng khi tập phụ thuộc hàm (F) và tập mục tiêu (X) đã được xóa trống trước đó.

    Args:
        attributes (list): Tập hợp các thuộc tính của quan hệ.
        fds (list): Tập phụ thuộc hàm hiện tại.
        target_attrs (list, optional): Tập thuộc tính mục tiêu X hiện tại.

    Returns:
        tuple: Bộ ba giá trị kết quả thực hiện hành động.
    """
    if target_attrs is not None:
        if fds or target_attrs:
            return (
                False,
                LoaiThongBao.WARNING,
                "Không thể xoá toàn bộ tập thuộc tính khi F hoặc X chưa rỗng"
            )
    else:
        if fds:
            return (
                False,
                LoaiThongBao.WARNING,
                "Không thể xoá toàn bộ tập thuộc tính khi F chưa rỗng"
            )
    attributes.clear()

    return True, LoaiThongBao.SUCCESS, "Đã xoá toàn bộ tập thuộc tính"


# ====================<< FUNCTIONAL DEPENDENCY >>====================
def them_phu_thuoc_ham(thuoc_tinh_ve_trai, thuoc_tinh_ve_phai, attributes, fds):
    """
    Chuẩn hóa và thêm một phụ thuộc hàm mới dạng vế trái (LHS) -> vế phải (RHS) vào tập F.
    Ràng buộc: Các vế không được rỗng, mọi thuộc tính thành phần bắt buộc phải tồn tại
    trong tập thuộc tính gốc (R) và phụ thuộc hàm chưa từng tồn tại trong hệ thống.

    Args:
        thuoc_tinh_ve_trai (str/iterable): Thuộc tính thô vế trái.
        thuoc_tinh_ve_phai (str/iterable): Thuộc tính thô vế phải.
        attributes (list): Tập thuộc tính hiện tại của quan hệ R.
        fds (list): Tập chuỗi các phụ thuộc hàm hiện tại.

    Returns:
        tuple: Bộ ba giá trị (Trạng thái thực thi, Phân loại thông báo UI, Nội dung thông báo).
    """
    ve_trai = normalize_fd_side(thuoc_tinh_ve_trai)
    ve_phai = normalize_fd_side(thuoc_tinh_ve_phai)

    if not ve_trai or not ve_phai:
        return False, LoaiThongBao.DANGER, "Hai vế của phụ thuộc hàm không được rỗng"

    if not is_valid_fd(ve_trai, ve_phai, attributes):
        return False, LoaiThongBao.WARNING, "Mọi thuộc tính trong F phải thuộc tập R"

    if is_trivial_fd(thuoc_tinh_ve_trai, thuoc_tinh_ve_phai):
        return False, LoaiThongBao.WARNING, "Phụ thuộc hàm hiển nhiên"

    fd_string = format_fd(ve_trai, ve_phai)
    if fd_string in fds:
        return False, LoaiThongBao.WARNING, "Phụ thuộc hàm đã tồn tại"

    fds.append(fd_string)

    return True, LoaiThongBao.SUCCESS, f"Đã thêm phụ thuộc hàm {fd_string}"


def xoa_phu_thuoc_ham(thuoc_tinh_ve_trai, thuoc_tinh_ve_phai, fds):
    """
    Xóa một phụ thuộc hàm xác định ra khỏi tập phụ thuộc hàm (F) của hệ thống.

    Args:
        thuoc_tinh_ve_trai (str/iterable): Thành phần vế trái của phụ thuộc hàm cần xóa.
        thuoc_tinh_ve_phai (str/iterable): Thành phần vế phải của phụ thuộc hàm cần xóa.
        fds (list): Danh sách các chuỗi phụ thuộc hàm hiện tại.

    Returns:
        tuple: Bộ ba giá trị kết quả trả về tương tự các tác vụ trên.
    """
    ve_trai = normalize_fd_side(thuoc_tinh_ve_trai)
    ve_phai = normalize_fd_side(thuoc_tinh_ve_phai)

    fd_string = format_fd(ve_trai, ve_phai)

    if fd_string not in fds:
        return False, LoaiThongBao.WARNING, "Phụ thuộc hàm không tồn tại"

    fds.remove(fd_string)

    return True, LoaiThongBao.SUCCESS, f"Đã xoá phụ thuộc hàm {fd_string}"


def xoa_trong_tap_phu_thuoc_ham(fds):
    """
    Xóa sạch toàn bộ các phụ thuộc hàm có trong tập phụ thuộc hàm (F).

    Args:
        fds (list): Tập chuỗi phụ thuộc hàm của hệ thống cần làm rỗng.

    Returns:
        tuple: Bộ ba giá trị trạng thái hoàn thành công việc.
    """
    fds.clear()
    return True, LoaiThongBao.SUCCESS, "Đã xoá toàn bộ tập phụ thuộc hàm"


# ====================<< TARGET ATTRIBUTE >>====================
def them_thuoc_tinh_can_tim(attribute, attributes, target_attrs):
    """
    Chuẩn hóa và nạp thêm một thuộc tính đích vào tập thuộc tính mục tiêu (X) để chuẩn bị tìm bao đóng thuộc tính.
    Ràng buộc: Thuộc tính bổ sung phải thuộc tập thuộc tính gốc (R) và chưa tồn tại sẵn trong tập X.

    Args:
        attribute (str): Thuộc tính thô đầu vào cần thêm.
        attributes (list): Tập thuộc tính gốc của lược đồ quan hệ.
        target_attrs (list): Tập thuộc tính mục tiêu X hiện tại.

    Returns:
        tuple: Bộ ba giá trị thông điệp điều hướng phản hồi ở giao diện người dùng.
    """
    attribute = normalize_attr(attribute)

    if not is_attribute(attribute):
        return False, LoaiThongBao.DANGER, "Thuộc tính phải là một chữ cái tiếng Anh"

    if attribute not in attributes:
        return False, LoaiThongBao.WARNING, f"Thuộc tính {attribute} không thuộc tập R"

    if attribute in target_attrs:
        return False, LoaiThongBao.WARNING, f"Thuộc tính {attribute} đã tồn tại trong X"

    target_attrs.append(attribute)
    target_attrs.sort()

    return True, LoaiThongBao.SUCCESS, f"Đã thêm thuộc tính"


def xoa_thuoc_tinh_can_tim(attribute, target_attrs):
    """
    Xóa một thuộc tính cụ thể ra khỏi tập thuộc tính mục tiêu (X).

    Args:
        attribute (str): Ký tự thuộc tính mục tiêu cần xóa bỏ.
        target_attrs (list): Tập thuộc tính mục tiêu X hiện tại.

    Returns:
        tuple: Bộ ba giá trị thông điệp trạng thái hệ thống.
    """
    attribute = normalize_attr(attribute)

    if not is_attribute(attribute):
        return False, LoaiThongBao.DANGER, "Thuộc tính phải là một chữ cái tiếng Anh"

    if attribute not in target_attrs:
        return False, LoaiThongBao.WARNING, f"Thuộc tính {attribute} không tồn tại trong X"

    target_attrs.remove(attribute)

    return True, LoaiThongBao.SUCCESS, f"Đã xoá thuộc tính {attribute} khỏi X"


def xoa_trong_tap_thuoc_tinh_can_tim(target_attrs):
    """
    Xóa trống toàn bộ tập thuộc tính mục tiêu (X) hiện tại.

    Args:
        target_attrs (list): Tập thuộc tính mục tiêu X cần làm sạch.

    Returns:
        tuple: Bộ ba giá trị xác nhận tác vụ xóa hoàn tất.
    """
    target_attrs.clear()
    return True, LoaiThongBao.SUCCESS, "Đã xoá toàn bộ tập X"