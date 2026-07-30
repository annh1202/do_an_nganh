import React, { useState, useEffect } from 'react';
import TapThuocTinh from '../components/TapThuocTinh';
import TapPhuThuocHam from '../components/TapPhuThuocHam';

import { TaoTapThuocTinh } from "../actions/TaoTapThuocTinh";
import { TaoTapPhuThuocHam } from "../actions/TaoTapPhuThuocHam";

import TapThuocTinhApi from "../api/TapThuocTinh"
import TapPhuThuocHamApi from "../api/TapPhuThuocHam"
import TrangThaiApi from "../api/TrangThai";

const BaoDongTapThuocTinh = () => {
    const [tapThuocTinh, setTapThuocTinh] = useState([]);
    const [tapPhuThuocHam, setTapPhuThuocHam] = useState([]);

    const [loadingThuocTinh, setLoadingThuocTinh] = useState(false);
    const [loadingPhuThuocHam, setLoadingPhuThuocHam] = useState(false);

    const [thongBaoThuocTinh, setThongBaoThuocTinh] = useState(null);
    const [thongBaoPhuThuocHam, setThongBaoPhuThuocHam] = useState(null);

    const thuocTinhApi = TapThuocTinhApi(
        "/khoa-ung-vien"
    );

    const thuocTinhActions = TaoTapThuocTinh({
        api: thuocTinhApi,
        setTapThuocTinh,
        setLoading: setLoadingThuocTinh,
        setThongBao: setThongBaoThuocTinh,
    });

    const phuThuocHamApi = TapPhuThuocHamApi(
        "/khoa-ung-vien"
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
                const response = await TrangThaiApi.fetchTrangThaiKhoaUngVien();
                const doi_tuong = response.data.doi_tuong;
                setTapThuocTinh(doi_tuong.tap_thuoc_tinh);
                setTapPhuThuocHam(doi_tuong.tap_phu_thuoc_ham);
            } catch (err) {
                console.error("Lỗi khi lấy state:",err);
            }
        };

        fetchState();
    }, []);

  return (
    <div className="container py-3">
      <h2 className="text-center mb-4 fw-bold text-dark">Tìm khóa ứng viên</h2>
      <TapThuocTinh
        tapThuocTinh={tapThuocTinh}
        actions={thuocTinhActions}
        thongBao={thongBaoThuocTinh}
        onCloseThongBao={() => setThongBaoThuocTinh(null)}
      />
      <TapPhuThuocHam
        tapPhuThuocHam={tapPhuThuocHam}
        actions={phuThuocHamActions}
        thongBao={thongBaoPhuThuocHam}
        onCloseThongBao={() => setThongBaoPhuThuocHam(null)}
      />

    </div>
  )
};

export default BaoDongTapThuocTinh;