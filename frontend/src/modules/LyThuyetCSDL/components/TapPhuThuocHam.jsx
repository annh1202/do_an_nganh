import React, { useState } from "react";
import ThongBao from "./ThongBao";

const TapPhuThuocHam = ({
  tap_phu_thuoc_ham = [],
  actions,
  thong_bao,
  onCloseThongBao,
}) => {
  const [veTrai, setVeTrai] = useState("");
  const [vePhai, setVePhai] = useState("");

  const { them, xoa, xoaTrong } = actions;

  const chon_them = async (e) => {
    e.preventDefault();

    const vt = veTrai.trim().toUpperCase();
    const vp = vePhai.trim().toUpperCase();

    if (!vt || !vp) return;

    await them({
      ve_trai: vt,
      ve_phai: vp,
    });

    setVeTrai("");
    setVePhai("");
  };

  const chon_xoa = async (e) => {
    e.preventDefault();

    const vt = veTrai.trim().toUpperCase();
    const vp = vePhai.trim().toUpperCase();

    if (!vt || !vp) return;

    await xoa({
      ve_trai: vt,
      ve_phai: vp,
    });

    setVeTrai("");
    setVePhai("");
  };

  const chon_xoa_trong = async (e) => {
    e.preventDefault();
    await xoaTrong();
  };

  return (
    <div className="container mt-4">
      <form id="fd_form">
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
                  Xóa
                </button>
              </div>
            </div>

            <button
              type="button"
              className="btn btn-secondary w-100"
              onClick={chon_xoa_trong}
            >
              Xóa trống
            </button>
          </div>

          <div className="col-md-7">
            <h5 className="fw-bold mb-3">Tập phụ thuộc hàm</h5>

            <div
              className="border border-secondary p-3 fs-5 mb-2 bg-white rounded"
            >
              <strong>F = </strong>

              {tap_phu_thuoc_ham.length > 0 ? (
                <span>
                  {"{ "}
                  {tap_phu_thuoc_ham.map((fd, index) => (
                    <span key={index}>
                      {fd.ve_trai} → {fd.ve_phai}
                      {index < tap_phu_thuoc_ham.length - 1 ? ", " : ""}
                    </span>
                  ))}
                  {" }"}
                </span>
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

export default TapPhuThuocHam;