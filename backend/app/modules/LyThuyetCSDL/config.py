class KhoaSession:
    TAP_THUOC_TINH = "tap_thuoc_tinh"
    TAP_PHU_THUOC_HAM = "tap_phu_thuoc_ham"
    TAP_THUOC_TINH_CAN_TIM = "tap_thuoc_tinh_muc_tieu"
    BAO_DONG_TAP_THUOC_TINH = "bao_dong_tap_thuoc_tinh"
    BAO_DONG_TAP_PHU_THUOC_HAM = "bao_dong_tap_phu_thuoc_ham"
    KHOA_UNG_VIEN = "khoa_ung_vien"
    DANG_CHUAN = "dang_chuan"
    DANH_SACH_DANG_CHUAN = "danh_sach_dang_chuan"

class LoaiThongBao:
    THANH_CONG = "success"
    CANH_BAO = "warning"
    NGUY_HIEM = "danger"

MODULE_LY_THUYET_CSDL = [
    {
        "id": "gioi-thieu",
        "label": "1. Giới thiệu các chức năng"
    },
    {
        "id": "bao-dong-tap-thuoc-tinh",
        "label": "2. Tìm bao đóng tập thuộc tính"
    },
    {
        "id": "bao-dong-tap-phu-thuoc-ham",
        "label": "3. Tìm bao đóng tập phụ thuộc hàm"
    },
    {
        "id": "khoa-ung-vien",
        "label": "4. Tìm khóa ứng viên"
    },
    {
        "id": "dang-chuan",
        "label": "5. Nâng dạng chuẩn CSDL"
    }
]

DANH_SACH_DANG_CHUAN = [
    {
        "value": "2NF",
        "label": "2NF - Dạng chuẩn 2",
    },
    {
        "value": "3NF",
        "label": "3NF - Dạng chuẩn 3",
    },
    {
        "value": "BCNF",
        "label": "BCNF - Dạng chuẩn Boyce-Codd",
    },
]