import subprocess


if __name__ == "__main__":

    backend = subprocess.Popen(
        ["uvicorn", "app.main:app", "--reload"],
        cwd=r"A:\DoAnNganh\do_an_nganh\backend",
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )

    frontend = subprocess.Popen(
        ["npm", "run", "dev"],
        cwd=r"A:\DoAnNganh\do_an_nganh\frontend",
        shell=True,
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )

    print("Đã khởi động Backend và Frontend")