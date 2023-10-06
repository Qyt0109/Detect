# region G IMPORT
# Import modules
from enum import Enum
import os
import time
from datetime import datetime
import sys
from typing import Tuple
import cv2
from PIL import Image
# Import modules

# Enviroment variables
from Env.env import device_id
# Enviroment variables

# PyQt6
from PyQt6.QtCore import QSize, Qt, QUrl, QByteArray, QBuffer, QThread, pyqtSignal, QEvent
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtMultimedia import QCamera
from PyQt6.QtMultimedia import QMediaDevices
from PyQt6.QtMultimediaWidgets import *
from PyQt6 import uic
from Frontend.Models.models import ImageModel
from Backend.Services.image_processing import add_filter, get_speed_plate
from main_app_ui import *
# PyQt6

# Frontend constant variable
from Frontend.Constants.name_constants import APP_TITLE
# Frontend constant variable

# Frontend models
from Frontend.Models.history_queue import QueueEvent, MaxSizeQueue
from Frontend.Models.qt_models import CameraCapturedImage, Timer, TimerMode
# Frontend models

# Backend services
from Backend.Common.gps import get_current_gps
from Backend.Services.request import get_map_info_from_server, MapInfo
from Backend.Database.local_database import DatabaseManager, ImageDatabaseManager
# Backend services

# endregion G IMPORT

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
yes_path = "Resources/PNG/Yes.png"
no_path = "Resources/PNG/No.png"

TEST_MODE = True
TEST_IMAGE_PATH = "Frontend/Images/Test/Test.jpg"

# database_manager = DatabaseManager()


class CameraThread(QThread):
    image_update = pyqtSignal(QImage)

    def __init__(self, parent=None, camera_index = 0):
        super().__init__(parent)
        self.is_active = False
        self.is_paused = False
        self.camera_index = camera_index
        self.frame = None
        self.capture = cv2.VideoCapture(self.camera_index)

    def start_camera(self, camera_index=0):
        self.camera_index = camera_index
        self.is_active = True
        self.is_paused = False
        self.start()

    def stop_camera(self):
        self.is_active = False

    def pause_camera(self):
        self.is_paused = True

    def resume_camera(self):
        self.is_paused = False

    def capture_camera(self):
        return self.frame
        """
        if self.frame:
            image_folder = "Images/CapturedImages"
            os.makedirs(image_folder, exist_ok=True)
            file_path = os.path.join(image_folder, image_name)
            print(file_path)
            self.frame.save(file_path)
        """

    def run(self):
        #capture = cv2.VideoCapture(self.camera_index)
        while self.is_active:
            ret, frame = self.capture.read()
            if ret:
                if not self.is_paused:
                    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    # image = cv2.flip(image, 1)             # Flip the image

                    # Convert numpy array to bytes buffer
                    height, width, channel = image.shape
                    bytes_per_line = 3 * width
                    qt_format = QImage(image.data,
                                       width,
                                       height,
                                       bytes_per_line,
                                       QImage.Format.Format_RGB888)
                    
                    # Store the current frame
                    self.frame = qt_format

                    # Emit the image signal
                    self.image_update.emit(qt_format)

        self.capture.release()

def pil_image_to_pyqt_pixmap(pil_image: Image.Image):
    # Convert PIL Image to raw image data in RGB mode (without alpha channel)
    byte_array = pil_image.convert("RGB").tobytes()

    # Convert raw image data to QImage
    qimage = QImage(byte_array, pil_image.width, pil_image.height, QImage.Format.Format_RGB888)

    # Convert QImage to QPixmap
    qpixmap = QPixmap.fromImage(qimage)

    return qpixmap

def setup_label_icon(label:QLabel,
                     size:int = 28,
                     text:str = None,
                     icon:QPixmap = None):
    label.setMinimumSize(QSize(size, size))
    label.setMaximumSize(QSize(size, size))
    label.setScaledContents(True)
    if text:
        label.setText(text)
    if icon:
        label.setPixmap(icon)

