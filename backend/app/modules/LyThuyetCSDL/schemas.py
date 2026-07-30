from typing import Generic, TypeVar

from pydantic import BaseModel, Field


# ===================================================
# 1. ĐỊNH NGHĨA CÁC ĐỐI TƯỢNG DỮ LIỆU ĐƯỢC GỬI LÊN
# ===================================================
class ThuocTinh(BaseModel):
    thuoc_tinh: str

class PhuThuocHam(BaseModel):
    ve_trai: str = Field(..., description="Vế trái của phụ thuộc hàm, ví dụ: AB")
    ve_phai: str = Field(..., description="Vế phải của phụ thuộc hàm, ví dụ: C")

class DangChuan(BaseModel):
    dang_chuan: str

# ===================================================
# 2. ĐỊNH NGHĨA CÁC ĐỐI TƯỢNG DỮ LIỆU ĐƯỢC TRẢ VỀ
# ===================================================
T = TypeVar("T")

class PhanHoi(BaseModel, Generic[T]):
    doi_tuong: T
    loai_thong_bao: str
    thong_bao: str

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

class DeBaiTimBaoDongTapPhuThuocHam(BaseModel):
    tap_phu_thuoc_ham: list[PhuThuocHam] = Field(
        default_factory=list,
        description="Tập phụ thuộc hàm F"
    )

class DeBaiTimKhoaUngVien(BaseModel):
    tap_thuoc_tinh: list[str] = Field(
        default_factory=list,
        description="Danh sách các thuộc tính trong R"
    )

    tap_phu_thuoc_ham: list[PhuThuocHam] = Field(
        default_factory=list,
        description="Tập phụ thuộc hàm F"
    )

class DeBaiNangDangChuan(BaseModel):
    tap_thuoc_tinh: list[str] = Field(
        default_factory=list,
        description="Danh sách các thuộc tính trong R"
    )

    tap_phu_thuoc_ham: list[PhuThuocHam] = Field(
        default_factory=list,
        description="Tập phụ thuộc hàm F"
    )

    dang_chuan: str


