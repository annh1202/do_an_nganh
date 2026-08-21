import React from "react";

const GioiThieu = () => {
    return (
        <div className="container py-4">

            {/* Tiêu đề */}
            <div className="p-5 mb-4 bg-primary text-white rounded-3 text-center shadow-sm">
                <h1 className="display-5 fw-bold text-uppercase">
                    Module Database Theory
                </h1>
                <p className="lead mb-0 opacity-75">
                    Tài Liệu Giới Thiệu Chức Năng Hệ Thống
                </p>
            </div>

            {/* Giới thiệu */}
            <div className="alert alert-info border-0 shadow-sm p-4 mb-5">
                <h5 className="alert-heading fw-bold mb-2">
                    Giới thiệu chung
                </h5>

                <p className="mb-0 lh-lg">
                    Module <code className="bg-white px-2 py-1 rounded text-danger fw-semibold">
                        Database Theory
                    </code>{" "}
                    là công cụ hỗ trợ học tập và nghiên cứu các bài toán trong
                    lý thuyết cơ sở dữ liệu quan hệ. Hệ thống cho phép người dùng
                    xây dựng đề bài theo cách thủ công hoặc sinh ngẫu nhiên,
                    đồng thời cung cấp lời giải chi tiết giúp dễ dàng theo dõi
                    quá trình suy luận và áp dụng thuật toán.
                </p>
            </div>

            {/* Chức năng */}
            <h2 className="h3 fw-bold text-primary border-bottom pb-2 mb-3">
                1. Danh Sách Các Chức Năng Cốt Lõi
            </h2>

            <p className="text-muted mb-4">
                Hệ thống hiện hỗ trợ các bài toán nền tảng trong lý thuyết cơ sở
                dữ liệu quan hệ.
            </p>

            <div className="table-responsive mb-5 shadow-sm rounded">
                <table className="table table-hover table-bordered align-middle mb-0">
                    <thead className="table-primary text-uppercase text-center">
                    <tr>
                        <th style={{width: "30%"}}>Chức Năng</th>
                        <th style={{width: "70%"}}>Mô Tả</th>
                    </tr>
                    </thead>

                    <tbody>
                    <tr>
                        <td className="fw-bold bg-light-subtle">
                            Bao đóng tập thuộc tính
                        </td>
                        <td>
                            Tính bao đóng của một tập thuộc tính dựa trên tập
                            phụ thuộc hàm đã cho nhằm xác định các thuộc tính có
                            thể suy diễn được.
                        </td>
                    </tr>

                    <tr>
                        <td className="fw-bold bg-light-subtle">
                            Bao đóng tập phụ thuộc hàm
                        </td>
                        <td>
                            Tìm toàn bộ các phụ thuộc hàm có thể suy diễn từ tập
                            phụ thuộc hàm ban đầu theo hệ tiên đề Armstrong.
                        </td>
                    </tr>

                    <tr>
                        <td className="fw-bold bg-light-subtle">
                            Tìm khóa ứng viên
                        </td>
                        <td>
                            Xác định tất cả khóa ứng viên của lược đồ quan hệ
                            bằng thuật toán tối ưu, đảm bảo đầy đủ và không trùng
                            lặp.
                        </td>
                    </tr>

                    <tr>
                        <td className="fw-bold bg-light-subtle">
                            Chuẩn hóa lược đồ quan hệ
                        </td>
                        <td>
                            Phân tích dạng chuẩn hiện tại (1NF, 2NF, 3NF, BCNF)
                            và thực hiện phân rã để đưa lược đồ lên dạng chuẩn
                            cao hơn.
                        </td>
                    </tr>
                    </tbody>
                </table>
            </div>

            {/* Tiện ích */}
            <h2 className="h3 fw-bold text-primary border-bottom pb-2 mb-3">
                2. Các Tiện Ích Hỗ Trợ
            </h2>

            <p className="text-muted mb-4">
                Mỗi chức năng đều được tích hợp các công cụ hỗ trợ giúp người
                dùng thao tác nhanh chóng và thuận tiện.
            </p>

            <div className="card border-0 shadow-sm mb-5">
                <div className="card-body p-0">

                    <ul className="list-group list-group-flush">

                        <li className="list-group-item p-3">
                            <strong>Quản lý dữ liệu thủ công:</strong>{" "}
                            Thêm, sửa và xóa các thuộc tính, phụ thuộc hàm hoặc
                            các thành phần của đề bài.
                        </li>

                        <li className="list-group-item p-3">
                            <strong>Tạo đề bài ngẫu nhiên:</strong>{" "}
                            Sinh tự động các bài toán hợp lệ với nhiều mức độ
                            khác nhau phục vụ luyện tập.
                        </li>

                        <li className="list-group-item p-3">
                            <strong>Xuất đề bài:</strong>{" "}
                            Lưu đề bài hiện tại thành tệp{" "}
                            <code>.json</code>.
                        </li>

                        <li className="list-group-item p-3">
                            <strong>Nhập đề bài:</strong>{" "}
                            Nạp lại tệp{" "}
                            <code>.json</code>{" "}
                            để tiếp tục làm việc mà không cần nhập lại dữ liệu.
                        </li>

                        <li className="list-group-item p-3 bg-warning-subtle">
                            <strong>Hiển thị lời giải chi tiết:</strong>{" "}
                            Kết quả không chỉ bao gồm đáp án cuối cùng mà còn
                            trình bày từng bước thực hiện, các phụ thuộc hàm
                            được sử dụng và quá trình suy luận của thuật toán.
                        </li>

                    </ul>

                </div>
            </div>

            {/* JSON */}
            <h2 className="h3 fw-bold text-primary border-bottom pb-2 mb-3">
                3. Cấu Trúc File JSON
            </h2>

            <p className="text-muted mb-3">
                Dữ liệu khi xuất hoặc nhập được chuẩn hóa theo định dạng JSON
                sau:
            </p>

            <div className="position-relative mb-5">
                <pre
                    className="bg-dark text-warning p-4 rounded-3 shadow-sm m-0"
                    style={{fontSize: "0.95rem"}}
                >{`{
  "tap_thuoc_tinh": ["A", "B", "C"],
  "tap_phu_thuoc_ham": [
    {
      "ve_trai": "A",
      "ve_phai": "B"
    },
    {
      "ve_trai": "A",
      "ve_phai": "C"
    }
  ]
}`}</pre>
            </div>

        </div>
    );
};

export default GioiThieu;