import React from 'react';
import { Routes, Route, useParams } from 'react-router-dom';
import DanhSachChucNang from '../../components/DanhSachChucNang';
import GioiThieu from './services/GioiThieu';
import BaoDongTapThuocTinh from './services/BaoDongTapThuocTinh';
import BaoDongTapPhuThuocHam from './services/BaoDongTapPhuThuocHam';
import KhoaUngVien from './services/KhoaUngVien';
import DangChuan from './services/DangChuan';

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
  const menuItems = [
    { id: 'gioi-thieu', label: '1. Giới thiệu nhóm chức năng' },
    { id: 'bao-dong-tap-thuoc-tinh', label: '2. Tìm bao đóng tập thuộc tính' },
    { id: 'bao-dong-tap-phu-thuoc-ham', label: '3. Tìm bao đóng tập phụ thuộc ham' },
    { id: 'khoa-ung-vien', label: '4. Tìm khóa ứng viên' },
    { id: 'dang-chuan', label: '5. Nâng dạng chuẩn CSDL' },
  ];

  return (
    // Thay "container" thành "container-fluid px-4" để tràn viền và giữ lề nhẹ hai bên cực đẹp
    <div className="container-fluid py-4">
      {/* Sử dụng Grid của Bootstrap để chia cột */}
      <div className="row g-4">
        {/* Cột trái: Chiếm 3/12 cột */}
        <div className="col-md-3">
          <DanhSachChucNang
            menuItems={menuItems}
            title="Lý thuyết CSDL"
            basePath="/ly-thuyet-csdl"
          />
        </div>

        {/* Cột phải: Chiếm 9/12 cột chứa nội dung chi tiết */}
        <div className="col-md-9">
          <section className="card shadow-sm p-4 bg-white rounded" style={{ minHeight: '400px' }}>
            <Routes>
              {/* Đường dẫn mặc định khi chưa chọn bài học */}
              <Route
                index
                element={
                  <div className="text-center py-5 text-muted">
                    <i className="bi bi-arrow-left-circle fs-1 d-block mb-3 text-secondary"></i>
                    <p className="fs-5">Vui lòng chọn một bài học ở danh mục bên trái để bắt đầu.</p>
                  </div>
                }
              />

              {/* Đường dẫn động chi tiết bài học */}
              <Route path=":baiHocId" element={<ChiTietBaiHoc />} />
            </Routes>
          </section>
        </div>
      </div>
    </div>
  );
};

export default LyThuyetCSDL;