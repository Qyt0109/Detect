from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class MyBoxLayout(BoxLayout):
    def show_notification(self):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Button(text='Close', on_release=self.dismiss_popup))
        content.add_widget(Button(text='Other Action'))

        popup = Popup(title='Notification',
                      content=content,
                      size_hint=(None, None),
                      size=(400, 200))
        popup.open()

    def dismiss_popup(self, instance):
        instance.parent.parent.dismiss()

class MyApp(App):
    def build(self):
        return MyBoxLayout()

if __name__ == '__main__':
    MyApp().run()
