"""
Các thông số cố định, thường dùng để kiểm tra, so sánh các giá trị điều kiện
"""
from enum import Enum

class ImageCaptureDirections(Enum):
    """Hướng chụp hình ảnh về phương tiện"""
    front = "Front"
    back = "Back"

class ColorConst(Enum):
    """RGB code cho các màu sắc cơ bản"""
    RED = (255, 0, 0)
    BLUE = (0, 255, 0)
    GREEN = (0, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    ORANGE = (255, 165, 0)
    BLACK = (0, 0, 0)
    GRAY = (128, 128, 128)
    WHITE = (255, 255, 255)

class JoinImageDirectionConst(Enum):
    """Hướng ghép ảnh, xác định bằng: Ảnh cần ghép vào >> Hướng ghép so với >> Ảnh gốc được ghép"""
    UP = "UP"
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"