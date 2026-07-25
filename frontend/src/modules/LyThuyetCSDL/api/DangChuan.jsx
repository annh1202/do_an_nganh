import api from "./CauHinh";

const DangChuanApi = (prefix) => ({
    chonDangChuan: (dang_chuan) =>
        api.post(`${prefix}/chon-dang-chuan`, {
            dang_chuan
        }),
});

export default DangChuanApi;