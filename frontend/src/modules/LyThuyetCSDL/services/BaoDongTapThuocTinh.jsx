import React, { useState, useEffect } from 'react';
import axios from 'axios';
import TapThuocTinh from '../components/TapThuocTinh';
import TapPhuThuocHam from '../components/TapPhuThuocHam';

// Đã sửa: Thêm hẳn /api vào base URL để các route con ngắn gọn hơn
const API_BASE_URL = 'http://localhost:8000/api';

// BỔ SUNG QUAN TRỌNG: Cấu hình Axios luôn gửi kèm Cookie Session qua các cổng (Cross-Origin)
axios.defaults.withCredentials = true;

const BaoDongTapThuocTinh = () => {
  const [tap_thuoc_tinh, set_tap_thuoc_tinh] = useState([]);
  const [tap_phu_thuoc_ham, set_tap_phu_thuoc_ham] = useState([]);
  const [loading, set_loading] = useState(false);
  const [thong_bao, set_thong_bao] = useState(null);

  useEffect(() => {
    fetchData();
  }, []);

  const hien_thong_bao = (loai_thong_bao, noi_dung) => {
    set_thong_bao({
      loai_thong_bao,
      noi_dung,
    });
  };

  const fetchData = async () => {
    try {
      set_loading(true);
      const response = await axios.get(`${API_BASE_URL}/state`);
      set_tap_thuoc_tinh(response.data.doi_tuong.tap_thuoc_tinh);
      set_tap_phu_thuoc_ham(response.data.doi_tuong.tap_phu_thuoc_ham);
      set_thong_bao(null);
    } catch (err) {
      console.error("Lỗi khi tải dữ liệu từ FastAPI:", err);
      hien_thong_bao(
        "danger",
        "Không thể kết nối đến máy chủ FastAPI."
      );
    } finally {
      set_loading(false);
    }
  };

  // ==================== XỬ LÝ TẬP THUỘC TÍNH R ====================

  const them_thuoc_tinh = async (thuoc_tinh_moi) => {
    try {
      set_thong_bao(null);
      const response = await axios.post(`${API_BASE_URL}/bao-dong-tap-thuoc-tinh/them-thuoc-tinh`, {
        thuoc_tinh: thuoc_tinh_moi
      });
      set_tap_thuoc_tinh(response.data.doi_tuong.tap_thuoc_tinh);
      set_tap_phu_thuoc_ham(response.data.doi_tuong.tap_phu_thuoc_ham);

      hien_thong_bao(
        response.data.loai_thong_bao,
        response.data.thong_bao
      );
    } catch (err) {
      console.error("Lỗi thêm thuộc tính:", err);
      if (err.response?.data?.detail) {
        hien_thong_bao(
          err.response.data.detail.loai_thong_bao,
          err.response.data.detail.thong_bao
      );
      } else {
        hien_thong_bao(
          "danger",
          "Có lỗi xảy ra."
        );
      }
    }
  };

  const xoa_thuoc_tinh = async (thuoc_tinh_can_xoa) => {
    try {
      set_thong_bao(null);
      const response = await axios.post(`${API_BASE_URL}/bao-dong-tap-thuoc-tinh/xoa-thuoc-tinh`, {
        thuoc_tinh: thuoc_tinh_can_xoa
      });
      set_tap_thuoc_tinh(response.data.doi_tuong.tap_thuoc_tinh);
      set_tap_phu_thuoc_ham(response.data.doi_tuong.tap_phu_thuoc_ham);

      hien_thong_bao(
        response.data.loai_thong_bao,
        response.data.thong_bao
      );
    } catch (err) {
      console.error("Lỗi xóa thuộc tính:", err);
      if (err.response?.data?.detail) {
      hien_thong_bao(
        err.response.data.detail.loai_thong_bao,
        err.response.data.detail.thong_bao
      );
      } else {
        hien_thong_bao(
          "danger",
          "Có lỗi xảy ra."
        );
      }
    }
  };

  const xoa_trong_thuoc_tinh = async () => {
  try {
    set_thong_bao(null);
    const response = await axios.post(`${API_BASE_URL}/bao-dong-tap-thuoc-tinh/xoa-trong-thuoc-tinh`);
    set_tap_thuoc_tinh(response.data.doi_tuong.tap_thuoc_tinh);
    set_tap_phu_thuoc_ham(response.data.doi_tuong.tap_phu_thuoc_ham);

    hien_thong_bao(
      response.data.loai_thong_bao,
      response.data.thong_bao
    );
  } catch (err) {
    console.error("Lỗi dọn dẹp tập thuộc tính R:", err);
    if (err.response?.data?.detail) {
      hien_thong_bao(
        err.response.data.detail.loai_thong_bao,
        err.response.data.detail.thong_bao
      );
    } else {
      hien_thong_bao(
        "danger",
        "Có lỗi xảy ra."
      );
    }
  }
};


  // ==================== XỬ LÝ TẬP PHỤ THUỘC HÀM F ====================

  const them_phu_thuoc_ham = async (phu_thuoc_ham_moi) => {
    try {
      set_thong_bao(null);
      const response = await axios.post(`${API_BASE_URL}/bao-dong-tap-thuoc-tinh/them-phu-thuoc-ham`, {
        ve_trai: phu_thuoc_ham_moi.ve_trai,
        ve_phai: phu_thuoc_ham_moi.ve_phai
      });
      set_tap_thuoc_tinh(response.data.doi_tuong.tap_thuoc_tinh);
      set_tap_phu_thuoc_ham(response.data.doi_tuong.tap_phu_thuoc_ham);

      hien_thong_bao(
        response.data.loai_thong_bao,
        response.data.thong_bao
      );
    } catch (err) {
      console.error("Lỗi thêm phụ thuộc hàm:", err);
      if (err.response?.data?.detail) {
        hien_thong_bao(
          err.response.data.detail.loai_thong_bao,
          err.response.data.detail.thong_bao
        );
      } else {
        hien_thong_bao(
          "danger",
          "Có lỗi xảy ra."
        );
      }
    }
  };

  const xoa_phu_thuoc_ham = async (phu_thuoc_ham_can_xoa) => {
    try {
      set_thong_bao(null);
      const response = await axios.post(`${API_BASE_URL}/bao-dong-tap-thuoc-tinh/xoa-phu-thuoc-ham`, {
        ve_trai: phu_thuoc_ham_can_xoa.ve_trai,
        ve_phai: phu_thuoc_ham_can_xoa.ve_phai
      });
      set_tap_thuoc_tinh(response.data.doi_tuong.tap_thuoc_tinh);
      set_tap_phu_thuoc_ham(response.data.doi_tuong.tap_phu_thuoc_ham);

      hien_thong_bao(
        response.data.loai_thong_bao,
        response.data.thong_bao
      );
    } catch (err) {
      console.error("Lỗi xóa phụ thuộc hàm:", err);
      if (err.response?.data?.detail) {
        hien_thong_bao(
          err.response.data.detail.loai_thong_bao,
          err.response.data.detail.thong_bao
        );
      } else {
        hien_thong_bao(
          "danger",
          "Có lỗi xảy ra."
        );
      }
    }
  };

  const xoa_trong_phu_thuoc_ham = async () => {
  try {
    set_thong_bao(null);
    const response = await axios.post(`${API_BASE_URL}/bao-dong-tap-thuoc-tinh/xoa-trong-phu-thuoc-ham`);
    set_tap_thuoc_tinh(response.data.doi_tuong.tap_thuoc_tinh);
    set_tap_phu_thuoc_ham(response.data.doi_tuong.tap_phu_thuoc_ham);

    hien_thong_bao(
      response.data.loai_thong_bao,
      response.data.thong_bao
    );
  } catch (err) {
    console.error("Lỗi dọn dẹp tập phụ thuộc hàm F:", err);

    if (err.response?.data?.detail) {
      hien_thong_bao(
        err.response.data.detail.loai_thong_bao,
        err.response.data.detail.thong_bao
      );
    } else {
      hien_thong_bao(
        "danger",
        "Có lỗi xảy ra."
      );
    }
  }
};

  return (
    <div className="container py-3">
      <h2 className="text-center mb-4 fw-bold text-dark">Tìm bao đóng tập thuộc tính</h2>

      {thong_bao && (
        <div
          className={`alert alert-${thong_bao.loai_thong_bao} alert-dismissible fade show`}
          role="alert"
        >
          {thong_bao.noi_dung}
          <button
            type="button"
            className="btn-close"
            onClick={() => set_thong_bao(null)}
          ></button>
        </div>
      )}

      {loading ? (
        <div className="text-center my-4">
          <div className="spinner-border text-primary" role="status">
            <span className="visually-hidden">Đang tải...</span>
          </div>
        </div>
      ) : (
        <>
          <TapThuocTinh
            tap_thuoc_tinh={tap_thuoc_tinh}
            them={them_thuoc_tinh}
            xoa={xoa_thuoc_tinh}
            xoa_trong={xoa_trong_thuoc_tinh}
          />
          
            <TapPhuThuocHam
              tap_phu_thuoc_ham={tap_phu_thuoc_ham}
              them={them_phu_thuoc_ham}
              xoa={xoa_phu_thuoc_ham}
              xoa_trong={xoa_trong_phu_thuoc_ham}
            />
        </>
      )}
    </div>
  );
};

export default BaoDongTapThuocTinh;