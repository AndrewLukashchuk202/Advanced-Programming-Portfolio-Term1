from __future__ import annotations

from player import Player


class PlayerNode:
    def __init__(self, player: Player):
        self._player = player
        self._player_next_node = None
        self._player_prev_node = None

    @property
    def player(self) -> Player:
        return self._player

    @property
    def player_next_node(self) -> PlayerNode:
        return self._player_next_node


