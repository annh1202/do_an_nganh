

from fastapi import APIRouter, HTTPException, Request

from backend.app.modules.LyThuyetCSDL.bai_giai.bao_dong_tap_thuoc_tinh import tinh_bao_dong_tap_thuoc_tinh
from backend.app.modules.LyThuyetCSDL.config import KhoaSession, LoaiThongBao
from backend.app.modules.LyThuyetCSDL.schemas import DeBaiTimBaoDongTapThuocTinh, PhuThuocHam, ThuocTinh, PhanHoi, \
    BaiGiai
from backend.app.modules.LyThuyetCSDL.utils.chuan_hoa import chuan_hoa_tap_thuoc_tinh
from backend.app.modules.LyThuyetCSDL.utils.dinh_dang import dinh_dang_tap_phu_thuoc_ham_object, \
    dinh_dang_tap_phu_thuoc_ham_tuple
from backend.app.modules.LyThuyetCSDL.utils.ho_tro_phan_hoi import tao_phan_hoi_bao_dong_tap_thuoc_tinh
from backend.app.modules.LyThuyetCSDL.utils.ho_tro_session import lay_bao_dong_tap_thuoc_tinh_session, \
    cap_nhat_bao_dong_tap_thuoc_tinh_session
from backend.app.modules.LyThuyetCSDL.utils.kiem_tra_hop_le import kiem_tra_file_bao_dong_tap_thuoc_tinh
from backend.app.modules.LyThuyetCSDL.utils.tao_ngau_nhien import tao_tap_thuoc_tinh_ngau_nhien, \
    tao_tap_phu_thuoc_ham_ngau_nhien, tao_tap_thuoc_tinh_can_tim_ngau_nhien
from backend.app.modules.LyThuyetCSDL.utils.them_xoa_sua import (
    them_thuoc_tinh, xoa_thuoc_tinh, xoa_trong_tap_thuoc_tinh,
    them_phu_thuoc_ham, xoa_phu_thuoc_ham, xoa_trong_tap_phu_thuoc_ham, them_thuoc_tinh_can_tim, xoa_thuoc_tinh_can_tim,
    xoa_trong_tap_thuoc_tinh_can_tim
)


router = APIRouter(prefix="/bao-dong-tap-thuoc-tinh", tags=["Bao đóng tập thuộc tính"])
# ==========================================
# TẬP THUỘC TÍNH R
# ==========================================
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


# ==========================================
# TẬP PHỤ THUỘC HÀM F
# ==========================================
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

# ==========================================
# TẬP THUỘC TÍNH CẦN TÌM X
# ==========================================
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

# ==========================================
# CÁC CHỨC NĂNG CHÍNH
# ==========================================
@router.post("/tao-de-bai-ngau-nhien", response_model=PhanHoi[DeBaiTimBaoDongTapThuocTinh])
def route_tao_de_bai_ngau_nhien(request: Request):
    tap_thuoc_tinh = tao_tap_thuoc_tinh_ngau_nhien()
    tap_phu_thuoc_ham = tao_tap_phu_thuoc_ham_ngau_nhien(tap_thuoc_tinh)
    tap_thuoc_tinh_can_tim = tao_tap_thuoc_tinh_can_tim_ngau_nhien(tap_thuoc_tinh)

    trang_thai = {
        KhoaSession.TAP_THUOC_TINH: tap_thuoc_tinh,
        KhoaSession.TAP_PHU_THUOC_HAM: dinh_dang_tap_phu_thuoc_ham_tuple(tap_phu_thuoc_ham),
        KhoaSession.TAP_THUOC_TINH_CAN_TIM: tap_thuoc_tinh_can_tim
    }

    cap_nhat_bao_dong_tap_thuoc_tinh_session(request, trang_thai)

    return tao_phan_hoi_bao_dong_tap_thuoc_tinh(
        trang_thai=trang_thai,
        loai_thong_bao="success",
        thong_bao="Tải đề bài lên hệ thống thành công!"
    )

@router.post("/tai-de-bai-len", response_model=PhanHoi[DeBaiTimBaoDongTapThuocTinh])
def route_tai_de_len(data: DeBaiTimBaoDongTapThuocTinh, request: Request):
    du_lieu = data.model_dump()

    hop_le, thong_bao = kiem_tra_file_bao_dong_tap_thuoc_tinh(du_lieu)

    if not hop_le:
        return tao_phan_hoi_bao_dong_tap_thuoc_tinh(
            trang_thai=lay_bao_dong_tap_thuoc_tinh_session(request),
            loai_thong_bao="warning",
            thong_bao=thong_bao
        )

    tap_thuoc_tinh = chuan_hoa_tap_thuoc_tinh(data.tap_thuoc_tinh)
    tap_phu_thuoc_ham = dinh_dang_tap_phu_thuoc_ham_object(
        data.tap_phu_thuoc_ham
    )
    tap_thuoc_tinh_can_tim = chuan_hoa_tap_thuoc_tinh(data.tap_thuoc_tinh_can_tim)

    trang_thai = {
        KhoaSession.TAP_THUOC_TINH: tap_thuoc_tinh,
        KhoaSession.TAP_PHU_THUOC_HAM: tap_phu_thuoc_ham,
        KhoaSession.TAP_THUOC_TINH_CAN_TIM: tap_thuoc_tinh_can_tim
    }

    cap_nhat_bao_dong_tap_thuoc_tinh_session(request, trang_thai)

    return tao_phan_hoi_bao_dong_tap_thuoc_tinh(
        trang_thai=trang_thai,
        loai_thong_bao="success",
        thong_bao="Tải đề bài lên hệ thống thành công!"
    )

@router.post("/giai-de", response_model=PhanHoi[BaiGiai])
def route_giai_bao_dong_tap_thuoc_tinh(request: Request):
    trang_thai = lay_bao_dong_tap_thuoc_tinh_session(request)

    tap_thuoc_tinh = trang_thai[KhoaSession.TAP_THUOC_TINH]
    tap_phu_thuoc_ham = trang_thai[KhoaSession.TAP_PHU_THUOC_HAM]
    tap_thuoc_tinh_can_tim = trang_thai[KhoaSession.TAP_THUOC_TINH_CAN_TIM]

    if not tap_thuoc_tinh:
        return PhanHoi(
            doi_tuong=None,
            loai_thong_bao=LoaiThongBao.CANH_BAO,
            thong_bao="Tập thuộc tính R không được để trống."
        )

    if not tap_phu_thuoc_ham:
        return PhanHoi(
            doi_tuong=None,
            loai_thong_bao=LoaiThongBao.CANH_BAO,
            thong_bao="Tập phụ thuộc hàm F không được để trống."
        )

    if not tap_thuoc_tinh_can_tim:
        return PhanHoi(
            doi_tuong=None,
            loai_thong_bao=LoaiThongBao.CANH_BAO,
            thong_bao="Tập thuộc tính cần tìm X không được để trống."
        )

    ket_qua, loi_giai = tinh_bao_dong_tap_thuoc_tinh(
        tap_thuoc_tinh_can_tim,
        tap_phu_thuoc_ham,
        tap_thuoc_tinh
    )

    ket_qua = f"X⁺ = {{ {", ".join(sorted(ket_qua))} }}"

    return PhanHoi(
        doi_tuong=BaiGiai(
            ket_qua=ket_qua,
            loi_giai=loi_giai
        ),
        loai_thong_bao=LoaiThongBao.THANH_CONG,
        thong_bao="Tính toán bao đóng tập thuộc tính thành công."
    )