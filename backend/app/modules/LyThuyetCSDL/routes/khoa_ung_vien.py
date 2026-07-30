from fastapi import APIRouter, HTTPException, Request


from backend.app.modules.LyThuyetCSDL.config import KhoaSession
from backend.app.modules.LyThuyetCSDL.schemas import DeBaiTimKhoaUngVien, PhuThuocHam, ThuocTinh, PhanHoi, \
    DeBaiTimKhoaUngVien

from backend.app.modules.LyThuyetCSDL.utils.them_xoa_sua import (
    them_thuoc_tinh, xoa_thuoc_tinh, xoa_trong_tap_thuoc_tinh,
    them_phu_thuoc_ham, xoa_phu_thuoc_ham, xoa_trong_tap_phu_thuoc_ham, them_thuoc_tinh_can_tim, xoa_thuoc_tinh_can_tim,
    xoa_trong_tap_thuoc_tinh_can_tim
)
from backend.app.modules.LyThuyetCSDL.utils.ho_tro_phan_hoi import tao_phan_hoi_khoa_ung_vien
from backend.app.modules.LyThuyetCSDL.utils.chuan_hoa import chuyen_tap_phu_thuoc_ham_sang_dang_class
from backend.app.modules.LyThuyetCSDL.utils.ho_tro_session import lay_bao_dong_tap_thuoc_tinh_session, \
    lay_khoa_ung_vien_session, cap_nhat_khoa_ung_vien_session

router = APIRouter(prefix="/khoa-ung-vien", tags=["Khóa ứng viên"])


# ====================<< TẬP THUỘC TÍNH R >>====================
@router.post("/them-thuoc-tinh", response_model=PhanHoi[DeBaiTimKhoaUngVien])
def route_them_thuoc_tinh(data: ThuocTinh, request: Request):
    trang_thai = lay_khoa_ung_vien_session(request)

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

    cap_nhat_khoa_ung_vien_session(request, trang_thai)

    return tao_phan_hoi_khoa_ung_vien(trang_thai, loai_thong_bao, thong_bao)


@router.post("/xoa-thuoc-tinh", response_model=PhanHoi[DeBaiTimKhoaUngVien])
def route_xoa_thuoc_tinh(data: ThuocTinh, request: Request):
    trang_thai = lay_khoa_ung_vien_session(request)

    co_thanh_cong, loai_thong_bao, thong_bao = xoa_thuoc_tinh(
        data.thuoc_tinh,
        trang_thai[KhoaSession.TAP_THUOC_TINH],
        trang_thai[KhoaSession.TAP_PHU_THUOC_HAM],
        None
    )

    if not co_thanh_cong:
        raise HTTPException(
            status_code=400,
            detail={
                "loai_thong_bao": loai_thong_bao,
                "thong_bao": thong_bao,
            }
        )

    cap_nhat_khoa_ung_vien_session(request, trang_thai)

    return tao_phan_hoi_khoa_ung_vien(trang_thai, loai_thong_bao, thong_bao)


@router.post("/xoa-trong-thuoc-tinh", response_model=PhanHoi[DeBaiTimKhoaUngVien])
def route_xoa_trong_thuoc_tinh(request: Request):
    trang_thai = lay_khoa_ung_vien_session(request)

    co_thanh_cong, loai_thong_bao, thong_bao = xoa_trong_tap_thuoc_tinh(
        trang_thai[KhoaSession.TAP_THUOC_TINH],
        trang_thai[KhoaSession.TAP_PHU_THUOC_HAM],
        None
    )

    if not co_thanh_cong:
        raise HTTPException(
            status_code=400,
            detail={
                "loai_thong_bao": loai_thong_bao,
                "thong_bao": thong_bao,
            }
        )

    cap_nhat_khoa_ung_vien_session(request, trang_thai)

    return tao_phan_hoi_khoa_ung_vien(trang_thai, loai_thong_bao, thong_bao)


# ====================<< TẬP PHỤ THUỘC HÀM F >>====================
@router.post("/them-phu-thuoc-ham", response_model=PhanHoi[DeBaiTimKhoaUngVien])
def route_them_phu_thuoc_ham(data: PhuThuocHam, request: Request):
    trang_thai = lay_khoa_ung_vien_session(request)

    # Gọi trực tiếp action thêm phụ thuộc hàm, truyền thẳng vế trái và vế phải thô vào
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

    cap_nhat_khoa_ung_vien_session(request, trang_thai)

    return tao_phan_hoi_khoa_ung_vien(trang_thai, loai_thong_bao, thong_bao)


@router.post("/xoa-phu-thuoc-ham", response_model=PhanHoi[DeBaiTimKhoaUngVien])
def route_xoa_phu_thuoc_ham(data: PhuThuocHam, request: Request):
    trang_thai = lay_khoa_ung_vien_session(request)

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

    cap_nhat_khoa_ung_vien_session(request, trang_thai)

    return tao_phan_hoi_khoa_ung_vien(trang_thai, loai_thong_bao, thong_bao)


@router.post("/xoa-trong-phu-thuoc-ham", response_model=PhanHoi[DeBaiTimKhoaUngVien])
def route_xoa_trong_phu_thuoc_ham(request: Request):
    trang_thai = lay_khoa_ung_vien_session(request)

    co_thanh_cong, loai_thong_bao, thong_bao = xoa_trong_tap_phu_thuoc_ham(
        trang_thai[KhoaSession.TAP_PHU_THUOC_HAM]
    )

    cap_nhat_khoa_ung_vien_session(request, trang_thai)

    return tao_phan_hoi_khoa_ung_vien(trang_thai, loai_thong_bao, thong_bao)

