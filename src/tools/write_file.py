from langchain_core.tools import tool

from src.utils.exception import he
from src.utils.logger import logger


@tool
@he
def write_file(filename: str, content: str):
    """
    Ghi nội dung code vào 1 file trên ổ cứng.
    Dùng tool này khi và chỉ khi cần lưu code trước khi chạy.

    Args:
        filename: Tên file (ví dụ: 'main.py', 'utils.py')
        content: Toàn bộ nội dung code cần ghi.
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
        logger.info(f"SUCCESS: Đã ghi thành công file '{filename}'.")
