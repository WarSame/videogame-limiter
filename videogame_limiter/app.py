from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from registry import enable_app_id_listener


class VideogameLimiter(App):
    def build(self):
        self.layout = BoxLayout(orientation = 'vertical')
        self.button = self.init_button()
        self.layout.add_widget(self.button)
        enable_app_id_listener(self)
        return self.layout

    def init_button(self):
        return Button(text='0')

    def set_button(self, app_id):
        self.button.text = f"{app_id}"