import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Login from './modules/XacThuc/Login';
import Register from './modules/XacThuc/Register';
import { RouteConfig } from './RouteConfig';

const NotFound = () => (
  <div className="container py-5">
    <div className="alert alert-danger text-center shadow-sm" role="alert">
      <h2 className="alert-heading fw-bold">404 - Không tìm thấy trang</h2>
      <p className="mb-0">Đường dẫn bạn truy cập không tồn tại hoặc đã bị thay đổi.</p>
    </div>
  </div>
);

const App = () => {
  return (
    <BrowserRouter>
      {/*
        - d-flex flex-column min-vh-100: Tạo layout flex dọc, chiều cao tối thiểu bằng 100% màn hình.
        - bg-light: Đổi nền tổng thể sang màu xám nhạt nhẹ nhàng, làm nổi bật các Card màu trắng lên.
      */}
      <div className="d-flex flex-column min-vh-100 bg-light">
        {/* Header ôm sát lề, tràn 100% chiều ngang */}
        <Header />

        {/*
          - flex-grow-1: Cho phép phần main chiếm hết không gian còn lại của màn hình.
          - w-100: Đảm bảo phần main luôn rộng tối đa 100% màn hình (full-width).
        */}
        <main className="flex-grow-1 w-100">
          <Routes>
            {/* TỰ ĐỘNG GENERATE CÁC ROUTE CHÍNH TỪ ROUTE CONFIG */}
            {RouteConfig.map(route => (
              <Route
                key={route.path}
                path={route.isNested ? `${route.path}/*` : route.path}
                element={route.element}
              />
            ))}

            {/* Các Tuyến đường cố định của hệ thống */}
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />

            {/* Trang lỗi */}
            <Route path="*" element={<NotFound />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  );
};

export default App;