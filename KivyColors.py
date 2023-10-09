from enum import Enum

class ColorRGBA(Enum):
    RED = 1, 0, 0, 1
    GREEN = 0, 1, 0, 1
    BLUE = 0, 0, 1, 1
    YELLOW = 1, 1, 0, 1
    PURPLE = 1, 0, 1, 1
    CYAN = 0, 1, 1, 1
    WHITE = 1, 1, 1, 1
    BLACK = 0, 0, 0, 1
    GRAY = 0.5, 0.5, 0.5, 1
    ORANGE = 1, 0.5, 0, 1
    PINK = 1, 0, 0.5, 1
    LIGHT_BLUE = 0.5, 0.5, 1, 1
    DARK_GREEN = 0, 1, 0, 1
    LIGHT_GRAY = 0.7, 0.7, 0.7, 1
    TRANSPARENT = 0, 0, 0, 0
