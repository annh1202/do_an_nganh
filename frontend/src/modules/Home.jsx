import '../index.css'


export default function Home() {
    return (
        <div className="container-fluid px-5">

            {/* Hero */}
            <section >
                <div className="row align-items-center py-5">
                    <div className="col-lg-7">
                        <h1 className="display-4 fw-bold">
                            Học Cơ sở dữ liệu
                            <span className="text-primary"> trực quan hơn</span>
                        </h1>

                        <p className="lead text-secondary mt-4">
                            DataLogic giúp bạn thực hành các thuật toán
                            trong lý thuyết cơ sở dữ liệu một cách trực quan
                            và dễ hiểu.
                        </p>

                        <div className="mt-4">
                            <a
                                href="#chuc-nang"
                                className="btn btn-primary btn-lg px-4 me-2"
                            >
                                Bắt đầu học
                            </a>

                            <a
                                href="#gioi-thieu"
                                className="btn btn-outline-secondary btn-lg px-4"
                            >
                                Tìm hiểu thêm
                            </a>
                        </div>
                    </div>

                    <div className="col-lg-5 mt-5 mt-lg-0">
                        <div className="d-flex justify-content-center">

                            <svg
                                className="datalogic-logo"
                                viewBox="0 0 300 300"
                                xmlns="http://www.w3.org/2000/svg"
                            >

                                {/* Vòng ngoài */}
                                <circle
                                    className="logo-ring logo-ring-1"
                                    cx="150"
                                    cy="150"
                                    r="115"
                                />

                                <circle
                                    className="logo-ring logo-ring-2"
                                    cx="150"
                                    cy="150"
                                    r="90"
                                />

                                {/* Các node */}
                                <circle
                                    className="logo-node logo-node-1"
                                    cx="150"
                                    cy="35"
                                    r="7"
                                />

                                <circle
                                    className="logo-node logo-node-2"
                                    cx="265"
                                    cy="150"
                                    r="7"
                                />

                                <circle
                                    className="logo-node logo-node-3"
                                    cx="150"
                                    cy="265"
                                    r="7"
                                />

                                <circle
                                    className="logo-node logo-node-4"
                                    cx="35"
                                    cy="150"
                                    r="7"
                                />

                                {/* Icon database */}
                                <g className="logo-database">
                                    <ellipse
                                        cx="150"
                                        cy="105"
                                        rx="45"
                                        ry="15"
                                    />

                                    <path
                                        d="M105 105 V155 C105 163 125 170 150 170 C175 170 195 163 195 155 V105"
                                    />

                                    <ellipse
                                        cx="150"
                                        cy="155"
                                        rx="45"
                                        ry="15"
                                    />

                                    <ellipse
                                        cx="150"
                                        cy="105"
                                        rx="45"
                                        ry="15"
                                    />
                                </g>

                            </svg>

                        </div>

                        <div className="text-center mt-3">
                            <h2 className="fw-bold mb-1">
                                Data<span className="text-primary">Logic</span>
                            </h2>

                            <p className="text-secondary mb-0">
                                Database Theory
                            </p>
                        </div>

                    </div>
                </div>
            </section>


            {/* Giới thiệu */}
            <section id="gioi-thieu" className="py-5">
                <div className="text-center mb-5">
                    <h2 className="fw-bold">
                        Học bằng cách thực hành
                    </h2>

                    <p className="text-secondary">
                        Nhập bài toán, chạy thuật toán và quan sát kết quả.
                    </p>
                </div>

                <div className="row g-4">

                    <div className="col-md-4">
                        <div className="card h-100 border-0 shadow-sm">
                            <div className="card-body p-4">
                                <i className="bi bi-pencil-square text-primary fs-1"></i>

                                <h5 className="fw-bold mt-3">
                                    Nhập dữ liệu
                                </h5>

                                <p className="text-secondary mb-0">
                                    Tạo tập thuộc tính và các phụ thuộc hàm
                                    cho bài toán.
                                </p>
                            </div>
                        </div>
                    </div>

                    <div className="col-md-4">
                        <div className="card h-100 border-0 shadow-sm">
                            <div className="card-body p-4">
                                <i className="bi bi-cpu text-primary fs-1"></i>

                                <h5 className="fw-bold mt-3">
                                    Chạy thuật toán
                                </h5>

                                <p className="text-secondary mb-0">
                                    Áp dụng các thuật toán lý thuyết
                                    cơ sở dữ liệu.
                                </p>
                            </div>
                        </div>
                    </div>

                    <div className="col-md-4">
                        <div className="card h-100 border-0 shadow-sm">
                            <div className="card-body p-4">
                                <i className="bi bi-check2-circle text-primary fs-1"></i>

                                <h5 className="fw-bold mt-3">
                                    Xem kết quả
                                </h5>

                                <p className="text-secondary mb-0">
                                    Kiểm tra và hiểu kết quả của thuật toán.
                                </p>
                            </div>
                        </div>
                    </div>

                </div>
            </section>


            {/* Chức năng */}
            <section id="chuc-nang" className="py-5">

                <div className="text-center mb-5">
                    <h2 className="fw-bold">
                        Các chức năng
                    </h2>

                    <p className="text-secondary">
                        Công cụ hỗ trợ học và thực hành lý thuyết cơ sở dữ liệu.
                    </p>
                </div>

                <div className="row g-4">

                    <div className="col-md-6 col-lg-3">
                        <div className="card h-100 shadow-sm">
                            <div className="card-body p-4">
                                <i className="bi bi-boxes text-primary fs-1"></i>

                                <h5 className="fw-bold mt-3">
                                    Bao đóng thuộc tính
                                </h5>

                                <p className="text-secondary">
                                    Tính bao đóng của tập thuộc tính
                                    dựa trên các phụ thuộc hàm.
                                </p>

                                <a
                                    href="/bao-dong-tap-thuoc-tinh"
                                    className="btn btn-outline-primary"
                                >
                                    Thực hành
                                </a>
                            </div>
                        </div>
                    </div>


                    <div className="col-md-6 col-lg-3">
                        <div className="card h-100 shadow-sm">
                            <div className="card-body p-4">
                                <i className="bi bi-diagram-3 text-primary fs-1"></i>

                                <h5 className="fw-bold mt-3">
                                    Bao đóng PTH
                                </h5>

                                <p className="text-secondary">
                                    Tính bao đóng của tập phụ thuộc hàm.
                                </p>

                                <a
                                    href="/bao-dong-tap-phu-thuoc-ham"
                                    className="btn btn-outline-primary"
                                >
                                    Thực hành
                                </a>
                            </div>
                        </div>
                    </div>


                    <div className="col-md-6 col-lg-3">
                        <div className="card h-100 shadow-sm">
                            <div className="card-body p-4">
                                <i className="bi bi-key text-primary fs-1"></i>

                                <h5 className="fw-bold mt-3">
                                    Khóa ứng viên
                                </h5>

                                <p className="text-secondary">
                                    Tìm các khóa ứng viên của lược đồ quan hệ.
                                </p>

                                <a
                                    href="/khoa-ung-vien"
                                    className="btn btn-outline-primary"
                                >
                                    Thực hành
                                </a>
                            </div>
                        </div>
                    </div>


                    <div className="col-md-6 col-lg-3">
                        <div className="card h-100 shadow-sm">
                            <div className="card-body p-4">
                                <i className="bi bi-bar-chart-steps text-primary fs-1"></i>

                                <h5 className="fw-bold mt-3">
                                    Dạng chuẩn
                                </h5>

                                <p className="text-secondary">
                                    Kiểm tra và nâng quan hệ lên 2NF,
                                    3NF hoặc BCNF.
                                </p>

                                <a
                                    href="/dang-chuan"
                                    className="btn btn-outline-primary"
                                >
                                    Thực hành
                                </a>
                            </div>
                        </div>
                    </div>

                </div>
            </section>


            {/* CTA */}
            <section className="py-5">
                <div className="bg-primary text-white rounded-4 p-5 text-center">
                    <i className="bi bi-database-fill display-5"></i>

                    <h2 className="fw-bold mt-3">
                        Sẵn sàng bắt đầu?
                    </h2>

                    <p className="mb-4">
                        Chọn một chức năng và bắt đầu thực hành.
                    </p>

                    <a
                        href="#chuc-nang"
                        className="btn btn-light btn-lg px-4 fw-semibold"
                    >
                        Bắt đầu ngay
                    </a>
                </div>
            </section>

        </div>
    );
}