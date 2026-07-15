import React from 'react';
import { Link, NavLink } from 'react-router-dom';
import { RouteConfig } from '../RouteConfig';

const Header = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark px-4 shadow-sm">
      <div className="container-fluid">
        {/* LOGO */}
        <Link className="navbar-brand fw-bold text-primary fs-4 me-4" to="/">
          DataLogic
        </Link>

        {/* Nút Hamburger cho giao diện điện thoại (Bootstrap tự xử lý) */}
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>

        {/* Khối menu collapse */}
        <div className="collapse navbar-collapse" id="navbarNav">
          {/* MENU TỰ ĐỘNG GENERATE (Khối bên trái) */}
          <ul className="navbar-nav me-auto mb-2 mb-lg-0 gap-2">
            {RouteConfig
              .filter(route => route.showInMenu)
              .map(route => (
                <li className="nav-item" key={route.path}>
                  <NavLink
                    to={route.path}
                    end={route.path === '/'}
                    className={({ isActive }) =>
                      `nav-link fw-semibold px-3 ${isActive ? 'active text-primary border-bottom border-primary' : ''}`
                    }
                  >
                    {route.label}
                  </NavLink>
                </li>
              ))
            }
          </ul>

          {/* KHỐI BÊN PHẢI: ĐĂNG NHẬP / ĐĂNG KÝ */}
          <div className="d-flex gap-2">
            <Link to="/login" className="btn btn-outline-light px-3 fw-semibold">
              Đăng nhập
            </Link>
            <Link to="/register" className="btn btn-primary px-3 fw-semibold">
              Đăng ký
            </Link>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Header;