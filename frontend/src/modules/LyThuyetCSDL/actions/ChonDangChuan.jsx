export const ChonDangChuanAction = ({
    api,
    setDangChuan,
    setThongBao,
}) => {
    return {
        async chonDangChuan(dang_chuan_duoc_chon) {
            try {
                const response = await api.chonDangChuan(dang_chuan_duoc_chon);
                setDangChuan(response.data.doi_tuong.dang_chuan)
                setThongBao({
                    loai_thong_bao: response.data.loai_thong_bao,
                    noi_dung: response.data.thong_bao,
                });
            } catch (err) {
                setThongBao(err.response?.data?.detail);
            }
        }
    };
};