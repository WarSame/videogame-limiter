import logging
import time
import threading
from winreg import ConnectRegistry, HKEY_CURRENT_USER, OpenKey, QueryValueEx
from steam.client import SteamClient

HKEY_PATH = "SOFTWARE\Valve\Steam"
HKEY_NAME = "RunningAppID"


def enable_app_id_listener(app):
    thread = threading.Thread(target=update_game_name, kwargs={"app": app})
    thread.daemon = True
    thread.start()


def update_game_name(app):
    reg = ConnectRegistry(None, HKEY_CURRENT_USER)
    with OpenKey(reg, HKEY_PATH) as key:
        while True:
            game_info = get_game_id_and_name(key)
            app.set_button(game_info["name"])
            time.sleep(5)


def get_game_id_and_name(key):
    game_id = QueryValueEx(key, HKEY_NAME)[0]
    logging.info(f"RunningAppId: {game_id}")
    if game_id == 0:
        return {"name":"No game running", "id": 0}
    game_name = get_game_name_from_id(game_id)
    return {"name": game_name, "id": game_id}


def get_game_name_from_id(game_id):
    client = SteamClient()
    client.anonymous_login()
    client.connect()
    info = client.get_product_info(apps=[game_id], timeout=10)
    name = info["apps"][game_id]["common"]["name"]
    print(name)
    return name
