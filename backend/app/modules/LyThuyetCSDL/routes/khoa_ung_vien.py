from fastapi import APIRouter, HTTPException, Request

from backend.app.modules.LyThuyetCSDL.config import KhoaSession, LoaiThongBao
from backend.app.modules.LyThuyetCSDL.schemas import PhuThuocHam, ThuocTinh, PhanHoi, \
    DeBaiTimKhoaUngVien, BaiGiai
from backend.app.modules.LyThuyetCSDL.utils.tao_ngau_nhien import tao_tap_thuoc_tinh_ngau_nhien, \
    tao_tap_phu_thuoc_ham_ngau_nhien
from backend.app.modules.LyThuyetCSDL.bai_giai.khoa_ung_vien import tim_khoa_ung_vien
from backend.app.modules.LyThuyetCSDL.utils.dinh_dang import dinh_dang_tap_phu_thuoc_ham_object, \
    dinh_dang_tap_phu_thuoc_ham_tuple
from backend.app.modules.LyThuyetCSDL.utils.ho_tro_phan_hoi import tao_phan_hoi_khoa_ung_vien
from backend.app.modules.LyThuyetCSDL.utils.ho_tro_session import lay_khoa_ung_vien_session, \
    cap_nhat_khoa_ung_vien_session
from backend.app.modules.LyThuyetCSDL.utils.them_xoa_sua import (
    them_thuoc_tinh, xoa_thuoc_tinh, xoa_trong_tap_thuoc_tinh,
    them_phu_thuoc_ham, xoa_phu_thuoc_ham, xoa_trong_tap_phu_thuoc_ham
)

router = APIRouter(prefix="/khoa-ung-vien", tags=["Khóa ứng viên"])

# ==========================================
# TẬP THUỘC TÍNH R
# ==========================================
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


# ==========================================
# TẬP PHỤ THUỘC HÀM F
# ==========================================
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

# ==========================================
# CÁC CHỨC NĂNG CHÍNH
# ==========================================
@router.post("/tao-de-bai-ngau-nhien", response_model=PhanHoi[DeBaiTimKhoaUngVien])
def route_tai_de_len(request: Request):
    tap_thuoc_tinh = tao_tap_thuoc_tinh_ngau_nhien(
        so_thuoc_tinh_toi_thieu=4,
        so_thuoc_tinh_toi_da=6
    )
    tap_phu_thuoc_ham = tao_tap_phu_thuoc_ham_ngau_nhien(tap_thuoc_tinh)

    trang_thai = {
        KhoaSession.TAP_THUOC_TINH: tap_thuoc_tinh,
        KhoaSession.TAP_PHU_THUOC_HAM: dinh_dang_tap_phu_thuoc_ham_tuple(tap_phu_thuoc_ham)
    }

    cap_nhat_khoa_ung_vien_session(request, trang_thai)

    return tao_phan_hoi_khoa_ung_vien(
        trang_thai=trang_thai,
        loai_thong_bao="success",
        thong_bao="Tải đề bài lên hệ thống thành công!"
    )


@router.post("/tai-de-bai-len", response_model=PhanHoi[DeBaiTimKhoaUngVien])
def route_tai_de_len(data: DeBaiTimKhoaUngVien, request: Request):
    tap_phu_thuoc_ham = dinh_dang_tap_phu_thuoc_ham_object(
        data.tap_phu_thuoc_ham
    )

    trang_thai = {
        KhoaSession.TAP_THUOC_TINH: data.tap_thuoc_tinh or [],
        KhoaSession.TAP_PHU_THUOC_HAM: tap_phu_thuoc_ham or []
    }

    cap_nhat_khoa_ung_vien_session(request, trang_thai)

    loai_thong_bao = "success"
    thong_bao = "Tải đề bài lên hệ thống thành công!"

    return tao_phan_hoi_khoa_ung_vien(trang_thai, loai_thong_bao, thong_bao)

@router.post("/giai-de", response_model=PhanHoi[BaiGiai])
def route_giai_bao_dong_tap_thuoc_tinh(request: Request):
    trang_thai = lay_khoa_ung_vien_session(request)

    tap_thuoc_tinh = trang_thai[KhoaSession.TAP_THUOC_TINH]
    tap_phu_thuoc_ham = trang_thai[KhoaSession.TAP_PHU_THUOC_HAM]

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

    ket_qua, loi_giai = tim_khoa_ung_vien(tap_thuoc_tinh, tap_phu_thuoc_ham)

    ket_qua = f"Các khóa ứng viên: {", ".join(sorted(ket_qua))}"

    return PhanHoi(
        doi_tuong=BaiGiai(
            ket_qua=ket_qua,
            loi_giai=loi_giai
        ),
        loai_thong_bao=LoaiThongBao.THANH_CONG,
        thong_bao="Tìm khóa ứng viên thành công."
    )