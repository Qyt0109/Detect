from datetime import datetime
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder


# Designs
from KivyAppDesign.main_design import MainDesign


# KivyAppDesign/Components
Builder.load_file("KivyUbuntuAppDesign/Components/header.kv")         # Header
Builder.load_file("KivyUbuntuAppDesign/Components/footer.kv")         # Footer
Builder.load_file("KivyUbuntuAppDesign/Components/selector.kv")         # Selector
# KivyAppDesign/Screens
Builder.load_file("KivyUbuntuAppDesign/Screens/capturing.kv")         # CapturingScreen
Builder.load_file("KivyUbuntuAppDesign/Screens/captured.kv")          # CapturedScreen
Builder.load_file("KivyUbuntuAppDesign/Screens/album.kv")             # AlbumScreen
Builder.load_file("KivyUbuntuAppDesign/Screens/screen_manager.kv")    # MainScreenManager
# KivyAppDesign
Builder.load_file("KivyUbuntuAppDesign/main_design.kv")               # MainDesign


class KivyMainUbuntuApp(MDApp):
    def build(self):
        Window.maximize()
        return MainDesign()
    
    def on_start(self):
        device_statuses = self.root.ids["header"].ids["device_statuses"]
        device_statuses.checkStatuses()
        self.root.ids["footer"].goToScreen("capturing_screen")


if __name__ == "__main__":
    app = KivyMainUbuntuApp()
    app.run()