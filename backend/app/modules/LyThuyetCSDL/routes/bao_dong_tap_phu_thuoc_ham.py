import random

from fastapi import APIRouter, HTTPException, Request

from backend.app.modules.LyThuyetCSDL.config import KhoaSession, LoaiThongBao
from backend.app.modules.LyThuyetCSDL.schemas import PhuThuocHam, PhanHoi, DeBaiTimBaoDongTapPhuThuocHam, BaiGiai
from backend.app.modules.LyThuyetCSDL.utils.tao_ngau_nhien import tao_tap_thuoc_tinh_ngau_nhien, \
    tao_tap_phu_thuoc_ham_ngau_nhien
from backend.app.modules.LyThuyetCSDL.utils.dinh_dang import dinh_dang_phu_thuoc_ham, dinh_dang_tap_phu_thuoc_ham_tuple, \
    dinh_dang_tap_phu_thuoc_ham_object
from backend.app.modules.LyThuyetCSDL.utils.ho_tro_phan_hoi import tao_phan_hoi_bao_dong_tap_phu_thuoc_ham
from backend.app.modules.LyThuyetCSDL.utils.ho_tro_session import lay_bao_dong_tap_phu_thuoc_ham_session, \
    cap_nhat_bao_dong_tap_phu_thuoc_ham_session
from backend.app.modules.LyThuyetCSDL.bai_giai.bao_dong_tap_phu_thuoc_ham import tinh_bao_dong_tap_phu_thuoc_ham
from backend.app.modules.LyThuyetCSDL.utils.them_xoa_sua import (
    them_phu_thuoc_ham,
    xoa_phu_thuoc_ham,
    xoa_trong_tap_phu_thuoc_ham
)


router = APIRouter(prefix="/bao-dong-tap-phu-thuoc-ham", tags=["Bao đóng tập phụ thuộc hàm"])

# ==========================================
# TẬP PHỤ THUỘC HÀM F
# ==========================================
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

# ==========================================
# CÁC CHỨC NĂNG CHÍNH
# ==========================================
@router.post("/tao-de-bai-ngau-nhien", response_model=PhanHoi[DeBaiTimBaoDongTapPhuThuocHam])
def route_tai_de_len(request: Request):
    tap_thuoc_tinh = tao_tap_thuoc_tinh_ngau_nhien(
        so_thuoc_tinh_toi_thieu=3,
        so_thuoc_tinh_toi_da=4
    )

    tap_phu_thuoc_ham = tao_tap_phu_thuoc_ham_ngau_nhien(
        tap_thuoc_tinh=tap_thuoc_tinh,
        so_luong_phu_thuoc_ham=random.choice([3, 4])
    )

    trang_thai = {
        KhoaSession.TAP_PHU_THUOC_HAM: dinh_dang_tap_phu_thuoc_ham_tuple(tap_phu_thuoc_ham)
    }

    cap_nhat_bao_dong_tap_phu_thuoc_ham_session(request, trang_thai)

    return tao_phan_hoi_bao_dong_tap_phu_thuoc_ham(
        trang_thai=trang_thai,
        loai_thong_bao="success",
        thong_bao="Tải đề bài lên hệ thống thành công!"
    )


@router.post("/tai-de-bai-len", response_model=PhanHoi[DeBaiTimBaoDongTapPhuThuocHam])
def route_tai_de_len(data: DeBaiTimBaoDongTapPhuThuocHam, request: Request):
    tap_phu_thuoc_ham = dinh_dang_tap_phu_thuoc_ham_object(
        data.tap_phu_thuoc_ham
    )

    trang_thai = {
        KhoaSession.TAP_PHU_THUOC_HAM: tap_phu_thuoc_ham
    }

    cap_nhat_bao_dong_tap_phu_thuoc_ham_session(request, trang_thai)

    loai_thong_bao = "success"
    thong_bao = "Tải đề bài lên hệ thống thành công!"

    return tao_phan_hoi_bao_dong_tap_phu_thuoc_ham(trang_thai, loai_thong_bao, thong_bao)

@router.post("/giai-de", response_model=PhanHoi[BaiGiai])
def route_giai_bao_dong_tap_thuoc_tinh(request: Request):
    trang_thai = lay_bao_dong_tap_phu_thuoc_ham_session(request)

    tap_phu_thuoc_ham = trang_thai[KhoaSession.TAP_PHU_THUOC_HAM]

    if not tap_phu_thuoc_ham:
        return PhanHoi(
            doi_tuong=None,
            loai_thong_bao=LoaiThongBao.CANH_BAO,
            thong_bao="Tập phụ thuộc hàm F không được để trống."
        )


    ket_qua, loi_giai = tinh_bao_dong_tap_phu_thuoc_ham(tap_phu_thuoc_ham)

    ket_qua = f"F⁺ = {{ {", ".join(sorted(ket_qua))} }}"

    return PhanHoi(
        doi_tuong=BaiGiai(
            ket_qua=ket_qua,
            loi_giai=loi_giai
        ),
        loai_thong_bao=LoaiThongBao.THANH_CONG,
        thong_bao="Tính toán bao đóng tập phụ thuộc hàm thành công."
    )