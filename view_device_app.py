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
from PyQt6.QtGui import QPixmap, QImage, QIcon
from PyQt6.QtMultimedia import QCamera
from PyQt6.QtMultimedia import QMediaDevices
from PyQt6.QtMultimediaWidgets import *
from PyQt6 import uic
from Frontend.Models.models import ImageModel
from Backend.Services.image_processing import add_filter, get_speed_plate
from view_device_ui import *
# PyQt6

# Frontend constant variable
#from Frontend.Constants.name_constants import APP_TITLE
# Frontend constant variable

# Frontend models
from Frontend.Models.history_queue import QueueEvent, MaxSizeQueue
#from Frontend.Models.qt_models import CameraCapturedImage, Timer, TimerMode
# Frontend models

# Backend services
#from Backend.Common.gps import get_current_gps
#from Backend.Services.request import get_map_info_from_server, MapInfo
#from Backend.Database.local_database import DatabaseManager, ImageDatabaseManager
# Backend services

# endregion G IMPORT


bluetooth_on_path = "Resources/PNG/BluetoothOn.png"
bluetooth_off_path = "Resources/PNG/BluetoothOff.png"
bell_path = "Resources/PNG/Bell.png"



def pil_image_to_pyqt_pixmap(pil_image: Image.Image):
    copy_image = pil_image.copy()
    # Convert PIL Image to raw image data in RGB mode (without alpha channel)
    byte_array = copy_image.convert("RGB").tobytes()

    # Convert raw image data to QImage
    qimage = QImage(byte_array, pil_image.width, pil_image.height, QImage.Format.Format_RGB888)

    # Convert QImage to QPixmap
    qpixmap = QPixmap.fromImage(qimage)

    return qpixmap


def set_label_icon_size(label:QLabel,
                   size:int = 28):
    label.setMinimumSize(QSize(size, size))
    label.setMaximumSize(QSize(size, size))
    label.setScaledContents(True)

def set_button_icon_size(button:QPushButton,
                   icon_size:int = 28,
                   align:str = None):
    button.setIconSize(QSize(icon_size, icon_size))
    style = "QPushButton {background-color: rgba(128, 200, 255, 0.2); border: 2px solid black; border-radius: 15px; padding: 5px;"
    if align:
        style += f"text-align: {align};"
    style += "} QPushButton:hover {background-color: rgba(128, 200, 255, 0.6);}"
    button.setStyleSheet(style)

from Backend.Database.Components.db_session import default_session, Session
from Backend.Database.Components.db_models import ViolationImage as ImageDB

from sqlalchemy import desc, func

   
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setup_all()
        self.setup_icons()
        self.image = Image.open("Resources/PNG/JoinedImage.jpg")
        self.display_image()
        self.display_image_query()
        self.is_view_image_mode = True
    
