import React, { useState, useEffect } from 'react';
import TapThuocTinh from '../components/TapThuocTinh';
import TapPhuThuocHam from '../components/TapPhuThuocHam';

import { TaoTapThuocTinh } from "../actions/TaoTapThuocTinh";
import { TaoTapPhuThuocHam } from "../actions/TaoTapPhuThuocHam";

import TapThuocTinhApi from "../api/TapThuocTinh"
import TapPhuThuocHamApi from "../api/TapPhuThuocHam"
import { StateActions } from "../actions/StateKhoaUngVien";

const BaoDongTapThuocTinh = () => {
    const [tap_thuoc_tinh, setTapThuocTinh] = useState([]);
    const [tap_phu_thuoc_ham, setTapPhuThuocHam] = useState([]);

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

    const stateActions = StateActions({
        setTapThuocTinh,
        setTapPhuThuocHam
    });

    useEffect(() => {
        stateActions.fetchState();
    }, []);

  return (
    <div className="container py-3">
      <h2 className="text-center mb-4 fw-bold text-dark">Tìm khóa ứng viên</h2>
      <TapThuocTinh
        tap_thuoc_tinh={tap_thuoc_tinh}
        actions={thuocTinhActions}
        thong_bao={thongBaoThuocTinh}
        onCloseThongBao={() => setThongBaoThuocTinh(null)}
      />
      <TapPhuThuocHam
        tap_phu_thuoc_ham={tap_phu_thuoc_ham}
        actions={phuThuocHamActions}
        thong_bao={thongBaoPhuThuocHam}
        onCloseThongBao={() => setThongBaoPhuThuocHam(null)}
      />

    </div>
  )
};

export default BaoDongTapThuocTinh;