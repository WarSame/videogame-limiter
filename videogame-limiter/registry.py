from winreg import *
import logging
import time
import threading

HKEY_PATH = "SOFTWARE\Valve\Steam"
HKEY_NAME = "RunningAppID"


def enable_app_id_listener(app):
    thread = threading.Thread(target=update_value, kwargs={"app": app})
    thread.daemon = True
    thread.start()


def update_value(app):
    reg = ConnectRegistry(None, HKEY_CURRENT_USER)
    with OpenKey(reg, HKEY_PATH) as key:
        while True:
            val = QueryValueEx(key, HKEY_NAME)[0]
            logging.info(f"RunningAppId: {val}")
            app.set_button(val)
            time.sleep(5)
