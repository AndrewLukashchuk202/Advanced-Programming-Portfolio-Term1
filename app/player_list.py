from typing import Optional
from player_node import PlayerNode
from player import Player


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

    def push_front(self, player_node: Optional[PlayerNode]):
        if self._is_empty:
            self._head = self._tail = player_node
            self._is_empty = False
        else:
            player_node.player_next_node = self._head
            self._head.player_prev_node = player_node
            self._head = player_node

    def push_back(self, player_node: Optional[PlayerNode]):
        if self._is_empty:
            self._head = self._tail = player_node
            self._is_empty = False
        else:
            player_node.player_prev_node = self._tail
            self._tail.player_next_node = player_node
            self._tail = player_node

    def pop_front(self) -> Optional[PlayerNode]:
        if self._is_empty:
            raise IndexError("List is empty")

        deleted_node = self._head

        if self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            self._head.player_next_node.player_prev_node = None
            self._head = self._head.player_next_node

        self._is_empty = self._head is None

        return deleted_node

    def pop_back(self) -> Optional[PlayerNode]:
        if self._is_empty:
            raise IndexError("List is empty")

        deleted_node = self._tail

        if self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            self._tail.player_prev_node.player_next_node = None
            self._tail = self._tail.player_prev_node

        self._is_empty = self._head is None

        return deleted_node

    def pop_by_uid(self, key: str) -> Optional[PlayerNode]:
        if self._is_empty:
            raise IndexError("List is empty")

        current_node = self._head

        while current_node is not None:
            if current_node.key == key:

                # situation where node is in between the head and the tail
                if current_node.player_prev_node and current_node.player_next_node:
                    current_node.player_prev_node.player_next_node = current_node.player_next_node
                    current_node.player_next_node.player_prev_node = current_node.player_prev_node

                # situation where node is a head
                elif current_node.player_next_node:
                    current_node.player_next_node.player_prev_node = None
                    self._head = current_node.player_next_node

                # situation where node is a tail
                elif current_node.player_prev_node:
                    current_node.player_prev_node.player_next_node = None
                    self._tail = current_node.player_prev_node

                self._is_empty = self._head is None
                return current_node

            current_node = current_node.player_next_node
        raise ValueError("Value not found")

    def display(self, forward=True):
        if forward:
            current_node = self._head
            next_attr = "player_next_node"
        else:
            current_node = self._tail
            next_attr = "player_previous_node"

        while current_node is not None:
            print(current_node)
            current_node = getattr(current_node, next_attr)


if __name__ == '__main__':
    player1 = Player("1", "Andrew")
    player2 = Player("2", "Rafael")
    player_node1 = PlayerNode(player1)
    player_node2 = PlayerNode(player2)
    player_list = PlayerList()

    player_list.push_front(player_node1)
    player_list.push_front(player_node2)

    player_list.display()
