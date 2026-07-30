from fastapi import APIRouter, HTTPException, Request

from backend.app.modules.LyThuyetCSDL.config import KhoaSession
from backend.app.modules.LyThuyetCSDL.schemas import DeBaiTimBaoDongTapThuocTinh, PhuThuocHam, ThuocTinh, PhanHoi
from backend.app.modules.LyThuyetCSDL.utils.dinh_dang import dinh_dang_phu_thuoc_ham, dinh_dang_tap_phu_thuoc_ham
from backend.app.modules.LyThuyetCSDL.utils.them_xoa_sua import (
    them_thuoc_tinh, xoa_thuoc_tinh, xoa_trong_tap_thuoc_tinh,
    them_phu_thuoc_ham, xoa_phu_thuoc_ham, xoa_trong_tap_phu_thuoc_ham, them_thuoc_tinh_can_tim, xoa_thuoc_tinh_can_tim,
    xoa_trong_tap_thuoc_tinh_can_tim
)
from backend.app.modules.LyThuyetCSDL.utils.ho_tro_phan_hoi import tao_phan_hoi_bao_dong_tap_thuoc_tinh
from backend.app.modules.LyThuyetCSDL.utils.ho_tro_session import lay_bao_dong_tap_thuoc_tinh_session, \
    cap_nhat_bao_dong_tap_thuoc_tinh_session

router = APIRouter(prefix="/bao-dong-tap-thuoc-tinh", tags=["Bao đóng tập thuộc tính"])

# ====================<< TẬP THUỘC TÍNH R >>====================
@router.post("/them-thuoc-tinh", response_model=PhanHoi[DeBaiTimBaoDongTapThuocTinh])
def route_them_thuoc_tinh(data: ThuocTinh, request: Request):
    trang_thai = lay_bao_dong_tap_thuoc_tinh_session(request)

    co_thanh_cong, loai_thong_bao, thong_bao = them_thuoc_tinh(
        data.thuoc_tinh,
        trang_thai[KhoaSession.TAP_THUOC_TINH]
    )

    if not co_thanh_cong:
        
        raise HTTPException(
            status_code=400,
            detail={
                "loai_thong_bao": loai_thong_bao,
                "thong_bao": thong_bao,
            }
        )

    cap_nhat_bao_dong_tap_thuoc_tinh_session(request, trang_thai)

    return tao_phan_hoi_bao_dong_tap_thuoc_tinh(trang_thai, loai_thong_bao, thong_bao)


@router.post("/xoa-thuoc-tinh", response_model=PhanHoi[DeBaiTimBaoDongTapThuocTinh])
def route_xoa_thuoc_tinh(data: ThuocTinh, request: Request):
    trang_thai = lay_bao_dong_tap_thuoc_tinh_session(request)

    co_thanh_cong, loai_thong_bao, thong_bao = xoa_thuoc_tinh(
        data.thuoc_tinh,
        trang_thai[KhoaSession.TAP_THUOC_TINH],
        trang_thai[KhoaSession.TAP_PHU_THUOC_HAM],
        trang_thai[KhoaSession.TAP_THUOC_TINH_CAN_TIM]
    )

    if not co_thanh_cong:
        raise HTTPException(
            status_code=400,
            detail={
                "loai_thong_bao": loai_thong_bao,
                "thong_bao": thong_bao,
            }
        )

    cap_nhat_bao_dong_tap_thuoc_tinh_session(request, trang_thai)

    return tao_phan_hoi_bao_dong_tap_thuoc_tinh(trang_thai, loai_thong_bao, thong_bao)


