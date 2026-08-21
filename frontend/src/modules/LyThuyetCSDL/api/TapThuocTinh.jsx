import api from "../../../CauHinh";

const TapThuocTinhApi = (prefix) => ({
    fetchData: () =>
        api.get("/trang-thai"),

    them: (thuocTinh) =>
        api.post(`${prefix}/them-thuoc-tinh`, {
            thuoc_tinh: thuocTinh,
        }),

    xoa: (thuocTinh) =>
        api.post(`${prefix}/xoa-thuoc-tinh`, {
            thuoc_tinh: thuocTinh,
        }),

    xoaTrong: () =>
        api.post(`${prefix}/xoa-trong-thuoc-tinh`),
});

export default TapThuocTinhApi;