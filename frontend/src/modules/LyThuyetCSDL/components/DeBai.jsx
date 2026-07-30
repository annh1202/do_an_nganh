import ThanhCongCu from "./ThanhCongCu";


const DeBai = ({
  tapThuocTinh,
  tapPhuThuocHam,
  tapThuocTinhCanTim,

  chonTaoDeBaiNgauNhien,
  chonTaiVe,
  chonTaiLen,
  chonGiai,
  fileInputRef,

  thongBao,
  onCloseThongBao,
}) => {
  return (
    <div className="row mb-4 p-3 border">
      <div className="col-md-12 mb-3">
        <div className="card shadow-sm">
          <div className="card-header problem-header">
            <strong>ĐỀ BÀI</strong>
          </div>

          <div className="card-body fs-5">
            <p>
              <strong>Cho lược đồ quan hệ:</strong>
            </p>

            <div className="border rounded p-3 mb-3 bg-light">
              R = {tapThuocTinh.length > 0 ? `{ ${tapThuocTinh.join(", ")} }` : "∅"}
            </div>

            <p>
              <strong>Và tập phụ thuộc hàm:</strong>
            </p>

            <div className="border rounded p-3 bg-light">
              F = {tapPhuThuocHam.length > 0 ? (
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

            <hr />

            <p>
              <strong>Tìm bao đóng X⁺ với:</strong>
            </p>

            <div className="border rounded p-3 mb-3 bg-light">
              X = {tapThuocTinhCanTim.length > 0 ? `{ ${tapThuocTinhCanTim.join(", ")} }` : "∅"}
            </div>
          </div>
        </div>
      </div>

      <ThanhCongCu
        chonTaoDeBaiNgauNhien={chonTaoDeBaiNgauNhien}
        chonTaiVe={chonTaiVe}
        chonTaiLen={chonTaiLen}
        chonGiai={chonGiai}
        fileInputRef={fileInputRef}
        thongBao={thongBao}
        onCloseThongBao={onCloseThongBao}
      />
    </div>
  );
};

export default DeBai;