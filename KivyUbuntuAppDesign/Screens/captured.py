from datetime import datetime
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from PIL import Image
import subprocess

class CapturedScreen(Screen):
    image_source = StringProperty("")
    def on_image_captured(self, image_path, application):
        image = Image.open(image_path)
        temp_image_path = "KivyUbuntuAppDesign/Temp/TempCapturedImage.jpg"
        image.save(temp_image_path)
        command = 'python3 test_detect.py'
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result)
        self.image_source = temp_image_path