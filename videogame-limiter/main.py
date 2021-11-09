from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from registry import read_app_id
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
        Clock.schedule_interval(self.listen_button, 5)
        return self.layout

    def init_button(self):
        return Button(text=f'0')

    def listen_button(self, *args):
        for app_id in read_app_id():
            self.button.text = f"{app_id}"

if __name__ == "__main__":
    VideogameLimiter().run()