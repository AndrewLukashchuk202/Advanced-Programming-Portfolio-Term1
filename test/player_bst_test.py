import unittest
from player import Player
from player_bnode import PlayerBNode
from player_bst import PlayerBST


class PlayerBSTTest(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("1", "Andrew")
        self.player2 = Player("2", "Rafael")
        self.player3 = Player("3", "Donatello")
        self.player4 = Player("4", "Michelangelo")

        self.player_bnode1 = PlayerBNode(self.player1)
        self.player_bnode2 = PlayerBNode(self.player2)
        self.player_bnode3 = PlayerBNode(self.player3)
        self.player_bnode4 = PlayerBNode(self.player4)

        self.player_bst = PlayerBST()

    def test_insert_new_player(self):
        self.player_bst.insert(self.player1)

        self.assertEqual(self.player_bst.root.player.name, "Andrew")

    def test_insert_multiple_players(self):
        self.player_bst.insert(self.player1)
        self.player_bst.insert(self.player2)
        self.player_bst.insert(self.player3)
        self.player_bst.insert(self.player4)

        # BST should look like next based on names:
        #                Andrew
        #              /        \
        #            None      Rafael
        #                      /      \
        #                Donatello     None
        #                /       \
        #               None       Michelangelo
        self.assertEqual(self.player_bst.root.player.name, "Andrew")
        self.assertEqual(self.player_bst.root.right.player.name, "Rafael")
        self.assertEqual(self.player_bst.root.right.left.player.name, "Donatello")
        self.assertEqual(self.player_bst.root.right.left.right.player.name, "Michelangelo")
