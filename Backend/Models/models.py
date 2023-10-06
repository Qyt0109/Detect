from datetime import datetime
from pydantic import BaseModel
from PIL import Image

# -> G MapInfo
class MapInfo:
    """Lớp MapInfo tạo đối tượng lưu trữ dữ liệu về thông tin bản đồ"""
    def __init__(self,
                 image:Image,
                 speed_limit:int,
                 plan_id:int,
                 latitude:float,
                 longitude:float) -> None:
        self.image = image
        self.speed_limit = speed_limit
        self.plan_id = plan_id
        self.latitude = latitude
        self.longitude = longitude

class ViolationImageModel():
    """Hình ảnh vi phạm căn cứ xử phạt (Bản ảnh chuẩn hoá)\n
    Một hình ảnh có thể được sử dụng để làm căn cứ xử phạt cần phải có đủ những yếu tố được quy định trong Thông tư 65/2020/TT-BCA [3] như sau:
    - Điểm ngắm bắn tốc độ (dấu chấm đỏ) đúng vào xe vi phạm
    - Có thời gian (đầy đủ định dạng ngày, tháng, năm, giờ, phút, giây) tại thời điểm bắn tốc độ
    - Có tọa độ nơi chụp được hình ảnh vi phạm. Trường hợp thiết bị ghi hình không có chức năng xác định địa điểm thì trong phiếu xác nhận kết quả thiết bị ghi hình phải ghi rõ địa điểm ghi hình
    - Có điểm giằng (như biển báo, cột điện, nhà cửa… có vị trí cố định) mà không có ở chỗ khác để xác định vị trí của xe trên thực tế có đang đi trên đoạn đường hạn chế tốc độ không
    - Biển số xe vi phạm phải rõ nét, không bị mờ, loá, che mất ký tự,... để khẳng định đúng là xe đó vi phạm;
    - Hiện tốc độ xe chạy thực tế tại thời điểm bị bắn tốc độ
    """
    def __init__(self,
                data: bytes,
                license_plate :str,
                speed:int,
                speed_limit:int,
                record_time:datetime,
                latitude:float,
                longitude:float,
                device_info: str,
                distance:float = None,
                name: str = None,
                road_address: str = None,
                description: str = None,
                vehicle_type: str = None,
                capture_direction:str = None):
        self.data = data
        self.license_plate = license_plate
        self.speed = speed
        self.speed_limit = speed_limit
        self.distance = distance
        self.record_time = record_time
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
        self.road_address = road_address
        self.description = description
        self.vehicle_type = vehicle_type
        self.capture_direction = capture_direction
        self.device_info = device_info

    def __repr__(self):
        return f"### BEGIN IMAGE ### >>\
        name: {self.name}, \
        data: {self.data[:20] + b'...' if len(self.data) > 20 else {self.data}}, \
        lisence plate number: {self.license_plate}, \
        spd: {self.speed}, spd limit: {self.speed_limit}, \
        road address: {self.road_address}, \
        vehicle type: {self.vehicle_type}, \
        device info: {self.device_info}, capture datetime: {self.record_time}, \
        capture direction: {self.capture_direction}, speed: {self.speed}, \
        distance: {self.distance}, lat, lon: {self.latitude}, {self.longitude}, \
        description: {self.description}\
        << ### END IMAGE ###"