def set_button_icon_size(button:QPushButton,
                   icon_size:int = 28,
                   align:str = None):
    button.setIconSize(QSize(icon_size, icon_size))
    style = "QPushButton {background-color: rgba(128, 200, 255, 0.2); border: 2px solid black; border-radius: 15px; padding: 5px;"
    if align:
        style += f"text-align: {align};"
    style += "} QPushButton:hover {background-color: rgba(128, 200, 255, 0.6);}"
    button.setStyleSheet(style)

def setup_button(button:QPushButton,
                 icon_size:int = 48,
                 text:str = None,
                 icon:QIcon = None):
    set_button_icon_size(button, icon_size, "left")
    if text:
        button.setText(text)
    if icon:
        button.setIcon(icon)

from Backend.Database.Components.db_session import default_session, Session
from Backend.Database.Components.db_models import ViolationImage as ImageDB

from sqlalchemy import desc, func

   
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setup_all()
        self.is_query_database_mode = False
    
# region SETUP
    def setup_all(self):
        self.setup_main_ui()
        self.setup_history_queue()
        self.setup_map()
        self.setup_camera()
        self.setup_icons()
        self.setup_buttons()

    def setup_main_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(APP_TITLE + " - TEST MODE" if TEST_MODE else APP_TITLE)
        self.ui.frame_info.setMaximumWidth(200)
        # self.setMaximumSize(800, 500)
        self.switch_to_capture_image()

    def add_event(self, event):
        self.queue.put(event)
        events = sorted(list(self.queue.queue),
                        key=lambda x: x.time,
                        reverse=True)
        history = ""
        for event in events:
            history += f"{event.time}: {event.event}\n"
        self.ui.plainTextEdit_history_event.setPlainText(history)

    def setup_history_queue(self):
        self.queue = MaxSizeQueue(10)
        self.ui.plainTextEdit_history_event.setMaximumWidth(400)
        if TEST_MODE:
            self.add_event(QueueEvent("TEST MODE ENABLED"))

    def setup_icons(self):
        setup_label_icon(self.ui.label_server,
                         icon=QPixmap(server_on_path))
        setup_label_icon(self.ui.label_internet,
                         icon=QPixmap(wifi_on_path))
        setup_label_icon(self.ui.label_bluetooth,
                         icon=QPixmap(bluetooth_on_path))

    def setup_buttons(self):
        setup_button(self.ui.pushButton_fn1,
                     icon=QIcon(camera_capture_path))
        self.ui.pushButton_fn1.clicked.connect(self.capture_camera_image)
        setup_button(self.ui.pushButton_fn2,
                     icon=QIcon(yes_path))
        self.ui.pushButton_fn2.clicked.connect(self.accept_captured_image)
        setup_button(self.ui.pushButton_fn3,
                     icon=QIcon(no_path))
        self.ui.pushButton_fn3.clicked.connect(self.remove_captured_image)

# endregion SETUP

# region MAP
    def setup_map(self):
        setup_label_icon(self.ui.label_map_icon)
        self.map_info = None
        self.ui.label_map_icon.setPixmap(QPixmap(gps_off_path))
        self.get_map()
    
    def get_map(self):
        self.ui.label_map_info.setText("Xin đợi...")
        lon, lat = get_current_gps()
        if lon and lat:
            self.map_info = get_map_info_from_server(longitude=lon, latitude=lat)
        else:
            noity = "Không lấy được thông tin toạ độ"
            self.add_event(QueueEvent(noity))
            self.ui.label_map_icon.setPixmap(QPixmap(gps_off_path))
            self.ui.label_map_info.setText(noity)
            return

        if self.map_info:
            noity = f"Lấy thông tin bản đồ thành công (Số hiệu kế hoạch: {self.map_info.plan_id}\n({lon:.4f}, {lat:.4f}))"
            self.add_event(QueueEvent(noity,"16/07/2023 16:40:27"))   # -> R  nho bo record_time di
            self.ui.label_map_icon.setPixmap(QPixmap(gps_on_path))
            self.ui.label_map_info.setText(f"Số hiệu kế hoạch: {self.map_info.plan_id}\n({lon:.4f}, {lat:.4f})")
        else:
            noity = "Không lấy được thông tin bản đồ"
            self.add_event(QueueEvent(noity))
            self.ui.label_map_icon.setPixmap(QPixmap(gps_off_path))
            self.ui.label_map_info.setText(noity)

