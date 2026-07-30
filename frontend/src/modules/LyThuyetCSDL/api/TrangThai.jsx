import api from "./CauHinh";

const TrangThaiApi = {

    fetchTrangThaiBaoDongTapThuocTinh: () =>
        api.get("/bao-dong-tap-thuoc-tinh/trang-thai"),

    fetchTrangThaiBaoDongTapPhuThuocHam: () =>
        api.get("/bao-dong-tap-phu-thuoc-ham/trang-thai"),

    fetchTrangThaiKhoaUngVien: () =>
        api.get("/khoa-ung-vien/trang-thai"),

    fetchTrangThaiDangChuan: () =>
        api.get("/dang-chuan/trang-thai")

};

export default TrangThaiApi;