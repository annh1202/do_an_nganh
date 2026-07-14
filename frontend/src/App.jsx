import React from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Header from './components/Header'
import Login from './modules/XacThuc/Login'
import Register from './modules/XacThuc/Register'
import { RouteConfig } from './RouteConfig';
import './App.css';

const NotFound = () => (
  <div style={{ padding: '20px' }}>
    <h2 style={{ textAlign: 'left' }}>404 - Không tìm thấy trang</h2>
  </div>
);

export default function App() {
  return (
    <BrowserRouter>
      <div className="app-container">
        <Header />

        <main>
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
}