# endregion MAP

# region CAMERA
    def setup_camera(self):
        # Camera
        setup_label_icon(self.ui.label_image_status_icon)
        self.camera_off_view()
        self.capture_image = None   # Variable to store the image data as bytes
        self.view_image = None    # Accepted image stored here
        self.ui.frame_view_image.resizeEvent = self.update_image_size
        self.camera = CameraThread(camera_index=0)
        self.camera.start_camera()
        self.camera.image_update.connect(self.update_camera_frame)
        self.camera_on_view()
        # Camera

        # Camera timer
        self.camera_timer = Timer(timer_mode=TimerMode.DOWN.value,
                                  time_limit=10)
        self.camera_timer.time_changed.connect(self.display_timer)
        # Camera timer

    def camera_off_view(self):
        self.ui.label_image_status_icon.setPixmap(QPixmap(server_off_path))
        self.ui.label_image_status_info.setText("Không kết nối")

    def camera_pause_view(self, time = None):
        self.camera.pause_camera()
        self.ui.label_image_status_icon.setPixmap(QPixmap(camera_pause_path))
        noity = "Tạm ngưng..."
        if time:
            noity += f"\nTiếp tục sau {time} s"
        self.ui.label_image_status_info.setText(noity)

    def camera_on_view(self):
        self.switch_to_capture_image()
        self.camera.resume_camera()
        self.ui.label_image_status_icon.setPixmap(QPixmap(camera_on_path))
        self.ui.label_image_status_info.setText("Đã kết nối")

    def toogle_camera(self):
        if self.camera.is_active and self.camera.is_paused:
            self.camera_on_view()
        else:
            self.camera_pause_view()
    
    def update_camera_frame(self, frame_image):
        # REPONSIVE VIEW
        # Calculate the width for scaling
        scaled_width = self.ui.frame_camera.width() - 40  # Subtract a margin of 20 (adjust as needed)

        # Scale the QImage to fit the width while preserving the aspect ratio
        scaled_image = frame_image.scaledToWidth(scaled_width)

        # Convert the scaled QImage to a QPixmap and update the QLabel
        self.ui.label_camera_frame.setPixmap(QPixmap.fromImage(scaled_image))
        #self.ui.label_image_status_icon.setPixmap(QPixmap(camera_pause_path))
        #noity = "Tạm ngưng..."
        #time = 12
        #if time:
        #    noity += f"\nTiếp tục sau {time} s"
        #self.ui.label_image_status_info.setText(noity)
        #self.ui.label_camera_frame.setPixmap(QPixmap("added.jpg").scaledToWidth(scaled_width))

    def update_image_size(self, event):
        self.display_image()
    
    def display_image(self):
        if self.view_image:
            qpixmap = pil_image_to_pyqt_pixmap(self.view_image.image)
            # RESPONSIVE VIEW
            # Calculate the width for scaling
            scaled_width = self.ui.frame_view_image.width() - 40  # Subtract a margin (adjust as needed)

            # Convert the scaled QImage to a QPixmap and update the QLabel
            self.ui.label_view_image.setPixmap(qpixmap.scaledToWidth(scaled_width))
    
    def switch_to_view_image(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_view_image_info)

    def switch_to_capture_image(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_capture_image)
    
    def capture_camera_image(self):
        self.camera_pause_view()
        captured_image = self.camera.capture_camera()
        self.capture_image = CameraCapturedImage(captured_image)
        self.update_camera_frame(captured_image)
        self.camera_timer.reset()
        self.camera_timer.start()
    
    def accept_captured_image(self):
        accepted_captured_image_temp_path = "Frontend/Images/Temp/AcceptedCapturedImageTemp.jpg"
        if self.capture_image:
            self.capture_image.image.save(accepted_captured_image_temp_path)
            if TEST_MODE:
                accepted_captured_image_temp_path = TEST_IMAGE_PATH # -> For testing only
            self.ui.label_view_image_info.setText("Xem thông tin hình ảnh vi phạm")
            spd, plate = get_speed_plate(accepted_captured_image_temp_path)
            image = Image.open(accepted_captured_image_temp_path)
            image_model = ImageModel(image=image,
                                     license_plate=plate,
                                     speed=spd,
                                     speed_limit=self.map_info.speed_limit if self.map_info else None,
                                     record_time=self.capture_image.record_time,
                                     latitude=self.map_info.latitude if self.map_info else None,
                                     longitude=self.map_info.longitude if self.map_info else None,
                                     device_info=device_id,
                                     distance=None,
                                     name=None,
                                     road_address=None,
                                     description=None,
                                     vehicle_type=None,
                                     capture_direction=None)
            filted_image = add_filter(image_model=image_model,
                                      map_image=self.map_info.image if self.map_info else None)
            filted_image_model = image_model
            filted_image_model.image = filted_image
            self.view_image = filted_image_model
            self.capture_image = None
            self.camera_timer.stop()
            self.camera_pause_view()
            self.switch_to_view_image()
            image_info = self.view_image.describe()
            self.ui.plainTextEdit_view_image_info.setPlainText(image_info)
            self.display_image()
            #self.update_accepted_image()

    def save_captured_image(self):
        if self.view_image:
            if self.view_image.save_to_database():
                self.add_event(QueueEvent("Đã lưu hình ảnh vi phạm"))
                self.view_image = None
            else:
                self.add_event(QueueEvent("Không thể lưu hình ảnh vi phạm (Có thể do một số thông tin bị thiếu)"))
            self.camera_on_view()

    def remove_captured_image(self):
        self.capture_image = None
        self.view_image = None
        self.camera_timer.timer.stop()
        self.camera_on_view()

    def display_timer(self, time):
        if not self.camera_timer.timer.isActive():
            self.camera_on_view()
            return
        self.camera_pause_view(time)

    def test(self):
        self.ui.label_test_icon.setPixmap(QPixmap("Resources/PNG/Yes.png").scaledToWidth(48))
        self.camera_pause_view(2)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_test)
        
