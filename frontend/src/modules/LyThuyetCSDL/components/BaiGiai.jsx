import React from "react";

const BaiGiai = ({ baiGiai }) => {
    if (!baiGiai) return null;

    return (
        <div className="row mb-4 p-3 border">

            <h4 className="fw-bold text-primary mb-4">
                Bài giải
            </h4>

            <h5 className="fw-bold">
                Kết quả
            </h5>

            <div className="alert alert-success" style={{ whiteSpace: "pre-line" }}>
                {baiGiai.ket_qua}
            </div>

            <h5 className="fw-bold mt-3">
                Lời giải
            </h5>

            <div className="border rounded p-3 bg-light">
                {baiGiai.loi_giai?.length > 0 ? (
                    baiGiai.loi_giai.map((buoc, index) => (
                        <div
                            key={index}
                            className={
                                index !== baiGiai.loi_giai.length - 1
                                    ? "mb-3 pb-3 border-bottom"
                                    : ""
                            }
                            style={{ whiteSpace: "pre-line" }}
                        >
                            {buoc}
                        </div>
                    ))
                ) : (
                    <p className="text-muted mb-0">
                        Không có lời giải.
                    </p>
                )}
            </div>

        </div>
    );
};

export default BaiGiai;