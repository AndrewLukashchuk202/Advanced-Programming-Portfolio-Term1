import unittest
from player import Player
from player_node import PlayerNode
from player_list import PlayerList


class PlayerListTest(unittest.TestCase):

    def test_push_single_node(self):
        player = Player("1", "Andrew")

        player_node = PlayerNode(player)

        player_list = PlayerList()

        player_list.push(player_node)

        self.assertFalse(player_list.is_empty)
        self.assertEqual(player_list.head, player_node)
        self.assertEqual(player_list.tail, player_node)

    def test_push_multiple_nodes(self):
        player1 = Player("1", "Andrew")
        player2 = Player("2", "Rafael")

        player_node1 = PlayerNode(player1)
        player_node2 = PlayerNode(player2)

        player_list = PlayerList()

        player_list.push(player_node1)
        player_list.push(player_node2)

        self.assertFalse(player_list.is_empty)
        self.assertEqual(player_list.head, player_node2)
        self.assertEqual(player_list.tail, player_node1)
        self.assertEqual(player_list.head.player_next_node, player_node1)
        self.assertEqual(player_list.tail.player_prev_node, player_node2)

    def test_empty_list(self):
        player_list = PlayerList()

        self.assertTrue(player_list.is_empty)
        self.assertIsNone(player_list.head)
        self.assertIsNone(player_list.tail)


if __name__ == "__main__":
    unittest.main()
