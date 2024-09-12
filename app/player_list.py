from typing import Optional
from player_node import PlayerNode
from player import Player


class PlayerList:
    """
    A doubly linked list implementation for managing PlayerNodes.

    Attributes:
    -----------
    _head : Optional[PlayerNode]
        The first node in the list, or None if the list is empty.
    _tail : Optional[PlayerNode]
        The last node in the list, or None if the list is empty.
    _is_empty : bool
        Indicates whether the list is empty.
    _length: int
        Keeps track of PlayerList size
    """

    _head: PlayerNode | None = None
    _tail: PlayerNode | None = None
    _is_empty: bool
    _length: int

    def __init__(self):
        """
        Initializes an empty PlayerList with no head, tail, and sets the list as empty.
        """
        self._head = None
        self._tail = None
        self._is_empty = True
        self._length = 0

    def __len__(self) -> int:
        """
        Returns the number of PlayerNode objects currently in the PlayerList.

        Returns:
            int: The number of PlayerNode objects in the PlayerList.
        """
        return self._length

    @property
    def is_empty(self) -> bool:
        """
        Returns whether the list is empty.

        Returns:
        --------
        bool
            True if the list is empty, False otherwise.
        """
        return self._is_empty

    @property
    def head(self) -> PlayerNode | None:
        """
        Returns the head node of the list.

        Returns:
        --------
        Optional[PlayerNode]
            The first node in the list, or None if the list is empty.
        """
        return self._head

    @property
    def tail(self) -> PlayerNode | None:
        """
        Returns the tail node of the list.

        Returns:
        --------
        Optional[PlayerNode]
            The last node in the list, or None if the list is empty.
        """
        return self._tail

    def can_add_node(self, new_node: PlayerNode | None = None) -> bool:
        """
        Checks if a node can be added to the list by ensuring there are no duplicates.

        Parameters:
        -----------
        new_node : Optional[PlayerNode]
            The node to check for duplication.

        Returns:
        --------
        bool
            True if the node can be added (i.e., it is not a duplicate), False otherwise.
        """
        return not any(filter(new_node.equals, self.iterate()))

    def push_front(self, player_node: PlayerNode | None = None):
        """
        Adds a node to the front of the list.

        Parameters:
        -----------
        player_node : Optional[PlayerNode]
            The node to add to the front of the list.

        Raises:
        -------
        ValueError:
            If the node already exists in the list.
        """
        if not self.can_add_node(player_node):
            raise ValueError(f"Player or PlayerNode already exists in the list with uid{player_node.key}")

        if self._is_empty:
            self._head = self._tail = player_node
            self._is_empty = False
        else:
            player_node.player_next_node = self._head
            self._head.player_prev_node = player_node
            self._head = player_node

        self._length += 1

    def push_back(self, player_node: PlayerNode | None = None):
        """
        Adds a node to the end of the list.

        Parameters:
        -----------
        player_node : Optional[PlayerNode]
            The node to add to the end of the list.

        Raises:
        -------
        ValueError:
            If the node already exists in the list.
        """
        if not self.can_add_node(player_node):
            raise ValueError(f"Player or PlayerNode already exists in the list with uid{player_node.key}")

        if self._is_empty:
            self._head = self._tail = player_node
            self._is_empty = False
        else:
            player_node.player_prev_node = self._tail
            self._tail.player_next_node = player_node
            self._tail = player_node

        self._length += 1

    def pop_from_front(self) -> PlayerNode | None:
        """
        Removes and returns the node at the front of the list.

        Returns:
        --------
        Optional[PlayerNode]
            The node that was removed from the front of the list.

        Raises:
        -------
        IndexError:
            If the list is empty.
        """
        if self._is_empty:
            raise IndexError("List is empty")

        deleted_node = self._head

        if self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            self._head.player_next_node.player_prev_node = None
            self._head = self._head.player_next_node
            self._head.player_next_node = None  # actually clearing the next reference to the node for the deleted node

        self._is_empty = self._head is None

        self._length -= 1

        return deleted_node

    def pop_from_back(self) -> PlayerNode | None:
        """
        Removes and returns the node at the end of the list.

        Returns:
        --------
        Optional[PlayerNode]
            The node that was removed from the end of the list.

        Raises:
        -------
        IndexError:
            If the list is empty.
        """
        if self._is_empty:
            raise IndexError("List is empty")

        deleted_node = self._tail

        if self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            self._tail.player_prev_node.player_next_node = None
            self._tail = self._tail.player_prev_node
            self._tail.player_prev_node = None  # clearing the prev reference to the node for the deleted node

        self._is_empty = self._head is None

        self._length -= 1

        return deleted_node

    def pop_by_uid(self, key: str) -> PlayerNode | None:
        """
        Removes and returns a node with the specified unique ID (key).

        Parameters:
        -----------
        key : str
            The unique ID of the node to remove.

        Returns:
        --------
        Optional[PlayerNode]
            The node that was removed.

        Raises:
        -------
        IndexError:
            If the list is empty.
        ValueError:
            If no node with the given ID is found.
        """
        if self._is_empty:
            raise IndexError("List is empty")

        current_node = self._head

        while current_node is not None:
            if current_node.key == key:

                # situation where node is in between the head and the tail
                if current_node.player_prev_node and current_node.player_next_node:
                    current_node.player_prev_node.player_next_node = current_node.player_next_node
                    current_node.player_next_node.player_prev_node = current_node.player_prev_node
                    # actually clearing the next reference to the node for the deleted node
                    current_node.player_prev_node = None
                    # clearing the prev reference to the node for the deleted node
                    current_node.player_next_node = None

                # situation where node is a head
                elif current_node.player_next_node:
                    current_node.player_next_node.player_prev_node = None
                    self._head = current_node.player_next_node
                    # actually clearing next reference to the node for the deleted node
                    current_node.player_next_node = None

                # situation where node is a tail
                elif current_node.player_prev_node:
                    current_node.player_prev_node.player_next_node = None
                    self._tail = current_node.player_prev_node
                    # actually clearing the prev reference to the node for the deleted node
                    current_node.player_prev_node = None

                # situation where node is a head and tail at the same time
                elif current_node == self._head and current_node == self._tail:
                    self._head = self._tail = None

                self._is_empty = self._head is None
                self._length -= 1
                return current_node

            current_node = current_node.player_next_node
        raise ValueError("Value not found")

    def iterate(self, forward: bool = True):
        """
        Iterates over the nodes in the list.

        Parameters:
        -----------
        forward : bool
            If True, iterates from head to tail; otherwise, from tail to head.

        Yields:
        -------
        PlayerNode
            The nodes in the list, one at a time.
        """
        direction = self._head if forward else self._tail

        while direction is not None:
            yield direction
            direction = direction.player_next_node if forward else direction.player_prev_node

    def display(self, forward=True):
        """
        Prints the nodes in the list.

        Parameters:
        -----------
        forward : bool
            If True, prints from head to tail; otherwise, from tail to head.

        Raises:
        -------
        ValueError:
            If the list is empty.
        """
        if self._is_empty:
            raise ValueError("List is empty!")

        if forward:
            current_node = self._head
            next_attr = "player_next_node"
        else:
            current_node = self._tail
            next_attr = "player_previous_node"

        while current_node is not None:
            print(current_node)
            current_node = getattr(current_node, next_attr)

    def find_node_by_key(self, uid: str) -> Optional[PlayerNode]:
        current = self._head
        while current:
            if current.key == uid:
                return current
            current = current.player_next_node
        return None


if __name__ == '__main__':
    player1 = Player("1", "Andrew")
    player2 = Player("2", "Rafael")
    player_node1 = PlayerNode(player1)
    player_node2 = PlayerNode(player2)
    player_list = PlayerList()

    player_list.push_front(player_node1)
    player_list.push_front(player_node2)

    player_list.display()
