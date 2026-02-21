class UserRepository:
    def __init__(self) -> None:
        self._users: dict[int, str] = {}

    def add(self, user_id: int, username: str | None) -> None:
        self._users[user_id] = username or ""

    def exists(self, user_id: int) -> bool:
        return user_id in self._users
    