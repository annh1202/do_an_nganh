import React, { useState } from 'react';

// Nhận tập phụ thuộc hàm và các hàm hành động từ component cha
const TapPhuThuocHam = ({ tap_phu_thuoc_ham = [], them, xoa, xoa_trong }) => {
  const [veTrai, setVeTrai] = useState('');
  const [vePhai, setVePhai] = useState('');

  // 1. Chỉ lấy dữ liệu từ ô input và gửi ra ngoài để xử lý
  const chon_them = (e) => {
    e.preventDefault();
    const vt = veTrai.trim().toUpperCase();
    const vp = vePhai.trim().toUpperCase();
    if (vt && vp && them) {
      them({ ve_trai: vt, ve_phai: vp }); // Gửi object chứa vế trái (ve_trai) và vế phải (ve_phai) ra ngoài
      setVeTrai('');              // Reset ô nhập liệu
      setVePhai('');
    }
  };

  // 2. Chỉ gửi phụ thuộc hàm cần xóa ra ngoài
  const chon_xoa = (e) => {
    e.preventDefault();
    const vt = veTrai.trim().toUpperCase();
    const vp = vePhai.trim().toUpperCase();
    if (vt && vp && xoa) {
      xoa({ ve_trai: vt, ve_phai: vp });
      setVeTrai('');
      setVePhai('');
    }
  };

  // 3. Gọi hàm xóa trống từ bên ngoài
  const chon_xoa_trong = (e) => {
    e.preventDefault();
    if (xoa_trong) {
      xoa_trong();
    }
  };

  return (
    <div className="container mt-4">
      <form id="fd_form">
        {/* Đồng bộ: Sử dụng row mb-4 p-3 border rounded bg-light */}
        <div className="row mb-4 p-3 border rounded bg-light">

          {/* Cột trái: Nhập liệu và các nút chức năng */}
          <div className="col-md-5">
            <h5 className="fw-bold mb-3">Tạo tập phụ thuộc hàm F</h5>

            {/* Ô nhập liệu vế trái & vế phải xếp ngang */}
            <div className="d-flex align-items-center gap-2 mb-2">
              <input
                type="text"
                className="form-control"
                placeholder="Thuộc tính trái (VD: AB)"
                autoComplete="off"
                value={veTrai}
                onChange={(e) => setVeTrai(e.target.value)}
              />
              <span className="text-secondary fw-bold">→</span>
              <input
                type="text"
                className="form-control"
                placeholder="Thuộc tính phải (VD: C)"
                autoComplete="off"
                value={vePhai}
                onChange={(e) => setVePhai(e.target.value)}
              />
            </div>

            {/* Hàng nút Thêm / Xóa */}
            <div className="row g-2 mb-2">
              <div className="col-md-6">
                <button
                  type="button"
                  className="btn btn-success w-100"
                  onClick={chon_them}
                >
                  Thêm
                </button>
              </div>
              <div className="col-md-6">
                <button
                  type="button"
                  className="btn btn-danger w-100"
                  onClick={chon_xoa}
                >
                  Xoá
                </button>
              </div>
            </div>

            {/* Nút Xóa trống */}
            <button
              type="button"
              className="btn btn-secondary w-100"
              onClick={chon_xoa_trong}
            >
              Xoá trống
            </button>
          </div>

          {/* Cột phải: Chỉ hiển thị dữ liệu nhận được */}
          <div className="col-md-7">
            <h5 className="fw-bold mb-3">Tập phụ thuộc hàm</h5>
            <div className="border border-secondary p-3 fs-5 mb-2 bg-white rounded" id="fd_set">
              <strong>F = </strong>
              {tap_phu_thuoc_ham.length > 0 ? (
                <span>
                  {"{ "}
                  {tap_phu_thuoc_ham.map((fd, index) => (
                    <span key={index}>
                      {fd.ve_trai} → {fd.ve_phai}
                      {index < tap_phu_thuoc_ham.length - 1 ? ', ' : ''}
                    </span>
                  ))}
                  {" }"}
                </span>
              ) : (
                <span className="text-muted">∅</span>
              )}
            </div>
          </div>

        </div>
      </form>
    </div>
  );
};

export default TapPhuThuocHam;