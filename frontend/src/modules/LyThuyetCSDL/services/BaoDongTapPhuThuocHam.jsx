import React, { useState, useEffect } from 'react';
import TapPhuThuocHam from '../components/TapPhuThuocHam';
import { TaoTapPhuThuocHam } from "../actions/TaoTapPhuThuocHam";
import TapPhuThuocHamApi from "../api/TapPhuThuocHam"
import { StateActions } from "../actions/StateBaoDongTapPhuThuocHam";

const BaoDongTapPhuThuocHam = () => {
    const [tap_phu_thuoc_ham, setTapPhuThuocHam] = useState([]);

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

    const stateActions = StateActions({
        setTapPhuThuocHam
    });

    useEffect(() => {
        stateActions.fetchState();
    }, []);

  return (
    <div className="container py-3">
      <h2 className="text-center mb-4 fw-bold text-dark">Tìm bao đóng tập phụ thuộc hàm</h2>

      <TapPhuThuocHam
        tap_phu_thuoc_ham={tap_phu_thuoc_ham}
        actions={phuThuocHamActions}
        thong_bao={thongBaoPhuThuocHam}
        onCloseThongBao={() => setThongBaoPhuThuocHam(null)}
      />

    </div>
  )
};

export default BaoDongTapPhuThuocHam;