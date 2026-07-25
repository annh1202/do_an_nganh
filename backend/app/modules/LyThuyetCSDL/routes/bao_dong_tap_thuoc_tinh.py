from fastapi import APIRouter, HTTPException, Request


from backend.app.modules.LyThuyetCSDL.config import KhoaSession
from backend.app.modules.LyThuyetCSDL.schemas import DeBaiTimBaoDongTapThuocTinh, PhuThuocHam, ThuocTinh, PhanHoi

from backend.app.modules.LyThuyetCSDL.utils.actions import (
    them_thuoc_tinh, xoa_thuoc_tinh, xoa_trong_tap_thuoc_tinh,
    them_phu_thuoc_ham, xoa_phu_thuoc_ham, xoa_trong_tap_phu_thuoc_ham, them_thuoc_tinh_can_tim, xoa_thuoc_tinh_can_tim,
    xoa_trong_tap_thuoc_tinh_can_tim
)
from backend.app.modules.LyThuyetCSDL.utils.normalizers import chuyen_tap_phu_thuoc_ham_sang_dang_class
from backend.app.modules.LyThuyetCSDL.utils.session_helpers import lay_bao_dong_tap_thuoc_tinh_session

router = APIRouter(prefix="/bao-dong-tap-thuoc-tinh", tags=["Bao đóng tập thuộc tính"])


# ====================<< TẬP THUỘC TÍNH R >>====================
@router.post("/them-thuoc-tinh", response_model=PhanHoi[DeBaiTimBaoDongTapThuocTinh])
def route_them_thuoc_tinh(data: ThuocTinh, request: Request):
    state = lay_bao_dong_tap_thuoc_tinh_session(request)

    # Gọi trực tiếp action để xử lý. Action tự chuẩn hóa, tự check lỗi định dạng và check trùng
    co_thanh_cong, loai_thong_bao, thong_bao = them_thuoc_tinh(data.thuoc_tinh, state[KhoaSession.TAP_THUOC_TINH])
    if not co_thanh_cong:
        # Nếu nghiệp vụ thất bại (False), ném thông báo chi tiết của action dưới dạng lỗi HTTP 400
        raise HTTPException(
            status_code=400,
            detail={
                "loai_thong_bao": loai_thong_bao,
                "thong_bao": thong_bao,
            }
        )

    # Đồng bộ ép cứng xuống Session Cookie bằng một bản sao mới (tránh lỗi nuốt thuộc tính cũ)
    request.session[KhoaSession.BAO_DONG_TAP_THUOC_TINH] = {
        KhoaSession.TAP_THUOC_TINH: list(state[KhoaSession.TAP_THUOC_TINH]),
        KhoaSession.TAP_PHU_THUOC_HAM: list(state[KhoaSession.TAP_PHU_THUOC_HAM]),
        KhoaSession.TAP_THUOC_TINH_CAN_TIM: list(state[KhoaSession.TAP_THUOC_TINH_CAN_TIM])
    }

    return PhanHoi(
        doi_tuong=DeBaiTimBaoDongTapThuocTinh(
            tap_thuoc_tinh=state[KhoaSession.TAP_THUOC_TINH],
            tap_phu_thuoc_ham=chuyen_tap_phu_thuoc_ham_sang_dang_class(
                state[KhoaSession.TAP_PHU_THUOC_HAM]
            ),
            tap_thuoc_tinh_can_tim=state[KhoaSession.TAP_THUOC_TINH_CAN_TIM]
        ),
        loai_thong_bao=loai_thong_bao,
        thong_bao=thong_bao
    )


@router.post("/xoa-thuoc-tinh", response_model=PhanHoi[DeBaiTimBaoDongTapThuocTinh])
def route_xoa_thuoc_tinh(data: ThuocTinh, request: Request):
    state = lay_bao_dong_tap_thuoc_tinh_session(request)

    co_thanh_cong, loai_thong_bao, thong_bao = xoa_thuoc_tinh(
        data.thuoc_tinh,
        state[KhoaSession.TAP_THUOC_TINH],
        state[KhoaSession.TAP_PHU_THUOC_HAM],
        state[KhoaSession.TAP_THUOC_TINH_CAN_TIM]
    )

    if not co_thanh_cong:
        raise HTTPException(
            status_code=400,
            detail={
                "loai_thong_bao": loai_thong_bao,
                "thong_bao": thong_bao,
            }
        )

    request.session[KhoaSession.BAO_DONG_TAP_THUOC_TINH] = {
        KhoaSession.TAP_THUOC_TINH: list(state[KhoaSession.TAP_THUOC_TINH]),
        KhoaSession.TAP_PHU_THUOC_HAM: list(state[KhoaSession.TAP_PHU_THUOC_HAM]),
        KhoaSession.TAP_THUOC_TINH_CAN_TIM: list(state[KhoaSession.TAP_THUOC_TINH_CAN_TIM])
    }

    return PhanHoi(
        doi_tuong=DeBaiTimBaoDongTapThuocTinh(
            tap_thuoc_tinh=state[KhoaSession.TAP_THUOC_TINH],
            tap_phu_thuoc_ham=chuyen_tap_phu_thuoc_ham_sang_dang_class(
                state[KhoaSession.TAP_PHU_THUOC_HAM]
            ),
            tap_thuoc_tinh_can_tim=state[KhoaSession.TAP_THUOC_TINH_CAN_TIM]
        ),
        loai_thong_bao=loai_thong_bao,
        thong_bao=thong_bao
    )


