from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDTextButton

class Footer(MDBoxLayout):
    def goToScreen(self, screen_name):
        self.parent.ids["screen_manager"].current = screen_name
        self.ids["go_to_capturing_screen"].icon_color = "white"
        self.ids["go_to_capturing_screen"].md_bg_color = (80/256, 80/256, 80/256, 1)
        self.ids["go_to_captured_screen"].icon_color = "white"
        self.ids["go_to_captured_screen"].md_bg_color = (80/256, 80/256, 80/256, 1)
        self.ids["go_to_album_screen"].icon_color = "white"
        self.ids["go_to_album_screen"].md_bg_color = (80/256, 80/256, 80/256, 1)
        if screen_name == "capturing_screen":
            self.ids["go_to_capturing_screen"].icon_color = "cyan"
            self.ids["go_to_capturing_screen"].md_bg_color = (30/256, 30/256, 30/256, 1)
        elif screen_name == "captured_screen":
            self.ids["go_to_captured_screen"].icon_color = "cyan"
            self.ids["go_to_captured_screen"].md_bg_color = (30/256, 30/256, 30/256, 1)
        elif screen_name == "album_screen":
            self.ids["go_to_album_screen"].icon_color = "cyan"
            self.ids["go_to_album_screen"].md_bg_color = (30/256, 30/256, 30/256, 1)