from kivymd.uix.screen import MDScreen

class CapturedScreen(MDScreen):
    def on_image_captured(self, image):
        temp_captured_image_path = "KivyAppDesign/Temp/TempCapturedImage.jpg"
        image.save(temp_captured_image_path)
        self.ids["captured_image_layout"].ids["captured_image_viewer"].ids["image_view"].source = temp_captured_image_path
        print("Captured screen received at KivyAppDesign/Temp/TempCapturedImage.jpg: ", image)