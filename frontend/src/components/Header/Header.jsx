import React from 'react';
import { Link, NavLink } from 'react-router-dom';
import { RouteConfig } from '@/RouteConfig';
import './Header.css';

export default function Header() {
  return (
    <nav className="main-header">
      {/* KHỐI BÊN TRÁI: GỒM LOGO VÀ MENU CHỨC NĂNG TỰ ĐỘNG */}
      <div className="header-left">
        {/* LOGO */}
        <div className="header-logo">
          <Link to="/">DataLogic</Link>
        </div>

        {/* MENU TỰ ĐỘNG GENERATE */}
        <div className="header-menu">
          {RouteConfig
            .filter(route => route.showInMenu)
            .map(route => (
              <NavLink
                key={route.path}
                to={route.path}
                // Thêm thuộc tính end cho đường dẫn trang chủ '/' để tránh trùng active với các trang con
                end={route.path === '/'}
                className={({ isActive }) => `header-link ${isActive ? 'active' : ''}`}
              >
                {route.label}
              </NavLink>
            ))
          }
        </div>
      </div>

      {/* KHỐI BÊN PHẢI: CHỪA CHỖ CHO ĐĂNG KÝ / ĐĂNG NHẬP */}
      <div className="header-auth">
        <Link to="/login" className="btn-login">
          Đăng nhập
        </Link>
        <Link to="/register" className="btn-register">
          Đăng ký
        </Link>
      </div>
    </nav>
  );
}