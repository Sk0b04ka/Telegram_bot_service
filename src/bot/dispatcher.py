from typing import Iterable
from bot.handlers.base import CommandHandler
from bot.handlers.unknown import UnknownHandler


class CommandDispatcher:
    def __init__(self, handlers: Iterable[CommandHandler]) -> None:
        self._handlers = {h.command(): h for h in handlers}
        self._unknown_handler = UnknownHandler()

    async def dispatch(
        self, command: str, user_id: int, username: str | None
    ) -> str:
        handler = self._handlers.get(command)
        if handler:
            return await handler.handle(user_id, username)

        return await self._unknown_handler.handle()