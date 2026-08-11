export const ChonDangChuanAction = ({
    api,
    setDangChuan,
    setThongBao,
}) => {
    return {
        async chonDangChuan(dangChuanDuocChon) {
            try {
                const phanHoi = await api.chonDangChuan(dangChuanDuocChon);
                setDangChuan(phanHoi.data.doi_tuong.dang_chuan)
                setThongBao({
                    loai_thong_bao: phanHoi.data.loai_thong_bao,
                    noi_dung: phanHoi.data.thong_bao,
                });
            } catch (err) {
                setThongBao(err.phanHoi?.data?.detail);
            }
        }
    };
};