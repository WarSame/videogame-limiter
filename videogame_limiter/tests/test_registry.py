from steam.client import SteamClient


def test_get_game_name():
    dst_id = 322330
    client = SteamClient()
    client.anonymous_login()
    client.connect()
    info = client.get_product_info(apps=[dst_id], timeout=10)
    name = info["apps"][dst_id]["common"]["name"]
    print(name)
    assert(name == "Don't Starve Together")
