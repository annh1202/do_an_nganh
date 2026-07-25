import React, { useState, useEffect } from 'react';
import TapThuocTinh from '../components/TapThuocTinh';
import TapPhuThuocHam from '../components/TapPhuThuocHam';
import ChonDangChuan from '../components/ChonDangChuan';

import { TaoTapThuocTinh } from "../actions/TaoTapThuocTinh";
import { TaoTapPhuThuocHam } from "../actions/TaoTapPhuThuocHam";
import { ChonDangChuanAction } from "../actions/ChonDangChuan";
import { StateActions } from "../actions/StateDangChuan";

import TapThuocTinhApi from "../api/TapThuocTinh"
import TapPhuThuocHamApi from "../api/TapPhuThuocHam"
import DangChuanApi from "../api/DangChuan"


const DangChuan = () => {
    const [tap_thuoc_tinh, setTapThuocTinh] = useState([]);
    const [tap_phu_thuoc_ham, setTapPhuThuocHam] = useState([]);
    const [dangChuan, setDangChuan] = useState("");

    const [loadingThuocTinh, setLoadingThuocTinh] = useState(false);
    const [loadingPhuThuocHam, setLoadingPhuThuocHam] = useState(false);

    const [thongBaoThuocTinh, setThongBaoThuocTinh] = useState(null);
    const [thongBaoPhuThuocHam, setThongBaoPhuThuocHam] = useState(null);
    const [thongBaoDangChuan, setThongBaoDangChuan] = useState(null);

    const thuocTinhApi = TapThuocTinhApi(
        "/dang-chuan"
    );

    const thuocTinhActions = TaoTapThuocTinh({
        api: thuocTinhApi,
        setTapThuocTinh,
        setLoading: setLoadingThuocTinh,
        setThongBao: setThongBaoThuocTinh,
    });

    const phuThuocHamApi = TapPhuThuocHamApi(
        "/dang-chuan"
    );

    const phuThuocHamActions = TaoTapPhuThuocHam({
        api: phuThuocHamApi,
        setTapPhuThuocHam,
        setLoading: setLoadingPhuThuocHam,
        setThongBao: setThongBaoPhuThuocHam,
    });

    const dangChuanApi = DangChuanApi("/dang-chuan");

    const dangChuanActions = ChonDangChuanAction({
        api: dangChuanApi,
        setDangChuan: setDangChuan,
        setThongBao: setThongBaoDangChuan,
    });

    const stateActions = StateActions({
        setTapThuocTinh,
        setTapPhuThuocHam,
        setDangChuan
    });

    useEffect(() => {
        stateActions.fetchState();
    }, []);

  return (
    <div className="container py-3">
      <h2 className="text-center mb-4 fw-bold text-dark">Nâng dạng chuẩn</h2>
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

       <ChonDangChuan
        dangChuan={dangChuan}
        setDangChuan={setDangChuan}
        actions={dangChuanActions}
        thong_bao={thongBaoDangChuan}
        onCloseThongBao={() => setThongBaoDangChuan(null)}
      />

    </div>
  )
};

export default DangChuan;