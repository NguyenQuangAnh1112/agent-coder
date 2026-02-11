import subprocess

from langchain_core.tools import tool

from src.utils.exception import he
from src.utils.logger import logger


@tool
@he
def execute_python_file(filename: str):
    """
    Thực thi một file python và trả về kết quả (stdout) hoặc lỗi (stderr).
    Sử dụng tool này để kiểm tra xem code có chạy đúng không.

    Args:
        filename: Tên file cần chạy (Ví dụ: 'main.py')
    """
    result = subprocess.run(
        ["python", filename], capture_output=True, text=True, timeout=10
    )

    if result.returncode == 0:
        logger.info(f"Chạy file {filename} thành công")
        if result.stdout:
            print(f"\n{result.stdout}")
    else:
        logger.info(f"Chạy file {filename} thất bại.")
        print(f"\n{result.stderr}")
