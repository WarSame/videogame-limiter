import registry
import unittest
from steam.client import SteamClient


class TestRegistry(unittest.TestCase):
    def test_get_game_name(self):
        client = SteamClient()
        client.connect()
        client.anonymous_login()
        info = client.get_product_info(apps=[322330], timeout=10)
        print(info)


if __name__ == "__main__":
    unittest.main()