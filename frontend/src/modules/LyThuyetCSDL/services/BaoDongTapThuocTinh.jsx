import React, { useState, useEffect } from 'react';
import axios from 'axios';
import TapThuocTinh from '../components/TapThuocTinh';
import TapPhuThuocHam from '../components/TapPhuThuocHam';

// Đã sửa: Thêm hẳn /api vào base URL để các route con ngắn gọn hơn
const API_BASE_URL = 'http://localhost:8000/api';

// BỔ SUNG QUAN TRỌNG: Cấu hình Axios luôn gửi kèm Cookie Session qua các cổng (Cross-Origin)
axios.defaults.withCredentials = true;

const BaoDongTapThuocTinh = () => {
  const [thuoc_tinh, setThuocTinh] = useState([]);
  const [phu_thuoc_ham, setPhuThuocHam] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      setLoading(true);
      const response = await axios.get(`${API_BASE_URL}/state`);
      setThuocTinh(response.data.R || []);
      setPhuThuocHam(response.data.F || []);
      setError('');
    } catch (err) {
      console.error("Lỗi khi tải dữ liệu từ FastAPI:", err);
      setError('Không thể kết nối đến máy chủ FastAPI.');
    } finally {
      setLoading(false);
    }
  };

  // ==================== XỬ LÝ TẬP THUỘC TÍNH R ====================

  const them_thuoc_tinh = async (newAttr) => {
    try {
      setError('');
      const response = await axios.post(`${API_BASE_URL}/bao-dong-tap-thuoc-tinh/them-thuoc-tinh`, {
        attribute: newAttr
      });
      setThuocTinh(response.data.R);
      setPhuThuocHam(response.data.F);
    } catch (err) {
      console.error("Lỗi thêm thuộc tính:", err);
      setError(err.response?.data?.detail || 'Lỗi khi thêm thuộc tính.');
    }
  };

  const xoa_thuoc_tinh = async (attrToDelete) => {
    try {
      setError('');
      const response = await axios.post(`${API_BASE_URL}/bao-dong-tap-thuoc-tinh/xoa-thuoc-tinh`, {
        attribute: attrToDelete
      });
      setThuocTinh(response.data.R);
      setPhuThuocHam(response.data.F);
    } catch (err) {
      console.error("Lỗi xóa thuộc tính:", err);
      setError(err.response?.data?.detail || 'Lỗi khi xóa thuộc tính.');
    }
  };

  const xoa_trong_thuoc_tinh = async () => {
  try {
    setError('');
    const response = await axios.post(`${API_BASE_URL}/bao-dong-tap-thuoc-tinh/xoa-trong-thuoc-tinh`);
    setThuocTinh(response.data.R);
    setPhuThuocHam(response.data.F);
  } catch (err) {
    console.error("Lỗi dọn dẹp tập thuộc tính R:", err);
    setError(err.response?.data?.detail || 'Lỗi khi xóa trống tập thuộc tính R.');
  }
};


  // ==================== XỬ LÝ TẬP PHỤ THUỘC HÀM F ====================

  const them_phu_thuoc_ham = async (newDf) => {
    try {
      setError('');
      const response = await axios.post(`${API_BASE_URL}/bao-dong-tap-thuoc-tinh/them-phu-thuoc-ham`, {
        lhs: newDf.lhs,
        rhs: newDf.rhs
      });
      setThuocTinh(response.data.R);
      setPhuThuocHam(response.data.F);
    } catch (err) {
      console.error("Lỗi thêm phụ thuộc hàm:", err);
      setError(err.response?.data?.detail || 'Lỗi khi thêm phụ thuộc hàm.');
    }
  };

  const xoa_phu_thuoc_ham = async (dfToDelete) => {
    try {
      setError('');
      const response = await axios.post(`${API_BASE_URL}/bao-dong-tap-thuoc-tinh/xoa-phu-thuoc-ham`, {
        lhs: dfToDelete.lhs,
        rhs: dfToDelete.rhs
      });
      setThuocTinh(response.data.R);
      setPhuThuocHam(response.data.F);
    } catch (err) {
      console.error("Lỗi xóa phụ thuộc hàm:", err);
      setError(err.response?.data?.detail || 'Lỗi khi xóa phụ thuộc hàm.');
    }
  };

  const xoa_trong_phu_thuoc_ham = async () => {
  try {
    setError('');
    const response = await axios.post(`${API_BASE_URL}/bao-dong-tap-thuoc-tinh/xoa-trong-phu-thuoc-ham`);
    setThuocTinh(response.data.R);
    setPhuThuocHam(response.data.F);
  } catch (err) {
    console.error("Lỗi dọn dẹp tập phụ thuộc hàm F:", err);

    setError(err.response?.data?.detail || 'Lỗi khi xóa trống tập phụ thuộc hàm F.');
  }
};

  return (
    <div className="container py-3">
      <h2 className="text-center mb-4 fw-bold text-dark">Tìm bao đóng tập thuộc tính</h2>

      {error && (
        <div className="alert alert-danger alert-dismissible fade show" role="alert">
          <i className="bi bi-exclamation-triangle-fill me-2"></i>
          {error}
          <button type="button" className="btn-close" onClick={() => setError('')}></button>
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
            tap_thuoc_tinh={thuoc_tinh}
            them={them_thuoc_tinh}
            xoa={xoa_thuoc_tinh}
            xoa_trong={xoa_trong_thuoc_tinh}
          />
          
          <TapPhuThuocHam
            tap_phu_thuoc_ham={phu_thuoc_ham}
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