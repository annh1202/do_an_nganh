import React, { useEffect, useState } from 'react';
import { Routes, Route, useParams } from 'react-router-dom';

import DanhSachChucNang from '../../components/DanhSachChucNang';
import GioiThieu from './services/GioiThieu';
import BaoDongTapThuocTinh from './services/BaoDongTapThuocTinh';
import BaoDongTapPhuThuocHam from './services/BaoDongTapPhuThuocHam';
import KhoaUngVien from './services/KhoaUngVien';
import DangChuan from './services/DangChuan';

import TrangThaiApi from './api/TrangThai';


const serviceComponentMap = {
    'gioi-thieu': <GioiThieu />,
    'bao-dong-tap-thuoc-tinh': <BaoDongTapThuocTinh />,
    'bao-dong-tap-phu-thuoc-ham': <BaoDongTapPhuThuocHam />,
    'khoa-ung-vien': <KhoaUngVien />,
    'dang-chuan': <DangChuan />,
};


const ChiTietBaiHoc = () => {
    const { baiHocId } = useParams();

    const ComponentHienThi = serviceComponentMap[baiHocId] || (
        <div className="alert alert-warning" role="alert">
            Nội dung bài học đang được biên soạn hoặc chưa tồn tại...
        </div>
    );

    return <div className="p-1">{ComponentHienThi}</div>;
};


const LyThuyetCSDL = () => {
    const [cacChucNang, setCacChucNang] = useState([]);

    useEffect(() => {
        const layTrangThai = async () => {
            try {
                const response = await TrangThaiApi.fetchTrangThai();

                setCacChucNang(response.data.cau_hinh);
            } catch (error) {
                console.error(
                    'Không thể lấy cấu hình module Lý thuyết CSDL:',
                    error
                );
            }
        };

        layTrangThai();
    }, []);

    return (
        <div className="container-fluid py-4">
            <div className="row g-4">

                <div className="col-md-3">
                    <DanhSachChucNang
                        cacChucNang={cacChucNang}
                        title="Lý thuyết CSDL"
                        basePath="/ly-thuyet-csdl"
                    />
                </div>

                <div className="col-md-9">
                    <section
                        className="card shadow-sm p-4 bg-white rounded"
                        style={{ minHeight: '400px' }}
                    >
                        <Routes>

                            <Route
                                index
                                element={
                                    <div
                                        className="d-flex flex-column justify-content-center align-items-center text-center py-5"
                                        style={{ minHeight: '65vh' }}
                                    >
                                        <div className="mb-4">
                                            <i
                                                className="bi bi-journal-bookmark-fill text-primary"
                                                style={{ fontSize: '5rem' }}
                                            ></i>
                                        </div>

                                        <h2 className="fw-bold text-primary mb-3">
                                            Chào mừng đến với Module Lý
                                            thuyết Cơ sở dữ liệu
                                        </h2>

                                        <p
                                            className="text-muted fs-5 mb-4"
                                            style={{ maxWidth: '800px' }}
                                        >
                                            Module cung cấp các công cụ hỗ trợ
                                            học tập như tìm bao đóng tập thuộc
                                            tính, bao đóng tập phụ thuộc hàm,
                                            tìm khóa ứng viên và chuẩn hóa
                                            lược đồ quan hệ.
                                        </p>

                                        <div className="alert alert-light border shadow-sm px-4 py-3">
                                            <i className="bi bi-arrow-left-circle-fill text-primary me-2"></i>

                                            <span>
                                                Vui lòng chọn một{' '}
                                                <strong>bài học</strong> trong
                                                danh mục bên trái để bắt đầu.
                                            </span>
                                        </div>
                                    </div>
                                }
                            />

                            <Route
                                path=":baiHocId"
                                element={<ChiTietBaiHoc />}
                            />

                        </Routes>
                    </section>
                </div>

            </div>
        </div>
    );
};


export default LyThuyetCSDL;