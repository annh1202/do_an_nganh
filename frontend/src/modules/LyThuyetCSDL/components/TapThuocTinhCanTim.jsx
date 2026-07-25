import React, { useState } from 'react';
import ThongBao from "./ThongBao";

// Nhận tập thuộc tính và các hàm hành động từ component cha (hoặc từ API controller)
const TapThuocTinhCanTim = ({
    tap_thuoc_tinh_can_tim = [],
    actions,
    thong_bao,
    onCloseThongBao,
}) => {
  const [thuoc_tinh_can_tim, set_tap_thuoc_tinh_can_tim] = useState('');
  const { them, xoa, xoaTrong } = actions;


  const chon_them = async (e) => {
    e.preventDefault();

    const formattedInput = thuoc_tinh_can_tim.trim().toUpperCase();

    if (!formattedInput) return;

    await them(formattedInput);

    set_tap_thuoc_tinh_can_tim('');
  };

  const chon_xoa = async (e) => {
    e.preventDefault();

    const formattedInput = thuoc_tinh_can_tim.trim().toUpperCase();

    if (!formattedInput) return;

    await xoa(formattedInput);

    set_tap_thuoc_tinh_can_tim('');
  };

  const chon_xoa_trong = async (e) => {
    e.preventDefault();

    await xoaTrong();
  };

  return (
    <div className="container mt-4">
      <form>
        <div className="row mb-4 p-3 border rounded bg-light">
          {/* Cột trái: Nhập liệu và các nút chức năng */}
          <div className="col-md-5">
            <h5 className="fw-bold mb-3">Tạo tập thuộc tính cần tìm X</h5>

            <input
              id="target_attribute_input"
              type="text"
              className="form-control mb-2"
              placeholder="Nhập một thuộc tính (VD: A)"
              autoComplete="off"
              value={thuoc_tinh_can_tim}
              onChange={(e) => set_tap_thuoc_tinh_can_tim(e.target.value)}
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
            <h5 className="fw-bold mb-3">Tập thuộc tính cần tìm</h5>
            <div className="border border-secondary p-3 fs-5 mb-2 bg-white rounded" id="target_attr_set">
              <strong>X = </strong>
              {tap_thuoc_tinh_can_tim.length > 0 ? (
                <span>{`{ ${tap_thuoc_tinh_can_tim.join(', ')} }`}</span>
              ) : (
                <span className="text-muted">∅</span>
              )}
            </div>
            <ThongBao
              thong_bao={thong_bao}
              onClose={onCloseThongBao}
            />
          </div>
        </div>
      </form>
    </div>
  );
};

export default TapThuocTinhCanTim;