from PIL import Image
import base64
import io

# Load the original image using PIL.Image.open() or any other method.
# For example:
original_image = Image.open("test.jpg")

# Perform any processing or modifications to the original image if needed.

# Save the modified image to bytes.
with io.BytesIO() as byte_io:
    original_image.save(byte_io, format='JPEG')
    byte_io.seek(0)
    image_bytes = byte_io.read()
base64_image_bytes = base64.b64encode(image_bytes).decode('utf-8')
print(len(base64_image_bytes))

# Now, you have the image saved as bytes.
# You can send the bytes to another process, store it in a database, or do anything you want.

# To create a new PIL Image object from the bytes data:
new_image = Image.open(io.BytesIO(image_bytes))
new_image.save("output.jpg")
print("Saved to output.jpg")
# Now, you have a new PIL Image object created from the bytes data.
