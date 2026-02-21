import logging
from .base import CommandHandler
from repository.user_repository import UserRepository

logger = logging.getLogger(__name__)


class StartHandler(CommandHandler):
    def __init__(self, user_repository: UserRepository) -> None:
        self._repo = user_repository

    def command(self) -> str:
        return "/start"

    async def handle(self, user_id: int, username: str | None) -> str:
        is_new = not self._repo.exists(user_id)
        if is_new:
            self._repo.add(user_id, username)

        logger.info(
            "start_command_received",
            extra={"user_id": user_id, "username": username, "is_new": is_new},
        )

        return "Добро пожаловать! Используйте /help, чтобы посмотреть доступные команды."