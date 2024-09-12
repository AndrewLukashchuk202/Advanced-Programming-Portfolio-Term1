from __future__ import annotations
from player import Player
from typing import Optional


class PlayerNode:
    """
    Represents a node in a doubly linked list that contains a Player instance.

    Attributes:
    -----------
    _player : Player
        The player associated with this node.
    _player_next_node : Optional[PlayerNode]
        A reference to the next node in the linked list.
    _player_prev_node : Optional[PlayerNode]
        A reference to the previous node in the linked list.
    """
    _player = Player
    _player_next_node: PlayerNode | None
    _player_prev_node: PlayerNode | None

    def __init__(self, player: Player):
        """
        Initializes a PlayerNode with a given Player instance.

        Parameters:
        -----------
        player : Player
            The player instance to be associated with this node.

        Raises:
        -------
        ValueError:
            If the provided player is None or not an instance of Player.
        """
        if player is None or not isinstance(player, Player):
            raise ValueError("Must provide Player instance!")

        self._player = player
        self._player_next_node = None
        self._player_prev_node = None

    @property
    def player(self) -> Player:
        """
        Returns the player associated with this node.

        Returns:
        --------
        Player
            The player instance stored in this node.
        """
        return self._player

    @property
    def player_next_node(self) -> PlayerNode | None:
        """
       Returns the next node in the linked list.

       Returns:
       --------
       Optional[PlayerNode]
           The next PlayerNode in the list, or None if this is the last node.
       """
        return self._player_next_node

    @player_next_node.setter
    def player_next_node(self, player_next_node: PlayerNode | None = None):
        """
        Sets the reference to the next node in the linked list.

        Parameters:
        -----------
        player_next_node : Optional[PlayerNode]
            The next PlayerNode in the list, or None if this is the last node.
        """
        self._player_next_node = player_next_node

    @property
    def player_prev_node(self) -> PlayerNode | None:
        """
       Returns the previous node in the linked list.

       Returns:
       --------
       Optional[PlayerNode]
           The previous PlayerNode in the list, or None if this is the first node.
       """
        return self._player_prev_node

    @player_prev_node.setter
    def player_prev_node(self, player_prev_node: PlayerNode | None = None):
        """
        Sets the reference to the previous node in the linked list.

        Parameters:
        -----------
        player_prev_node : Optional[PlayerNode]
            The previous PlayerNode in the list, or None if this is the first node.
        """
        self._player_prev_node = player_prev_node

    @property
    def key(self) -> str:
        """
       Returns the unique ID of the player associated with this node.

       Returns:
       --------
       str
           The unique ID (uid) of the player.
       """
        return self._player.uid

    def equals(self, other) -> bool:
        """
       Checks if this node is equal to another PlayerNode.

       Equality is determined based on either:
       - The two nodes being the same instance.
       - The players they contain being equal.
       - The unique IDs (keys) of the players being the same.

       Parameters:
       -----------
       other : Any
           The other object to compare against.

       Returns:
       --------
       bool
           True if the nodes are considered equal, False otherwise.
       """
        if isinstance(other, PlayerNode):
            return (self == other or
                    self.player == other.player or
                    self.key == other.key)

        return False

    def __str__(self) -> str:
        """
       Returns a string representation of the PlayerNode.

       The string includes the player details and the memory addresses of
       the next and previous nodes.

       Returns:
       --------
       str
           A string representing the PlayerNode in the format:
           'PlayerNode(player=<Player>, next_node_id=<id>, prev_node_id=<id>)'.
       """
        return (f"PlayerNode(player={self._player}, "
                f"next_node_id={id(self._player_next_node)}, "
                f"prev_node_id={id(self._player_prev_node)})")


if __name__ == '__main__':
    player1 = Player("3", "Andrew")
    player_node = PlayerNode(player1)
    print(player_node.__str__())
