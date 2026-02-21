from abc import ABC, abstractmethod


class CommandHandler(ABC):
    @abstractmethod
    def command(self) -> str:
        pass

    @abstractmethod
    async def handle(self, user_id: int, username: str | None) -> str:
        pass