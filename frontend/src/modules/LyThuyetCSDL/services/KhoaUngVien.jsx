import React, { useState, useEffect, useRef } from 'react';
import TapThuocTinh from '../components/TapThuocTinh';
import TapPhuThuocHam from '../components/TapPhuThuocHam';
import ThanhCongCu from "../components/ThanhCongCu";
import BaiGiai from "../components/BaiGiai";

import { TaoTapThuocTinh } from "../actions/TaoTapThuocTinh";
import { TaoTapPhuThuocHam } from "../actions/TaoTapPhuThuocHam";

import TapThuocTinhApi from "../api/TapThuocTinh"
import TapPhuThuocHamApi from "../api/TapPhuThuocHam"
import TrangThaiApi from "../api/TrangThai";
import ChucNangChinhApi from "../api/ChucNangChinh";

const BaoDongTapThuocTinh = () => {
    const [tapThuocTinh, setTapThuocTinh] = useState([]);
    const [tapPhuThuocHam, setTapPhuThuocHam] = useState([]);
    const [baiGiai, setBaiGiai] = useState(null);

    const [loadingThuocTinh, setLoadingThuocTinh] = useState(false);
    const [loadingPhuThuocHam, setLoadingPhuThuocHam] = useState(false);

    const [thongBaoThuocTinh, setThongBaoThuocTinh] = useState(null);
    const [thongBaoPhuThuocHam, setThongBaoPhuThuocHam] = useState(null);
    const [thongBaoDeBai, setThongBaoDeBai] = useState(null);


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

    const chucNangApi = ChucNangChinhApi("/khoa-ung-vien");

    // 1. HÀM TẠO ĐỀ BÀI NGẪU NHIÊN
    const chonTaoDeBaiNgauNhien = async () => {
        try {
            setBaiGiai(null);
            setThongBaoDeBai(null);
            const response = await chucNangApi.taoDeBaiNgauNhien();
            const doiTuong = response?.data?.doi_tuong;

            if (doiTuong) {
                setTapThuocTinh(doiTuong.tap_thuoc_tinh || []);
                setTapPhuThuocHam(doiTuong.tap_phu_thuoc_ham || []);

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
                tap_phu_thuoc_ham: tapPhuThuocHam
            };

            const jsonString = JSON.stringify(duLieuDuocTaiVe, null, 2);
            const blob = new Blob([jsonString], { type: "application/json" });
            const url = URL.createObjectURL(blob);

            const link = document.createElement("a");
            link.href = url;
            link.download = `khoa_ung_vien_${Date.now()}.json`;
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
                setBaiGiai(null);
                setThongBaoDeBai(null);

                const parsedData = JSON.parse(e.target.result);

                // =========================================================
                // 1. KIỂM TRA CÁC TRƯỜNG BẮT BUỘC
                // =========================================================
                const truongBatBuoc = [
                    "tap_thuoc_tinh",
                    "tap_phu_thuoc_ham"
                ];

                const truongTrongFile = Object.keys(parsedData);

                // Trường bị thiếu
                const truongBiThieu = truongBatBuoc.filter(
                    (truong) => !truongTrongFile.includes(truong)
                );

                // Trường dư
                const truongBiDu = truongTrongFile.filter(
                    (truong) => !truongBatBuoc.includes(truong)
                );

                // Nếu thiếu trường
                if (truongBiThieu.length > 0) {
                    setThongBaoDeBai({
                        loai_thong_bao: "warning",
                        noi_dung:
                            `File bị thiếu trường bắt buộc: ${truongBiThieu.join(", ")}`
                    });

                    return;
                }

                // Nếu dư trường
                if (truongBiDu.length > 0) {
                    setThongBaoDeBai({
                        loai_thong_bao: "warning",
                        noi_dung:
                            `File chứa trường không hợp lệ: ${truongBiDu.join(", ")}`
                    });

                    return;
                }

                // =========================================================
                // 2. KIỂM TRA CẤU TRÚC tap_phu_thuoc_ham
                // =========================================================
                const tapPhuThuocHam = parsedData.tap_phu_thuoc_ham;

                if (!Array.isArray(tapPhuThuocHam)) {
                    setThongBaoDeBai({
                        loai_thong_bao: "warning",
                        noi_dung: "Trường tap_phu_thuoc_ham phải là một mảng!"
                    });

                    return;
                }

                const phuThuocHamKhongHopLe = tapPhuThuocHam.find(
                    (phuThuocHam) => {
                        if (
                            typeof phuThuocHam !== "object" ||
                            phuThuocHam === null ||
                            Array.isArray(phuThuocHam)
                        ) {
                            return true;
                        }

                        const truongPhuThuocHam =
                            Object.keys(phuThuocHam);

                        return !(
                            truongPhuThuocHam.length === 2 &&
                            truongPhuThuocHam.includes("ve_trai") &&
                            truongPhuThuocHam.includes("ve_phai")
                        );
                    }
                );

                if (phuThuocHamKhongHopLe) {
                    setThongBaoDeBai({
                        loai_thong_bao: "warning",
                        noi_dung:
                            "Cấu trúc của tap_phu_thuoc_ham không hợp lệ! " +
                            "Mỗi phụ thuộc hàm phải có đúng hai trường: ve_trai và ve_phai."
                    });

                    return;
                }

                // =========================================================
                // 3. GỌI API NẠP ĐỀ
                // =========================================================
                const response = await chucNangApi.taiLen(parsedData);

                const duLieuPhanHoi = response?.data;

                const loaiThongBao = duLieuPhanHoi?.loai_thong_bao;
                const thongBao = duLieuPhanHoi?.thong_bao;

                if (loaiThongBao === "success") {
                    const doiTuong = duLieuPhanHoi?.doi_tuong;

                    setTapThuocTinh(doiTuong?.tap_thuoc_tinh || []);
                    setTapPhuThuocHam(doiTuong?.tap_phu_thuoc_ham || []);

                    setThongBaoThuocTinh(null);
                    setThongBaoPhuThuocHam(null);

                    setThongBaoDeBai({
                        loai_thong_bao: "success",
                        noi_dung: thongBao || "Tải đề bài lên hệ thống thành công!"
                    });
                } else {
                    setThongBaoDeBai({
                        loai_thong_bao: loaiThongBao || "warning",
                        noi_dung: thongBao || "File không hợp lệ!"
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
            setBaiGiai(null);
            setThongBaoDeBai(null);

            const response = await chucNangApi.giaiDe();

            const doiTuong = response?.data?.doi_tuong;
            const loaiThongBao = response?.data?.loai_thong_bao;
            const thongBao = response?.data?.thong_bao;

            if (loaiThongBao === "success") {
                setBaiGiai(doiTuong);

                setThongBaoDeBai({
                    loai_thong_bao: "success",
                    noi_dung: thongBao
                });
            } else {
                setThongBaoDeBai({
                    loai_thong_bao: "warning",
                    noi_dung: thongBao
                });
            }

        } catch (err) {
            console.error(err);

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
            <div className="row mb-4 p-3 border">

                <h5 className="fw-bold mb-3">
                    Đề bài
                </h5>

                <p>
                    <strong>Cho lược đồ quan hệ:</strong>
                </p>

                <div className="border rounded p-3 mb-3 bg-light">
                    R = {tapThuocTinh.length > 0
                        ? `{ ${tapThuocTinh.join(", ")} }`
                        : "∅"}
                </div>

                <p>
                    <strong>Và tập phụ thuộc hàm:</strong>
                </p>

                <div className="border rounded p-3 mb-3 bg-light">
                    {tapPhuThuocHam.length > 0 ? (
                        <>
                            F = {"{ "}
                            {tapPhuThuocHam.map((phuThuocHam, index) => (
                                <span key={index}>
                                    {phuThuocHam.ve_trai} → {phuThuocHam.ve_phai}
                                    {index < tapPhuThuocHam.length - 1 ? ", " : ""}
                                </span>
                            ))}
                            {" }"}
                        </>
                    ) : (
                        <>F = ∅</>
                    )}
                </div>

                <p>
                    <strong>Hãy tìm các khóa ứng viên.</strong>
                </p>

                <ThanhCongCu
                    chonTaoDeBaiNgauNhien={chonTaoDeBaiNgauNhien}
                    chonTaiVe={chonTaiVe}
                    chonTaiLen={chonTaiLen}
                    chonGiai={chonGiai}
                    fileInputRef={fileInputRef}
                    thongBao={thongBaoDeBai}
                    onCloseThongBao={() => setThongBaoDeBai(null)}
                />
            </div>

            <BaiGiai baiGiai={baiGiai} />
        </div>
    )
};

export default BaoDongTapThuocTinh;