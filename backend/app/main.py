from fastapi import FastAPI
import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from starlette.middleware.sessions import SessionMiddleware

from backend.app.modules.LyThuyetCSDL.routes.trang_thai import router_tong as csdl_router


load_dotenv()

app = FastAPI(
    title="Đồ án Lý thuyết Cơ sở dữ liệu API",
    description="Hệ thống Backend FastAPI phục vụ tính toán bao đóng, khóa ứng viên và dạng chuẩn.",
    version="1.0.0"
)

# 1. Cấu hình Session Middleware
SECRET_KEY = os.getenv("SECRET_KEY")
app.add_middleware(
    SessionMiddleware,
    secret_key=SECRET_KEY, # Đặt chuỗi bất kỳ tùy ý
    session_cookie="session_csdl",
    max_age=3600 # Thời gian sống của session (1 tiếng)
)

# 2. Cấu hình CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True, # gửi Cookie/Session kèm theo API
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(csdl_router)


@app.get("/")
def kiem_tra_he_thong():
    return {"status": "running", "message": "FastAPI đang hoạt động ổn định!"}

