from starlette.requests import Request

from backend.app.modules.LyThuyetCSDL.config import KhoaSession


def lay_bao_dong_tap_thuoc_tinh_session(request: Request) -> dict:
    """Khởi tạo session nếu user mới truy cập lần đầu"""
    if KhoaSession.BAO_DONG_TAP_THUOC_TINH not in request.session:
        request.session[KhoaSession.BAO_DONG_TAP_THUOC_TINH] = {
            KhoaSession.TAP_THUOC_TINH: [],
            KhoaSession.TAP_PHU_THUOC_HAM: [],
            KhoaSession.TAP_THUOC_TINH_CAN_TIM: []
        }

    return request.session[KhoaSession.BAO_DONG_TAP_THUOC_TINH]


def lay_bao_dong_tap_phu_thuoc_ham_session(request: Request) -> dict:
    """Khởi tạo session nếu user mới truy cập lần đầu"""
    if KhoaSession.BAO_DONG_TAP_PHU_THUOC_HAM not in request.session:
        request.session[KhoaSession.BAO_DONG_TAP_PHU_THUOC_HAM] = {
            KhoaSession.TAP_PHU_THUOC_HAM: []
        }

    return request.session[KhoaSession.BAO_DONG_TAP_PHU_THUOC_HAM]


def lay_khoa_ung_vien_session(request: Request) -> dict:
    """Khởi tạo session nếu user mới truy cập lần đầu"""
    if KhoaSession.KHOA_UNG_VIEN not in request.session:
        request.session[KhoaSession.KHOA_UNG_VIEN] = {
            KhoaSession.TAP_THUOC_TINH: [],
            KhoaSession.TAP_PHU_THUOC_HAM: []
        }

    return request.session[KhoaSession.KHOA_UNG_VIEN]


def lay_dang_chuan_session(request: Request) -> dict:
    """Khởi tạo session nếu user mới truy cập lần đầu"""
    if KhoaSession.DANG_CHUAN not in request.session:
        request.session[KhoaSession.DANG_CHUAN] = {
            KhoaSession.TAP_THUOC_TINH: [],
            KhoaSession.TAP_PHU_THUOC_HAM: [],
            KhoaSession.DANG_CHUAN: ""
        }

    return request.session[KhoaSession.DANG_CHUAN]