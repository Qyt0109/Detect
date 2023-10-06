from ast import Tuple
from Backend.Common.gps import get_current_gps
from Backend.Services.request import get_map_info_from_server
from Backend.Models.models import MapInfo, ViolationImageModel
from Frontend.Models.models import ImageModel
from ImageProcessing.detect import detect_speed_plate_schema

MAP_IMAGE_PATH = "Frontend/Images/Map/map.png"

def pullGPSAndMapInfo()->Tuple[float, float, MapInfo]:
    # -> R Lấy dữ liệu map và dữ liệu cần thiết từ server vào lúc bắt đầu phiên làm việc hoặc khi cần cập nhật lại
    # Lấy vị trí
    lon, lat = get_current_gps()
    # Lấy từ server thông tin map tại vị trí
    map_info = get_map_info_from_server(latitude=lat, longitude=lon)
    """
	MapInfo(image= image,
			speed_limit=speed_limit,
			plan_id=plan_id,
			latitude=latitude,
			longitude=longitude)
	"""
    return lon, lat, map_info
    
# Ảnh vi phạm #TODO: Lấy hình ảnh từ camera thay vì sử dụng ảnh có sẵn
image_path = 'Frontend/Images/CapturedImages/250723-024717.jpg'
# Trích xuất tốc độ, biển kiểm soát từ hình ảnh vi phạm
detected_speed, detected_license_plate = detect_speed_plate_schema(image_path)