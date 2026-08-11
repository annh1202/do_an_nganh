from backend.app.modules.LyThuyetCSDL.config import KhoaSession, DANH_SACH_DANG_CHUAN
from backend.app.modules.LyThuyetCSDL.schemas import (
    PhanHoi,
    DeBaiTimBaoDongTapThuocTinh,
    DeBaiTimBaoDongTapPhuThuocHam,
    DeBaiTimKhoaUngVien,
    DeBaiNangDangChuan
)
from backend.app.modules.LyThuyetCSDL.utils.chuan_hoa import chuyen_tap_phu_thuoc_ham_sang_dang_class


# ==============================
# BAO ĐÓNG TẬP THUỘC TÍNH
# ==============================
def tao_phan_hoi_bao_dong_tap_thuoc_tinh(trang_thai, loai_thong_bao, thong_bao):
    return PhanHoi(
        doi_tuong=DeBaiTimBaoDongTapThuocTinh(
            tap_thuoc_tinh=trang_thai[KhoaSession.TAP_THUOC_TINH],
            tap_phu_thuoc_ham=chuyen_tap_phu_thuoc_ham_sang_dang_class(
                trang_thai[KhoaSession.TAP_PHU_THUOC_HAM]
            ),
            tap_thuoc_tinh_can_tim=trang_thai[KhoaSession.TAP_THUOC_TINH_CAN_TIM]
        ),
        loai_thong_bao=loai_thong_bao,
        thong_bao=thong_bao
    )

# ==============================
# BAO ĐÓNG TẬP PHỤ THUỘC HÀM
# ==============================
def tao_phan_hoi_bao_dong_tap_phu_thuoc_ham(trang_thai, loai_thong_bao, thong_bao):
    return PhanHoi(
        doi_tuong=DeBaiTimBaoDongTapPhuThuocHam(
            tap_phu_thuoc_ham=chuyen_tap_phu_thuoc_ham_sang_dang_class(
                trang_thai[KhoaSession.TAP_PHU_THUOC_HAM]
            ),
        ),
        loai_thong_bao=loai_thong_bao,
        thong_bao=thong_bao
    )

# ==============================
# KHÓA ỨNG VIÊN
# ==============================
def tao_phan_hoi_khoa_ung_vien(trang_thai, loai_thong_bao, thong_bao):
    return PhanHoi(
        doi_tuong=DeBaiTimKhoaUngVien(
            tap_thuoc_tinh=trang_thai[KhoaSession.TAP_THUOC_TINH],
            tap_phu_thuoc_ham=chuyen_tap_phu_thuoc_ham_sang_dang_class(
                trang_thai[KhoaSession.TAP_PHU_THUOC_HAM]
            )
        ),
        loai_thong_bao=loai_thong_bao,
        thong_bao=thong_bao
    )

# ==============================
# DẠNG CHUẨN
# ==============================
def tao_phan_hoi_dang_chuan(trang_thai, loai_thong_bao, thong_bao):
    return PhanHoi(
        doi_tuong=DeBaiNangDangChuan(
            tap_thuoc_tinh=trang_thai[KhoaSession.TAP_THUOC_TINH],
            tap_phu_thuoc_ham=chuyen_tap_phu_thuoc_ham_sang_dang_class(
                trang_thai[KhoaSession.TAP_PHU_THUOC_HAM]
            ),
            dang_chuan=trang_thai[KhoaSession.DANG_CHUAN],
            danh_sach_dang_chuan=DANH_SACH_DANG_CHUAN
        ),
        loai_thong_bao=loai_thong_bao,
        thong_bao=thong_bao
    )