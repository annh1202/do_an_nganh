import React from 'react';
import { Link, NavLink } from 'react-router-dom';
import { CauHinhRoute } from '../CauHinhRoute';

const Header = () => {
    return (
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark px-4 shadow-sm">
            <div className="container-fluid">

                {/* LOGO */}
                <Link
                    className="navbar-brand fw-bold text-primary fs-4 me-4"
                    to="/"
                >
                    DataLogic
                </Link>

                {/* Nút Hamburger cho giao diện điện thoại */}
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

                {/* MENU */}
                <div className="collapse navbar-collapse" id="navbarNav">
                    <ul className="navbar-nav me-auto mb-2 mb-lg-0 gap-2">
                        {CauHinhRoute
                            .filter(route => route.showInMenu)
                            .map(route => (
                                <li className="nav-item" key={route.path}>
                                    <NavLink
                                        to={route.path}
                                        end={route.path === '/'}
                                        className={({ isActive }) =>
                                            `nav-link fw-semibold px-3 ${
                                                isActive
                                                    ? 'active text-primary border-bottom border-primary'
                                                    : ''
                                            }`
                                        }
                                    >
                                        {route.label}
                                    </NavLink>
                                </li>
                            ))
                        }
                    </ul>
                </div>
            </div>
        </nav>
    );
};

export default Header;