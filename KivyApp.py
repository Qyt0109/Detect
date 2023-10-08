from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, FadeTransition, FallOutTransition
from kivy.lang import Builder

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout


from kivy.uix.button import Button
from kivy.uix.widget import Widget

from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty

Config.set('graphics', 'width', 1200)
Config.set('graphics', 'height', 800)


"""Layouts
"""

server_on_path = "Resources/PNG/ServerOn.png"
server_off_path = "Resources/PNG/ServerOff.png"
wifi_on_path = "Resources/PNG/WifiOn.png"
wifi_off_path = "Resources/PNG/WifiOff.png"
bluetooth_on_path = "Resources/PNG/BluetoothOn.png"
bluetooth_off_path = "Resources/PNG/BluetoothOff.png"
bell_path = "Resources/PNG/Bell.png"
camera_on_path = "Resources/PNG/CameraOn.png"
camera_off_path = "Resources/PNG/CameraOff.png"
camera_retake_path = "Resources/PNG/CameraRetake.png"
camera_pause_path = "Resources/PNG/CameraPause.png"
gps_on_path = "Resources/PNG/GPSOn.png"
gps_off_path = "Resources/PNG/GPSOff.png"

camera_capture_path = "Resources/PNG/CameraCapture.png"
image_gallery_path = "Resources/PNG/ImageGallery.png"
yes_path = "Resources/PNG/Yes.png"
no_path = "Resources/PNG/No.png"
TEST_IMAGE_PATH = "Frontend/Images/Test/Test.jpg"

class MainLayout(BoxLayout):
    pass

class HeaderLayout(BoxLayout):
    pass

class FooterLayout(BoxLayout):
    capturing_image_button_image_path = camera_capture_path
    image_gallery_button_image_path = image_gallery_path

    pass

class ScreenLayoutManager(ScreenManager):
    pass

class CapturingImageScreenLayout(Screen):
    pass

class CapturedImageScreenLayout(Screen):
    pass

class ImageGalleryScreenLayout(Screen):
    pass



"""App
"""
design = Builder.load_file('KivyMain.kv')

class KivyMainApp(App):
    def build(self):
        return design

if __name__ == '__main__':
    app = KivyMainApp()
    app.run()
