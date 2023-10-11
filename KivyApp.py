from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, FadeTransition, FallOutTransition
from kivy.lang import Builder

from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFloatingActionButton
from kivy.uix.stacklayout import StackLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup


from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.graphics.texture import Texture

from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty



#Config.set('graphics', 'width', 1200)
#Config.set('graphics', 'height', 800)
Window.size=(800, 400)

"""Layouts
"""

class MainLayout(MDBoxLayout):
    pass

class HeaderLayout(MDBoxLayout):
    pass

class FooterLayout(MDBoxLayout):
    pass

class ScreenSwitchLayout(MDBoxLayout):

    def onGoToCapturingImageScreenButtonPress(self, button):
        button1 = self.ids._go_to_capturing_image_screen_button_
        button2 = self.ids._go_to_image_gallery_screen_button_

        button1.disabled = True
        #button1.background_color = ColorRGBA.WHITE.value
        
        button2.disabled = False
        #button2.background_color = ColorRGBA.TRANSPARENT.value

        app.switchScreen('capturing_image_screen_')
    def onGoToImageGalleryScreenButtonPress(self, button):
        button1 = self.ids._go_to_capturing_image_screen_button_
        button2 = self.ids._go_to_image_gallery_screen_button_

        button1.disabled = False
        #button1.background_color = ColorRGBA.TRANSPARENT.value
        
        button2.disabled = True
        #button2.background_color = ColorRGBA.WHITE.value

        app.switchScreen('image_gallery_screen_')

class ScreenLayoutManager(ScreenManager):
    pass

class CapturingImageScreenLayout(Screen):
    pass

class CapturedImageScreenLayout(Screen):
    pass

class ImageGalleryScreenLayout(Screen):
    pass


class DeviceStatusLayout(MDBoxLayout):
    def showNotification(self):

        popup = Popup(title='Notification',
                      pos_hint={'center_x': 0.5, 'center_t': 0.5},
                      size_hint=(0.6, 0.8))
        content = MDBoxLayout(orientation='vertical')
        content.add_widget(MDFloatingActionButton(
            icon="close-box", text_color="red", on_release=popup.dismiss))
        content.add_widget(Button(text='Other Action'))
        popup.content = content
        popup.open()

        

    def dismissPopup(self, instance):
        instance.parent.parent.dismiss()

class DeviceStatusPopupLayout(Popup):
    pass

class CaptureImageHolderLayout(FloatLayout):
    pass

from Backend.Common.device_status import getInternetStatus, getCurrentGPS, getDiskStatus
from Backend.Services.request import getMapInfoFromServer
from Backend.Models.models import MapInfo, ViolationImageModel

"""App
"""
#design = Builder.load_file('KivyMainDesign.kv')
class KivyMainApp(MDApp):
    map_info = MapInfo()
    def build(self):
        design = Builder.load_file('KivyMainDesign.kv')
        return design
    
    def on_start(self):
        self.checkStatus()
    
    def switchScreen(self, screen_name):
        self.root.ids["screen_manager"].current = screen_name

    def checkStatus(self, status=None):
        device_statuses = self.root.ids["_header_layout_"].ids["_device_status_layout_"]
        status_gps = device_statuses.ids["_status_gps_"]
        status_internet = device_statuses.ids["_status_internet_"]
        if status == None or status == "GPS":
            status_gps.icon = "autorenew"
            status_gps.text_color = "orange"
            lon, lat = getCurrentGPS()
            if lon and lat:
                status_gps.icon = "map-marker"
                status_gps.text_color = "green"
                self.map_info = getMapInfoFromServer(lat, lon)
                if self.map_info:
                    pass
                else:
                    pass
                print(self.map_info)
            else:
                status_gps.icon = "map-marker-off"
                status_gps.text_color = "red"
        if status == None or status == "INTERNET":
            status_internet.icon = "autorenew"
            status_internet.text_color = "orange"
            getInternetStatus(result_callback=self.checkedInternet)

    def checkedInternet(self, internet_status):
        device_statuses = self.root.ids["_header_layout_"].ids["_device_status_layout_"]
        status_internet = device_statuses.ids["_status_internet_"]
        if internet_status:
            status_internet.icon = "web"
            status_internet.text_color = "green"
        else:
            status_internet.icon = "web-off"
            status_internet.text_color = "red"


            





if __name__ == '__main__':
    app = KivyMainApp()
    app.run()
