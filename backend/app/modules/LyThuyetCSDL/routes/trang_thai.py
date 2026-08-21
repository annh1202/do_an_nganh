from fastapi import APIRouter, Request

from backend.app.modules.LyThuyetCSDL.utils.ho_tro_session import lay_bao_dong_tap_thuoc_tinh_session, \
    lay_bao_dong_tap_phu_thuoc_ham_session, lay_khoa_ung_vien_session, lay_dang_chuan_session
from .bao_dong_tap_phu_thuoc_ham import router as router_bao_dong_tap_phu_thuoc_ham
from .bao_dong_tap_thuoc_tinh import router as router_bao_dong_tap_thuoc_tinh
from .dang_chuan import router as router_dang_chuan
from .khoa_ung_vien import router as router_khoa_ung_vien
from ..config import MODULE_LY_THUYET_CSDL
from ..schemas import PhanHoi, DeBaiTimBaoDongTapThuocTinh, DeBaiTimBaoDongTapPhuThuocHam, DeBaiTimKhoaUngVien, \
    DeBaiNangDangChuan
from ..utils.ho_tro_phan_hoi import tao_phan_hoi_bao_dong_tap_thuoc_tinh, tao_phan_hoi_bao_dong_tap_phu_thuoc_ham, \
    tao_phan_hoi_khoa_ung_vien, tao_phan_hoi_dang_chuan


@router_bao_dong_tap_thuoc_tinh.get("/trang-thai", response_model=PhanHoi[DeBaiTimBaoDongTapThuocTinh])
def lay_trang_thai_ban_dau(request: Request):
    trang_thai = lay_bao_dong_tap_thuoc_tinh_session(request)

    return tao_phan_hoi_bao_dong_tap_thuoc_tinh(trang_thai, loai_thong_bao="info", thong_bao="")


@router_bao_dong_tap_phu_thuoc_ham.get("/trang-thai", response_model=PhanHoi[DeBaiTimBaoDongTapPhuThuocHam])
def lay_trang_thai_ban_dau(request: Request):
    trang_thai = lay_bao_dong_tap_phu_thuoc_ham_session(request)

    return tao_phan_hoi_bao_dong_tap_phu_thuoc_ham(trang_thai, loai_thong_bao="info", thong_bao="")


@router_khoa_ung_vien.get("/trang-thai", response_model=PhanHoi[DeBaiTimKhoaUngVien])
def lay_trang_thai_ban_dau(request: Request):
    trang_thai = lay_khoa_ung_vien_session(request)

    return tao_phan_hoi_khoa_ung_vien(trang_thai, loai_thong_bao="info", thong_bao="")


@router_dang_chuan.get("/trang-thai", response_model=PhanHoi[DeBaiNangDangChuan])
def lay_trang_thai_ban_dau(request: Request):
    trang_thai = lay_dang_chuan_session(request)

    return tao_phan_hoi_dang_chuan(trang_thai, loai_thong_bao="info", thong_bao="")


router_tong = APIRouter(prefix="/api")

@router_tong.get("/trang-thai")
def lay_trang_thai_module():
    return {
        "cau_hinh": MODULE_LY_THUYET_CSDL
    }

router_tong.include_router(router_bao_dong_tap_thuoc_tinh)
router_tong.include_router(router_bao_dong_tap_phu_thuoc_ham)
router_tong.include_router(router_khoa_ung_vien)
router_tong.include_router(router_dang_chuan)