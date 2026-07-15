from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from backend.app.modules.LyThuyetCSDL.__init__ import router_tong as csdl_router
from dotenv import load_dotenv
import os


load_dotenv()

app = FastAPI(
    title="Đồ án Lý thuyết Cơ sở dữ liệu API",
    description="Hệ thống Backend FastAPI phục vụ tính toán bao đóng, khóa ứng viên và dạng chuẩn.",
    version="1.0.0"
)

# 1. Cấu hình Session Middleware (Thay thế hoàn toàn cho biến global db trên RAM)
SECRET_KEY = os.getenv("SECRET_KEY")
app.add_middleware(
    SessionMiddleware,
    secret_key=SECRET_KEY, # Đặt chuỗi bất kỳ tùy ý
    session_cookie="session_csdl",                          # Tên cookie lưu ở trình duyệt
    max_age=3600                                            # Thời gian sống của session (1 tiếng)
)

# 2. Cấu hình CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Chỉ định đích danh port của React
    allow_credentials=True,                   # BẮT BUỘC bằng True để trình duyệt chịu gửi Cookie/Session kèm theo API
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Nhúng router tổng vào FastAPI instance
app.include_router(csdl_router)

# 3. Endpoint kiểm tra nhanh trạng thái server
@app.get("/")
def kiem_tra_he_thong():
    return {"status": "running", "message": "FastAPI đang hoạt động ổn định!"}