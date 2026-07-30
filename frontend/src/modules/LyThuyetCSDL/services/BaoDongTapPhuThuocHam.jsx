import React, { useState, useEffect } from 'react';
import TapPhuThuocHam from '../components/TapPhuThuocHam';

import { TaoTapPhuThuocHam } from "../actions/TaoTapPhuThuocHam";

import TapPhuThuocHamApi from "../api/TapPhuThuocHam"
import TrangThaiApi from "../api/TrangThai";


const BaoDongTapPhuThuocHam = () => {
    const [tapPhuThuocHam, setTapPhuThuocHam] = useState([]);

    const [loadingPhuThuocHam, setLoadingPhuThuocHam] = useState(false);

    const [thongBaoPhuThuocHam, setThongBaoPhuThuocHam] = useState(null);

    const phuThuocHamApi = TapPhuThuocHamApi(
        "/bao-dong-tap-phu-thuoc-ham"
    );

    const phuThuocHamActions = TaoTapPhuThuocHam({
        api: phuThuocHamApi,
        setTapPhuThuocHam,
        setLoading: setLoadingPhuThuocHam,
        setThongBao: setThongBaoPhuThuocHam,
    });

    useEffect(() => {
        const fetchState = async () => {
            try {
                const response = await TrangThaiApi.fetchTrangThaiBaoDongTapPhuThuocHam();
                const doiTuong = response.data.doi_tuong;
                setTapPhuThuocHam(doiTuong.tap_phu_thuoc_ham);
            } catch (err) {
                console.error("Lỗi khi lấy state:",err);
            }
        };

        fetchState();
    }, []);

  return (
    <div className="container py-3">
      <h2 className="text-center mb-4 fw-bold text-dark">Tìm bao đóng tập phụ thuộc hàm</h2>

      <TapPhuThuocHam
        tapPhuThuocHam={tapPhuThuocHam}
        actions={phuThuocHamActions}
        thongBao={thongBaoPhuThuocHam}
        onCloseThongBao={() => setThongBaoPhuThuocHam(null)}
      />

    </div>
  )
};

export default BaoDongTapPhuThuocHam;