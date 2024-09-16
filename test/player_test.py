import unittest
from player import Player


class PlayerTest(unittest.TestCase):

    def setUp(self):
        """Set up the test environment by creating Player instances."""
        self.player1 = Player("1_uid", "Andrew", 100)
        self.player2 = Player("2_uid", "Rafael", 99)
        self.player3 = Player("3_uid", "Sam", 75)
        self.player4 = Player("4_uid", "Cam", 43)
        self.player5 = Player("5_uid", "Mason", 1)
        self.player6 = Player("6_uid", "John", 12)
        self.player7 = Player("7_uid", "Stefan", 34)

        self.player_list = [
            self.player1,
            self.player2,
            self.player3,
            self.player4,
            self.player5,
            self.player6,
            self.player7,
        ]

    def test_return_player_uid(self):
        """Test if the player's UID is correctly returned."""
        self.assertEqual(self.player1.uid, "1_uid")

    def test_return_player_name(self):
        """Test if the player's name is correctly returned."""
        self.assertEqual(self.player2.name, "Rafael")

    def test_eq_player_score(self):
        """Test the equality comparison of player scores."""
        self.assertFalse(self.player1.score == self.player2.score)

    def test_ne_player_score(self):
        """Test the inequality comparison of player scores."""
        self.assertTrue(self.player1.score != self.player2.score)

    def test_gt_player_score(self):
        """Test if player1's score is greater than player2's score."""
        self.assertTrue(self.player1.score > self.player2.score)

    def test_lt_player_score(self):
        """Test if player1's score is less than player2's score."""
        self.assertFalse(self.player1.score < self.player2.score)

    def test_ge_player_score(self):
        """Test if player1's score is greater than or equal to player2's score."""
        self.player2.score = 100
        self.assertTrue(self.player1.score >= self.player2.score)

    def test_le_player_score(self):
        """Test if player1's score is less than or equal to player2's score."""
        self.player1.score = 99
        self.assertTrue(self.player1.score <= self.player2.score)

    def test_quicksort_descending(self):
        """Test if sort function implemented in the Player class sort in the descended order correctly"""
        expected_player_list = sorted(self.player_list, reverse=True)

        self.assertEqual(Player.quicksort_descending(self.player_list), expected_player_list)


if __name__ == "__main__":
    unittest.main()
