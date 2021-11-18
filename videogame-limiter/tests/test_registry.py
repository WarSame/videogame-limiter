import registry
import unittest
from steam.client import SteamClient


class TestRegistry(unittest.TestCase):
    def test_get_game_name(self):
        dst_id = 322330
        client = SteamClient()
        client.connect()
        client.anonymous_login()
        info = client.get_product_info(apps=[dst_id], timeout=10)
        assert(info["apps"][dst_id]["common"]["name"] == "Don't Starve Together")


if __name__ == "__main__":
    unittest.main()