from kivy.uix.floatlayout import FloatLayout
import time
import numpy
from PIL import Image



class CapturingCamera(FloatLayout):
    def capture(self, callback = None, save_path:str = None):
        camera = self.ids.capturing_camera
        texture = camera.texture
        size = texture.size
        pixels = texture.pixels
        image = Image.frombytes(mode='RGBA', size=size,data=pixels)
        if callback:
            callback(image)
        if save_path:
            camera.export_to_png(save_path)
        print("Captured")
        return image

    def change_camera(self, index = None):
        camera = self.ids.capturing_camera
        if index:
            camera.index = index
        else:
            camera.index = 0 if camera.index == 1 else 1

    def turn(self, is_on = None):
        camera = self.ids.capturing_camera
        if is_on:
            camera.play = is_on
        else:
            camera.play = not camera.play