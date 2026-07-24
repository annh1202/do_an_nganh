import api from "./CauHinh";

const TapPhuThuocHamApi = (prefix) => ({
    fetchData: () =>
        api.get("/state"),

    them: ({ ve_trai, ve_phai }) =>
        api.post(`${prefix}/them-phu-thuoc-ham`, {
            ve_trai,
            ve_phai,
        }),

    xoa: ({ ve_trai, ve_phai }) =>
        api.post(`${prefix}/xoa-phu-thuoc-ham`, {
            ve_trai,
            ve_phai,
        }),

    xoaTrong: () =>
        api.post(`${prefix}/xoa-trong-phu-thuoc-ham`),
});

export default TapPhuThuocHamApi;