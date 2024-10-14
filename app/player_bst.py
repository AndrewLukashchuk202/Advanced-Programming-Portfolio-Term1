from __future__ import annotations
from player_bnode import PlayerBNode
from player import Player


class PlayerBST:
    root: PlayerBNode | None

    def __init__(self):
        self._root = None

    @property
    def root(self) -> PlayerBNode:
        return self._root

    @root.setter
    def root(self, root: PlayerBNode):
        self._root = root

    def insert(self, player: Player):
        if not self._root:
            self._root = PlayerBNode(player)
        else:
            self._insert_recursively(self._root, player)

    def _insert_recursively(self, node: PlayerBNode, player: Player):
        if player.name < node.player.name:
            if node.left is None:
                node.left = PlayerBNode(player)
            else:
                self._insert_recursively(node.left, player)
        elif player.name > node.player.name:
            if node.right is None:
                node.right = PlayerBNode(player)
            else:
                self._insert_recursively(node.right, player)
        else:  # if names are equal, we update the object(PlayerBNode) so the player's information stays relevant
            node.player = player
