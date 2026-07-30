from fastapi import APIRouter, HTTPException, Request

from backend.app.modules.LyThuyetCSDL.config import KhoaSession
from backend.app.modules.LyThuyetCSDL.schemas import PhuThuocHam, PhanHoi, DeBaiTimBaoDongTapPhuThuocHam
from backend.app.modules.LyThuyetCSDL.utils.them_xoa_sua import (
    them_phu_thuoc_ham,
    xoa_phu_thuoc_ham,
    xoa_trong_tap_phu_thuoc_ham
)
from backend.app.modules.LyThuyetCSDL.utils.ho_tro_phan_hoi import tao_phan_hoi_bao_dong_tap_phu_thuoc_ham
from backend.app.modules.LyThuyetCSDL.utils.ho_tro_session import lay_bao_dong_tap_phu_thuoc_ham_session, \
    cap_nhat_bao_dong_tap_phu_thuoc_ham_session
from backend.app.modules.LyThuyetCSDL.utils.chuan_hoa import chuyen_tap_phu_thuoc_ham_sang_dang_class

router = APIRouter(prefix="/bao-dong-tap-phu-thuoc-ham", tags=["Bao đóng tập phụ thuộc hàm"])


# ====================<< TẬP PHỤ THUỘC HÀM F >>====================
@router.post("/them-phu-thuoc-ham", response_model=PhanHoi[DeBaiTimBaoDongTapPhuThuocHam])
def route_them_phu_thuoc_ham(data: PhuThuocHam, request: Request):
    trang_thai = lay_bao_dong_tap_phu_thuoc_ham_session(request)

    # Gọi trực tiếp action thêm phụ thuộc hàm, truyền thẳng vế trái và vế phải thô vào
    co_thanh_cong, loai_thong_bao, thong_bao = them_phu_thuoc_ham(
        data.ve_trai,
        data.ve_phai,
        None,
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

    cap_nhat_bao_dong_tap_phu_thuoc_ham_session(request, trang_thai)

    return tao_phan_hoi_bao_dong_tap_phu_thuoc_ham(trang_thai, loai_thong_bao, thong_bao)


@router.post("/xoa-phu-thuoc-ham", response_model=PhanHoi[DeBaiTimBaoDongTapPhuThuocHam])
def route_xoa_phu_thuoc_ham(data: PhuThuocHam, request: Request):
    trang_thai = lay_bao_dong_tap_phu_thuoc_ham_session(request)

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

    cap_nhat_bao_dong_tap_phu_thuoc_ham_session(request, trang_thai)

    return tao_phan_hoi_bao_dong_tap_phu_thuoc_ham(trang_thai, loai_thong_bao, thong_bao)


@router.post("/xoa-trong-phu-thuoc-ham", response_model=PhanHoi[DeBaiTimBaoDongTapPhuThuocHam])
def route_xoa_trong_phu_thuoc_ham(request: Request):
    trang_thai = lay_bao_dong_tap_phu_thuoc_ham_session(request)

    co_thanh_cong, loai_thong_bao, thong_bao = xoa_trong_tap_phu_thuoc_ham(
        trang_thai[KhoaSession.TAP_PHU_THUOC_HAM]
    )

    cap_nhat_bao_dong_tap_phu_thuoc_ham_session(request, trang_thai)

    return tao_phan_hoi_bao_dong_tap_phu_thuoc_ham(trang_thai, loai_thong_bao, thong_bao)