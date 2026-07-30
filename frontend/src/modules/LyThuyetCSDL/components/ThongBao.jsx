import React from "react";

const ThongBao = ({ thongBao, onClose }) => {
  if (!thongBao) return null;

  return (
    <div
      className={`alert alert-${thongBao.loai_thong_bao} alert-dismissible fade show`}
      role="alert"
    >
      {thongBao.noi_dung}

      <button
        type="button"
        className="btn-close"
        onClick={onClose}
      ></button>
    </div>
  );
};

export default ThongBao;