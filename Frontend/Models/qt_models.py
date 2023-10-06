from datetime import datetime
from enum import Enum
import os
import time
import cv2
from PyQt6.QtCore import QThread, pyqtSignal, QObject, pyqtSlot, QTimer
from PyQt6.QtGui import QImage
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QLabel
from PIL import Image

IMAGE_FOLDER = "Frontend/Images/CapturedImages"

class CameraCapturedImage():
    def __init__(self, image: QImage) -> None:
        self.record_time = datetime.now()  # Update the timestamp to use datetime.now()
        self.image = image

    def save(self):
        timestamp_str = self.record_time.strftime("%d%m%y-%H%M%S")  # Convert datetime to a formatted string
        img_file_name = "%s.jpg" % timestamp_str
        os.makedirs(IMAGE_FOLDER, exist_ok=True)
        file_path = os.path.join(IMAGE_FOLDER, img_file_name)
        print(file_path)
        self.image.save(file_path)

class AcceptedCapturedImage():
    def __init__(self,
                 image: Image,
                 record_time: datetime) -> None:
        self.record_time = record_time  # Update the timestamp to use datetime.now()
        self.image = image
    def save(self):
        timestamp_str = self.record_time.strftime("%d%m%y-%H%M%S")  # Convert datetime to a formatted string
        img_file_name = "%s.jpg" % timestamp_str
        os.makedirs(IMAGE_FOLDER, exist_ok=True)
        file_path = os.path.join(IMAGE_FOLDER, img_file_name)
        print(file_path)
        self.image.save(file_path)

class TimerMode(Enum):
    TIMER = "timer"
    UP = "count up"
    DOWN = "count down"

class Timer(QObject):
    time_changed = pyqtSignal(int)

    def __init__(self,
                 timespand_ms:int = 1000,
                 timer_mode: str = TimerMode.TIMER.value,
                 time_limit:int = 10):
        super().__init__()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.is_paused = False
        self.time_limit = time_limit
        self.timer_mode = timer_mode
        self.time_elapsed = time_limit if self.timer_mode == TimerMode.DOWN.value else 0
        self.timespand_ms = timespand_ms

    @pyqtSlot()
    def reset(self):
        self.timer.stop()
        self.time_elapsed = self.time_limit if self.timer_mode == TimerMode.DOWN.value else 0
        self.time_changed.emit(self.time_elapsed)

    @pyqtSlot()
    def start(self):
        if not self.timer.isActive():
            self.timer.start(self.timespand_ms) # Update every timespand_ms (ms)

    @pyqtSlot()
    def pause(self):
        if self.timer.isActive() and not self.is_paused:
            self.timer.stop()
            self.is_paused = True

    @pyqtSlot()
    def resume(self):
        if self.is_paused:
            self.timer.start()
            self.is_paused = False
    
    @pyqtSlot()
    def stop(self):
        self.timer.stop()
        self.time_elapsed = 0
        self.time_changed.emit(self.time_elapsed)
    
    def update_time(self):
        if self.timer_mode == TimerMode.TIMER.value:
            self.time_elapsed += 1
        if self.timer_mode == TimerMode.UP.value:
            if self.time_limit is None or self.time_elapsed < self.time_limit:
                self.time_elapsed += 1
            else:
                self.stop()
        if self.timer_mode == TimerMode.DOWN.value:
            if self.time_limit is None or self.time_elapsed > 0:
                self.time_elapsed -= 1
            else:
                self.stop()
        self.time_changed.emit(self.time_elapsed)
    
