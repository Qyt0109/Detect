from cv2 import VideoCapture, cvtColor, COLOR_BGR2RGB, flip
from threading import Thread
import numpy as np

from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.graphics.texture import Texture

class CameraThread(Image):
    def __init__(self, camera_index=0, fps = 30, **kwargs):
        super(CameraThread, self).__init__(**kwargs)
        self.camera_index = camera_index
        self.is_running = False
        self.is_pause = False
        self.camera_capture = None
        self.start()
        Clock.schedule_interval(self.run, 1.0 / fps)

    def run(self, _):
        while self.is_running and not self.is_pause:
            ret, frame = self.camera_capture.read()
            if ret:
                # convert to texture
                buff = flip(frame, 1).tostring()
                texture = Texture.create(size=(frame.shape[1],
                                            frame.shape[0]),
                                        colorfmt='bgr')
                texture.blit_buffer(buff, colorfmt='bgr', bufferfmt='ubyte')
                self.texture = texture
                    
                    

    def start(self, camera_index=None):
        if camera_index:
            self.camera_index = camera_index
        self.stop()
        self.camera_capture = VideoCapture(self.camera_index)
        self.is_running = True
        self.is_pause = False

    def stop(self):
        self.is_running = False
        if self.camera_capture:
            self.camera_capture.release()

    def pause(self):
        self.is_pause = True

    def resume(self):
        self.is_pause = False