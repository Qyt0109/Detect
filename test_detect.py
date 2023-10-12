from datetime import datetime
from Backend.Common.gps import getCurrentGPS
from Backend.Services.image_processing import add_filter
from Backend.Services.request import getMapInfoFromServer
from Frontend.Models.models import ImageModel
from ImageProcessing.detect import detect_speed_schema, detect_license_plate_schema
from PIL import Image
import time

temp_image_path = "KivyUbuntuAppDesign/Temp/TempCapturedImage.jpg"
image = Image.open(temp_image_path)
lon, lat = getCurrentGPS()
map_info = getMapInfoFromServer(lat,lon)
speed, _ = detect_speed_schema(temp_image_path)
plate = detect_license_plate_schema(temp_image_path)
image_model = ImageModel(image=image,
                        license_plate=plate,
                        speed=speed,
                        speed_limit=map_info.speed_limit,
                        record_time=datetime.now(),
                        latitude=lat,
                        longitude=lon,
                        device_info="Thiết bị 1",
                        distance=None,
                        name="Hình ảnh vi phạm",
                        road_address=None,
                        description=None,
                        vehicle_type=None,
                        capture_direction=None)
filted_image = add_filter(image_model, map_info.image)
filted_image.save(temp_image_path)