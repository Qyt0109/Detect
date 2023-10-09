from datetime import datetime
from Backend.Services.request import getMapInfoFromServer
from Backend.Common.gps import getCurrentGPS
from Backend.Common.defined_constants import ColorConst, JoinImageDirectionConst
from Backend.Common.image_features import CustomImage
from Frontend.Models.models import ImageModel
from ImageProcessing.detect import detect_speed_schema, detect_license_plate_schema
from Env.env import device_id
from PIL import Image
import io, os
import base64
from io import BytesIO

"""
# -> Example usage:
# -> R Get data
lon, lat = get_current_gps()

image_bytes, speed_limit, plan_id = get_map_info_from_server(lat,lon)
image_path = 'Frontend/Images/CapturedImages/250723-024717.jpg'
map_image_path = "Frontend/Images/Map/map.png"
license_plate = detect_license_plate_schema(image_path)
speed, _ = detect_speed_schema(image_path)
image_file_name = os.path.basename(image_path)  # Example: 250723-024717.jpg
# Parse the image file name and convert it to a datetime object
image_datetime = datetime.strptime(image_file_name, "%y%m%d-%H%M%S.jpg")
# Format the datetime object as "25/07/23 01:44:28"
formatted_datetime = image_datetime.strftime("%d/%m/%y %H:%M:%S")
image_model = ImageModel(image=image_bytes,
                         license_plate=license_plate,
                         speed=speed,
                         speed_limit=speed_limit,
                         record_time=image_datetime,
                         latitude=lat,
                         longitude=lon,
                         device_info=device_id,
                         distance=None,
                         name=image_file_name,
                         road_address=None,
                         description=None,
                         vehicle_type=None,
                         capture_direction=None)
"""

""" Just do this one to save map image
# Convert binary data to an image
map_image = Image.open(BytesIO(image_bytes))
# Save the image to the specified location
map_image_path = "Frontend/Images/Map/map.png"
map_image.save(map_image_path, "PNG")
print("Image saved successfully to:", map_image_path)    # Save map
"""


"""
            ┌─────────────────┬─────┐
            │                 │     │
            │                 │     │
            │      IMAGE      │ MAP │
            │                 │     │
            │                 │     │
            ├─────────────────┴─────┤
            │      INFO IMAGE       │
            └───────────────────────┘
"""

dir = "Backend/Services/ImageProcessingTemp"

def get_speed_plate(image_path:str):
    speed, digit_probabilities = detect_speed_schema(image_path)
    plate = detect_license_plate_schema(image_path)
    return speed, plate


def add_filter(image_model: ImageModel,
               map_image: Image = None) -> Image:
    # -> G Load image
    custom_image = CustomImage(image=image_model.image.resize((1920, 1080)))
    # -> P Add info to image
    custom_image.add_text_line(text=f"Biển kiểm soát: {image_model.license_plate if image_model.license_plate else 'Không rõ'}",
                            font=custom_image.font.md,
                            fill=ColorConst.WHITE.value,
                            is_border=True,
                            border_fill=ColorConst.BLACK.value)
    custom_image.add_text_line(text=f"Tốc độ ghi nhận: {str(image_model.speed) + ' (km/h)' if image_model.speed else 'Không rõ'}, Giới hạn tốc độ: {str(image_model.speed_limit) + ' (km/h)' if image_model.speed_limit else 'Không rõ'}",
                            font=custom_image.font.md,
                            fill=ColorConst.WHITE.value,
                            is_border=True,
                            border_fill=ColorConst.BLACK.value)
    custom_image.add_inv_text_line(text=f"Toạ độ ghi nhận: {str(image_model.longitude) + ', ' + str(image_model.latitude) if image_model.longitude and image_model.latitude else 'Không rõ'}",
                            font=custom_image.font.md,
                            fill=ColorConst.WHITE.value,
                            is_border=True,
                            border_fill=ColorConst.BLACK.value)
    custom_image.add_inv_text_line(text=f"{'Thời điểm ghi nhận: ' + image_model.record_time.strftime('%d/%m/%y %H:%M:%S') if image_model.record_time else ''}",
                            font=custom_image.font.md,
                            fill=ColorConst.WHITE.value,
                            is_border=True,
                            border_fill=ColorConst.BLACK.value)
    custom_image.save_image(f"{dir}/Filted.jpg")
    # -> G Load map image
    if(map_image):
        custom_map_image = CustomImage(image=map_image)
    else:
        blank_map = Image.open(f"{dir}/BlankedMap.jpg")
        custom_map_image = CustomImage(image=blank_map)
    # -> Y JOIN image & map
    custom_image.join_image(image_to_join=custom_map_image.image,
                            join_direction=JoinImageDirectionConst.RIGHT)
    custom_image.save_image(f"{dir}/JoinMap.jpg")

    # -> G Create info image
    info_image = Image.new('RGB',
                        (2000, 400),
                        ColorConst.WHITE.value)
    custom_info_image = CustomImage(info_image)
    # -> P Add info to info image
    image_info = image_model.describe()
    custom_info_image.add_text_line(text=image_info,
                                    fill=ColorConst.BLACK.value,
                                    font=custom_info_image.font.sm)
    custom_info_image.save_image(save_path=f"{dir}/InfoImage.jpg")
    # -> Y JOIN image & map & info image
    custom_image.join_image(image_to_join=custom_info_image.image,
                            join_direction=JoinImageDirectionConst.DOWN)
    custom_image.save_image(f"{dir}/JoinInfoImage.jpg")
    return custom_image.image

