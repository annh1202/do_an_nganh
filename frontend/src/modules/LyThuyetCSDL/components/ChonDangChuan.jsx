import React from "react";
import ThongBao from "./ThongBao";

const ChonDangChuan = ({
  dangChuan,
  setDangChuan,
  actions,
  thongBao,
  onCloseThongBao,
}) => {
  return (
    <div className="container mt-4">
      <div className="row mb-4 p-3 border rounded align-items-center shadow-sm">
        <div className="col-md-5">
          <h5 className="fw-bold mb-3">
            Chọn dạng chuẩn của cơ sở dữ liệu
          </h5>

          <select
            className="form-select form-select-lg"
            value={dangChuan}
            onChange={(e) => {
              const value = e.target.value;
              setDangChuan(value);
              actions.chonDangChuan(value);
            }}
          >
            <option value="">-- Chọn dạng chuẩn --</option>
            <option value="2NF">2NF - Second Normal Form</option>
            <option value="3NF">3NF - Third Normal Form</option>
            <option value="BCNF">BCNF - Boyce-Codd Normal Form</option>
          </select>
        </div>

        <div className="col-md-7">
          <ThongBao
            thongBao={thongBao}
            onClose={onCloseThongBao}
          />
        </div>
      </div>
    </div>
  );
};

export default ChonDangChuan;