import base64
import io
from PIL import Image, ImageDraw, ImageFont
from PIL.ImageFont import FreeTypeFont
from Env.env import font_path
from typing import Tuple
from Backend.Common.defined_constants import ColorConst, JoinImageDirectionConst

class CustomFont:
    """Lớp định nghĩa cho phông chữ làm việc cùng module PIL Image, các tham số cài đặt mặc định được định nghĩa trong hàm khởi tạo"""
    def __init__(self,
                 font_path:str = font_path,
                 font_sm_size: int = 40,
                 font_md_size: int = 60,
                 font_lg_size: int = 80,
                 font_xl_size: int = 100):
        """Hàm khởi tạo cho lớp phông chữ làm việc cùng module PIL Image"""
        self.sm = ImageFont.truetype(font=font_path,
                                     size=font_sm_size,
                                     encoding="utf-8")
        """Small font"""
        self.md = ImageFont.truetype(font=font_path,
                                     size=font_md_size,
                                     encoding="utf-8")
        """Medium font"""
        self.lg = ImageFont.truetype(font=font_path,
                                     size=font_lg_size,
                                     encoding="utf-8")
        """Large font"""
        self.xl = ImageFont.truetype(font=font_path,
                                     size=font_xl_size,
                                     encoding="utf-8")
        """Extra large font"""
        
BORDER_MARGIN = 4   # px                                     
"""Độ lệch bo viền của chữ"""

class CustomImage:
    """Lớp CustomImage bọc hình ảnh để sử dụng một số phương thức thuận tiện cho lúc xử lý các tác vụ cần thiết"""
    image:Image
    font: CustomFont
    drawer: ImageDraw
    xy: Tuple[int, int]
    inv_xy: Tuple[int, int]
    
    def __init__(self,
                 image: Image,
                 font: CustomFont = None) -> None:
        """Hàm khởi tạo"""
        self.image = image
        self.drawer = ImageDraw.Draw(self.image)
        self.xy = (20, 20)
        self.inv_xy = (20, image.height - 20)
        if font:
            self.font = font
        else:
            self.font = CustomFont()

    def resize(self,
               width:int = None,
               height:int = None):
        """Phương thức tuỳ chỉnh kích cỡ ảnh"""
        self.image.resize((width, height))
        return

    def set_xy(self,
               x:int,
               y:int):
        """Tuỳ chỉnh vị trí con trỏ đi (x, y) so với (0, 0) để ghi chữ lên hình ảnh"""
        self.xy = (x, y)

    def set_inv_xy(self,
                   inv_x:int,
                   int_y:int):
        """Tuỳ chỉnh vị trí con trỏ nghịch đi (x, -y) so với (0, maxHeight) để ghi chữ lên hình ảnh"""
        self.inv_xy = (inv_x, self.image.height - int_y)

    def add_text_line(self,
                      text: str,
                      font: FreeTypeFont,
                      fill: Tuple[int, int, int] = None,
                      xy: Tuple[int, int] = None,
                      is_border: bool = False,
                      border_fill: Tuple[int, int, int] = None):
        """Ghi chữ lên vị trí con trỏ"""
        x, y = xy if xy else self.xy
        if is_border:
            self.drawer.text(xy=(x + BORDER_MARGIN, y + BORDER_MARGIN),
                         text=text,
                         font=font,
                         fill = border_fill if border_fill else ColorConst.BLACK.value)
        self.drawer.text(xy=(x, y),
                         text=text,
                         font=font,
                         fill = fill if fill else ColorConst.BLACK.value)
        
        self.xy = (x, y + font.size)

    def add_inv_text_line(self,
                      text: str,
                      font: FreeTypeFont,
                          fill: Tuple[int, int, int] = None,
                          inv_xy: Tuple[int, int] = None,
                      is_border: bool = False,
                      border_fill: Tuple[int, int, int] = None):
        """Ghi chữ lên vị trí con trỏ nghịch"""
        inv_x, inv_y = inv_xy if inv_xy else self.inv_xy
        font_size = font.size
        if is_border:
            self.drawer.text(xy=(inv_x + BORDER_MARGIN, inv_y - font_size + BORDER_MARGIN),
                         text=text,
                         font=font,
                         fill = border_fill if border_fill else ColorConst.BLACK.value)
        self.drawer.text(xy=(inv_x, inv_y - font_size),
                         text=text,
                         font=font,
                         fill = fill if fill else ColorConst.BLACK.value)
        
        self.inv_xy = (inv_x, inv_y - font.size)

    def save_image(self,
                   save_path:str):
        """Lưu lại hình ảnh đang được bọc bởi lớp CustomImage"""
        self.image.save(save_path)
        print(f"Saved to {save_path}")

    def join_image(self,
                   image_to_join: Image,
                   join_direction: JoinImageDirectionConst):
        """Ghép hình ảnh khác vào hình ảnh đang được bọc theo hướng chỉ định"""
        target_image = self.image
        join_image = image_to_join
        # Resize the join_image to match target_image
        # If direction is RIGHT or LEFT, adjust the join_image's height to match the target_image
        if join_direction in (JoinImageDirectionConst.LEFT, JoinImageDirectionConst.RIGHT):
            join_height = target_image.height
            join_aspect_ratio = join_image.width / join_image.height
            join_width = round(join_height * join_aspect_ratio)
        # If direction is UP or DOWN, adjust the join_image's width to match the target_image
        elif join_direction in (JoinImageDirectionConst.UP, JoinImageDirectionConst.DOWN):
            join_width = target_image.width
            join_aspect_ratio = join_image.height / join_image.width
            join_height = round(join_width * join_aspect_ratio)
        else:
            return
        join_image = join_image.resize((join_width, join_height))

        # Create a new blank image with the calculated dimensions
        if join_direction == JoinImageDirectionConst.RIGHT or join_direction == JoinImageDirectionConst.LEFT:
            output_width = target_image.width + join_width
            output_height = join_height
        elif join_direction == JoinImageDirectionConst.UP or join_direction == JoinImageDirectionConst.DOWN:
            output_width = join_width
            output_height = target_image.height + join_height

        output_image = Image.new('RGB', (output_width, output_height))

        # Paste the resized target and join images onto the output image
        if join_direction == JoinImageDirectionConst.RIGHT:
            output_image.paste(target_image,
                               (0, 0))
            output_image.paste(join_image,
                               (target_image.width, 0))
        elif join_direction == JoinImageDirectionConst.LEFT:
            output_image.paste(join_image,
                               (0, 0))
            output_image.paste(target_image,
                               (join_width, 0))
        elif join_direction == JoinImageDirectionConst.UP:
            output_image.paste(join_image,
                               (0, 0))
            output_image.paste(target_image,
                               (0, join_height))
        elif join_direction == JoinImageDirectionConst.DOWN:
            output_image.paste(target_image,
                               (0, 0))
            output_image.paste(join_image,
                               (0, target_image.height))
        
        self.image = output_image


    def get_image(self):
        """Trả lại hình ảnh đang được bọc"""
        return self.image
    
    def to_bytes(self):
        """Trả lại hình ảnh đang được bọc dưới dạng bytes"""
        with io.BytesIO() as byte_io:
            self.image.save(byte_io, format='JPEG')
            byte_io.seek(0)
            image_bytes = byte_io.read()
        base64_image_bytes = base64.b64encode(image_bytes)
        return base64_image_bytes