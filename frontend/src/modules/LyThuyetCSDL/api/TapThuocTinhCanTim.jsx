import api from "./CauHinh";

const TapThuocTinhCanTimApi = (prefix) => ({
    fetchData: () =>
        api.get("/state"),

    them: (thuoc_tinh) =>
        api.post(`${prefix}/them-thuoc-tinh-can-tim`, {
            thuoc_tinh,
        }),

    xoa: (thuoc_tinh) =>
        api.post(`${prefix}/xoa-thuoc-tinh-can-tim`, {
            thuoc_tinh,
        }),

    xoaTrong: () =>
        api.post(`${prefix}/xoa-trong-thuoc-tinh-can-tim`)
});

export default TapThuocTinhCanTimApi;