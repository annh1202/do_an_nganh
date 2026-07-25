import StateApi from "../api/State";


export const StateActions = ({setTapThuocTinh, setTapPhuThuocHam, setDangChuan}) => {
    return {
        async fetchState() {
            try {
                const response = await StateApi.fetchDangChuanState();
                const doi_tuong = response.data.doi_tuong;
                setTapThuocTinh(doi_tuong.tap_thuoc_tinh);
                setTapPhuThuocHam(doi_tuong.tap_phu_thuoc_ham);
                setDangChuan(doi_tuong.dang_chuan)
            } catch (err) {
                console.error(
                    "Lỗi khi lấy state:",
                    err
                );
            }
        }
    };
};