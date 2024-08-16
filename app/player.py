class Player:
    def __init__(self, player_id: str, player_name: str):
        self._player_id = player_id
        self._player_name = player_name

    @property
    def uid(self) -> str:
        return self._player_id

    @property
    def name(self) -> str:
        return self._player_name

    def __str__(self):
        class_name = self.__class__.__name__
        return (f"class name={class_name}, "
                f"player name={self._player_name}, "
                f"player id={self._player_id}")



