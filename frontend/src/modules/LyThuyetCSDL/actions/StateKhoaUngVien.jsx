import StateApi from "../api/State";


export const StateActions = ({setTapThuocTinh, setTapPhuThuocHam}) => {
    return {
        async fetchState() {
            try {
                const response = await StateApi.fetchKhoaUngVienState();
                const doi_tuong = response.data.doi_tuong;
                setTapThuocTinh(doi_tuong.tap_thuoc_tinh);
                setTapPhuThuocHam(doi_tuong.tap_phu_thuoc_ham);
            } catch (err) {
                console.error(
                    "Lỗi khi lấy state:",
                    err
                );
            }
        }
    };
};