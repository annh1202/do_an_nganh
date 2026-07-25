from fastapi import APIRouter, HTTPException, Request

from backend.app.modules.LyThuyetCSDL.config import KhoaSession
from backend.app.modules.LyThuyetCSDL.schemas import PhuThuocHam, PhanHoi, DeBaiTimBaoDongTapPhuThuocHam
from backend.app.modules.LyThuyetCSDL.utils.actions import (
    them_phu_thuoc_ham, xoa_phu_thuoc_ham, xoa_trong_tap_phu_thuoc_ham
)
from backend.app.modules.LyThuyetCSDL.utils.normalizers import chuyen_tap_phu_thuoc_ham_sang_dang_class
from backend.app.modules.LyThuyetCSDL.utils.session_helpers import lay_bao_dong_tap_phu_thuoc_ham_session

router = APIRouter(prefix="/bao-dong-tap-phu-thuoc-ham", tags=["Bao đóng tập phụ thuộc hàm"])


# ====================<< TẬP PHỤ THUỘC HÀM F >>====================
@router.post("/them-phu-thuoc-ham", response_model=PhanHoi[DeBaiTimBaoDongTapPhuThuocHam])
def route_them_phu_thuoc_ham(data: PhuThuocHam, request: Request):
    state = lay_bao_dong_tap_phu_thuoc_ham_session(request)

    # Gọi trực tiếp action thêm phụ thuộc hàm, truyền thẳng vế trái và vế phải thô vào
    co_thanh_cong, loai_thong_bao, thong_bao = them_phu_thuoc_ham(
        data.ve_trai,
        data.ve_phai,
        None,
        state[KhoaSession.TAP_PHU_THUOC_HAM]
    )

    if not co_thanh_cong:
        raise HTTPException(
            status_code=400,
            detail={
                "loai_thong_bao": loai_thong_bao,
                "thong_bao": thong_bao,
            }
        )

    request.session[KhoaSession.BAO_DONG_TAP_PHU_THUOC_HAM] = {
        KhoaSession.TAP_PHU_THUOC_HAM: list(state[KhoaSession.TAP_PHU_THUOC_HAM])
    }

    return PhanHoi(
        doi_tuong=DeBaiTimBaoDongTapPhuThuocHam(
            tap_phu_thuoc_ham=chuyen_tap_phu_thuoc_ham_sang_dang_class(
                state[KhoaSession.TAP_PHU_THUOC_HAM]
            ),
        ),
        loai_thong_bao=loai_thong_bao,
        thong_bao=thong_bao
    )


@router.post("/xoa-phu-thuoc-ham", response_model=PhanHoi[DeBaiTimBaoDongTapPhuThuocHam])
def route_xoa_phu_thuoc_ham(data: PhuThuocHam, request: Request):
    state = lay_bao_dong_tap_phu_thuoc_ham_session(request)

    co_thanh_cong, loai_thong_bao, thong_bao = xoa_phu_thuoc_ham(
        data.ve_trai,
        data.ve_phai,
        state[KhoaSession.TAP_PHU_THUOC_HAM]
    )

    if not co_thanh_cong:
        raise HTTPException(
            status_code=400,
            detail={
                "loai_thong_bao": loai_thong_bao,
                "thong_bao": thong_bao,
            }
        )

    request.session[KhoaSession.BAO_DONG_TAP_PHU_THUOC_HAM] = {
        KhoaSession.TAP_PHU_THUOC_HAM: list(state[KhoaSession.TAP_PHU_THUOC_HAM])
    }

    return PhanHoi(
        doi_tuong=DeBaiTimBaoDongTapPhuThuocHam(
            tap_phu_thuoc_ham=chuyen_tap_phu_thuoc_ham_sang_dang_class(
                state[KhoaSession.TAP_PHU_THUOC_HAM]
            )
        ),
        loai_thong_bao=loai_thong_bao,
        thong_bao=thong_bao
    )


@router.post("/xoa-trong-phu-thuoc-ham", response_model=PhanHoi[DeBaiTimBaoDongTapPhuThuocHam])
def route_xoa_trong_phu_thuoc_ham(request: Request):
    state = lay_bao_dong_tap_phu_thuoc_ham_session(request)

    co_thanh_cong, loai_thong_bao, thong_bao = xoa_trong_tap_phu_thuoc_ham(
        state[KhoaSession.TAP_PHU_THUOC_HAM]
    )

    request.session[KhoaSession.BAO_DONG_TAP_PHU_THUOC_HAM] = {
        KhoaSession.TAP_PHU_THUOC_HAM: list(state[KhoaSession.TAP_PHU_THUOC_HAM])
    }

    return PhanHoi(
        doi_tuong=DeBaiTimBaoDongTapPhuThuocHam(
            tap_phu_thuoc_ham=chuyen_tap_phu_thuoc_ham_sang_dang_class(
                state[KhoaSession.TAP_PHU_THUOC_HAM]
            )
        ),
        loai_thong_bao=loai_thong_bao,
        thong_bao=thong_bao
    )