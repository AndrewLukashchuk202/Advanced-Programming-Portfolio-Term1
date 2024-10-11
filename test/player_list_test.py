import unittest
from player import Player
from player_node import PlayerNode
from player_list import PlayerList


class PlayerListTest(unittest.TestCase):

    def setUp(self):
        """Initialize a new Player, PlayerNode, and a PlayerList for each test"""
        self.player1 = Player("1", "Andrew")
        self.player2 = Player("2", "Rafael")
        self.player3 = Player("3", "Sam")

        self.player_node1 = PlayerNode(player=self.player1)
        self.player_node2 = PlayerNode(player=self.player2)
        self.player_node3 = PlayerNode(player=self.player3)

        self.player_list = PlayerList()

    def test_push_front_single_node(self):
        self.player_list.push_front(self.player_node1)

        self.assertEqual(self.player_list.head, self.player_node1)
        self.assertEqual(self.player_list.tail, self.player_node1)

    def test_push_front_multiple_nodes(self):
        self.player_list.push_front(self.player_node1)
        self.player_list.push_front(self.player_node2)

        self.assertEqual(self.player_list.head, self.player_node2)
        self.assertEqual(self.player_list.tail, self.player_node1)
        self.assertEqual(self.player_list.head.player_next_node, self.player_node1)
        self.assertEqual(self.player_list.tail.player_prev_node, self.player_node2)

    def test_push_back_single_node(self):
        self.player_list.push_back(self.player_node1)

        self.assertEqual(self.player_list.head, self.player_node1)
        self.assertEqual(self.player_list.tail, self.player_node1)

    def test_push_back_multiple_nodes(self):
        self.player_list.push_back(self.player_node1)
        self.player_list.push_back(self.player_node2)

        self.assertEqual(self.player_list.tail, self.player_node2)
        self.assertEqual(self.player_list.tail.player_prev_node, self.player_node1)

    def test_pop_front_from_empty_list(self):
        with self.assertRaises(IndexError, msg="List is empty"):
            self.player_list.pop_from_front()

    def test_pop_front_single_node(self):
        self.player_list.push_front(self.player_node1)

        removed_node = self.player_list.pop_from_front()

        self.assertTrue(self.player_list.is_empty)
        self.assertIsNone(self.player_list.head)
        self.assertIsNone(self.player_list.tail)

    def test_pop_front_multiple_nodes(self):
        self.player_list.push_front(self.player_node1)
        self.player_list.push_front(self.player_node2)

        removed_node = self.player_list.pop_from_front()

        self.assertEqual(removed_node, self.player_node2)
        self.assertEqual(self.player_list.head, self.player_node1)
        self.assertEqual(self.player_list.tail, self.player_node1)
        self.assertIsNone(self.player_list.head.player_prev_node)

    def test_pop_back_empty_list(self):
        with self.assertRaises(IndexError, msg="List is empty"):
            self.player_list.pop_from_back()

    def test_pop_back_single_node(self):
        self.player_list.push_back(self.player_node1)

        removed_node = self.player_list.pop_from_back()

        self.assertEqual(removed_node, self.player_node1)
        self.assertIsNone(self.player_list.head)
        self.assertIsNone(self.player_list.tail)

    def test_pop_back_multiple_nodes(self):
        self.player_list.push_back(self.player_node1)
        self.player_list.push_back(self.player_node2)

        removed_node = self.player_list.pop_from_back()

        self.assertEqual(removed_node, self.player_node2)
        self.assertEqual(self.player_list.head, self.player_node1)
        self.assertEqual(self.player_list.tail, self.player_node1)
        self.assertIsNone(self.player_list.tail.player_next_node)

    def test_empty_list(self):
        self.assertTrue(self.player_list.is_empty)

    def test_pop_by_uid_middle(self):
        self.player_list.push_back(self.player_node1)
        self.player_list.push_back(self.player_node2)
        self.player_list.push_back(self.player_node3)

        removed_node = self.player_list.pop_by_uid("2")

        self.assertEqual(removed_node, self.player_node2)
        self.assertEqual(self.player_list.head, self.player_node1)
        self.assertEqual(self.player_list.tail, self.player_node3)
        self.assertEqual(self.player_list.head.player_next_node, self.player_node3)
        self.assertEqual(self.player_list.tail.player_prev_node, self.player_node1)

    def test_pop_by_uid_head(self):
        self.player_list.push_back(self.player_node1)
        self.player_list.push_back(self.player_node2)

        removed_node = self.player_list.pop_by_uid("1")

        self.assertEqual(len(self.player_list), 1)
        self.assertEqual(removed_node, self.player_node1)
        self.assertEqual(self.player_list.head, self.player_node2)
        self.assertEqual(self.player_list.tail, self.player_node2)

    def test_pop_by_uid_tail(self):
        self.player_list.push_back(self.player_node1)
        self.player_list.push_back(self.player_node2)

        removed_node = self.player_list.pop_by_uid("2")

        self.assertEqual(len(self.player_list), 1)
        self.assertEqual(removed_node, self.player_node2)
        self.assertEqual(self.player_list.head, self.player_node1)
        self.assertEqual(self.player_list.tail, self.player_node1)

    def test_pop_by_uid_empty_list(self):
        with self.assertRaises(IndexError, msg="List is empty"):
            self.player_list.pop_by_uid("1")

    def test_pop_by_uid_not_found(self):
        self.player_list.push_back(self.player_node1)
        self.player_list.push_back(self.player_node2)

        with self.assertRaises(ValueError, msg="Value not found"):
            self.player_list.pop_by_uid("3")

    def test_add_duplicate_player_node_by_uid(self):
        player_duplicate = Player("1", "Bob")  # Same UID as player1
        node_duplicate = PlayerNode(player_duplicate)

        self.player_list.push_front(self.player_node1)

        with self.assertRaises(ValueError):
            self.player_list.push_front(node_duplicate)

    def test_add_duplicate_player_node_same_object(self):
        self.player_list.push_front(self.player_node1)

        with self.assertRaises(ValueError):
            self.player_list.push_front(self.player_node1)


if __name__ == "__main__":
    unittest.main()
