import StateApi from "../api/State";


export const StateActions = ({setTapPhuThuocHam}) => {
    return {
        async fetchState() {
            try {
                const response = await StateApi.fetchBaoDongTapPhuThuocHamState();
                const doi_tuong = response.data.doi_tuong;
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