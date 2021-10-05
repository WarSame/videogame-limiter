from kivy.app import App
from kivy.uix.button import Button
from registry import read_app_id
import logging


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
        read_app_id()
        return Button(text='Hello World')

if __name__ == "__main__":
    VideogameLimiter().run()