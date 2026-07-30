import React, { useState, useEffect } from 'react';
import TapThuocTinh from '../components/TapThuocTinh';
import TapPhuThuocHam from '../components/TapPhuThuocHam';
import ChonDangChuan from '../components/ChonDangChuan';

import { TaoTapThuocTinh } from "../actions/TaoTapThuocTinh";
import { TaoTapPhuThuocHam } from "../actions/TaoTapPhuThuocHam";
import { ChonDangChuanAction } from "../actions/ChonDangChuan";

import TapThuocTinhApi from "../api/TapThuocTinh"
import TapPhuThuocHamApi from "../api/TapPhuThuocHam"
import DangChuanApi from "../api/DangChuan"
import TrangThaiApi from "../api/TrangThai";


const DangChuan = () => {
    const [tapThuocTinh, setTapThuocTinh] = useState([]);
    const [tapPhuThuocHam, setTapPhuThuocHam] = useState([]);
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

    useEffect(() => {
        const fetchState = async () => {
            try {
                const response = await TrangThaiApi.fetchTrangThaiDangChuan();
                const doiTuong = response.data.doi_tuong;
                setTapThuocTinh(doiTuong.tap_thuoc_tinh);
                setTapPhuThuocHam(doiTuong.tap_phu_thuoc_ham);
                setDangChuan(doiTuong.dang_chuan)
            } catch (err) {
                console.error("Lỗi khi lấy state:",err);
            }
        };

        fetchState();
    }, []);

  return (
    <div className="container py-3">
      <h2 className="text-center mb-4 fw-bold text-dark">Nâng dạng chuẩn</h2>
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

       <ChonDangChuan
        dangChuan={dangChuan}
        setDangChuan={setDangChuan}
        actions={dangChuanActions}
        thongBao={thongBaoDangChuan}
        onCloseThongBao={() => setThongBaoDangChuan(null)}
      />

    </div>
  )
};

export default DangChuan;