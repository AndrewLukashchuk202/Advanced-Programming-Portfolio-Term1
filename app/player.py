from __future__ import annotations
from collections import abc
import random


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
    _player_score: int

    def __init__(self, player_id: str, player_name: str, score: int = 0):
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
        self._player_score = score

    @property
    def score(self) -> int:
        """
        Get the player's score.

        Returns:
            int: The current score of the player.
        """
        return self._player_score

    @score.setter
    def score(self, player_score: int):
        """
        Set the player's score, ensuring it is a positive integer.

        Args:
            player_score (int): The new score for the player.

        Raises:
            ValueError: If the score is not a positive integer.
        """
        if player_score > 0:
            self._player_score = player_score

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
        """
        Set the player's name.

        Args:
           player_name (str): The new name for the player.
        """
        self._player_name = player_name

    @staticmethod
    def quicksort_descending(collection: abc.Iterable) -> list:
        """
        Sorts a collection of elements in descending order using the quicksort algorithm.

        This static method implements the quicksort algorithm to sort the given collection.
        It divides the collection into two sublists: one with elements greater than the pivot
        and the other with elements less than or equal to the pivot. It then recursively sorts
        these sublists and combines them with the pivot to form the final sorted list.

        Parameters:
        collection (Iterable): An iterable collection (e.g., list, tuple) of elements to be sorted.
                                The collection will be converted to a list if it is not already one.

        Returns:
        list: A new list containing all elements from the original collection, sorted in descending order.

        Example:
        >>> Player.quicksort_descending([4, 2, 7, 1, 3])
        [7, 4, 3, 2, 1]

        Notes:
        - The method assumes that the elements in the collection are comparable.
        - This method uses the first element of the collection as the pivot.
        - The time complexity of this implementation is O(n log n) on average, but can degrade to O(n^2) in the worst case.
        """
        collection = list(collection)
        if len(collection) < 2:
            return collection

        pivot = collection[0]
        gt_than_pivot = [v for v in collection[1:] if v > pivot]
        le_than_pivot = [v for v in collection[1:] if v <= pivot]
        return Player.quicksort_descending(gt_than_pivot) + [pivot] + Player.quicksort_descending(le_than_pivot)

    @staticmethod
    def sum_of_ascii_values(key: str | Player) -> int:
        """
        Calculate the sum of ASCII values of the characters in a string or a player's UID.

        Args:
            key (str | Player): A string or a Player object whose UID's ASCII sum is calculated.

        Returns:
            int: The sum of ASCII values of the characters in the key.

        Raises:
            TypeError: If the key is neither a string nor a Player object.
        """
        if isinstance(key, Player):
            key = key.uid
        elif not isinstance(key, str):
            raise TypeError("Key must be a string or a Player object")

        return sum(ord(char) for char in key)

    def __hash__(self) -> int:
        """
        Compute the hash value of the player using the sum of ASCII values of the UID.

        Returns:
            int: The hash value of the player.
        """
        return self.sum_of_ascii_values(self.uid)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Player):
            return NotImplemented
        else:
            return self._player_score == other._player_score

    def __ne__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        else:
            return self._player_score != other._player_score

    def __ge__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        else:
            return self._player_score >= other._player_score

    def __le__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        else:
            return self._player_score <= other._player_score

    def __gt__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        else:
            return self._player_score > other._player_score

    def __lt__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        else:
            return self._player_score < other._player_score

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


if __name__ == '__main__':
    # print(bin(Player.sum_of_ascii_values("12342Anrw25")))

    player = Player("uid", "Andrew").score = 100
    player1 = Player("uid", "Andrew").score = 80
    print(player)
    print(player1)

    arr = random.sample(range(20), 20)
    print(Player.quicksort_descending(arr))


