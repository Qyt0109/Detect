from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivy.uix.image import Image
from kivymd.uix.list import MDList,OneLineAvatarListItem,ImageLeftWidget
import time
from kivy.uix.widget import Widget
from kivy.app import App

Window.size = (600,400)

class MyLayout(Widget):
	pass


class MyApp(App):
	def build(self):
		return Builder.load_file("KivyTest2.kv")

if __name__ == "__main__":
	MyApp().run()
