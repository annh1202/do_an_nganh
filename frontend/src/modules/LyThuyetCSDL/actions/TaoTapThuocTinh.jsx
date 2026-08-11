export const TaoTapThuocTinh = ({
    api,
    setTapThuocTinh,
    setLoading,
    setThongBao,
}) => {

    const hienThongBaoLoi = (loi) => {
        // Axios
        const detail = loi.response?.data?.detail;

        if (detail && detail.thong_bao) {
            setThongBao({
                loai_thong_bao: detail.loai_thong_bao || "danger",
                noi_dung: detail.thong_bao,
            });
        } else {
            setThongBao({
                loai_thong_bao: "danger",
                noi_dung: "Có lỗi xảy ra.",
            });
        }
    };


    const capNhatDuLieu = (phanHoi) => {
        console.log(phanHoi.data);

        setTapThuocTinh(
            phanHoi.data.doi_tuong.tap_thuoc_tinh
        );

        setThongBao({
            loai_thong_bao: phanHoi.data.loai_thong_bao,
            noi_dung: phanHoi.data.thong_bao,
        });
    };


    return {

        async fetchData() {
            try {
                setLoading(true);

                const phanHoi = await api.fetchData();

                setTapThuocTinh(
                    phanHoi.data.doi_tuong.tap_thuoc_tinh
                );

                setThongBao(null);

            } catch(loi) {
                hienThongBaoLoi(loi);
            }
            finally {
                setLoading(false);
            }
        },


        async them(value) {
            try {
                const phanHoi = await api.them(value);
                capNhatDuLieu(phanHoi);
            }
            catch(loi) {
                hienThongBaoLoi(loi);
            }
        },


        async xoa(value) {
            try {
                const phanHoi = await api.xoa(value);
                capNhatDuLieu(phanHoi);
            }
            catch(loi) {
                hienThongBaoLoi(loi);
            }
        },


        async xoaTrong() {
            try {
                const phanHoi = await api.xoaTrong();
                capNhatDuLieu(phanHoi);
            }
            catch(loi) {
                hienThongBaoLoi(loi);
            }
        }
    };
};