from __future__ import annotations
from player import Player
from typing import Optional


class PlayerNode:
    _player = Player
    _player_next_node: Optional[PlayerNode]
    _player_prev_node: Optional[PlayerNode]

    def __init__(self, player: Player):
        self._player = player
        self._player_next_node = None
        self._player_prev_node = None

    @property
    def player(self) -> Player:
        return self._player

    @property
    def player_next_node(self) -> Optional[PlayerNode]:
        return self._player_next_node

    @player_next_node.setter
    def player_next_node(self, player_next_node: Optional[PlayerNode]):
        self._player_next_node = player_next_node

    @property
    def player_prev_node(self) -> Optional[PlayerNode]:
        return self._player_prev_node

    @player_prev_node.setter
    def player_prev_node(self, player_prev_node: Optional[PlayerNode]):
        self._player_prev_node = player_prev_node

    @property
    def key(self) -> str:
        return self._player.uid

    def __str__(self) -> str:
        return (f"PlayerNode(player={self._player}, "
                f"next_node_id={id(self._player_next_node)}, "
                f"prev_node_id={id(self._player_prev_node)})")


if __name__ == '__main__':
    player1 = Player("3", "Andrew")
    player_node = PlayerNode(player1)
    print(player_node.__str__())
