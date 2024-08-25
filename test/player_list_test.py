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

    def test_pop_front_from_empty_list(self):
        player_list = PlayerList()
        with self.assertRaises(IndexError, msg="List is empty"):
            player_list.pop_front()

    def test_pop_front_single_node(self):
        player = Player("1", "Andrew")
        player_node = PlayerNode(player)
        player_list = PlayerList()
        player_list.push_front(player_node)

        removed_node = player_list.pop_front()

        self.assertEqual(removed_node, player_node, "Removed node should be the node that was pushed.")
        self.assertTrue(player_list.is_empty, "List should be empty after removing the only node.")
        self.assertIsNone(player_list.head, "Head should be None after removing the only node.")
        self.assertIsNone(player_list.tail, "Tail should be None after removing the only node.")

    def test_pop_front_multiple_nodes(self):
        player1 = Player("1", "Andrew")
        player2 = Player("2", "Rafael")

        player_node1 = PlayerNode(player1)
        player_node2 = PlayerNode(player2)

        player_list = PlayerList()
        player_list.push_front(player_node1)
        player_list.push_front(player_node2)

        removed_node = player_list.pop_front()

        self.assertEqual(removed_node, player_node2, "Removed node should be the node that was pushed last.")
        self.assertEqual(player_list.head, player_node1, "Head should be the previous node after removal.")
        self.assertEqual(player_list.tail, player_node1, "Tail should remain unchanged after removal.")
        self.assertIsNone(player_list.head.player_prev_node, "Head node's previous_node should be None.")

    def test_pop_back_empty_list(self):
        player_list = PlayerList()
        with self.assertRaises(IndexError, msg="List is empty"):
            player_list.pop_back()

    def test_pop_back_single_node(self):
        player = Player("1", "Andrew")
        player_node = PlayerNode(player)
        player_list = PlayerList()
        player_list.push_back(player_node)

        removed_node = player_list.pop_back()

        self.assertEqual(removed_node, player_node, "Removed node should be the node that was pushed.")
        self.assertTrue(player_list.is_empty, "List should be empty after removing the only node.")
        self.assertIsNone(player_list.head, "Head should be None after removing the only node.")
        self.assertIsNone(player_list.tail, "Tail should be None after removing the only node.")

    def test_pop_back_multiple_nodes(self):
        player1 = Player("1", "Andrew")
        player2 = Player("2", "Rafael")

        player_node1 = PlayerNode(player1)
        player_node2 = PlayerNode(player2)

        player_list = PlayerList()
        player_list.push_back(player_node1)
        player_list.push_back(player_node2)

        removed_node = player_list.pop_back()

        self.assertEqual(removed_node, player_node2, "Removed node should be the node that was pushed last.")
        self.assertEqual(player_list.head, player_node1, "Head should remain unchanged after removal.")
        self.assertEqual(player_list.tail, player_node1, "Tail should be the previous node after removal.")
        self.assertIsNone(player_list.tail.player_next_node, "Tail node's next_node should be None.")

    def test_empty_list(self):
        player_list = PlayerList()

        self.assertTrue(player_list.is_empty, "PlayerList should be empty when initialized")

    def test_pop_by_uid_middle(self):
        player1 = Player("1", "Andrew")
        player2 = Player("2", "Rafael")
        player3 = Player("3", "Sam")

        player_node1 = PlayerNode(player1)
        player_node2 = PlayerNode(player2)
        player_node3 = PlayerNode(player3)

        player_list = PlayerList()

        player_list.push_back(player_node1)
        player_list.push_back(player_node2)
        player_list.push_back(player_node3)

        removed_node = player_list.pop_by_uid("2")

        self.assertEqual(len(player_list), 2)
        self.assertEqual(removed_node, player_node2, "The removed node should be player_node2")
        self.assertEqual(player_list.head, player_node1, "Head should still be player_node1")
        self.assertEqual(player_list.tail, player_node3, "Tail should still be player_node3")
        self.assertEqual(player_list.head.player_next_node, player_node3,
                         "player_node1's next_node should be player_node3")
        self.assertEqual(player_list.tail.player_prev_node, player_node1,
                         "player_node3's previous_node should be player_node1")

    def test_pop_by_uid_head(self):
        player1 = Player("1", "Andrew")
        player2 = Player("2", "Rafael")

        player_node1 = PlayerNode(player1)
        player_node2 = PlayerNode(player2)

        player_list = PlayerList()

        player_list.push_back(player_node1)
        player_list.push_back(player_node2)

        removed_node = player_list.pop_by_uid("1")

        self.assertEqual(len(player_list), 1)
        self.assertEqual(removed_node, player_node1, "The removed node should be player_node1")
        self.assertEqual(player_list.head, player_node2, "Head should now be player_node2")
        self.assertEqual(player_list.tail, player_node2, "Tail should also be player_node2")

    def test_pop_by_uid_tail(self):
        player1 = Player("1", "Andrew")
        player2 = Player("2", "Rafael")

        player_node1 = PlayerNode(player1)
        player_node2 = PlayerNode(player2)

        player_list = PlayerList()

        player_list.push_back(player_node1)
        player_list.push_back(player_node2)

        removed_node = player_list.pop_by_uid("2")

        self.assertEqual(len(player_list), 1)
        self.assertEqual(removed_node, player_node2, "The removed node should be player_node2")
        self.assertEqual(player_list.head, player_node1, "Head should still be player_node1")
        self.assertEqual(player_list.tail, player_node1, "Tail should also be player_node1")

    def test_pop_by_uid_empty_list(self):
        player_list = PlayerList()

        with self.assertRaises(IndexError, msg="List is empty"):
            player_list.pop_by_uid("1")

    def test_pop_by_uid_not_found(self):
        player1 = Player("1", "Andrew")
        player2 = Player("2", "Rafael")

        player_node1 = PlayerNode(player1)
        player_node2 = PlayerNode(player2)

        player_list = PlayerList()

        player_list.push_back(player_node1)
        player_list.push_back(player_node2)

        with self.assertRaises(ValueError, msg="Value not found"):
            player_list.pop_by_uid("3")

    def test_add_duplicate_player_node_by_uid(self):
        player1 = Player("1", "Alice")
        player2 = Player("1", "Bob")  # Same UID as player1

        node1 = PlayerNode(player1)
        node2 = PlayerNode(player2)

        player_list = PlayerList()

        player_list.push_front(node1)

        with self.assertRaises(ValueError):
            player_list.push_front(node2)

    def test_add_duplicate_player_node_same_object(self):
        player = Player("4", "David")

        node = PlayerNode(player)

        player_list = PlayerList()

        player_list.push_front(node)

        with self.assertRaises(ValueError):
            player_list.push_front(node)


if __name__ == "__main__":
    unittest.main()
