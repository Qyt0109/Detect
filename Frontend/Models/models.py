import datetime
import io
import os
from PIL import Image

from Frontend.Models.qt_models import IMAGE_FOLDER
#from Backend.Database.local_database import DatabaseManager

#database_manager = DatabaseManager()


class ImageModel():
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
                image: Image,
                license_plate :str,
                speed:int,
                speed_limit,
                record_time:datetime,
                latitude:float,
                longitude:float,
                device_info: str = None,
                distance:float = None,
                name: str = None,
                road_address: str = None,
                description: str = None,
                vehicle_type: str = None,
                capture_direction:str = None):
        self.image = image
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

    def save(self):
        timestamp_str = self.record_time.strftime("%d%m%y-%H%M%S")  # Convert datetime to a formatted string
        img_file_name = "%s.jpg" % timestamp_str
        os.makedirs(IMAGE_FOLDER, exist_ok=True)
        file_path = os.path.join(IMAGE_FOLDER, img_file_name)
        print(file_path)
        self.image.save(file_path)

    """
    def save_to_database(self):
        with io.BytesIO() as byte_io:
            self.image.save(byte_io, format='JPEG')
            byte_io.seek(0)
            image_bytes = byte_io.read()
        
        timestamp_str = self.record_time.strftime("%d%m%y-%H%M%S")  # Convert datetime to a formatted string
        img_file_name = "%s.jpg" % timestamp_str
        return database_manager.create_image(data=image_bytes,
                                      license_plate=self.license_plate,
                                      speed=self.speed,
                                      speed_limit=self.speed_limit,
                                      record_time=self.record_time,
                                      latitude=self.latitude,
                                      longitude=self.longitude,
                                      device_info=self.device_info,
                                      distance=self.distance,
                                      name=img_file_name,
                                      road_address=self.road_address,
                                      description=self.description,
                                      vehicle_type=self.vehicle_type,
                                      capture_direction=self.capture_direction)
    """

    def describe(self):
        not_defined = 'Chưa xác định'
        not_info = 'Không có thông tin'
        return f"\
        Biển kiểm soát: {self.license_plate if self.license_plate else not_defined}\n\
        Tốc độ ghi nhận: {str(self.speed) + '(km/h)' if self.speed else not_defined}\n\
        Tốc độ giới hạn: {str(self.speed_limit) + '(km/h)' if self.speed_limit else not_defined}\n\
        Thời điểm ghi nhận: {self.record_time.strftime('%d%m%y-%H%M%S') if self.record_time else not_defined}\n\
        Vị trí ghi nhận: {'(' + str(self.latitude) + ', ' + str(self.longitude) + ')' if self.latitude is not None and self.longitude is not None else not_defined}\n\
        {'Thiết bị ghi nhận: ' + self.device_info if self.device_info else ''}\n\
        {'Ghi chú: ' + self.description if self.description else ''}"

    def __repr__(self):
        return f"### BEGIN IMAGE ### >>\
        id: {self.id}, name: {self.name}, \
        data: {self.image[:20] + b'...' if len(self.image) > 20 else {self.image}}, \
        lisence plate number: {self.license_plate}, \
        spd: {self.speed}, spd limit: {self.speed_limit}, \
        road address: {self.road_address}, \
        vehicle type: {self.vehicle_type}, \
        device info: {self.device_info}, capture datetime: {self.record_time}, \
        capture direction: {self.capture_direction}, speed: {self.speed}, \
        distance: {self.distance}, lat, lon: {self.latitude}, {self.longitude}, \
        description: {self.description}\
        << ### END IMAGE ###"
