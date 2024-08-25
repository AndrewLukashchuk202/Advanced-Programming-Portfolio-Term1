from __future__ import annotations


class Player:
    """
       Represents a player with a unique ID and a name.

       Attributes:
       -----------
       _player_id : str
           A unique identifier for the player.
       _player_name : str
           The name of the player.

       Methods:
       --------
       uid() -> str
           Returns the player's unique ID.

       name() -> str
           Returns the player's name.

       __str__() -> str
           Returns a string representation of the Player instance in the
           format 'Player(player_name=<name>, player_id=<id>)'.
       """

    _player_id: str
    _player_name: str

    def __init__(self, player_id: str, player_name: str):
        """
       Initializes a Player instance with the provided ID and name.

       Parameters:
       -----------
       player_id : str
           The unique identifier for the player.
       player_name : str
           The name of the player.
       """
        self._player_id = player_id
        self._player_name = player_name

    @property
    def uid(self) -> str:
        """
        Returns the unique ID of the player.

        Returns:
        --------
        str
            The unique identifier of the player.
        """
        return self._player_id

    @property
    def name(self) -> str:
        """
        Returns the name of the player.

        Returns:
        --------
        str
            The name of the player.
        """
        return self._player_name

    @name.setter
    def name(self, player_name: str):
        self._player_name = player_name

    @staticmethod
    def sum_of_ascii_values(key: str | Player) -> int:
        if isinstance(key, Player):
            key = key.uid
        elif not isinstance(key, str):
            raise TypeError("Key must be a string or a Player object")

        return sum(ord(char) for char in key)

    def __hash__(self) -> int:
        return self.sum_of_ascii_values(self.uid)

    def __eq__(self, other) -> bool:
        return isinstance(other, Player) and self.uid == other.uid

    def __str__(self) -> str:
        """
        Returns a string representation of the Player instance.

        The string includes the player's name and ID in the format:
        'Player(player_name=<name>, player_id=<id>)'.

        Returns:
        --------
        str
            A string representing the Player instance.
        """
        return (f"Player(player_name={self.name}, "
                f"player_id={self.uid})")

print(bin(Player.sum_of_ascii_values("12342Anrw25")))