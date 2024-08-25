import unittest
from player import Player
from data_stuctures.player_hash_map import PlayerHashMap


class HashMapTest(unittest.TestCase):

    def setUp(self):
        """Initialize a new PlayerHashMap for each test."""
        self.hash_map = PlayerHashMap()
        self.player1 = Player("And12rew", "Andrew")
        self.player2 = Player("Raf34el", "Rafael")
        self.player3 = Player("Sa45m", "Samuel")
        self.hash_map[self.player1.uid] = self.player1.name
        self.hash_map[self.player2.uid] = self.player2.name

    def test_add_player(self):
        """Test adding players to the hash map."""
        self.hash_map[self.player3.uid] = self.player3.name
        self.assertEqual(len(self.hash_map), 3)
        self.assertEqual(self.hash_map["Sa45m"].name, "Samuel")

    def test_retrieve_player(self):
        """Test retrieving players from the hash map."""
        retrieved_player = self.hash_map["And12rew"]
        self.assertEqual(retrieved_player.name, "Andrew")
        self.assertEqual(retrieved_player.uid, "And12rew")

    def test_update_player(self):
        """Test updating an existing player in the hash map."""
        self.hash_map["And12rew"] = "Andrii"
        updated_player = self.hash_map["And12rew"]
        self.assertEqual(updated_player.name, "Andrii")

    def test_remove_player(self):
        """Test removing a player from the hash map."""
        del self.hash_map["And12rew"]
        self.assertEqual(len(self.hash_map), 1)
        self.hash_map.display()
        with self.assertRaises(KeyError):
            self.hash_map["And12rew"]

    def test_collision_handling(self):
        """Test how the hash map handles collisions."""
        # Assuming these keys produce the same hash index:
        colliding_player1 = Player("123", "John")
        colliding_player2 = Player("321", "Karl Theodor Maria Georg "
                                          "Achaz Eberhardt Josef Freiherr von und zu Guttenberg")
        self.hash_map[colliding_player1.uid] = colliding_player1.name
        self.hash_map[colliding_player2.uid] = colliding_player2.name

        self.assertEqual(len(self.hash_map), 4)  # 2 original players + 2 colliding players
        self.assertEqual(self.hash_map["123"].name, "John")
        self.assertEqual(self.hash_map["321"].name, "Karl Theodor Maria Georg "
                                                    "Achaz Eberhardt Josef Freiherr von und zu Guttenberg")

    def test_empty_hash_map(self):
        """Test behavior when the hash map is empty."""
        empty_hash_map = PlayerHashMap()
        with self.assertRaises(KeyError):
            empty_hash_map["non_existent"]

    def test_len_on_empty(self):
        """Test the length of an empty hash map."""
        empty_hash_map = PlayerHashMap()
        self.assertEqual(len(empty_hash_map), 0)

    def test_display(self):
        """Test the display method output."""
        # Capture the printed output
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.hash_map.display()
        sys.stdout = sys.__stdout__

        # Ensure some expected output is in the display
        output = captured_output.getvalue()
        self.assertIn("Index of the player_list", output)
