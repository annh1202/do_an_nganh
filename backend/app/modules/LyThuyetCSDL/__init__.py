# # backend/app/modules/LyThuyetCSDL/routes.py
# from fastapi import APIRouter, Request
#
# from backend.app.modules.LyThuyetCSDL.config import KhoaSession
# from backend.app.modules.LyThuyetCSDL.schemas import DeBaiTimBaoDongTapThuocTinh, PhanHoi, DeBaiTimBaoDongTapPhuThuocHam
# from backend.app.modules.LyThuyetCSDL.routes.bao_dong_tap_thuoc_tinh import (
#     router as router_bao_dong_tap_thuoc_tinh
# )
# from backend.app.modules.LyThuyetCSDL.utils.session_helpers import lay_bao_dong_tap_thuoc_tinh_session, \
#     lay_bao_dong_tap_phu_thuoc_ham_session
# from backend.app.modules.LyThuyetCSDL.routes.bao_dong_tap_phu_thuoc_ham import (
#     router as router_bao_dong_tap_phu_thuoc_ham
# )
# from backend.app.modules.LyThuyetCSDL.utils.normalizers import chuyen_tap_phu_thuoc_ham_sang_dang_class
#
# router_tong = APIRouter(prefix="/api")
#
# @router_bao_dong_tap_thuoc_tinh.get("/api/state", response_model=PhanHoi[DeBaiTimBaoDongTapThuocTinh])
# def lay_trang_thai_ban_dau(request: Request):
#     state = lay_bao_dong_tap_thuoc_tinh_session(request)
#
#     return PhanHoi(
#         doi_tuong=DeBaiTimBaoDongTapThuocTinh(
#             tap_thuoc_tinh=state[KhoaSession.TAP_THUOC_TINH],
#             tap_phu_thuoc_ham=chuyen_tap_phu_thuoc_ham_sang_dang_class(
#                 state[KhoaSession.TAP_PHU_THUOC_HAM]
#             ),
#             tap_thuoc_tinh_can_tim=state[KhoaSession.TAP_THUOC_TINH_CAN_TIM],
#         ),
#         loai_thong_bao="info",
#         thong_bao=""
#     )
#
# @router_bao_dong_tap_phu_thuoc_ham.get("/api/state", response_model=PhanHoi[DeBaiTimBaoDongTapPhuThuocHam])
# def lay_trang_thai_ban_dau(request: Request):
#     state = lay_bao_dong_tap_phu_thuoc_ham_session(request)
#
#     return PhanHoi(
#         doi_tuong=DeBaiTimBaoDongTapPhuThuocHam(
#             tap_phu_thuoc_ham=chuyen_tap_phu_thuoc_ham_sang_dang_class(
#                 state[KhoaSession.TAP_PHU_THUOC_HAM]
#             )
#         ),
#         loai_thong_bao="info",
#         thong_bao=""
#     )
#
# router_tong.include_router(router_bao_dong_tap_thuoc_tinh)
# router_tong.include_router(router_bao_dong_tap_phu_thuoc_ham)