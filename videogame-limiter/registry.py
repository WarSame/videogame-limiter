from winreg import *
import logging
import time

HKEY_PATH = "SOFTWARE\Valve\Steam"
HKEY_NAME = "RunningAppID"

def read_app_id():
    key_name = HKEY_PATH
    reg = ConnectRegistry(None, HKEY_CURRENT_USER)
    with OpenKey(reg, key_name) as key:
        while True:
            val = QueryValueEx(key, HKEY_NAME)[0]
            logging.info(f"RunningAppId: {val}")
            yield val
            time.sleep(5)
