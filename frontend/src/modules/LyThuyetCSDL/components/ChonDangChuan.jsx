import React from "react";
import ThongBao from "../../../components/ThongBao";

const ChonDangChuan = ({
    dangChuan,
    danhSachDangChuan = [],
    actions,
    thongBao,
    onCloseThongBao,
}) => {
    return (
        <div className="row mb-4 p-3 border">

            <div className="col-md-5">
                <h5 className="fw-bold mb-3">
                    Chọn dạng chuẩn
                </h5>

                <select
                    className="form-select"
                    value={dangChuan}
                    onChange={(e) => {
                        actions.chonDangChuan(e.target.value);
                    }}
                >
                    <option value="">
                        -- Chọn dạng chuẩn --
                    </option>

                    {danhSachDangChuan.map((item) => (
                        <option
                            key={item.value}
                            value={item.value}
                        >
                            {item.label}
                        </option>
                    ))}
                </select>
            </div>


            <div className="col-md-7">
                 <h5 className="fw-bold mb-3">
                     Thông báo
                 </h5>

                <ThongBao
                    thongBao={thongBao}
                    onClose={onCloseThongBao}
                />
            </div>
        </div>
    );
};

export default ChonDangChuan;