# region SETUP
    def setup_all(self):
        self.setup_main_ui()
        self.showFullScreen()
        self.setup_history_queue()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_capture_image)
        self.resizeEvent = self.window_resize_event

    def window_resize_event(self, event):
        print("display")
        self.display_image()
        self.display_image_query()
    
    def display_image(self):
        if self.image:
            print("display image")
            qpixmap = pil_image_to_pyqt_pixmap(self.image)
            # RESPONSIVE VIEW
            # Calculate the width for scaling
            scaled_width = self.ui.frame_image.width() - 150  # Subtract a margin (adjust as needed)

            # Convert the scaled QImage to a QPixmap and update the QLabel
            self.ui.label_image.setPixmap(qpixmap.scaledToWidth(scaled_width))

    
    def display_image_query(self):
        if self.image:
            print("display query image")
            qpixmap = pil_image_to_pyqt_pixmap(self.image)
            #qpixmap = QPixmap("Resources/PNG/JoinedImage.jpg")
            # RESPONSIVE VIEW
            # Calculate the width for scaling
            scaled_width = self.ui.frame_image.width() -  150 # Subtract a margin (adjust as needed)

            # Convert the scaled QImage to a QPixmap and update the QLabel
            self.ui.label_image_query.setPixmap(qpixmap.scaledToWidth(scaled_width))

    def setup_main_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def add_event(self, event):
        self.queue.put(event)
        events = sorted(list(self.queue.queue),
                        key=lambda x: x.time,
                        reverse=True)
        history = ""
        for event in events:
            history += f"{event.time}: {event.event}\n"
        self.ui.plainTextEdit_info.setPlainText(history)

    def setup_history_queue(self):
        self.queue = MaxSizeQueue(10)

    def setup_icons(self):
        # -> R MAIN WINDOW
        self.setWindowTitle("THIẾT BỊ TRUY CẬP")
        # -> R CAPTURED IMAGE INFO
        self.ui.label_info_header.setText("THÔNG TIN")
        self.ui.plainTextEdit_info.setPlainText("Biển kiểm soát: 99A-05517\t\
                                    Tốc độ ghi nhận: 52(km/h)\t\
                                    Tốc độ giới hạn: 60(km/h)\t\
                                    Thời điểm ghi nhận: 2023-07-29 14:56:11.619538\t\
                                    Vị trí ghi nhận: (21.007347222222222, 105.84743666666667)\t\
                                    Thiết bị ghi nhận: device_01\t\
                                    Ghi chú: ")
        # -> R QUERY IMAGE INFO
        self.ui.label_info_header_query.setText("THÔNG TIN")
        self.ui.plainTextEdit_info_query.setPlainText("Biển kiểm soát: 99A-05517\t\
                                    Tốc độ ghi nhận: 52(km/h)\t\
                                    Tốc độ giới hạn: 60(km/h)\t\
                                    Thời điểm ghi nhận: 2023-07-29 14:56:11.619538\t\
                                    Vị trí ghi nhận: (21.007347222222222, 105.84743666666667)\t\
                                    Thiết bị ghi nhận: device_01\t\
                                    Ghi chú: ")
        # -> R MENU INFO
        #self.ui.label_section_info.setText("CHỨC NĂNG > XEM HÌNH ẢNH ĐÃ CHỤP")
        self.ui.label_section_info.setText("CHỨC NĂNG > DUYỆT KHO ẢNH")
        set_button_icon_size(self.ui.pushButton_menu, 48)
        self.ui.pushButton_menu.clicked.connect(self.toggle_menu)
        self.ui.pushButton_menu.setIcon(QIcon("Resources/PNG/Menu.png"))
        set_button_icon_size(self.ui.pushButton_slot1,48,"left")
        self.ui.pushButton_slot1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_capture_image))
        self.ui.pushButton_slot1.setIcon(QIcon("Resources/PNG/Picture.png"))
        self.ui.pushButton_slot1.setText("Xem hình ảnh")
        set_button_icon_size(self.ui.pushButton_slot2,48,"left")
        self.ui.pushButton_slot2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_query))
        self.ui.pushButton_slot2.setIcon(QIcon("Resources/PNG/Database.png"))
        self.ui.pushButton_slot2.setText("Duyệt kho ảnh")
        # -> R WINDOW HEADER RIGHT
        set_button_icon_size(self.ui.pushButton_power_off,48)
        self.ui.pushButton_power_off.clicked.connect(lambda: self.close())
        self.ui.pushButton_power_off.setIcon(QIcon("Resources/PNG/PowerOff.png"))
        #self.ui.pushButton_slot3.setText("Tắt thiết bị")
        set_button_icon_size(self.ui.pushButton_noity,48)
        self.ui.pushButton_noity.clicked.connect(self.show_noity)
        self.ui.pushButton_noity.setIcon(QIcon("Resources/PNG/Bell.png"))
        set_label_icon_size(self.ui.label_bluetooth)
        self.ui.label_bluetooth.setPixmap(QPixmap("Resources/PNG/BluetoothOn.png"))
        set_button_icon_size(self.ui.pushButton_delete, 48)
        # -> G CAPTURE IMAGE PAGE ICON
        set_button_icon_size(self.ui.pushButton_accept, 48)
        self.ui.pushButton_accept.clicked.connect(self.noity_save_view)
        self.ui.pushButton_accept.setIcon(QIcon("Resources/PNG/Yes.png"))
        set_button_icon_size(self.ui.pushButton_send, 48)
        self.ui.pushButton_send.clicked.connect(self.noity_send_view)
        self.ui.pushButton_send.setIcon(QIcon("Resources/PNG/Sent.png"))
        set_button_icon_size(self.ui.pushButton_delete, 48)
        self.ui.pushButton_delete.clicked.connect(self.noity_delete_view)
        self.ui.pushButton_delete.setIcon(QIcon("Resources/PNG/Remove.png"))
        set_button_icon_size(self.ui.pushButton_delete_query, 48)
        # -> G QUERY IMAGE PAGE ICON
        self.ui.pushButton_delete_query.setIcon(QIcon("Resources/PNG/Remove.png"))
        set_label_icon_size(self.ui.label_status_icon, 48)
        self.ui.label_status_icon.setPixmap(QPixmap("Resources/PNG/Yes.png"))
        set_button_icon_size(self.ui.pushButton_previous, 48)
        self.ui.pushButton_previous.setIcon(QIcon("Resources/PNG/LeftArrow.png"))
        set_button_icon_size(self.ui.pushButton_next, 48)
        self.ui.pushButton_next.setIcon(QIcon("Resources/PNG/RightArrow.png"))
        # -> G NOITY PAGE ICON
        set_label_icon_size(self.ui.label_noity_header_icon, 48)
        set_button_icon_size(self.ui.pushButton_noity_ok, 48)
        set_button_icon_size(self.ui.pushButton_noity_clear, 48, "right")
        self.ui.pushButton_noity_clear.clicked.connect(self.reset_noity)
        self.ui.pushButton_noity_clear.setIcon(QIcon("Resources/PNG/Remove.png"))
        self.ui.pushButton_noity_clear.setText("Xoá thông báo")
        self.ui.pushButton_noity_ok.setIcon(QIcon("Resources/PNG/Done.png"))
        set_button_icon_size(self.ui.pushButton_noity_cancel, 48)
        self.ui.pushButton_noity_cancel.setIcon(QIcon("Resources/PNG/Close.png"))
        set_button_icon_size(self.ui.pushButton_noity_try_again, 48)
        self.ui.pushButton_noity_try_again.setIcon(QIcon("Resources/PNG/Restart.png"))
        self.reset_noity()

