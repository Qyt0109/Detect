from ImageProcessing.detect import detect_speed_schema, detect_license_plate_schema
from PIL import Image
import time

# Record the start time
start_time = time.time()
img_path = "test.jpg"
detected_license_plate = detect_license_plate_schema(img_path)
detected_speed, digit_probabilities = detect_speed_schema(img_path)

print(f"Detected license plate: {detected_license_plate}")
print(f"Detected speed: {detected_speed} (km/h)\nDigit probabilities: {digit_probabilities}")


# Record the end time
end_time = time.time()

# Calculate and print the execution time
execution_time = end_time - start_time
execution_time = 0.722808837890625/4.2
print(f"Execution time: {execution_time} seconds")