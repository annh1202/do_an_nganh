import React, { useState, useEffect } from 'react';
import TapThuocTinh from '../components/TapThuocTinh';
import TapPhuThuocHam from '../components/TapPhuThuocHam';
import TapThuocTinhCanTim from '../components/TapThuocTinhCanTim';
import { TaoTapThuocTinh } from "../actions/TaoTapThuocTinh";
import { TaoTapPhuThuocHam } from "../actions/TaoTapPhuThuocHam";
import { TaoTapThuocTinhCanTim } from "../actions/TaoTapThuocTinhCanTim";
import TapThuocTinhApi from "../api/TapThuocTinh"
import TapPhuThuocHamApi from "../api/TapPhuThuocHam"
import TapThuocTinhCanTimApi from "../api/TapThuocTinhCanTim"
import { StateActions } from "../actions/State";

const BaoDongTapThuocTinh = () => {
    const [tap_thuoc_tinh, setTapThuocTinh] = useState([]);
    const [tap_phu_thuoc_ham, setTapPhuThuocHam] = useState([]);
    const [tap_thuoc_tinh_can_tim, setTapThuocTinhCanTim] = useState([]);

    const [loadingThuocTinh, setLoadingThuocTinh] = useState(false);
    const [loadingPhuThuocHam, setLoadingPhuThuocHam] = useState(false);
    const [loadingThuocTinhCanTim, setLoadingThuocTinhCanTim] = useState(false);

    const [thongBaoThuocTinh, setThongBaoThuocTinh] = useState(null);
    const [thongBaoPhuThuocHam, setThongBaoPhuThuocHam] = useState(null);
    const [thongBaoThuocTinhCanTim, setThongBaoThuocTinhCanTim] = useState(null);

    const thuocTinhApi = TapThuocTinhApi(
        "/bao-dong-tap-thuoc-tinh"
    );

    const thuocTinhActions = TaoTapThuocTinh({
        api: thuocTinhApi,
        setTapThuocTinh,
        setLoading: setLoadingThuocTinh,
        setThongBao: setThongBaoThuocTinh,
    });

    const phuThuocHamApi = TapPhuThuocHamApi(
        "/bao-dong-tap-thuoc-tinh"
    );

    const phuThuocHamActions = TaoTapPhuThuocHam({
        api: phuThuocHamApi,
        setTapPhuThuocHam,
        setLoading: setLoadingPhuThuocHam,
        setThongBao: setThongBaoPhuThuocHam,
    });

    const thuocTinhCanTimApi = TapThuocTinhCanTimApi(
        "/bao-dong-tap-thuoc-tinh"
    );

    const thuocTinhCanTimActions = TaoTapThuocTinhCanTim({
        api: thuocTinhCanTimApi,
        setTapThuocTinhCanTim,
        setLoading: setLoadingThuocTinhCanTim,
        setThongBao: setThongBaoThuocTinhCanTim,
    });

    const stateActions = StateActions({
        setTapThuocTinh,
        setTapPhuThuocHam,
        setTapThuocTinhCanTim
    });

    useEffect(() => {
        stateActions.fetchState();
    }, []);

  return (
    <div className="container py-3">
      <h2 className="text-center mb-4 fw-bold text-dark">Tìm bao đóng tập thuộc tính</h2>
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
       <TapThuocTinhCanTim
         tap_thuoc_tinh_can_tim={tap_thuoc_tinh_can_tim}
         actions={thuocTinhCanTimActions}
         thong_bao={thongBaoThuocTinhCanTim}
         onCloseThongBao={() => setThongBaoThuocTinhCanTim(null)}
       />
    </div>
  )
};

export default BaoDongTapThuocTinh;