from typing import Optional
from player_node import PlayerNode


class PlayerList:
    _head: Optional[PlayerNode]
    _tail: Optional[PlayerNode]
    _is_empty: bool

    def __init__(self):
        self._head = None
        self._tail = None
        self._is_empty = True

    @property
    def is_empty(self) -> bool:
        return self._is_empty

    @property
    def head(self) -> Optional[PlayerNode]:
        return self._head

    @property
    def tail(self) -> Optional[PlayerNode]:
        return self._tail

    def push_front(self, player_node: PlayerNode):
        if self.is_empty:
            self._head = self._tail = player_node
            self._is_empty = False
        else:
            player_node.player_next_node = self._head
            self._head.player_prev_node = player_node
            self._head = player_node

    def push_back(self, player_node: PlayerNode):
        if self.is_empty:
            self._head = self._tail = player_node
            self._is_empty = False
        else:
            player_node.player_prev_node = self._tail
            self._tail.player_next_node = player_node
            self._tail = player_node

