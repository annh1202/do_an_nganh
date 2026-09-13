# Hướng Dẫn Cài Đặt và Khởi Chạy Dự Án

Tài liệu hướng dẫn chi tiết các bước từ tải mã nguồn (clone), thiết lập môi trường ảo, cấu hình biến môi trường đến cài đặt thư viện và khởi chạy ứng dụng.

---

## Cấu Trúc Dự Án (Project Structure)

```text
do_an_nganh/
│
├── backend/
    ├── app/
    ├── pytest/
    ├── .env              # File chứa biến môi trường (Cần tạo thủ công)
    ├── run.py            # File thực thi chính khởi chạy ứng dụng
├── frontend/
├── requirements.txt       # Danh sách các thư viện phụ thuộc            
├── README.md              # Tài liệu hướng dẫn sử dụng
└── venv/
```

---

## Các Bước Cài Đặt & Khởi Chạy

### Bước 1: Clone Mã Nguồn (Repository)

Mở terminal/command prompt và thực hiện lệnh clone dự án về máy:

```bash
git clone https://github.com/annh1202/do_an_nganh.git
```

---

### Bước 2: Tạo File Cấu Hình Biến Môi Trường (`.env`)

Tạo một file mới tên `.env` tại thư mục gốc của dự án. Thêm cấu hình `SECRET_KEY`

```env
# Cấu hình biến môi trường
SECRET_KEY=
```

---

### Bước 3: Khởi Tạo Môi Trường Ảo & Chọn Python Interpreter

Tạo môi trường ảo để cô lập các thư viện phụ thuộc của dự án.

#### 1. Tạo môi trường ảo:
```bash
python -m venv venv
```

#### 2. Kích hoạt môi trường ảo (Activate):
- **Windows (PowerShell):**
  ```powershell
  . env\Scripts\Activate.ps1
  ```
  *(Nếu gặp lỗi Execution Policy, mở PowerShell dưới quyền Admin và chạy: `Set-ExecutionPolicy Unrestricted`)*

- **Windows (Command Prompt - CMD):**
  ```cmd
  . env\Scripts ctivate.bat
  ```

- **macOS / Linux:**
  ```bash
  source venv/bin/activate
  ```

#### 3. Cấu hình Python Interpreter trong IDE:
- **VS Code:**
  1. Nhấn tổ hợp phím `Ctrl + Shift + P` (hoặc `Cmd + Shift + P` trên Mac).
  2. Gõ và chọn `Python: Select Interpreter`.
  3. Chọn đường dẫn tới môi trường `venv` vừa tạo (ví dụ: `./venv/bin/python` hoặc `./venv/Scripts/python.exe`).
- **PyCharm:**
  1. Vào `File` > `Settings` (trên Mac: `PyCharm` > `Preferences`).
  2. Chọn `Project: <Tên_Dự_Án>` > `Python Interpreter`.
  3. Click `Add Interpreter` > `Add Local Interpreter...` > Chọn `Existing environment` và trỏ tới file python trong thư mục `venv`.

---

### Bước 4: Cài Đặt Các Thư Viện Trong `requirements.txt`

Sau khi đã kích hoạt môi trường ảo (tên `(venv)` xuất hiện ở đầu dòng lệnh), tiến hành cài đặt các gói phụ thuộc:

```bash
# Nâng cấp pip lên phiên bản mới nhất
python -m pip install --upgrade pip

# Cài đặt các gói thư viện
pip install -r requirements.txt
```

---

### Bước 5: Chạy Dự Án

Khởi chạy ứng dụng bằng cách thực thi file `run.py`:

```bash
python run.py
```

Khi ứng dụng chạy thành công, bạn sẽ thấy thông báo log trên màn hình terminal.
