import React from "react";

const ThongBao = ({ thong_bao, onClose }) => {
  if (!thong_bao) return null;

  return (
    <div
      className={`alert alert-${thong_bao.loai_thong_bao} alert-dismissible fade show`}
      role="alert"
    >
      {thong_bao.noi_dung}

      <button
        type="button"
        className="btn-close"
        onClick={onClose}
      ></button>
    </div>
  );
};

export default ThongBao;