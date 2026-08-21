import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import { CauHinhRoute } from './CauHinhRoute';

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
            <div className="d-flex flex-column min-vh-100 bg-light">
                <Header />
                <main className="flex-grow-1 w-100">
                    <Routes>
                        {CauHinhRoute.map(route => (
                            <Route
                                key={route.path}
                                path={route.isNested ? `${route.path}/*` : route.path}
                                element={route.element}
                            />
                        ))}


                        <Route path="*" element={<NotFound />} />
                    </Routes>
                </main>
            </div>
        </BrowserRouter>
    );
};

export default App;