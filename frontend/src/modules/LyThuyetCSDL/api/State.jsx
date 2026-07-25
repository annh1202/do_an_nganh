import api from "./CauHinh";

const StateApi = {

    fetchBaoDongTapThuocTinhState: () =>
        api.get("/bao-dong-tap-thuoc-tinh/state"),

    fetchBaoDongTapPhuThuocHamState: () =>
        api.get("/bao-dong-tap-phu-thuoc-ham/state"),

    fetchKhoaUngVienState: () =>
        api.get("/khoa-ung-vien/state"),

    fetchDangChuanState: () =>
        api.get("/dang-chuan/state")

};

export default StateApi;