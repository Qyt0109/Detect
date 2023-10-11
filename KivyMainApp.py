from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder

# Designs
from KivyAppDesign.main_design import MainDesign


# KivyAppDesign/Components
Builder.load_file("KivyAppDesign/Components/header.kv")         # Header
Builder.load_file("KivyAppDesign/Components/footer.kv")         # Footer
Builder.load_file("KivyAppDesign/Components/camera.kv")         # CapturingCamera
# KivyAppDesign/Screens
Builder.load_file("KivyAppDesign/Screens/capturing.kv")         # CapturingScreen
Builder.load_file("KivyAppDesign/Screens/captured.kv")          # CapturedScreen
Builder.load_file("KivyAppDesign/Screens/album.kv")             # AlbumScreen
Builder.load_file("KivyAppDesign/Screens/screen_manager.kv")    # MainScreenManager
# KivyAppDesign
Builder.load_file("KivyAppDesign/main_design.kv")               # MainDesign


class KivyMainApp(MDApp):
    def build(self):
        Window.size = [800, 600]
        return MainDesign()
    
    def on_start(self):
        device_statuses = self.root.ids["header"].ids["device_statuses"]
        device_statuses.checkStatuses()

    
    def onCameraCaptured(self, image):
        print(image)

    def camera_change(self, instance, index = None):
        camera = instance.parent.ids["capturing_camera"]
        if index:
            camera.index = index
        else:
            camera.index = 0 if camera.index == 1 else 1


if __name__ == "__main__":
    app = KivyMainApp()
    app.run()