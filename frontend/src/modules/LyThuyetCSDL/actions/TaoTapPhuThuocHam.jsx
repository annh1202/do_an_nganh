export const TaoTapPhuThuocHam = ({
    api,
    setTapPhuThuocHam,
    setLoading,
    setThongBao,
}) => {

    const hienThongBaoLoi = (err) => {
        if (err.response?.data?.detail) {
            setThongBao({
                loai_thong_bao: err.response.data.detail.loai_thong_bao,
                noi_dung: err.response.data.detail.thong_bao,
            });
        } else {
            setThongBao({
                loai_thong_bao: "danger",
                noi_dung: "Có lỗi xảy ra.",
            });
        }
    };


    const capNhatDuLieu = (response) => {
        setTapPhuThuocHam(
            response.data.doi_tuong.tap_phu_thuoc_ham
        );

        setThongBao({
            loai_thong_bao: response.data.loai_thong_bao,
            noi_dung: response.data.thong_bao,
        });
    };


    return {

        async fetchData() {
            try {
                setLoading(true);

                const response = await api.fetchData();

                setTapPhuThuocHam(
                    response.data.doi_tuong.tap_phu_thuoc_ham
                );

                setThongBao(null);

            } catch(err) {

                setThongBao({
                    loai_thong_bao: "danger",
                    noi_dung: "Không thể kết nối đến máy chủ FastAPI.",
                });

            } finally {
                setLoading(false);
            }
        },


        async them(value) {
            try {
                const response = await api.them(value);
                capNhatDuLieu(response);

            } catch(err) {
                hienThongBaoLoi(err);
            }
        },


        async xoa(value) {
            try {
                const response = await api.xoa(value);
                capNhatDuLieu(response);

            } catch(err) {
                hienThongBaoLoi(err);
            }
        },


        async xoaTrong() {
            try {
                const response = await api.xoaTrong();
                capNhatDuLieu(response);

            } catch(err) {
                hienThongBaoLoi(err);
            }
        }
    };
};