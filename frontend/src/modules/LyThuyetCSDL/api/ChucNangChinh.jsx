import api from "../../../CauHinh";

const ChucNangChinhApi = (prefix) => ({
    taiLen: (deBai) =>
        api.post(`${prefix}/tai-de-bai-len`, deBai),

    taoDeBaiNgauNhien: () =>
        api.post(`${prefix}/tao-de-bai-ngau-nhien`),

    giaiDe: () =>
        api.post(`${prefix}/giai-de`),
});

export default ChucNangChinhApi;