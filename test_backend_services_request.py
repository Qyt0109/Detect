# Example usage:
from datetime import datetime
from PIL import Image
from Backend.Common.image_features import CustomImage

from Backend.Models.models import ViolationImageModel
from Backend.Services.request import send_violation_image

if __name__ == "__main__":
    # Create an instance of ViolationImageModel
    image = Image.open("test.jpg")
    custom_image = CustomImage(image)
    image_data = custom_image.to_bytes()
    image_model = ViolationImageModel(
        data=image_data,
        license_plate="29-x10 32203",
        speed=40,
        speed_limit=30,
        record_time=datetime.now(),
        latitude=20.998579,
        longitude=105.813437,
        device_info="serial number",
        distance=100,
        name="tên ảnh",
        road_address="nguyen trai",
        description="Description here",
        vehicle_type="car",
        capture_direction="Front"
    )

    # Send the POST request with the image_model instance as a parameter
    send_violation_image(image_model)