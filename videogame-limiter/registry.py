from winreg import *
import logging


def read_app_id():
    key_name = "SOFTWARE\Valve\Steam"
    reg = ConnectRegistry(None, HKEY_CURRENT_USER)
    with OpenKey(reg, key_name) as key:
        val = QueryValueEx(key, "RunningAppID")[0]
        logging.info(f"RunningAppId: ${val}")
