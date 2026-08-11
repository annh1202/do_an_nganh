import ThongBao from "./ThongBao";

const ThanhCongCu = ({
    chonTaoDeBaiNgauNhien,
    chonTaiVe,
    chonTaiLen,
    chonGiai,
    fileInputRef,
    thongBao,
    onCloseThongBao,
}) => {
    return (
        <>
            <ThongBao
                thongBao={thongBao}
                onClose={onCloseThongBao}
            />

            <div className="row g-2">

                <div className="col-md-3">
                    <button
                        className="btn btn-success w-100"
                        onClick={chonTaoDeBaiNgauNhien}
                    >
                        Tạo đề mới
                    </button>
                </div>

                <div className="col-md-3">
                    <button
                        className="btn btn-warning w-100"
                        onClick={chonTaiVe}
                    >
                        Tải đề về
                    </button>
                </div>

                <div className="col-md-3">
                    <button
                        className="btn btn-primary w-100"
                        onClick={() => fileInputRef.current?.click()}
                    >
                        Nạp đề lên
                    </button>

                    <input
                        type="file"
                        ref={fileInputRef}
                        accept=".json"
                        hidden
                        onChange={chonTaiLen}
                    />
                </div>

                <div className="col-md-3">
                    <button
                        className="btn btn-dark w-100"
                        onClick={chonGiai}
                    >
                        Giải đề
                    </button>
                </div>

            </div>
        </>
    );
};

export default ThanhCongCu;