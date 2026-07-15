import React, { useState } from 'react';


// Nhận tập thuộc tính và các hàm hành động từ component cha (hoặc từ API controller)
const TapThuocTinh = ({ tap_thuoc_tinh = [], them, xoa, xoa_trong }) => {
  const [thuoc_tinh, set_tap_thuoc_tinh] = useState('');

  // 1. Chỉ lấy dữ liệu từ ô input và gửi ra ngoài để xử lý
  const chon_them = (e) => {
    e.preventDefault();
    const formattedInput = thuoc_tinh.trim().toUpperCase();
    if (formattedInput && them) {
      them(formattedInput); // Gọi hàm thêm từ bên ngoài truyền vào
      set_tap_thuoc_tinh('');     // Reset ô nhập liệu
    }
  };

  // 2. Chỉ gửi thuộc tính cần xóa ra ngoài
  const chon_xoa= (e) => {
    e.preventDefault();
    const formattedInput = thuoc_tinh.trim().toUpperCase();
    if (formattedInput && xoa) {
      xoa(formattedInput); // Gọi hàm xóa từ bên ngoài
      set_tap_thuoc_tinh('');
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
      <form id="attr_form">
        <div className="row mb-4 p-3 border rounded bg-light">
          {/* Cột trái: Nhập liệu và các nút chức năng */}
          <div className="col-md-5">
            <h5 className="fw-bold mb-3">Tạo tập thuộc tính gốc R</h5>

            <input
              id="attribute_input"
              type="text"
              className="form-control mb-2"
              placeholder="Nhập một thuộc tính (VD: A)"
              autoComplete="off"
              value={thuoc_tinh}
              onChange={(e) => set_tap_thuoc_tinh(e.target.value)}
            />

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
            <h5 className="fw-bold mb-3">Tập thuộc tính</h5>
            <div className="border border-secondary p-3 fs-5 mb-2 bg-white rounded" id="attr_set">
              <strong>R = </strong>
              {tap_thuoc_tinh.length > 0 ? (
                <span>{`{ ${tap_thuoc_tinh.join(', ')} }`}</span>
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

export default TapThuocTinh;