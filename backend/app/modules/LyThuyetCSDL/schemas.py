from pydantic import BaseModel, Field, field_validator
from typing import List
from typing import Generic, TypeVar


T = TypeVar("T")

class PhanHoi(BaseModel, Generic[T]):
    doi_tuong: T
    loai_thong_bao: str
    thong_bao: str

# ==========================================
# 1. ĐỊNH NGHĨA CÁC ĐỐI TƯỢNG DỮ LIỆU (SCHEMAS)
# ==========================================

# Cấu trúc của một Phụ thuộc hàm đơn lẻ (LHS -> RHS)
# LHS: Left-Hand Side (Vế trái), RHS: Right-Hand Side (Vế phải)
class PhuThuocHam(BaseModel):
    ve_trai: str = Field(..., description="Vế trái của phụ thuộc hàm, ví dụ: AB")
    ve_phai: str = Field(..., description="Vế phải của phụ thuộc hàm, ví dụ: C")

class TapPhuThuocHam(BaseModel):
    tap_phu_thuoc_ham: List[PhuThuocHam] = Field(..., description="Tập phụ thuộc hàm")

# Định dạng dữ liệu React gửi lên khi muốn Thêm/Xóa một thuộc tính trong R
class ThuocTinh(BaseModel):
    thuoc_tinh: str

class TapThuocTinh(BaseModel):
    tap_thuoc_tinh: List[str]

# Định dạng dữ liệu trả về cho React (Gồm danh sách thuộc tính R và tập F hiện tại)
class DeBaiTimBaoDongTapThuocTinh(BaseModel):
    tap_thuoc_tinh: list[str] = Field(
        default_factory=list,
        description="Danh sách các thuộc tính trong R"
    )

    tap_phu_thuoc_ham: list[PhuThuocHam] = Field(
        default_factory=list,
        description="Tập phụ thuộc hàm F"
    )

    tap_thuoc_tinh_can_tim: list[str] = Field(
        default_factory=list,
        description="Tập thuộc tính cần tìm bao đóng X"
    )

# ==========================================
# 2. BỘ NHỚ TẠM LƯU TRỮ TRẠNG THÁI (IN-MEMORY STATE)
# ==========================================
# Biến này đóng vai trò như một "Database ảo" nằm trên RAM.
# Khi bạn F5 lại server Python, dữ liệu trong này sẽ được reset về rỗng.
# db_ly_thuyet_csdl = {
#     # 1. Chức năng Bao đóng tập thuộc tính
#     "bao_dong_thuoc_tinh": {
#         "R": [],
#         "F": [],
#         "X": []  # Tập thuộc tính mục tiêu cần tìm bao đóng
#     },
#
#     # 2. Chức năng Bao đóng tập phụ thuộc hàm
#     "bao_dong_phu_thuoc_ham": {
#         "R": [],
#         "F": []
#     },
#
#     # 3. Chức năng Tìm khóa ứng viên
#     "khoa_ung_vien": {
#         "R": [],
#         "F": [],
#         "khoa_da_tim": []  # Lưu kết quả sau khi giải
#     },
#
#     # 4. Chức năng Xác định dạng chuẩn
#     "dang_chuan": {
#         "R": [],
#         "F": []
#     }
# }