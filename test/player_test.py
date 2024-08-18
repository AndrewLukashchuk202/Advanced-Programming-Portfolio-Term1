import unittest
from player import Player


class PlayerTest(unittest.TestCase):

    def test_return_player_uid(self):
        player = Player("1_uid", "Andrew")
        self.assertEqual(player.uid, "1_uid")

    def test_return_player_name(self):
        player = Player("2_uid", "Rafael")
        self.assertEqual(player.name, "Rafael")


if __name__ == "__main__":
    unittest.main()
