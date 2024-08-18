import unittest
from player import Player
from player_node import PlayerNode
from player_list import PlayerList


class PlayerListTest(unittest.TestCase):

    def test_push_front_single_node(self):
        player = Player("1", "Andrew")

        player_node = PlayerNode(player)

        player_list = PlayerList()

        player_list.push_front(player_node)

        self.assertFalse(player_list.is_empty, "PlayerList should not be empty after push_forward")
        self.assertEqual(player_list.head, player_node, f"Expected head to be {player_node},"
                                                        f" but got {player_list.head}")
        self.assertEqual(player_list.tail, player_node, f"Expected tail to be {player_node}, "
                                                        f"but got {player_list.tail}")

    def test_push_front_multiple_nodes(self):
        player1 = Player("1", "Andrew")
        player2 = Player("2", "Rafael")

        player_node1 = PlayerNode(player1)
        player_node2 = PlayerNode(player2)

        player_list = PlayerList()

        player_list.push_front(player_node1)
        player_list.push_front(player_node2)

        self.assertFalse(player_list.is_empty, "PlayerList should not be empty after push_forward")
        self.assertEqual(player_list.head, player_node2,
                         f"Expected head to be {player_node2}, but got {player_list.head}")
        self.assertEqual(player_list.tail, player_node1,
                         f"Expected tail to be {player_node1}, but got {player_list.tail}")
        self.assertEqual(player_list.head.player_next_node, player_node1,
                         "Head node's next_node should be player_node1")
        self.assertEqual(player_list.tail.player_prev_node, player_node2,
                         "Tail node's previous_node should be player_node2")

    def test_push_back_single_node(self):
        player = Player("1", "Andrew")

        player_node = PlayerNode(player)

        player_list = PlayerList()

        player_list.push_back(player_node)

        self.assertFalse(player_list.is_empty, "PlayerList should not be empty after push_back")
        self.assertEqual(player_list.head, player_node,
                         f"Expected head to be {player_node}, but got {player_list.head}")
        self.assertEqual(player_list.tail, player_node,
                         f"Expected tail to be {player_node}, but got {player_list.tail}")

    def test_push_back_multiple_nodes(self):
        player1 = Player("1", "Andrew")
        player2 = Player("2", "Rafael")

        player_node1 = PlayerNode(player1)
        player_node2 = PlayerNode(player2)

        player_list = PlayerList()

        player_list.push_back(player_node1)
        player_list.push_back(player_node2)

        self.assertFalse(player_list.is_empty, "PlayerList should not be empty after push_back")
        self.assertEqual(player_list.tail, player_node2,
                         f"Expected tail to be {player_node2}, but got {player_list.tail}")
        self.assertEqual(player_list.tail.player_prev_node, player_node1,
                         "Tail node's previous_node should be player_node1")

    def test_empty_list(self):
        player_list = PlayerList()

        self.assertTrue(player_list.is_empty, "PlayerList should be empty when initialized")


if __name__ == "__main__":
    unittest.main()
