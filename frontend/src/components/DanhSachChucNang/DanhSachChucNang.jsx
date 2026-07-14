import React from 'react';
import { NavLink } from 'react-router-dom';
import './DanhSachChucNang.css'


// Sử dụng destructuring để lấy dữ liệu từ props truyền vào
export default function DanhSachChucNang({ title = "Danh mục", menuItems = [] }) {
  return (
    <aside className="service-sidebar">
      <div className="sidebar-title">{title}</div>
      {menuItems.map((item) => (
        <NavLink
          key={item.id}
          to={`/ly-thuyet-csdl/${item.id}`}
          className={({ isActive }) => `sidebar-link ${isActive ? 'active' : ''}`}
        >
          {item.label}
        </NavLink>
      ))}
    </aside>
  );
}