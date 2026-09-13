import subprocess
import time
import urllib.request

def wait_for_server(url, timeout=30):
    start = time.perf_counter()
    while time.perf_counter() - start < timeout:
        try:
            with urllib.request.urlopen(url) as response:
                if response.status == 200:
                    return time.perf_counter() - start
        except Exception:
            time.sleep(0.3)
    return None

if __name__ == "__main__":
    start_time = time.perf_counter()

    backend = subprocess.Popen(
        ["uvicorn", "app.main:app", "--reload"],
        cwd=r"A:\DoAnNganh\do_an_nganh\backend",
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )

    frontend = subprocess.Popen(
        ["npm", "run", "dev"],
        cwd=r"A:\DoAnNganh\do_an_nganh\frontend",
        shell=True,
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )

    print("Đang chờ Backend và Frontend khởi động...")

    backend_time = wait_for_server("http://127.0.0.1:8000")
    frontend_time = wait_for_server("http://localhost:5173")

    total_ready_time = time.perf_counter() - start_time

    if backend_time:
        print(f"Backend đã sẵn sàng sau: {backend_time:.2f} giây")
    if frontend_time:
        print(f"Frontend đã sẵn sàng sau: {frontend_time:.2f} giây")

    print(f"Cả 2 dịch vụ hoàn tất khởi động trong: {total_ready_time:.2f} giây")