@router.post("/xoa-trong-thuoc-tinh", response_model=PhanHoi[DeBaiTimBaoDongTapThuocTinh])
def route_xoa_trong_thuoc_tinh(request: Request):
    state = lay_bao_dong_tap_thuoc_tinh_session(request)

    co_thanh_cong, loai_thong_bao, thong_bao = xoa_trong_tap_thuoc_tinh(
        state[KhoaSession.TAP_THUOC_TINH],
        state[KhoaSession.TAP_PHU_THUOC_HAM],
        state[KhoaSession.TAP_THUOC_TINH_CAN_TIM]
    )

    if not co_thanh_cong:
        raise HTTPException(
            status_code=400,
            detail={
                "loai_thong_bao": loai_thong_bao,
                "thong_bao": thong_bao,
            }
        )

    request.session[KhoaSession.BAO_DONG_TAP_THUOC_TINH] = {
        KhoaSession.TAP_THUOC_TINH: list(state[KhoaSession.TAP_THUOC_TINH]),
        KhoaSession.TAP_PHU_THUOC_HAM: list(state[KhoaSession.TAP_PHU_THUOC_HAM]),
        KhoaSession.TAP_THUOC_TINH_CAN_TIM: list(state[KhoaSession.TAP_THUOC_TINH_CAN_TIM])
    }

    return PhanHoi(
        doi_tuong=DeBaiTimBaoDongTapThuocTinh(
            tap_thuoc_tinh=state[KhoaSession.TAP_THUOC_TINH],
            tap_phu_thuoc_ham=chuyen_tap_phu_thuoc_ham_sang_dang_class(
                state[KhoaSession.TAP_PHU_THUOC_HAM]
            ),
            tap_thuoc_tinh_can_tim=state[KhoaSession.TAP_THUOC_TINH_CAN_TIM]
        ),
        loai_thong_bao=loai_thong_bao,
        thong_bao=thong_bao
    )


