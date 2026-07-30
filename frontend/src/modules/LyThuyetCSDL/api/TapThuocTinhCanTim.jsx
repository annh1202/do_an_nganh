import api from "./CauHinh";

const TapThuocTinhCanTimApi = (prefix) => ({
  fetchData: () =>
    api.get("/trang-thai"),

  them: (thuocTinh) =>
    api.post(`${prefix}/them-thuoc-tinh-can-tim`, {
      thuoc_tinh: thuocTinh,
    }),

  xoa: (thuocTinh) =>
    api.post(`${prefix}/xoa-thuoc-tinh-can-tim`, {
      thuoc_tinh: thuocTinh,
    }),

  xoaTrong: () =>
    api.post(`${prefix}/xoa-trong-thuoc-tinh-can-tim`),
});

export default TapThuocTinhCanTimApi;