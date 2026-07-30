import React, { useState } from "react";
import ThongBao from "./ThongBao";

const TapPhuThuocHam = ({
  tapPhuThuocHam = [],
  actions,
  thongBao,
  onCloseThongBao,
}) => {
  const [veTrai, setVeTrai] = useState("");
  const [vePhai, setVePhai] = useState("");

  const { them, xoa, xoaTrong } = actions;

  const chonThem = async (e) => {
    e.preventDefault();

    const vt = veTrai.trim().toUpperCase();
    const vp = vePhai.trim().toUpperCase();

    if (!vt || !vp) return;

    await them({
      veTrai: vt,
      vePhai: vp,
    });

    setVeTrai("");
    setVePhai("");
  };

  const chonXoa = async (e) => {
    e.preventDefault();

    const vt = veTrai.trim().toUpperCase();
    const vp = vePhai.trim().toUpperCase();

    if (!vt || !vp) return;

    await xoa({
      veTrai: vt,
      vePhai: vp,
    });

    setVeTrai("");
    setVePhai("");
  };

  const chonXoaTrong = async (e) => {
    e.preventDefault();
    await xoaTrong();
  };

  return (
    <div className="container mt-4">
      <div className="row mb-4 p-3 border rounded bg-light">
        <div className="col-md-5">
          <h5 className="fw-bold mb-3">Tạo tập phụ thuộc hàm F</h5>

          <div className="d-flex align-items-center gap-2 mb-2">
            <input
              type="text"
              className="form-control"
              placeholder="Thuộc tính trái (VD: AB)"
              value={veTrai}
              onChange={(e) => setVeTrai(e.target.value)}
            />

            <span className="fw-bold">→</span>

            <input
              type="text"
              className="form-control"
              placeholder="Thuộc tính phải (VD: C)"
              value={vePhai}
              onChange={(e) => setVePhai(e.target.value)}
            />
          </div>

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
                Xóa
              </button>
            </div>
          </div>

          <button
            className="btn btn-secondary w-100"
            onClick={chonXoaTrong}
          >
            Xóa trống
          </button>
        </div>

        <div className="col-md-7">
          <h5 className="fw-bold mb-3">Tập phụ thuộc hàm</h5>

          <div className="border border-secondary p-3 fs-5 mb-2 bg-white rounded">
            <strong>F = </strong>

            {tapPhuThuocHam.length > 0 ? (
              <span>
                {"{ "}
                {tapPhuThuocHam.map((phuThuocHam, index) => (
                  <span key={index}>
                    {phuThuocHam.ve_trai} → {phuThuocHam.ve_phai}
                    {index < tapPhuThuocHam.length - 1 ? ", " : ""}
                  </span>
                ))}
                {" }"}
              </span>
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

export default TapPhuThuocHam;