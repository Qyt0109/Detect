import base64
import io
import json
from Backend.Models.models import MapInfo, ViolationImageModel
from Env.env import server_url, device_id, api_server_url
from http import HTTPStatus
import requests
from datetime import datetime
from PIL import Image

def getMapInfoFromServer(latitude:float,
                        longitude:float)->MapInfo:
    """-> MapInfo(image, speed_limit, plan_id, latitude, longitude) | None"""
    # Get the current date and time
    now = datetime.now()
    # Format the date as "DD/MM/YYYY"
    date_work = now.strftime("%d/%m/%Y")
    date_work = "26/07/2023" # Fake date_work
    get_map_url = f"{api_server_url}/api/v1/plan-patrol/map-by-device?DeviceInfo={device_id}&Latitude={latitude}&Longitude={longitude}&DateWork={date_work}"
    print(get_map_url)
    # Get map from api server
    response = requests.request(method="GET",
                                url=get_map_url)
    """Example response:
    {
        "code": 200,
        "message": "successful",
        "err": "",
        "time": "2023-07-25T01:51:47.0844909+07:00",
        "data":
            {
                "maxSpeed": 60,
                "planId": 1,
                "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUg_IMAGE_DATA_IN_BYTES..."
            }
    }
    """
    if response.status_code == HTTPStatus.OK:
        response_json = response.json()
        #print(response_json)
        # The image data in bytes is available in the response content
        image_data = response_json["data"]["image"]
        _, image_data_base64 = image_data.split(",", 1)  # Remove the "data:image/png;base64," part
        image_bytes = base64.b64decode(image_data_base64)
        image = Image.open(io.BytesIO(image_bytes))
        #print(image_bytes)
        speed_limit = response_json["data"]["maxSpeed"]
        plan_id = response_json["data"]["planId"]
        map_info = MapInfo(image= image,
                           speed_limit=speed_limit,
                           plan_id=plan_id,
                           latitude=latitude,
                           longitude=longitude)
        return map_info
        # Now you can process the image_bytes as needed (e.g., save it to a file, display it, etc.).
    else:
        # TODO: REAL HANDLE THE ERROR
        # If the request was unsuccessful, handle the error
        print(f"Error: {response.status_code} - {response.json()}")
        image = Image.open("Frontend/Images/Map/map.png")
        return MapInfo(image=image,
                       speed_limit=90,
                       plan_id=2,
                       latitude=latitude,
                       longitude=longitude)

# Define the function to send a POST request with the ViolationImageModel instance
def send_violation_image(image_model: ViolationImageModel):
    # Convert the image_model instance to a dictionary
    data = {
        "Name": image_model.name,
        "Data": image_model.data.decode(),  # Convert bytes to UTF-8 string
        "LicensePlate": image_model.license_plate,
        "Speed": image_model.speed,
        "SpeedLimit": image_model.speed_limit,
        "Distance": image_model.distance,
        "RecordTime": image_model.record_time.strftime("%d/%m/%Y %H:%M:%S"),
        "Latitude": image_model.latitude,
        "Longitude": image_model.longitude,
        "RoadAddress": image_model.road_address,
        "DeviceInfo": image_model.device_info,
        "VehicleType": image_model.vehicle_type,
        "CaptureDirection": image_model.capture_direction
    }

    # Convert the data to JSON format
    json_data = json.dumps(data)

    # Set the headers for the request
    headers = {'Content-Type': 'application/json'}

    # Send the POST request
    url = f"{api_server_url}/api/v1/violation/create"
    response = requests.post(url, data=json_data, headers=headers)

    # Check the response status code
    if response.status_code == 200:
        print("POST request successful")
    else:
        print(f"POST request failed with status code: {response.status_code}")
        print(response.text)

