from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from PIL import Image
# app.root.ids["screen_manager"].ids["capturing_screen"].ids["capturing_camera_layout"].select_preset_image(choosen_image = self.selection)
class SelectPresetImagePopup(Popup):
    def on_select(self, application, selection):
        application.root.ids["screen_manager"].ids["capturing_screen"].ids["capturing_camera_layout"].on_select_preset_image(selection = selection)
        self.ids["select_preset_image_previewer"].source = selection[0]
    def remove_preset_image(self, application):
        application.root.ids["screen_manager"].ids["capturing_screen"].ids["capturing_camera_layout"].selected_preset_image = None
        application.root.ids["screen_manager"].ids["capturing_screen"].ids["capturing_camera_layout"].selected_preset_image = None
        self.ids["select_preset_image_previewer"].source = ""
        self.dismiss()
    def selected_preset_image(self, application):
        application.root.ids["screen_manager"].ids["capturing_screen"].ids["capturing_camera_layout"].on_selected_preset_image(application = application)
        self.dismiss()

class CapturingCamera(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.is_preset_image = False
        self.preset_image = None
        self.selected_preset_image = None

    def capture(self, callback = None, save_path:str = None):
        try:
                # Preset image
            if self.selected_preset_image:
                file_path = self.selected_preset_image[0]
                preset_image = Image.open(file_path)
                captured_image = preset_image
            else:
                # Camera image
                camera = self.ids["capturing_camera"]
                texture = camera.texture
                size = texture.size
                pixels = texture.pixels # Kivy Camera's texture pixels are in RGBA format, which can't save as jpeg
                captured_image = Image.frombytes(mode='RGBA', size=size,data=pixels).convert('RGB') # Convert pixels into RGBA image then convert RGBA into RGB image object
            # Done if else, now do some stuffs with captured_image
            if callback:
                callback(captured_image)
            if save_path:
                camera.export_to_png(save_path)
            print("Captured")
            return captured_image
        except Exception as e:
            print(f"Error: {e}")
            return None

    def change_camera(self, index = None):
        camera = self.ids["capturing_camera"]
        if index:
            camera.index = index
        else:
            camera.index = 0 if camera.index == 1 else 1

    def turn(self, is_on = None):
        camera = self.ids["capturing_camera"]
        if is_on:
            camera.play = is_on
        else:
            camera.play = not camera.play

    def on_select_preset_image(self, selection, callback = None):
        try:
            self.preset_image = selection
            """
            if selection:
                file_path = selection[0]
                preset_image = Image.open(file_path)
                print(preset_image)
            """
        except Exception as e:
            print(f"Error: {e}")

    def on_selected_preset_image(self, application):
        try:
            self.selected_preset_image = self.preset_image
        except Exception as e:
            print(f"Error: {e}")
