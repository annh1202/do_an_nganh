import random

from fastapi import APIRouter, HTTPException, Request

from backend.app.modules.LyThuyetCSDL.bai_giai.dang_chuan import nang_dang_chuan_2, nang_dang_chuan_3, \
    nang_dang_chuan_bcnf
from backend.app.modules.LyThuyetCSDL.config import KhoaSession, LoaiThongBao, DANH_SACH_DANG_CHUAN
from backend.app.modules.LyThuyetCSDL.schemas import PhuThuocHam, ThuocTinh, PhanHoi, \
    DeBaiNangDangChuan, DangChuan, BaiGiai
from backend.app.modules.LyThuyetCSDL.utils.chuan_hoa import chuan_hoa_tap_thuoc_tinh
from backend.app.modules.LyThuyetCSDL.utils.dinh_dang import dinh_dang_tap_phu_thuoc_ham_tuple, \
    dinh_dang_tap_phu_thuoc_ham_object
from backend.app.modules.LyThuyetCSDL.utils.ho_tro_phan_hoi import tao_phan_hoi_dang_chuan
from backend.app.modules.LyThuyetCSDL.utils.ho_tro_session import lay_dang_chuan_session, \
    cap_nhat_dang_chuan_session
from backend.app.modules.LyThuyetCSDL.utils.kiem_tra_hop_le import kiem_tra_file_dang_chuan
from backend.app.modules.LyThuyetCSDL.utils.tao_ngau_nhien import tao_tap_thuoc_tinh_ngau_nhien, \
    tao_tap_phu_thuoc_ham_ngau_nhien
from backend.app.modules.LyThuyetCSDL.utils.them_xoa_sua import (
    them_thuoc_tinh, xoa_thuoc_tinh, xoa_trong_tap_thuoc_tinh,
    them_phu_thuoc_ham, xoa_phu_thuoc_ham, xoa_trong_tap_phu_thuoc_ham
)


router = APIRouter(prefix="/dang-chuan", tags=["Dạng chuẩn"])

# ==========================================
# TẬP THUỘC TÍNH R
# ==========================================
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


# ==========================================
# TẬP PHỤ THUỘC HÀM F
# ==========================================
@router.post("/them-phu-thuoc-ham", response_model=PhanHoi[DeBaiNangDangChuan])
def route_them_phu_thuoc_ham(data: PhuThuocHam, request: Request):
    trang_thai = lay_dang_chuan_session(request)

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

# ==========================================
# CHỌN DẠNG CHUẨN
# ==========================================
dang_chuan_hop_le = {
    item["value"]
    for item in DANH_SACH_DANG_CHUAN
}

@router.post("/chon-dang-chuan", response_model=PhanHoi[DeBaiNangDangChuan])
def route_chon_dang_chuan(data: DangChuan, request: Request):
    trang_thai = lay_dang_chuan_session(request)

    if data.dang_chuan not in dang_chuan_hop_le:
        return tao_phan_hoi_dang_chuan(trang_thai, LoaiThongBao.NGUY_HIEM, "Dạng chuẩn không hợp lệ")

    trang_thai[KhoaSession.DANG_CHUAN] = data.dang_chuan

    cap_nhat_dang_chuan_session(request, trang_thai)

    return tao_phan_hoi_dang_chuan(
        trang_thai,
        LoaiThongBao.THANH_CONG,
        "Chọn dạng chuẩn thành công"
    )

# ==========================================
# CÁC CHỨC NĂNG CHÍNH
# ==========================================
@router.post("/tao-de-bai-ngau-nhien", response_model=PhanHoi[DeBaiNangDangChuan])
def route_tai_de_len(request: Request):
    tap_thuoc_tinh = tao_tap_thuoc_tinh_ngau_nhien(so_thuoc_tinh_toi_thieu=4, so_thuoc_tinh_toi_da=6)
    tap_phu_thuoc_ham = tao_tap_phu_thuoc_ham_ngau_nhien(tap_thuoc_tinh)
    dang_chuan = random.choice(list(dang_chuan_hop_le))

    trang_thai = {
        KhoaSession.TAP_THUOC_TINH: tap_thuoc_tinh,
        KhoaSession.TAP_PHU_THUOC_HAM: dinh_dang_tap_phu_thuoc_ham_tuple(tap_phu_thuoc_ham),
        KhoaSession.DANG_CHUAN: dang_chuan
    }

    cap_nhat_dang_chuan_session(request, trang_thai)

    return tao_phan_hoi_dang_chuan(
        trang_thai=trang_thai,
        loai_thong_bao="success",
        thong_bao="Tải đề bài lên hệ thống thành công!"
    )

@router.post("/tai-de-bai-len", response_model=PhanHoi[DeBaiNangDangChuan])
def route_tai_de_len(data: DeBaiNangDangChuan, request: Request):
    du_lieu = data.model_dump()

    hop_le, thong_bao = kiem_tra_file_dang_chuan(du_lieu)

    if not hop_le:
        return tao_phan_hoi_dang_chuan(
            trang_thai=lay_dang_chuan_session(request),
            loai_thong_bao="warning",
            thong_bao=thong_bao
        )

    tap_thuoc_tinh = chuan_hoa_tap_thuoc_tinh(data.tap_thuoc_tinh)
    tap_phu_thuoc_ham = dinh_dang_tap_phu_thuoc_ham_object(
        data.tap_phu_thuoc_ham
    )
    dang_chuan = data.dang_chuan.strip().upper()

    trang_thai = {
        KhoaSession.TAP_THUOC_TINH: tap_thuoc_tinh,
        KhoaSession.TAP_PHU_THUOC_HAM: tap_phu_thuoc_ham,
        KhoaSession.DANG_CHUAN: dang_chuan
    }

    cap_nhat_dang_chuan_session(request, trang_thai)

    return tao_phan_hoi_dang_chuan(
        trang_thai=trang_thai,
        loai_thong_bao="success",
        thong_bao="Tải đề bài lên hệ thống thành công!"
    )

@router.post("/giai-de", response_model=PhanHoi[BaiGiai])
def route_nang_dang_chuan(request: Request):
    trang_thai = lay_dang_chuan_session(request)

    tap_thuoc_tinh = trang_thai[KhoaSession.TAP_THUOC_TINH]
    tap_phu_thuoc_ham = trang_thai[KhoaSession.TAP_PHU_THUOC_HAM]
    dang_chuan = trang_thai[KhoaSession.DANG_CHUAN]

    # Kiểm tra dữ liệu đầu vào
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

    if not dang_chuan:
        return PhanHoi(
            doi_tuong=None,
            loai_thong_bao=LoaiThongBao.CANH_BAO,
            thong_bao="Dạng chuẩn không được để trống."
        )

    if dang_chuan == "2NF":
        ket_qua, loi_giai = nang_dang_chuan_2(tap_thuoc_tinh, tap_phu_thuoc_ham)

    elif dang_chuan == "3NF":
        ket_qua, loi_giai = nang_dang_chuan_3(tap_thuoc_tinh, tap_phu_thuoc_ham)

    elif dang_chuan == "BCNF":
        ket_qua, loi_giai = nang_dang_chuan_bcnf(tap_thuoc_tinh, tap_phu_thuoc_ham)
    else:
        ket_qua = "Không có kết quả"
        loi_giai = "Không có lời giải"

    return PhanHoi(
        doi_tuong=BaiGiai(
            ket_qua=ket_qua,
            loi_giai=loi_giai
        ),
        loai_thong_bao=LoaiThongBao.THANH_CONG,
        thong_bao="Tính toán dạng chuẩn thành công."
    )