import React, { useState } from 'react';
import ThongBao from "./ThongBao";

// Nhận tập thuộc tính và các hàm hành động từ component cha (hoặc từ API controller)
const TapThuocTinh = ({
    tapThuocTinh = [],
    actions,
    thongBao,
    onCloseThongBao,
}) => {
    const [thuocTinh, setThuocTinh] = useState('');
    const { them, xoa, xoaTrong } = actions;

    const chonThem = async (e) => {
        e.preventDefault();

        const formattedInput = thuocTinh.trim().toUpperCase();

        if (!formattedInput) return;

        await them(formattedInput);

        setThuocTinh('');
    };

    const chonXoa = async (e) => {
        e.preventDefault();

        const formattedInput = thuocTinh.trim().toUpperCase();

        if (!formattedInput) return;

        await xoa(formattedInput);

        setThuocTinh('');
    };

    const chonXoaTrong = async (e) => {
        e.preventDefault();

        await xoaTrong();
    };

    return (
        <div className="container mt-4">
            <div className="row mb-4 p-3 border rounded bg-light">
                <div className="col-md-5">
                    <h5 className="fw-bold mb-3">Tạo tập thuộc tính gốc R</h5>
                    <input
                        type="text"
                        className="form-control mb-2"
                        placeholder="Nhập một thuộc tính (VD: A)"
                        autoComplete="off"
                        value={thuocTinh}
                        onChange={(e) => setThuocTinh(e.target.value)}
                    />

                    <div className="row g-2 mb-2">
                        <div className="col-md-6">
                            <button
                                className="btn btn-success w-100"
                                onClick={chonThem}
                            >
                            Thêm
                            </button>
                        </div>
                        <div className="col-md-6">
                            <button
                                className="btn btn-danger w-100"
                                onClick={chonXoa}
                            >
                            Xoá
                            </button>
                        </div>
                    </div>

                    <button
                        className="btn btn-secondary w-100"
                        onClick={chonXoaTrong}
                    >
                    Xoá trống
                    </button>
                </div>
                <div className="col-md-7">
                    <h5 className="fw-bold mb-3">Tập thuộc tính</h5>
                    <div className="border border-secondary p-3 fs-5 mb-2 bg-white rounded">
                        <strong>R = </strong>
                        {tapThuocTinh.length > 0 ? (
                        <span>{`{ ${tapThuocTinh.join(", ")} }`}</span>
                        ) : (
                        <span className="text-muted">∅</span>
                        )}
                    </div>

                    <ThongBao
                        thongBao={thongBao}
                        onClose={onCloseThongBao}
                    />
                </div>
            </div>
        </div>
    );
};

export default TapThuocTinh;