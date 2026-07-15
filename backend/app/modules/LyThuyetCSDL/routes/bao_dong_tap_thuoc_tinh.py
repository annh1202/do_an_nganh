import re

from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel, Field

from backend.app.modules.LyThuyetCSDL.schemas import TrangThaiCSDLResponse, PhuThuocHamSchema

from backend.app.modules.LyThuyetCSDL.utils.actions import (
    add_attribute, delete_attribute, clear_attributes,
    add_fd, delete_fd, clear_fds
)

router = APIRouter(prefix="/bao-dong-tap-thuoc-tinh", tags=["Bao đóng thuộc tính"])


class YeuCauThemXoaThuocTinh(BaseModel):
    attribute: str = Field(..., description="Thuộc tính cần xử lý")


def get_or_init_session(request: Request) -> dict:
    """Khởi tạo session nếu user mới truy cập lần đầu"""
    if "bao_dong_thuoc_tinh" not in request.session:
        request.session["bao_dong_thuoc_tinh"] = {
            "R": [],
            "F": [],
            "X": []
        }
    return request.session["bao_dong_thuoc_tinh"]


def build_response_state(state):
    """
    Parse linh hoạt tập phụ thuộc hàm F từ chuỗi (format_fd) thành cấu trúc JSON
    để React nhận diện và hiển thị chuẩn xác, bất kể định dạng mũi tên nào.
    """
    parsed_fds = []
    for fd_str in state.get("F", []):
        if isinstance(fd_str, str):
            # Tách chuỗi dựa trên ký tự mũi tên phổ biến: "->" hoặc "→"
            # Kết quả trả về 2 vế độc lập, loại bỏ khoảng trắng thừa xung quanh
            parts = re.split(r'->|→', fd_str)
            if len(parts) == 2:
                parsed_fds.append({
                    "lhs": parts[0].strip(),
                    "rhs": parts[1].strip()
                })
            else:
                # Phòng hờ chuỗi định dạng lạ, giữ nguyên làm vế trái
                parsed_fds.append({
                    "lhs": fd_str.strip(),
                    "rhs": ""
                })

    return {
        "R": state.get("R", []),
        "F": parsed_fds,
        "X": state.get("X", [])
    }


# ====================<< TẬP THUỘC TÍNH R >>====================

@router.post("/them-thuoc-tinh", response_model=TrangThaiCSDLResponse)
def route_them_thuoc_tinh(data: YeuCauThemXoaThuocTinh, request: Request):
    state = get_or_init_session(request)

    # Gọi trực tiếp action để xử lý. Action tự chuẩn hóa, tự check lỗi định dạng và check trùng
    is_success, msg_type, message = add_attribute(data.attribute, state["R"])
    if not is_success:
        # Nếu nghiệp vụ thất bại (False), ném thông báo chi tiết của action dưới dạng lỗi HTTP 400
        raise HTTPException(status_code=400, detail=message)

    # Đồng bộ ép cứng xuống Session Cookie bằng một bản sao mới (tránh lỗi nuốt thuộc tính cũ)
    request.session["bao_dong_thuoc_tinh"] = {
        "R": list(state["R"]),
        "F": list(state["F"]),
        "X": list(state["X"])
    }
    return build_response_state(request.session["bao_dong_thuoc_tinh"])


@router.post("/xoa-thuoc-tinh", response_model=TrangThaiCSDLResponse)
def route_xoa_thuoc_tinh(data: YeuCauThemXoaThuocTinh, request: Request):
    state = get_or_init_session(request)

    is_success, msg_type, message = delete_attribute(data.attribute, state["R"], state["F"], state["X"])
    if not is_success:
        raise HTTPException(status_code=400, detail=message)

    request.session["bao_dong_thuoc_tinh"] = {
        "R": list(state["R"]),
        "F": list(state["F"]),
        "X": list(state["X"])
    }
    return build_response_state(request.session["bao_dong_thuoc_tinh"])


@router.post("/xoa-trong-thuoc-tinh", response_model=TrangThaiCSDLResponse)
def route_xoa_trong_thuoc_tinh(request: Request):
    state = get_or_init_session(request)

    is_success, msg_type, message = clear_attributes(state["R"], state["F"], state["X"])
    if not is_success:
        raise HTTPException(status_code=400, detail=message)

    request.session["bao_dong_thuoc_tinh"] = {
        "R": list(state["R"]),
        "F": list(state["F"]),
        "X": list(state["X"])
    }
    return build_response_state(request.session["bao_dong_thuoc_tinh"])


# ====================<< TẬP PHỤ THUỘC HÀM F >>====================

@router.post("/them-phu-thuoc-ham", response_model=TrangThaiCSDLResponse)
def route_them_phu_thuoc_ham(data: PhuThuocHamSchema, request: Request):
    state = get_or_init_session(request)

    # Gọi trực tiếp action thêm phụ thuộc hàm, truyền thẳng vế trái và vế phải thô vào
    is_success, msg_type, message = add_fd(data.lhs, data.rhs, state["R"], state["F"])
    if not is_success:
        raise HTTPException(status_code=400, detail=message)

    request.session["bao_dong_thuoc_tinh"] = {
        "R": list(state["R"]),
        "F": list(state["F"]),
        "X": list(state["X"])
    }
    return build_response_state(request.session["bao_dong_thuoc_tinh"])


@router.post("/xoa-phu-thuoc-ham", response_model=TrangThaiCSDLResponse)
def route_xoa_phu_thuoc_ham(data: PhuThuocHamSchema, request: Request):
    state = get_or_init_session(request)

    is_success, msg_type, message = delete_fd(data.lhs, data.rhs, state["F"])
    if not is_success:
        raise HTTPException(status_code=400, detail=message)

    request.session["bao_dong_thuoc_tinh"] = {
        "R": list(state["R"]),
        "F": list(state["F"]),
        "X": list(state["X"])
    }
    return build_response_state(request.session["bao_dong_thuoc_tinh"])


@router.post("/xoa-trong-phu-thuoc-ham", response_model=TrangThaiCSDLResponse)
def route_xoa_trong_phu_thuoc_ham(request: Request):
    state = get_or_init_session(request)

    clear_fds(state["F"])

    request.session["bao_dong_thuoc_tinh"] = {
        "R": list(state["R"]),
        "F": list(state["F"]),
        "X": list(state["X"])
    }
    return build_response_state(request.session["bao_dong_thuoc_tinh"])