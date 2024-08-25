from __future__ import annotations
from typing import List
from player_list import PlayerList
from player_node import PlayerNode
from player import Player


class PlayerHashMap:
    """
    A hash map implementation for storing and managing Player objects.

    This class uses a hash table with separate chaining to handle collisions.
    It provides functionality to insert, retrieve, update, and delete Player objects
    based on unique keys. It also supports efficient retrieval of the number of stored players.

    Attributes:
        SIZE (int): The size of the hash map (number of buckets).
        hashmap (List[PlayerList]): The list of PlayerList objects that represent the hash map.
        length (int): The current number of players in the hash map.
    """
    SIZE: int = 10
    length: int
    hashmap: List[PlayerList]  # A list where each element is a PlayerList.
    # This list represents the hash map's buckets for separate chaining.

    def __init__(self):
        """
        Initialize an empty hash map with a fixed size.
        """
        self.hashmap = [PlayerList() for _ in range(self.SIZE)]
        self._length = 0

    # For knowledge purposes, there is a check if an argument is an instance of the Player object or a string
    # to use the dunder hash function on the Player object or use the custom hash function directly using the static
    # method but in both cases we end up using the same function, though with a hash() function a value can be truncated
    def get_index(self, key: str | Player) -> int:
        """
        Calculate the index for the given key in the hash map.

        Args:
             key (str | Player): The key for which to calculate the index.

        Returns:
            int: The index in the hash map corresponding to the given key.
        """
        if isinstance(key, Player):
            return hash(key) % self.SIZE
        else:
            return Player.sum_of_ascii_values(key) % self.SIZE

    def __getitem__(self, key: str | Player) -> Player:
        """
        Retrieve a Player object from the hash map using the given key.

        Args:
            key (str): The key associated with the player to retrieve.

        Returns:
            Player: The Player object associated with the given key.

        Raises:
            KeyError: If no player is found with the given key.
        """
        index = self.get_index(key)
        player_list = self.hashmap[index]

        existing_player_node = player_list.find_node_by_key(key)

        if not existing_player_node:
            raise KeyError(f"Key {key} not found")

        return existing_player_node.player

    def __setitem__(self, key: str | Player, name: str):
        """
        Insert or update a Player in the hash map with the given key and name.

        Args:
            key (str): The key for the player.
            name (str): The name of the player.

        Raises:
            ValueError: If a player with the given key already exists and updating is not desired.
        """
        index = self.get_index(key)
        player_list = self.hashmap[index]

        existing_player_node = player_list.find_node_by_key(key)

        if not existing_player_node:
            new_player = Player(key, name)
            new_player_node = PlayerNode(new_player)
            player_list.push_front(new_player_node)
            self._length += 1
        else:
            existing_player_node.player.name = name

    def __len__(self) -> int:
        """
        Get the number of players currently stored in the hash map.

        Returns:
            int: The number of players in the hash map.
        """
        return self._length

    def __delitem__(self, key):
        """
        Delete a Player from the hash map using the given key.

        Args:
            key (str): The key of the player to delete.

        Raises:
            KeyError: If no player is found with the given key.
        """
        index = self.get_index(key)
        player_list = self.hashmap[index]

        existing_player_node = player_list.find_node_by_key(key)

        if not existing_player_node:
            raise KeyError(f"Key {key} not found")

        player_list.pop_by_uid(key)
        self._length -= 1

    def display(self):
        """
        Display the contents of the hash map.

        Prints the index and contents of each non-empty PlayerList in the hash map.
        """
        if len(self) == 0:
            print("The hash table is empty")
            return

        for index, player_list in enumerate(self.hashmap):
            if player_list.is_empty:
                continue
            print(f"Index of the player_list {index}")
            player_list.display()
