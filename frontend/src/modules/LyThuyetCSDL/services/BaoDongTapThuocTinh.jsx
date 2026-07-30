import React, { useState, useEffect, useRef } from "react";
import TapThuocTinh from '../components/TapThuocTinh';
import TapPhuThuocHam from '../components/TapPhuThuocHam';
import TapThuocTinhCanTim from '../components/TapThuocTinhCanTim';
import DeBai from "../components/DeBai";

import { TaoTapThuocTinh } from "../actions/TaoTapThuocTinh";
import { TaoTapPhuThuocHam } from "../actions/TaoTapPhuThuocHam";
import { TaoTapThuocTinhCanTim } from "../actions/TaoTapThuocTinhCanTim";

import TapThuocTinhApi from "../api/TapThuocTinh";
import TapPhuThuocHamApi from "../api/TapPhuThuocHam";
import TapThuocTinhCanTimApi from "../api/TapThuocTinhCanTim";
import TrangThaiApi from "../api/TrangThai";
import ChucNangChinhApi from "../api/ChucNangChinh";

const BaoDongTapThuocTinh = () => {
    const [tapThuocTinh, setTapThuocTinh] = useState([]);
    const [tapPhuThuocHam, setTapPhuThuocHam] = useState([]);
    const [tapThuocTinhCanTim, setTapThuocTinhCanTim] = useState([]);

    const [loadingThuocTinh, setLoadingThuocTinh] = useState(false);
    const [loadingPhuThuocHam, setLoadingPhuThuocHam] = useState(false);
    const [loadingThuocTinhCanTim, setLoadingThuocTinhCanTim] = useState(false);

    const [thongBaoThuocTinh, setThongBaoThuocTinh] = useState(null);
    const [thongBaoPhuThuocHam, setThongBaoPhuThuocHam] = useState(null);
    const [thongBaoThuocTinhCanTim, setThongBaoThuocTinhCanTim] = useState(null);

    // State thông báo cho Đề Bài
    const [thongBaoDeBai, setThongBaoDeBai] = useState(null);

    const thuocTinhApi = TapThuocTinhApi("/bao-dong-tap-thuoc-tinh");
    const thuocTinhActions = TaoTapThuocTinh({
        api: thuocTinhApi,
        setTapThuocTinh,
        setLoading: setLoadingThuocTinh,
        setThongBao: setThongBaoThuocTinh,
    });

    const phuThuocHamApi = TapPhuThuocHamApi("/bao-dong-tap-thuoc-tinh");
    const phuThuocHamActions = TaoTapPhuThuocHam({
        api: phuThuocHamApi,
        setTapPhuThuocHam,
        setLoading: setLoadingPhuThuocHam,
        setThongBao: setThongBaoPhuThuocHam,
    });

    const thuocTinhCanTimApi = TapThuocTinhCanTimApi("/bao-dong-tap-thuoc-tinh");
    const thuocTinhCanTimActions = TaoTapThuocTinhCanTim({
        api: thuocTinhCanTimApi,
        setTapThuocTinhCanTim,
        setLoading: setLoadingThuocTinhCanTim,
        setThongBao: setThongBaoThuocTinhCanTim,
    });

    const chucNangApi = ChucNangChinhApi("/bao-dong-tap-thuoc-tinh");

    // 1. HÀM TẠO ĐỀ BÀI NGẪU NHIÊN
    const chonTaoDeBaiNgauNhien = async () => {
        try {
            setThongBaoDeBai(null);
            const response = await chucNangApi.taoDeBaiNgauNhien();
            const doiTuong = response?.data?.doi_tuong;

            if (doiTuong) {
                setTapThuocTinh(doiTuong.tap_thuoc_tinh || []);
                setTapPhuThuocHam(doiTuong.tap_phu_thuoc_ham || []);
                setTapThuocTinhCanTim(doiTuong.tap_thuoc_tinh_can_tim || []);

                setThongBaoDeBai({
                    loai_thong_bao: "success",
                    noi_dung: "Đã tạo đề bài ngẫu nhiên thành công!"
                });
            }
        } catch (err) {
            console.error("Lỗi khi tạo đề ngẫu nhiên:", err);
            setThongBaoDeBai({
                loai_thong_bao: "danger",
                noi_dung: "Không thể tạo đề bài ngẫu nhiên!"
            });
        }
    };

    // 2. HÀM TẢI VỀ
    const chonTaiVe = () => {
        try {
            const duLieuDuocTaiVe = {
                tap_thuoc_tinh: tapThuocTinh,
                tap_phu_thuoc_ham: tapPhuThuocHam,
                tap_thuoc_tinh_can_tim: tapThuocTinhCanTim
            };

            const jsonString = JSON.stringify(duLieuDuocTaiVe, null, 2);
            const blob = new Blob([jsonString], { type: "application/json" });
            const url = URL.createObjectURL(blob);

            const link = document.createElement("a");
            link.href = url;
            link.download = `bao_dong_tap_thuoc_tinh_${Date.now()}.json`;
            document.body.appendChild(link);
            link.click();

            document.body.removeChild(link);
            URL.revokeObjectURL(url);

            setThongBaoDeBai({
                loai_thong_bao: "success",
                noi_dung: "Đã tải file đề bài thành công!"
            });
        } catch (err) {
            setThongBaoDeBai({
                loai_thong_bao: "danger",
                noi_dung: "Lỗi khi xuất file đề bài!"
            });
        }
    };

    // 3. HÀM NẠP ĐỀ LÊN
    const chonTaiLen = (event) => {
        const file = event.target.files[0];
        if (!file) return;

        const reader = new FileReader();

        reader.onload = async (e) => {
            try {
                setThongBaoDeBai(null);
                const parsedData = JSON.parse(e.target.result);

                if (
                    Array.isArray(parsedData.tap_thuoc_tinh) &&
                    Array.isArray(parsedData.tap_phu_thuoc_ham) &&
                    Array.isArray(parsedData.tap_thuoc_tinh_can_tim)
                ) {
                    const response = await chucNangApi.taiLen(parsedData);
                    const doiTuong = response?.data?.doi_tuong || parsedData;

                    setTapThuocTinh(doiTuong.tap_thuoc_tinh || []);
                    setTapPhuThuocHam(doiTuong.tap_phu_thuoc_ham || []);
                    setTapThuocTinhCanTim(doiTuong.tap_thuoc_tinh_can_tim || []);

                    setThongBaoThuocTinh(null);
                    setThongBaoPhuThuocHam(null);
                    setThongBaoThuocTinhCanTim(null);

                    setThongBaoDeBai({
                        loai_thong_bao: "success",
                        noi_dung: "Tải đề bài lên hệ thống thành công!"
                    });
                } else {
                    setThongBaoDeBai({
                        loai_thong_bao: "warning",
                        noi_dung: "File JSON không đúng cấu trúc đề bài!"
                    });
                }
            } catch (err) {
                console.error("Lỗi khi tải đề bài lên:", err);
                setThongBaoDeBai({
                    loai_thong_bao: "danger",
                    noi_dung: "Không thể nạp đề bài lên hệ thống!"
                });
            } finally {
                event.target.value = "";
            }
        };

        reader.readAsText(file);
    };

    // 4. HÀM GIẢI ĐỀ
    const chonGiai = async () => {
        try {
            setThongBaoDeBai(null);
            const response = await chucNangApi.giaiDe();
            const ketQua = response?.data?.ket_qua;

            console.log("Kết quả lời giải:", ketQua);
            setThongBaoDeBai({
                loai_thong_bao: "success",
                noi_dung: "Đã giải đề bài thành công!"
            });
        } catch (err) {
            console.error("Lỗi khi giải đề:", err);
            setThongBaoDeBai({
                loai_thong_bao: "danger",
                noi_dung: "Không thể thực hiện giải đề!"
            });
        }
    };

    const fileInputRef = useRef(null);

    useEffect(() => {
        const fetchState = async () => {
            try {
                const response = await TrangThaiApi.fetchTrangThaiBaoDongTapThuocTinh();
                const doiTuong = response?.data?.doi_tuong;

                if (doiTuong) {
                    setTapThuocTinh(doiTuong.tap_thuoc_tinh || []);
                    setTapPhuThuocHam(doiTuong.tap_phu_thuoc_ham || []);
                    setTapThuocTinhCanTim(doiTuong.tap_thuoc_tinh_can_tim || []);
                }
            } catch (err) {
                console.error("Lỗi khi lấy state:", err);
            }
        };

        fetchState();
    }, []);

    return (
        <div className="container py-3">
            <h2 className="text-center mb-4 fw-bold text-dark">Tìm bao đóng tập thuộc tính</h2>
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
            <TapThuocTinhCanTim
                tapThuocTinhCanTim={tapThuocTinhCanTim}
                actions={thuocTinhCanTimActions}
                thongBao={thongBaoThuocTinhCanTim}
                onCloseThongBao={() => setThongBaoThuocTinhCanTim(null)}
            />

            <DeBai
                tapThuocTinh={tapThuocTinh}
                tapPhuThuocHam={tapPhuThuocHam}
                tapThuocTinhCanTim={tapThuocTinhCanTim}
                chonTaoDeBaiNgauNhien={chonTaoDeBaiNgauNhien}
                chonTaiVe={chonTaiVe}
                chonTaiLen={chonTaiLen}
                chonGiai={chonGiai}
                fileInputRef={fileInputRef}
                thongBao={thongBaoDeBai}
                onCloseThongBao={() => setThongBaoDeBai(null)}
            />
        </div>
    );
};

export default BaoDongTapThuocTinh;