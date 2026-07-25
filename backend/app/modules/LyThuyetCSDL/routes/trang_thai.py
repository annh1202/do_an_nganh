from fastapi import APIRouter, Request
from .bao_dong_tap_thuoc_tinh import router as router_bao_dong_tap_thuoc_tinh
from .bao_dong_tap_phu_thuoc_ham import router as router_bao_dong_tap_phu_thuoc_ham
from .khoa_ung_vien import router as router_khoa_ung_vien
from .dang_chuan import router as router_dang_chuan
from backend.app.modules.LyThuyetCSDL.utils.session_helpers import lay_bao_dong_tap_thuoc_tinh_session, \
    lay_bao_dong_tap_phu_thuoc_ham_session, lay_khoa_ung_vien_session, lay_dang_chuan_session

from ..config import KhoaSession
from ..schemas import PhanHoi, DeBaiTimBaoDongTapThuocTinh, DeBaiTimBaoDongTapPhuThuocHam, DeBaiTimKhoaUngVien, \
    DeBaiNangDangChuan
from ..utils.normalizers import chuyen_tap_phu_thuoc_ham_sang_dang_class


@router_bao_dong_tap_thuoc_tinh.get("/state", response_model=PhanHoi[DeBaiTimBaoDongTapThuocTinh])
def lay_trang_thai_ban_dau(request: Request):
    state = lay_bao_dong_tap_thuoc_tinh_session(request)

    return PhanHoi(
        doi_tuong=DeBaiTimBaoDongTapThuocTinh(
            tap_thuoc_tinh=state[KhoaSession.TAP_THUOC_TINH],
            tap_phu_thuoc_ham=chuyen_tap_phu_thuoc_ham_sang_dang_class(
                state[KhoaSession.TAP_PHU_THUOC_HAM]
            ),
            tap_thuoc_tinh_can_tim=state[KhoaSession.TAP_THUOC_TINH_CAN_TIM],
        ),
        loai_thong_bao="info",
        thong_bao=""
    )

@router_bao_dong_tap_phu_thuoc_ham.get("/state", response_model=PhanHoi[DeBaiTimBaoDongTapPhuThuocHam])
def lay_trang_thai_ban_dau(request: Request):
    state = lay_bao_dong_tap_phu_thuoc_ham_session(request)

    return PhanHoi(
        doi_tuong=DeBaiTimBaoDongTapPhuThuocHam(
            tap_phu_thuoc_ham=chuyen_tap_phu_thuoc_ham_sang_dang_class(
                state[KhoaSession.TAP_PHU_THUOC_HAM]
            )
        ),
        loai_thong_bao="info",
        thong_bao=""
    )

@router_khoa_ung_vien.get("/state", response_model=PhanHoi[DeBaiTimKhoaUngVien])
def lay_trang_thai_ban_dau(request: Request):
    state = lay_khoa_ung_vien_session(request)

    return PhanHoi(
        doi_tuong=DeBaiTimKhoaUngVien(
            tap_thuoc_tinh=state[KhoaSession.TAP_THUOC_TINH],
            tap_phu_thuoc_ham=chuyen_tap_phu_thuoc_ham_sang_dang_class(
                state[KhoaSession.TAP_PHU_THUOC_HAM]
            )
        ),
        loai_thong_bao="info",
        thong_bao=""
    )

@router_dang_chuan.get("/state", response_model=PhanHoi[DeBaiNangDangChuan])
def lay_trang_thai_ban_dau(request: Request):
    state = lay_dang_chuan_session(request)
    return PhanHoi(
        doi_tuong=DeBaiNangDangChuan(
            tap_thuoc_tinh=state[KhoaSession.TAP_THUOC_TINH],
            tap_phu_thuoc_ham=chuyen_tap_phu_thuoc_ham_sang_dang_class(
                state[KhoaSession.TAP_PHU_THUOC_HAM]
            ),
            dang_chuan=state[KhoaSession.DANG_CHUAN]
        ),
        loai_thong_bao="info",
        thong_bao=""
    )

router_tong = APIRouter(prefix="/api")
router_tong.include_router(router_bao_dong_tap_thuoc_tinh)
router_tong.include_router(router_bao_dong_tap_phu_thuoc_ham)
router_tong.include_router(router_khoa_ung_vien)
router_tong.include_router(router_dang_chuan)