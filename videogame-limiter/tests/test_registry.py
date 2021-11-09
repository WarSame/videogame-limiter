import registry
import unittest


class TestRegistry(unittest.TestCase):
    def test_get_game_name(self):
        info = registry.get_game_name_from_id(322330)
        print(info)


if __name__ == "__main__":
    unittest.main()