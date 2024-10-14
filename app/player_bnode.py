from __future__ import annotations
from .player import Player


class PlayerBNode:
    _value: Player
    _right: PlayerBNode | None
    _left: PlayerBNode | None

    def __init__(self, player: Player):
        self._value = player
        self._left = None
        self._right = None

    @property
    def value(self):
        return self._value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, player: PlayerBNode):
        self._left = player

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, player: PlayerBNode):
        self._right = player
