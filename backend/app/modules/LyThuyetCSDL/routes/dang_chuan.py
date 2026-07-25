from fastapi import APIRouter, HTTPException, Request

from backend.app.modules.LyThuyetCSDL.config import KhoaSession, LoaiThongBao
from backend.app.modules.LyThuyetCSDL.schemas import PhuThuocHam, ThuocTinh, PhanHoi, \
    DeBaiNangDangChuan, DangChuan
from backend.app.modules.LyThuyetCSDL.utils.actions import (
    them_thuoc_tinh, xoa_thuoc_tinh, xoa_trong_tap_thuoc_tinh,
    them_phu_thuoc_ham, xoa_phu_thuoc_ham, xoa_trong_tap_phu_thuoc_ham
)
from backend.app.modules.LyThuyetCSDL.utils.normalizers import chuyen_tap_phu_thuoc_ham_sang_dang_class
from backend.app.modules.LyThuyetCSDL.utils.session_helpers import lay_dang_chuan_session, lay_dang_chuan_session

router = APIRouter(prefix="/dang-chuan", tags=["Dạng chuẩn"])


# ====================<< TẬP THUỘC TÍNH R >>====================
@router.post("/them-thuoc-tinh", response_model=PhanHoi[DeBaiNangDangChuan])
def route_them_thuoc_tinh(data: ThuocTinh, request: Request):
    state = lay_dang_chuan_session(request)

    # Gọi trực tiếp action để xử lý. Action tự chuẩn hóa, tự check lỗi định dạng và check trùng
    co_thanh_cong, loai_thong_bao, thong_bao = them_thuoc_tinh(
        data.thuoc_tinh,
        state[KhoaSession.TAP_THUOC_TINH]
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
    request.session[KhoaSession.DANG_CHUAN] = {
        KhoaSession.TAP_THUOC_TINH: list(state[KhoaSession.TAP_THUOC_TINH]),
        KhoaSession.TAP_PHU_THUOC_HAM: list(state[KhoaSession.TAP_PHU_THUOC_HAM]),
        KhoaSession.DANG_CHUAN: state[KhoaSession.DANG_CHUAN]
    }

    return PhanHoi(
        doi_tuong=DeBaiNangDangChuan(
            tap_thuoc_tinh=state[KhoaSession.TAP_THUOC_TINH],
            tap_phu_thuoc_ham=chuyen_tap_phu_thuoc_ham_sang_dang_class(
                state[KhoaSession.TAP_PHU_THUOC_HAM]
            ),
            dang_chuan=state[KhoaSession.DANG_CHUAN]
        ),
        loai_thong_bao=loai_thong_bao,
        thong_bao=thong_bao
    )


@router.post("/xoa-thuoc-tinh", response_model=PhanHoi[DeBaiNangDangChuan])
def route_xoa_thuoc_tinh(data: ThuocTinh, request: Request):
    state = lay_dang_chuan_session(request)

    co_thanh_cong, loai_thong_bao, thong_bao = xoa_thuoc_tinh(
        data.thuoc_tinh,
        state[KhoaSession.TAP_THUOC_TINH],
        state[KhoaSession.TAP_PHU_THUOC_HAM],
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

    request.session[KhoaSession.DANG_CHUAN] = {
        KhoaSession.TAP_THUOC_TINH: list(state[KhoaSession.TAP_THUOC_TINH]),
        KhoaSession.TAP_PHU_THUOC_HAM: list(state[KhoaSession.TAP_PHU_THUOC_HAM]),
        KhoaSession.DANG_CHUAN: state[KhoaSession.DANG_CHUAN]
    }

    return PhanHoi(
        doi_tuong=DeBaiNangDangChuan(
            tap_thuoc_tinh=state[KhoaSession.TAP_THUOC_TINH],
            tap_phu_thuoc_ham=chuyen_tap_phu_thuoc_ham_sang_dang_class(
                state[KhoaSession.TAP_PHU_THUOC_HAM]
            ),
            dang_chuan=state[KhoaSession.DANG_CHUAN]
        ),
        loai_thong_bao=loai_thong_bao,
        thong_bao=thong_bao
    )


@router.post("/xoa-trong-thuoc-tinh", response_model=PhanHoi[DeBaiNangDangChuan])
def route_xoa_trong_thuoc_tinh(request: Request):
    state = lay_dang_chuan_session(request)

    co_thanh_cong, loai_thong_bao, thong_bao = xoa_trong_tap_thuoc_tinh(
        state[KhoaSession.TAP_THUOC_TINH],
        state[KhoaSession.TAP_PHU_THUOC_HAM],
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

    request.session[KhoaSession.DANG_CHUAN] = {
        KhoaSession.TAP_THUOC_TINH: list(state[KhoaSession.TAP_THUOC_TINH]),
        KhoaSession.TAP_PHU_THUOC_HAM: list(state[KhoaSession.TAP_PHU_THUOC_HAM]),
        KhoaSession.DANG_CHUAN: state[KhoaSession.DANG_CHUAN]
    }

    return PhanHoi(
        doi_tuong=DeBaiNangDangChuan(
            tap_thuoc_tinh=state[KhoaSession.TAP_THUOC_TINH],
            tap_phu_thuoc_ham=chuyen_tap_phu_thuoc_ham_sang_dang_class(
                state[KhoaSession.TAP_PHU_THUOC_HAM]
            ),
            dang_chuan=state[KhoaSession.DANG_CHUAN]
        ),
        loai_thong_bao=loai_thong_bao,
        thong_bao=thong_bao
    )


# ====================<< TẬP PHỤ THUỘC HÀM F >>====================
@router.post("/them-phu-thuoc-ham", response_model=PhanHoi[DeBaiNangDangChuan])
def route_them_phu_thuoc_ham(data: PhuThuocHam, request: Request):
    state = lay_dang_chuan_session(request)

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

    request.session[KhoaSession.DANG_CHUAN] = {
        KhoaSession.TAP_THUOC_TINH: list(state[KhoaSession.TAP_THUOC_TINH]),
        KhoaSession.TAP_PHU_THUOC_HAM: list(state[KhoaSession.TAP_PHU_THUOC_HAM]),
        KhoaSession.DANG_CHUAN: state[KhoaSession.DANG_CHUAN]
    }

    return PhanHoi(
        doi_tuong=DeBaiNangDangChuan(
            tap_thuoc_tinh=state[KhoaSession.TAP_THUOC_TINH],
            tap_phu_thuoc_ham=chuyen_tap_phu_thuoc_ham_sang_dang_class(
                state[KhoaSession.TAP_PHU_THUOC_HAM]
            ),
            dang_chuan=state[KhoaSession.DANG_CHUAN]
        ),
        loai_thong_bao=loai_thong_bao,
        thong_bao=thong_bao
    )


@router.post("/xoa-phu-thuoc-ham", response_model=PhanHoi[DeBaiNangDangChuan])
def route_xoa_phu_thuoc_ham(data: PhuThuocHam, request: Request):
    state = lay_dang_chuan_session(request)

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

    request.session[KhoaSession.DANG_CHUAN] = {
        KhoaSession.TAP_THUOC_TINH: list(state[KhoaSession.TAP_THUOC_TINH]),
        KhoaSession.TAP_PHU_THUOC_HAM: list(state[KhoaSession.TAP_PHU_THUOC_HAM]),
        KhoaSession.DANG_CHUAN: state[KhoaSession.DANG_CHUAN]
    }

    return PhanHoi(
        doi_tuong=DeBaiNangDangChuan(
            tap_thuoc_tinh=state[KhoaSession.TAP_THUOC_TINH],
            tap_phu_thuoc_ham=chuyen_tap_phu_thuoc_ham_sang_dang_class(
                state[KhoaSession.TAP_PHU_THUOC_HAM]
            ),
            dang_chuan=state[KhoaSession.DANG_CHUAN]
        ),
        loai_thong_bao=loai_thong_bao,
        thong_bao=thong_bao
    )


@router.post("/xoa-trong-phu-thuoc-ham", response_model=PhanHoi[DeBaiNangDangChuan])
def route_xoa_trong_phu_thuoc_ham(request: Request):
    state = lay_dang_chuan_session(request)

    co_thanh_cong, loai_thong_bao, thong_bao = xoa_trong_tap_phu_thuoc_ham(
        state[KhoaSession.TAP_PHU_THUOC_HAM]
    )

    request.session[KhoaSession.DANG_CHUAN] = {
        KhoaSession.TAP_THUOC_TINH: list(state[KhoaSession.TAP_THUOC_TINH]),
        KhoaSession.TAP_PHU_THUOC_HAM: list(state[KhoaSession.TAP_PHU_THUOC_HAM]),
        KhoaSession.DANG_CHUAN: state[KhoaSession.DANG_CHUAN]
    }

    return PhanHoi(
        doi_tuong=DeBaiNangDangChuan(
            tap_thuoc_tinh=state[KhoaSession.TAP_THUOC_TINH],
            tap_phu_thuoc_ham=chuyen_tap_phu_thuoc_ham_sang_dang_class(
                state[KhoaSession.TAP_PHU_THUOC_HAM]
            ),
            dang_chuan=state[KhoaSession.DANG_CHUAN]
        ),
        loai_thong_bao=loai_thong_bao,
        thong_bao=thong_bao
    )

# ====================<< CHỌN DẠNG CHUẨN >>====================
@router.post("/chon-dang-chuan", response_model=PhanHoi[DeBaiNangDangChuan])
def route_chon_dang_chuan(data: DangChuan, request: Request):
    dang_chuan_hop_le = {"2NF", "3NF", "BCNF"}

    if data.dang_chuan not in dang_chuan_hop_le:
        raise HTTPException(
            status_code=400,
            detail={
                "loai_thong_bao": LoaiThongBao.DANGER,
                "thong_bao": "Dạng chuẩn không hợp lệ",
            }
        )

    state = lay_dang_chuan_session(request)

    request.session[KhoaSession.DANG_CHUAN] = {
        KhoaSession.TAP_THUOC_TINH: list(state[KhoaSession.TAP_THUOC_TINH]),
        KhoaSession.TAP_PHU_THUOC_HAM: list(state[KhoaSession.TAP_PHU_THUOC_HAM]),
        KhoaSession.DANG_CHUAN: data.dang_chuan
    }

    return PhanHoi(
        doi_tuong=DeBaiNangDangChuan(
            tap_thuoc_tinh=state[KhoaSession.TAP_THUOC_TINH],
            tap_phu_thuoc_ham=chuyen_tap_phu_thuoc_ham_sang_dang_class(
                state[KhoaSession.TAP_PHU_THUOC_HAM]
            ),
            dang_chuan=state[KhoaSession.DANG_CHUAN]
        ),
        loai_thong_bao=LoaiThongBao.SUCCESS,
        thong_bao="Chọn dạng chuẩn thành công"
    )
