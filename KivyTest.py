from kivy.app import App
from kivy.uix.image import Image
from io import BytesIO
from PIL import Image as PILImage

class PILImageApp(App):
    def build(self):
        # Load the PIL image
        pil_image = PILImage.open("test.jpg")
        
        # Convert the PIL image to BytesIO
        img_buffer = BytesIO()
        pil_image.save(img_buffer, format='jpeg')
        
        # Create a Kivy Image widget and set its source to the BytesIO data
        kivy_image = Image(source=img_buffer, allow_stretch=True)
        
        return kivy_image

if __name__ == '__main__':
    PILImageApp().run()
