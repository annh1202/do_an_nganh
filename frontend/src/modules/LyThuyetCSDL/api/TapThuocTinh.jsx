import api from "./CauHinh";

const TapThuocTinhApi = (prefix) => ({
    fetchData: () =>
        api.get("/state"),

    them: (thuoc_tinh) =>
        api.post(`${prefix}/them-thuoc-tinh`, {
            thuoc_tinh,
        }),

    xoa: (thuoc_tinh) =>
        api.post(`${prefix}/xoa-thuoc-tinh`, {
            thuoc_tinh,
        }),

    xoaTrong: () =>
        api.post(`${prefix}/xoa-trong-thuoc-tinh`)
});

export default TapThuocTinhApi;