# endregion SETUP

    def toggle_menu(self):
        self.ui.frame_menu.setHidden(not self.ui.frame_menu.isHidden())


    def show_noity(self,
                   header_icon_path:str=None,
                   header_icon_info:str=None,
                   body_info:str=None,
                   is_just_ok:bool=None):
        if header_icon_path:
            self.ui.label_noity_header_icon.setPixmap(QPixmap(header_icon_path))
        if header_icon_info:
            self.ui.label_noity_header_info.setText(header_icon_info)
        if body_info:
            self.ui.label_noity_body_info.setText(body_info)
        if is_just_ok:
            self.ui.pushButton_noity_cancel.setHidden(is_just_ok)
            self.ui.pushButton_noity_try_again.setHidden(is_just_ok)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_noity)

    def reset_noity(self):
        self.show_noity("Resources/PNG/Bell.png", "THÔNG BÁO",
                        "Không có thông báo nào",
                        is_just_ok=True)

    def noity_save_view(self):
        self.show_noity("Resources/PNG/Yes.png","THÀNH CÔNG",
                        "Đã lưu thành công bộ dữ liệu bản ảnh chuẩn hoá\nvào thiết bị làm căn cứ xác minh, xử phạt vi phạm hành chính!",
                        True)

    def noity_send_view(self):
        self.show_noity("Resources/PNG/Yes.png","THÀNH CÔNG",
                        "Đã gửi thành công bộ dữ liệu bản ảnh chuẩn hoá\nlên máy chủ làm căn cứ xác minh, xử phạt vi phạm hành chính!",
                        True)

    def noity_delete_view(self):
        self.show_noity("Resources/PNG/Yes.png","THÀNH CÔNG",
                        "Đã xoá thông tin bộ dữ liệu bản ảnh chuẩn hoá.",
                        True)
        

   
    # Event handler to capture the key press
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_M:
            pass
        if event.key() == Qt.Key.Key_T:
            self.test()


    
    

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
