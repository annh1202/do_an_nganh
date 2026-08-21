import React from 'react';
import { NavLink } from 'react-router-dom';

const DanhSachChucNang = ({ title = "Danh mục", cacChucNang = [] }) => {
    return (
        <aside className="card shadow-sm border-0 mb-4">
            {/* Tiêu đề thanh danh mục */}
            <div className="card-header bg-dark text-primary fw-bold py-3 fs-6">
                {title}
            </div>

            <div className="list-group list-group-flush">
                {cacChucNang.map((item) => (
                    <NavLink
                        key={item.id}
                        to={`/ly-thuyet-csdl/${item.id}`}
                        className={({ isActive }) =>
                          `list-group-item list-group-item-action py-2.5 px-3 fw-medium transition-all ${
                            isActive ? 'active bg-primary border-primary' : 'text-secondary'
                          }`
                        }
                    >
                        {item.label}
                    </NavLink>
                ))}
            </div>
        </aside>
    );
};

export default DanhSachChucNang;