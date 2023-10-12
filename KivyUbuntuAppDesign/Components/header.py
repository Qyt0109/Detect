from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

from Backend.Common.device_status import getBatteryStatus, getBluetoothStatus, getCurrentGPS, getInternetStatus
from Backend.Services.request import getMapInfoFromServer

class Header(BoxLayout):
    def settings(self):
        pass

class DeviceStatuses(BoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_gps = None
        self.map_info = None
        self.is_internet = None
        self.is_server = None
        self.is_bluetooth = None
        self.is_bluetooth_paired = None
        self.battery_charging_status = None

    def showNotification(self):

        popup = Popup(title='Notification',
                      pos_hint={'center_x': 0.5, 'center_y': 0.5},
                      size_hint=(0.8, 0.8))
        content = BoxLayout(orientation='vertical')
        content.add_widget(Button(text="Đóng", on_release=popup.dismiss))
        popup.content = content
        popup.open()

    def checkStatuses(self):
        self.checkStatusInternet()
        self.checkStatusGPS()
        self.checkStatusBluetooth()
        self.checkStatusBattery()
    
    def checkStatusGPS(self):
        status_gps = self.ids["status_gps"]
        status_gps.icon = "autorenew"
        status_gps.text_color = "orange"
        lon, lat = getCurrentGPS()
        if lon and lat:
            status_gps.icon = "map-marker"
            status_gps.text_color = "green"
            self.is_gps = True
        else:
            status_gps.icon = "map-marker-off"
            status_gps.text_color = "red"
            self.is_gps = False
    
    def getMapInfoFromServer(self):
        lon, lat = getCurrentGPS()
        if lon and lat:
            self.map_info = getMapInfoFromServer(lat, lon)
        if self.map_info:
            pass
        else:
            pass

    def checkStatusInternet(self):
        status_internet = self.ids["status_internet"]
        status_internet.icon = "autorenew"
        status_internet.text_color = "orange"
        getInternetStatus(result_callback = self.checkedStatusInternet)

    def checkedStatusInternet(self, internet_status):
        status_internet = self.ids["status_internet"]
        if internet_status:
            status_internet.icon = "web"
            status_internet.text_color = "green"
        else:
            status_internet.icon = "web-off"
            status_internet.text_color = "red"

    def checkStatusBluetooth(self):
        status_bluetooth = self.ids["status_bluetooth"]
        status_bluetooth.icon = "autorenew"
        status_bluetooth.text_color = "orange"
        bluetooth_status = getBluetoothStatus()
        if bluetooth_status:
            status_bluetooth.icon = "bluetooth"
            status_bluetooth.text_color = "green"
        else:
            status_bluetooth.icon = "bluetooth-off"
            status_bluetooth.text_color = "red"

    def checkStatusBattery(self):
        status_battery = self.ids["status_battery"]
        status_battery.icon = "autorenew"
        status_battery.text_color = "orange"
        self.battery_charging_status, battery_percent = getBatteryStatus()
        str_chargeing = "-charging" if self.battery_charging_status else ""
        percent = round(battery_percent / 10) * 10
        if percent <= 30:
            text_color = "red"
        elif percent <= 60:
            text_color = "orange"
        else:
            text_color = "green"
        if percent == 0:
            percent = "-outline"
        elif percent == 100:
            percent = ""
        else:
            percent = f"-{percent}"
        status_battery.icon = f"battery{str_chargeing}{percent}"
        status_battery.text_color = text_color

class Status(Button):
    pass