# endregion CAMERAd

    #def query_database_view(self, image_model:ImageModel):
    def query_database_view(self, image_model:ImageModel):
        self.switch_to_view_image()
        self.ui.label_view_image_info.setText("Xem thông tin hình ảnh vi phạm vừa chụp")
    
    def return_camera_view(self):
        self.switch_to_capture_image()
        self.ui.label_view_image_info.setText("Xem hình ảnh vi phạm trong kho ảnh")

    def toggle_query_database_mode(self):
        self.is_query_database_mode = not self.is_query_database_mode
        if self.is_query_database_mode:
            print("Query mode")
            self.image_manager = ImageDatabaseManager()
            self.query_database_view()
        else:
            print("Camera mode")
            self.image_manager = None
            self.return_camera_view()
   
    # Event handler to capture the key press
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_M:
            self.get_map()
        if event.key() == Qt.Key.Key_C:
            self.capture_camera_image()
            print("captured")
        if event.key() == Qt.Key.Key_P:
            self.toogle_camera()
        if event.key() == Qt.Key.Key_S:
            self.save_captured_image()
        if event.key() == Qt.Key.Key_A:
            self.accept_captured_image()
        if event.key() == Qt.Key.Key_R:
            self.remove_captured_image()
        if event.key() == Qt.Key.Key_D:
            self.toggle_query_database_mode()
        if event.key() == Qt.Key.Key_Left:
            if self.is_query_database_mode:
                print("LEFT KEY PRESSED")
                pass
        if event.key() == Qt.Key.Key_Right:
            if self.is_query_database_mode:
                print("RIGHT KEY PRESSED")
                pass
        
        if event.key() == Qt.Key.Key_T:
            self.test()    
    

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
