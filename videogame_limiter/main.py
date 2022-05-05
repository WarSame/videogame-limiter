from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from registry import enable_app_id_listener
import logging
import threading


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)


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

if __name__ == "__main__":
    VideogameLimiter().run()