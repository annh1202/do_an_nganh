# backend/app/modules/LyThuyetCSDL/routes.py
from fastapi import APIRouter, Request

from backend.app.modules.LyThuyetCSDL.config import KhoaSession
from backend.app.modules.LyThuyetCSDL.schemas import DeBaiTimBaoDongTapThuocTinh, PhanHoi
from backend.app.modules.LyThuyetCSDL.routes.bao_dong_tap_thuoc_tinh import (
    router as router_bao_dong_tap_thuoc_tinh, get_session
)
from backend.app.modules.LyThuyetCSDL.utils.normalizers import chuyen_tap_phu_thuoc_ham_sang_dang_class

router_tong = APIRouter(prefix="/api")

@router_tong.get("/state", response_model=PhanHoi[DeBaiTimBaoDongTapThuocTinh])
def lay_trang_thai_ban_dau(request: Request):
    state = get_session(request)

    return PhanHoi(
        doi_tuong=DeBaiTimBaoDongTapThuocTinh(
            tap_thuoc_tinh=state[KhoaSession.TAP_THUOC_TINH],
            tap_phu_thuoc_ham=chuyen_tap_phu_thuoc_ham_sang_dang_class(
                state[KhoaSession.TAP_PHU_THUOC_HAM]
            ),
            tap_thuoc_tinh_muc_tieu=state[KhoaSession.TAP_THUOC_TINH_MUC_TIEU],
        ),
        loai_thong_bao="info",
        thong_bao=""
    )

router_tong.include_router(router_bao_dong_tap_thuoc_tinh)