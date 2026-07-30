import api from "./CauHinh";

const TapPhuThuocHamApi = (prefix) => ({
  fetchData: () =>
    api.get("/trang-thai"),

  them: ({ veTrai, vePhai }) =>
    api.post(`${prefix}/them-phu-thuoc-ham`, {
      ve_trai: veTrai,
      ve_phai: vePhai,
    }),

  xoa: ({ veTrai, vePhai }) =>
    api.post(`${prefix}/xoa-phu-thuoc-ham`, {
      ve_trai: veTrai,
      ve_phai: vePhai,
    }),

  xoaTrong: () =>
    api.post(`${prefix}/xoa-trong-phu-thuoc-ham`),
});

export default TapPhuThuocHamApi;