@router.post("/xoa-trong-thuoc-tinh", response_model=PhanHoi[DeBaiTimBaoDongTapThuocTinh])
def route_xoa_trong_thuoc_tinh(request: Request):
    trang_thai = lay_bao_dong_tap_thuoc_tinh_session(request)

    co_thanh_cong, loai_thong_bao, thong_bao = xoa_trong_tap_thuoc_tinh(
        trang_thai[KhoaSession.TAP_THUOC_TINH],
        trang_thai[KhoaSession.TAP_PHU_THUOC_HAM],
        trang_thai[KhoaSession.TAP_THUOC_TINH_CAN_TIM]
    )

    if not co_thanh_cong:
        raise HTTPException(
            status_code=400,
            detail={
                "loai_thong_bao": loai_thong_bao,
                "thong_bao": thong_bao,
            }
        )

    cap_nhat_bao_dong_tap_thuoc_tinh_session(request, trang_thai)

    return tao_phan_hoi_bao_dong_tap_thuoc_tinh(trang_thai, loai_thong_bao, thong_bao)


# ====================<< TẬP PHỤ THUỘC HÀM F >>====================
@router.post("/them-phu-thuoc-ham", response_model=PhanHoi[DeBaiTimBaoDongTapThuocTinh])
def route_them_phu_thuoc_ham(data: PhuThuocHam, request: Request):
    trang_thai = lay_bao_dong_tap_thuoc_tinh_session(request)

    co_thanh_cong, loai_thong_bao, thong_bao = them_phu_thuoc_ham(
        data.ve_trai,
        data.ve_phai,
        trang_thai[KhoaSession.TAP_THUOC_TINH],
        trang_thai[KhoaSession.TAP_PHU_THUOC_HAM]
    )

    if not co_thanh_cong:
        raise HTTPException(
            status_code=400,
            detail={
                "loai_thong_bao": loai_thong_bao,
                "thong_bao": thong_bao,
            }
        )

    cap_nhat_bao_dong_tap_thuoc_tinh_session(request, trang_thai)

    return tao_phan_hoi_bao_dong_tap_thuoc_tinh(trang_thai, loai_thong_bao, thong_bao)


@router.post("/xoa-phu-thuoc-ham", response_model=PhanHoi[DeBaiTimBaoDongTapThuocTinh])
def route_xoa_phu_thuoc_ham(data: PhuThuocHam, request: Request):
    trang_thai = lay_bao_dong_tap_thuoc_tinh_session(request)

    co_thanh_cong, loai_thong_bao, thong_bao = xoa_phu_thuoc_ham(
        data.ve_trai,
        data.ve_phai,
        trang_thai[KhoaSession.TAP_PHU_THUOC_HAM]
    )

    if not co_thanh_cong:
        raise HTTPException(
            status_code=400,
            detail={
                "loai_thong_bao": loai_thong_bao,
                "thong_bao": thong_bao,
            }
        )

    cap_nhat_bao_dong_tap_thuoc_tinh_session(request, trang_thai)

    return tao_phan_hoi_bao_dong_tap_thuoc_tinh(trang_thai, loai_thong_bao, thong_bao)


@router.post("/xoa-trong-phu-thuoc-ham", response_model=PhanHoi[DeBaiTimBaoDongTapThuocTinh])
def route_xoa_trong_phu_thuoc_ham(request: Request):
    trang_thai = lay_bao_dong_tap_thuoc_tinh_session(request)

    co_thanh_cong, loai_thong_bao, thong_bao = xoa_trong_tap_phu_thuoc_ham(
        trang_thai[KhoaSession.TAP_PHU_THUOC_HAM]
    )

    cap_nhat_bao_dong_tap_thuoc_tinh_session(request, trang_thai)

    return tao_phan_hoi_bao_dong_tap_thuoc_tinh(trang_thai, loai_thong_bao, thong_bao)


# ====================<< TẬP THUỘC TÍNH CẦN TÌM X >>====================
@router.post("/them-thuoc-tinh-can-tim", response_model=PhanHoi[DeBaiTimBaoDongTapThuocTinh])
def route_them_thuoc_tinh(data: ThuocTinh, request: Request):
    trang_thai = lay_bao_dong_tap_thuoc_tinh_session(request)

    co_thanh_cong, loai_thong_bao, thong_bao = them_thuoc_tinh_can_tim(
        data.thuoc_tinh,
        trang_thai[KhoaSession.TAP_THUOC_TINH],
        trang_thai[KhoaSession.TAP_THUOC_TINH_CAN_TIM]
    )

    if not co_thanh_cong:
        raise HTTPException(
            status_code=400,
            detail={
                "loai_thong_bao": loai_thong_bao,
                "thong_bao": thong_bao,
            }
        )

    
    cap_nhat_bao_dong_tap_thuoc_tinh_session(request, trang_thai)

    return tao_phan_hoi_bao_dong_tap_thuoc_tinh(trang_thai, loai_thong_bao, thong_bao)


