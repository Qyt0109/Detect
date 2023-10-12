from kivy.uix.boxlayout import BoxLayout


class Selector(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.preview = None
        self.selected = None

    def on_select(self, selection):
        self.ids["preset_image"].source = selection[0]
        self.preview = selection

    def selected_preset_image(self, application):
        self.selected = self.preview
        #application.root.ids["screen_manager"].ids["captured_screen"].ids["captured_image_layout"].image_source = self.selected[0]
        application.root.ids["screen_manager"].ids["captured_screen"].on_image_captured(image_path = self.selected[0], application = application)
        application.root.ids["screen_manager"].current = "captured_screen"