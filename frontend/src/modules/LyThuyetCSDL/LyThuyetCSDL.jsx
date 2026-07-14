import React from 'react';
// 1. Thêm Routes và Route từ react-router-dom vào đây
import { Routes, Route, useParams } from 'react-router-dom';
import DanhSachChucNang from '@/components/DanhSachChucNang';
import './LyThuyetCSDL.css';
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
  const { baiHocId } = useParams(); // Bây giờ useParams đã hoạt động vì nằm trong <Route path=":baiHocId" />

  const ComponentHienThi = serviceComponentMap[baiHocId] || (
    <p>Nội dung bài học đang được biên soạn hoặc chưa tồn tại...</p>
  );

  return <div className="article-body">{ComponentHienThi}</div>;
};

export default function LyThuyetCSDL() {
  const menuItems = [
    { id: 'gioi-thieu', label: '1. Giới thiệu nhóm chức năng' },
    { id: 'bao-dong-tap-thuoc-tinh', label: '2. Tìm bao đóng tập thuộc tính' },
    { id: 'bao-dong-tap-phu-thuoc-ham', label: '3. Tìm bao đóng tập phụ thuộc hàm' },
    { id: 'khoa-ung-vien', label: '4. Tìm khóa ứng viên' },
    { id: 'dang-chuan', label: '5. Nâng dạng chuẩn CSDL' },
  ];

  return (
    <div className="theory-container">
      <DanhSachChucNang
        menuItems={menuItems}
        title="Lý thuyết CSDL"
        basePath="/ly-thuyet-csdl"
      />

      <section className="theory-content">
        {/* 2. Dùng bộ Routes để bọc lại, thay cho câu lệnh kiểm tra useParams() cũ */}
        <Routes>
          {/* Đường dẫn mặc định khi URL là /ly-thuyet-csdl */}
          <Route index element={<p>Chọn một bài học bên trái để bắt đầu đọc lý thuyết.</p>} />

          {/* Đường dẫn động khi có bài học con, ví dụ: /ly-thuyet-csdl/bao-dong-tap-thuoc-tinh */}
          <Route path=":baiHocId" element={<ChiTietBaiHoc />} />
        </Routes>
      </section>
    </div>
  );
}