@router.post("/xoa-thuoc-tinh-can-tim", response_model=PhanHoi[DeBaiTimBaoDongTapThuocTinh])
def route_xoa_thuoc_tinh(data: ThuocTinh, request: Request):
    trang_thai = lay_bao_dong_tap_thuoc_tinh_session(request)

    co_thanh_cong, loai_thong_bao, thong_bao = xoa_thuoc_tinh_can_tim(
        data.thuoc_tinh,
        trang_thai[KhoaSession.TAP_THUOC_TINH_CAN_TIM]
    )

    if not co_thanh_cong:
        raise HTTPException(
            status_code=400,
            detail={
                "loai_thong_bao": loai_thong_bao,
                "thong_bao": thong_bao,
            }
        )

    cap_nhat_bao_dong_tap_thuoc_tinh_session(request, trang_thai)

    return tao_phan_hoi_bao_dong_tap_thuoc_tinh(trang_thai, loai_thong_bao, thong_bao)


@router.post("/xoa-trong-thuoc-tinh-can-tim", response_model=PhanHoi[DeBaiTimBaoDongTapThuocTinh])
def route_xoa_trong_thuoc_tinh(request: Request):
    trang_thai = lay_bao_dong_tap_thuoc_tinh_session(request)

    co_thanh_cong, loai_thong_bao, thong_bao = xoa_trong_tap_thuoc_tinh_can_tim(
        trang_thai[KhoaSession.TAP_THUOC_TINH_CAN_TIM]
    )

    if not co_thanh_cong:
        raise HTTPException(
            status_code=400,
            detail={
                "loai_thong_bao": loai_thong_bao,
                "thong_bao": thong_bao,
            }
        )

    cap_nhat_bao_dong_tap_thuoc_tinh_session(request, trang_thai)

    return tao_phan_hoi_bao_dong_tap_thuoc_tinh(trang_thai, loai_thong_bao, thong_bao)

# =====================================
# CÁC CHỨC NĂNG CHÍNH
# =====================================
@router.post("/tai-de-bai-len", response_model=PhanHoi[DeBaiTimBaoDongTapThuocTinh])
def route_tai_de_len(data: DeBaiTimBaoDongTapThuocTinh, request: Request):
    print(data.tap_phu_thuoc_ham)
    # tap_phu_thuoc_ham = dinh_dang_tap_phu_thuoc_ham(data.tap_phu_thuoc_ham)
    tap_phu_thuoc_ham = []
    for phu_thuoc_ham in data.tap_phu_thuoc_ham:
        phu_thuoc_ham_dang_string = dinh_dang_phu_thuoc_ham(
            phu_thuoc_ham.ve_trai,
            phu_thuoc_ham.ve_phai
        )

        tap_phu_thuoc_ham.append(phu_thuoc_ham_dang_string)

    trang_thai = {
        KhoaSession.TAP_THUOC_TINH: data.tap_thuoc_tinh or [],
        KhoaSession.TAP_PHU_THUOC_HAM: tap_phu_thuoc_ham or [],
        KhoaSession.TAP_THUOC_TINH_CAN_TIM: data.tap_thuoc_tinh_can_tim or []
    }

    # 2. Lưu trạng thái mới vào session
    cap_nhat_bao_dong_tap_thuoc_tinh_session(request, trang_thai)

    loai_thong_bao = "success"
    thong_bao = "Tải đề bài lên hệ thống thành công!"

    return tao_phan_hoi_bao_dong_tap_thuoc_tinh(trang_thai, loai_thong_bao, thong_bao)

