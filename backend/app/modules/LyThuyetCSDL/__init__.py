# backend/app/modules/LyThuyetCSDL/routes.py
from fastapi import APIRouter, Request
from backend.app.modules.LyThuyetCSDL.schemas import TrangThaiCSDLResponse
from backend.app.modules.LyThuyetCSDL.routes.bao_dong_tap_thuoc_tinh import (
    router as router_bd_thuoc_tinh,
    get_or_init_session,
    build_response_state
)

router_tong = APIRouter(prefix="/api")

@router_tong.get("/state", response_model=TrangThaiCSDLResponse, tags=["Trạng thái"])
def lay_trang_thai_ban_dau(request: Request):
    # Lấy session tương ứng của user tạo request
    state = get_or_init_session(request)
    return build_response_state(state)

router_tong.include_router(router_bd_thuoc_tinh)