"""
# -> G Load image
image = Image.open(image_path)
custom_image = CustomImage(image=image) # Create an instance of CustomImage
print(custom_image.image.size)
# -> P Add info to image
custom_image.add_text_line(text=f"{'Biển kiểm soát: '+ image_model.license_plate if image_model.license_plate else ''}",
                           font=custom_image.font.md,
                           fill=ColorConst.WHITE.value,
                           is_border=True,
                           border_fill=ColorConst.BLACK.value)
custom_image.add_text_line(text=f"{'Tốc độ ghi nhận: '+ str(image_model.speed) + ' (km/h)' if image_model.speed else ''} {', Giới hạn tốc độ: '+ str(image_model.speed_limit) + ' (km/h)' if image_model.speed_limit else ''}",
                           font=custom_image.font.md,
                           fill=ColorConst.WHITE.value,
                           is_border=True,
                           border_fill=ColorConst.BLACK.value)
custom_image.add_inv_text_line(text=f"{'Toạ độ ghi nhận: (' + str(image_model.latitude) + ', ' + str(image_model.longitude) + ')' if image_model.record_time else ''}",
                           font=custom_image.font.md,
                           fill=ColorConst.WHITE.value,
                           is_border=True,
                           border_fill=ColorConst.BLACK.value)
custom_image.add_inv_text_line(text=f"{'Thời điểm ghi nhận: ' + image_model.record_time.strftime('%d/%m/%y %H:%M:%S') if image_model.record_time else ''}",
                           font=custom_image.font.md,
                           fill=ColorConst.WHITE.value,
                           is_border=True,
                           border_fill=ColorConst.BLACK.value)
# -> G Load map image
map_image = Image.open(map_image_path)
custom_map_image = CustomImage(image=map_image)
# -> Y JOIN image & map
custom_image.join_image(image_to_join=custom_map_image.image,
                        join_direction=JoinImageDirectionConst.RIGHT)
custom_image.save_image("Frontend/Images/Test/JoinMap.jpg")
print(custom_image.image.size)
# -> G Create info image
info_image = Image.new('RGB',
                       (2000, 400),
                       ColorConst.WHITE.value)
custom_info_image = CustomImage(info_image)
# -> P Add info to info image
image_info = image_model.describe()
custom_info_image.add_text_line(text=image_info,
                                fill=ColorConst.BLACK.value,
                                font=custom_info_image.font.sm)
custom_info_image.save_image(save_path="Frontend/Images/Test/InfoImage.jpg")
# -> Y JOIN image & map & info image
custom_image.join_image(image_to_join=custom_info_image.image,
                        join_direction=JoinImageDirectionConst.DOWN)
custom_image.save_image("Frontend/Images/Test/JoinInfoImage.jpg")
print(custom_image.image.size)

# Add text lines
custom_image.add_text_line("Hello, World!",
                           custom_image.font.sm,
                           fill=ColorConst.RED.value)
custom_image.add_text_line("Welcome to Pillow!",
                           custom_image.font.md,
                           fill=ColorConst.BLUE.value)
custom_image.add_text_line("Welcome to Pillow!",
                           custom_image.font.md,
                           fill=ColorConst.CYAN.value)
custom_image.add_inv_text_line("Custom Image",
                               custom_image.font.xl,
                               fill=ColorConst.GREEN.value,
                               is_border=True)
custom_image.add_inv_text_line("Custom Image",
                               custom_image.font.md,
                               fill=ColorConst.GRAY.value)
custom_image.add_inv_text_line("Custom Image",
                               custom_image.font.lg,
                               fill=ColorConst.ORANGE.value,
                               is_border=True)
custom_image.add_inv_text_line("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAsdasdasDasdasdasdasdasdas",
                               custom_image.font.xl,
                               fill=ColorConst.ORANGE.value,
                               is_border=True)

map_image = Image.open(io.BytesIO(image_bytes))
#custom_image.join_image(image_to_join=map_image,
#                        join_direction=JoinImageDirectionConst.RIGHT)
custom_map_image = CustomImage(image=map_image)
map_header_image = Image.new('RGB',
                       (1200, 100),
                       ColorConst.WHITE.value)
custom_map_header_image = CustomImage(image=map_header_image)
custom_map_header_image.add_text_line(text=f"Speed limit: {speed_limit} km/h",
                                      font=custom_map_header_image.font.lg,
                                      fill=ColorConst.RED.value,
                                      is_border=True,
                                      border_fill=ColorConst.ORANGE.value)
custom_map_image.join_image(image_to_join=custom_map_header_image.image,
                            join_direction=JoinImageDirectionConst.UP)

info_image = Image.new('RGB',
                       (1000, 1200),
                       ColorConst.WHITE.value)
custom_info_image = CustomImage(info_image)
custom_info_image.add_text_line(text=f"MORE INFO HERE",
                                fill=ColorConst.ORANGE.value,
                           font=custom_image.font.md,
                           is_border=True)

custom_map_image.join_image(image_to_join=custom_info_image.image,
                            join_direction=JoinImageDirectionConst.LEFT)


custom_image.join_image(image_to_join=custom_map_image.image,
                        join_direction=JoinImageDirectionConst.DOWN)

# Save the image
custom_image.save_image(save_path=output_image_path)
"""