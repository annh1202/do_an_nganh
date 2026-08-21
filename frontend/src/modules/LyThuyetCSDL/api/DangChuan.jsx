import api from "../../../CauHinh";

const DangChuanApi = (prefix) => ({
    chonDangChuan: (dangChuan) =>
        api.post(`${prefix}/chon-dang-chuan`, {
            dang_chuan: dangChuan,
        }),
});

export default DangChuanApi;