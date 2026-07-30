from fastapi import APIRouter, HTTPException, Request

from backend.app.modules.LyThuyetCSDL.config import KhoaSession, LoaiThongBao
from backend.app.modules.LyThuyetCSDL.schemas import PhuThuocHam, ThuocTinh, PhanHoi, \
    DeBaiNangDangChuan, DangChuan
from backend.app.modules.LyThuyetCSDL.utils.ho_tro_phan_hoi import tao_phan_hoi_dang_chuan
from backend.app.modules.LyThuyetCSDL.utils.ho_tro_session import lay_dang_chuan_session, \
    cap_nhat_dang_chuan_session
from backend.app.modules.LyThuyetCSDL.utils.them_xoa_sua import (
    them_thuoc_tinh, xoa_thuoc_tinh, xoa_trong_tap_thuoc_tinh,
    them_phu_thuoc_ham, xoa_phu_thuoc_ham, xoa_trong_tap_phu_thuoc_ham
)


router = APIRouter(prefix="/dang-chuan", tags=["Dạng chuẩn"])

# ====================<< TẬP THUỘC TÍNH R >>====================
@router.post("/them-thuoc-tinh", response_model=PhanHoi[DeBaiNangDangChuan])
def route_them_thuoc_tinh(data: ThuocTinh, request: Request):
    trang_thai = lay_dang_chuan_session(request)

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
    
    cap_nhat_dang_chuan_session(request, trang_thai)

    return tao_phan_hoi_dang_chuan(trang_thai, loai_thong_bao, thong_bao)


@router.post("/xoa-thuoc-tinh", response_model=PhanHoi[DeBaiNangDangChuan])
def route_xoa_thuoc_tinh(data: ThuocTinh, request: Request):
    trang_thai = lay_dang_chuan_session(request)

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

    cap_nhat_dang_chuan_session(request, trang_thai)

    return tao_phan_hoi_dang_chuan(trang_thai, loai_thong_bao, thong_bao)


@router.post("/xoa-trong-thuoc-tinh", response_model=PhanHoi[DeBaiNangDangChuan])
def route_xoa_trong_thuoc_tinh(request: Request):
    trang_thai = lay_dang_chuan_session(request)

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

    cap_nhat_dang_chuan_session(request, trang_thai)

    return tao_phan_hoi_dang_chuan(trang_thai, loai_thong_bao, thong_bao)


# ====================<< TẬP PHỤ THUỘC HÀM F >>====================
@router.post("/them-phu-thuoc-ham", response_model=PhanHoi[DeBaiNangDangChuan])
def route_them_phu_thuoc_ham(data: PhuThuocHam, request: Request):
    trang_thai = lay_dang_chuan_session(request)

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

    cap_nhat_dang_chuan_session(request, trang_thai)

    return tao_phan_hoi_dang_chuan(trang_thai, loai_thong_bao, thong_bao)


@router.post("/xoa-phu-thuoc-ham", response_model=PhanHoi[DeBaiNangDangChuan])
def route_xoa_phu_thuoc_ham(data: PhuThuocHam, request: Request):
    trang_thai = lay_dang_chuan_session(request)

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

    cap_nhat_dang_chuan_session(request, trang_thai)

    return tao_phan_hoi_dang_chuan(trang_thai, loai_thong_bao, thong_bao)


@router.post("/xoa-trong-phu-thuoc-ham", response_model=PhanHoi[DeBaiNangDangChuan])
def route_xoa_trong_phu_thuoc_ham(request: Request):
    trang_thai = lay_dang_chuan_session(request)

    co_thanh_cong, loai_thong_bao, thong_bao = xoa_trong_tap_phu_thuoc_ham(
        trang_thai[KhoaSession.TAP_PHU_THUOC_HAM]
    )

    cap_nhat_dang_chuan_session(request, trang_thai)

    return tao_phan_hoi_dang_chuan(trang_thai, loai_thong_bao, thong_bao)

# ====================<< CHỌN DẠNG CHUẨN >>====================
@router.post("/chon-dang-chuan", response_model=PhanHoi[DeBaiNangDangChuan])
def route_chon_dang_chuan(data: DangChuan, request: Request):
    dang_chuan_hop_le = {"2NF", "3NF", "BCNF"}

    trang_thai = lay_dang_chuan_session(request)

    if data.dang_chuan not in dang_chuan_hop_le:
        return tao_phan_hoi_dang_chuan(trang_thai, LoaiThongBao.DANGER, "Dạng chuẩn không hợp lệ")

    trang_thai[KhoaSession.DANG_CHUAN] = data.dang_chuan

    cap_nhat_dang_chuan_session(request, trang_thai)

    return tao_phan_hoi_dang_chuan(
        trang_thai,
        LoaiThongBao.SUCCESS,
        "Chọn dạng chuẩn thành công"
    )