# ====================<< TẬP PHỤ THUỘC HÀM F >>====================
@router.post("/them-phu-thuoc-ham", response_model=PhanHoi[DeBaiTimBaoDongTapThuocTinh])
def route_them_phu_thuoc_ham(data: PhuThuocHam, request: Request):
    state = lay_bao_dong_tap_thuoc_tinh_session(request)

    # Gọi trực tiếp action thêm phụ thuộc hàm, truyền thẳng vế trái và vế phải thô vào
    co_thanh_cong, loai_thong_bao, thong_bao = them_phu_thuoc_ham(
        data.ve_trai,
        data.ve_phai,
        state[KhoaSession.TAP_THUOC_TINH],
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

    request.session[KhoaSession.BAO_DONG_TAP_THUOC_TINH] = {
        KhoaSession.TAP_THUOC_TINH: list(state[KhoaSession.TAP_THUOC_TINH]),
        KhoaSession.TAP_PHU_THUOC_HAM: list(state[KhoaSession.TAP_PHU_THUOC_HAM]),
        KhoaSession.TAP_THUOC_TINH_CAN_TIM: list(state[KhoaSession.TAP_THUOC_TINH_CAN_TIM])
    }

    return PhanHoi(
        doi_tuong=DeBaiTimBaoDongTapThuocTinh(
            tap_thuoc_tinh=state[KhoaSession.TAP_THUOC_TINH],
            tap_phu_thuoc_ham=chuyen_tap_phu_thuoc_ham_sang_dang_class(
                state[KhoaSession.TAP_PHU_THUOC_HAM]
            ),
            tap_thuoc_tinh_can_tim=state[KhoaSession.TAP_THUOC_TINH_CAN_TIM]
        ),
        loai_thong_bao=loai_thong_bao,
        thong_bao=thong_bao
    )


@router.post("/xoa-phu-thuoc-ham", response_model=PhanHoi[DeBaiTimBaoDongTapThuocTinh])
def route_xoa_phu_thuoc_ham(data: PhuThuocHam, request: Request):
    state = lay_bao_dong_tap_thuoc_tinh_session(request)

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

    request.session[KhoaSession.BAO_DONG_TAP_THUOC_TINH] = {
        KhoaSession.TAP_THUOC_TINH: list(state[KhoaSession.TAP_THUOC_TINH]),
        KhoaSession.TAP_PHU_THUOC_HAM: list(state[KhoaSession.TAP_PHU_THUOC_HAM]),
        KhoaSession.TAP_THUOC_TINH_CAN_TIM: list(state[KhoaSession.TAP_THUOC_TINH_CAN_TIM])
    }

    return PhanHoi(
        doi_tuong=DeBaiTimBaoDongTapThuocTinh(
            tap_thuoc_tinh=state[KhoaSession.TAP_THUOC_TINH],
            tap_phu_thuoc_ham=chuyen_tap_phu_thuoc_ham_sang_dang_class(
                state[KhoaSession.TAP_PHU_THUOC_HAM]
            ),
            tap_thuoc_tinh_can_tim=state[KhoaSession.TAP_THUOC_TINH_CAN_TIM]
        ),
        loai_thong_bao=loai_thong_bao,
        thong_bao=thong_bao
    )


@router.post("/xoa-trong-phu-thuoc-ham", response_model=PhanHoi[DeBaiTimBaoDongTapThuocTinh])
def route_xoa_trong_phu_thuoc_ham(request: Request):
    state = lay_bao_dong_tap_thuoc_tinh_session(request)

    co_thanh_cong, loai_thong_bao, thong_bao = xoa_trong_tap_phu_thuoc_ham(
        state[KhoaSession.TAP_PHU_THUOC_HAM]
    )

    request.session[KhoaSession.BAO_DONG_TAP_THUOC_TINH] = {
        KhoaSession.TAP_THUOC_TINH: list(state[KhoaSession.TAP_THUOC_TINH]),
        KhoaSession.TAP_PHU_THUOC_HAM: list(state[KhoaSession.TAP_PHU_THUOC_HAM]),
        KhoaSession.TAP_THUOC_TINH_CAN_TIM: list(state[KhoaSession.TAP_THUOC_TINH_CAN_TIM])
    }

    return PhanHoi(
        doi_tuong=DeBaiTimBaoDongTapThuocTinh(
            tap_thuoc_tinh=state[KhoaSession.TAP_THUOC_TINH],
            tap_phu_thuoc_ham=chuyen_tap_phu_thuoc_ham_sang_dang_class(
                state[KhoaSession.TAP_PHU_THUOC_HAM]
            ),
            tap_thuoc_tinh_can_tim=state[KhoaSession.TAP_THUOC_TINH_CAN_TIM]
        ),
        loai_thong_bao=loai_thong_bao,
        thong_bao=thong_bao
    )


# ====================<< TẬP THUỘC TÍNH CẦN TÌM X >>====================
@router.post("/them-thuoc-tinh-can-tim", response_model=PhanHoi[DeBaiTimBaoDongTapThuocTinh])
def route_them_thuoc_tinh(data: ThuocTinh, request: Request):
    state = lay_bao_dong_tap_thuoc_tinh_session(request)

    # Gọi trực tiếp action để xử lý. Action tự chuẩn hóa, tự check lỗi định dạng và check trùng
    co_thanh_cong, loai_thong_bao, thong_bao = them_thuoc_tinh_can_tim(
        data.thuoc_tinh,
        state[KhoaSession.TAP_THUOC_TINH],
        state[KhoaSession.TAP_THUOC_TINH_CAN_TIM]
    )

    if not co_thanh_cong:
        # Nếu nghiệp vụ thất bại (False), ném thông báo chi tiết của action dưới dạng lỗi HTTP 400
        raise HTTPException(
            status_code=400,
            detail={
                "loai_thong_bao": loai_thong_bao,
                "thong_bao": thong_bao,
            }
        )

    # Đồng bộ ép cứng xuống Session Cookie bằng một bản sao mới (tránh lỗi nuốt thuộc tính cũ)
    request.session[KhoaSession.BAO_DONG_TAP_THUOC_TINH] = {
        KhoaSession.TAP_THUOC_TINH: list(state[KhoaSession.TAP_THUOC_TINH]),
        KhoaSession.TAP_PHU_THUOC_HAM: list(state[KhoaSession.TAP_PHU_THUOC_HAM]),
        KhoaSession.TAP_THUOC_TINH_CAN_TIM: list(state[KhoaSession.TAP_THUOC_TINH_CAN_TIM])
    }

    return PhanHoi(
        doi_tuong=DeBaiTimBaoDongTapThuocTinh(
            tap_thuoc_tinh=state[KhoaSession.TAP_THUOC_TINH],
            tap_phu_thuoc_ham=chuyen_tap_phu_thuoc_ham_sang_dang_class(
                state[KhoaSession.TAP_PHU_THUOC_HAM]
            ),
            tap_thuoc_tinh_can_tim=state[KhoaSession.TAP_THUOC_TINH_CAN_TIM]
        ),
        loai_thong_bao=loai_thong_bao,
        thong_bao=thong_bao
    )


@router.post("/xoa-thuoc-tinh-can-tim", response_model=PhanHoi[DeBaiTimBaoDongTapThuocTinh])
def route_xoa_thuoc_tinh(data: ThuocTinh, request: Request):
    state = lay_bao_dong_tap_thuoc_tinh_session(request)

    co_thanh_cong, loai_thong_bao, thong_bao = xoa_thuoc_tinh_can_tim(
        data.thuoc_tinh,
        state[KhoaSession.TAP_THUOC_TINH_CAN_TIM]
    )

    if not co_thanh_cong:
        raise HTTPException(
            status_code=400,
            detail={
                "loai_thong_bao": loai_thong_bao,
                "thong_bao": thong_bao,
            }
        )

    request.session[KhoaSession.BAO_DONG_TAP_THUOC_TINH] = {
        KhoaSession.TAP_THUOC_TINH: list(state[KhoaSession.TAP_THUOC_TINH]),
        KhoaSession.TAP_PHU_THUOC_HAM: list(state[KhoaSession.TAP_PHU_THUOC_HAM]),
        KhoaSession.TAP_THUOC_TINH_CAN_TIM: list(state[KhoaSession.TAP_THUOC_TINH_CAN_TIM])
    }

    return PhanHoi(
        doi_tuong=DeBaiTimBaoDongTapThuocTinh(
            tap_thuoc_tinh=state[KhoaSession.TAP_THUOC_TINH],
            tap_phu_thuoc_ham=chuyen_tap_phu_thuoc_ham_sang_dang_class(
                state[KhoaSession.TAP_PHU_THUOC_HAM]
            ),
            tap_thuoc_tinh_can_tim=state[KhoaSession.TAP_THUOC_TINH_CAN_TIM]
        ),
        loai_thong_bao=loai_thong_bao,
        thong_bao=thong_bao
    )


@router.post("/xoa-trong-thuoc-tinh-can-tim", response_model=PhanHoi[DeBaiTimBaoDongTapThuocTinh])
def route_xoa_trong_thuoc_tinh(request: Request):
    state = lay_bao_dong_tap_thuoc_tinh_session(request)

    co_thanh_cong, loai_thong_bao, thong_bao = xoa_trong_tap_thuoc_tinh_can_tim(
        state[KhoaSession.TAP_THUOC_TINH_CAN_TIM]
    )

    if not co_thanh_cong:
        raise HTTPException(
            status_code=400,
            detail={
                "loai_thong_bao": loai_thong_bao,
                "thong_bao": thong_bao,
            }
        )

    request.session[KhoaSession.BAO_DONG_TAP_THUOC_TINH] = {
        KhoaSession.TAP_THUOC_TINH: list(state[KhoaSession.TAP_THUOC_TINH]),
        KhoaSession.TAP_PHU_THUOC_HAM: list(state[KhoaSession.TAP_PHU_THUOC_HAM]),
        KhoaSession.TAP_THUOC_TINH_CAN_TIM: list(state[KhoaSession.TAP_THUOC_TINH_CAN_TIM])
    }

    return PhanHoi(
        doi_tuong=DeBaiTimBaoDongTapThuocTinh(
            tap_thuoc_tinh=state[KhoaSession.TAP_THUOC_TINH],
            tap_phu_thuoc_ham=chuyen_tap_phu_thuoc_ham_sang_dang_class(
                state[KhoaSession.TAP_PHU_THUOC_HAM]
            ),
            tap_thuoc_tinh_can_tim=state[KhoaSession.TAP_THUOC_TINH_CAN_TIM]
        ),
        loai_thong_bao=loai_thong_bao,
        thong_bao=thong_bao
    )