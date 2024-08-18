class Player:
    _player_id: str
    _player_name: str

    def __init__(self, player_id: str, player_name: str):
        self._player_id = player_id
        self._player_name = player_name

    @property
    def uid(self) -> str:
        return self._player_id

    @property
    def name(self) -> str:
        return self._player_name

    def __str__(self) -> str:
        return (f"Player(player_name={self.name}, "
                f"player_id={self.uid})")
