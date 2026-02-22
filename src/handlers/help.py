import structlog
from src.handlers.base import CommandHandler

logger = structlog.get_logger(__name__)


class HelpHandler(CommandHandler):
    def command(self) -> str:
        return "/help"

    async def handle(self, user_id: int, username: str | None) -> str:
        logger.info(
            "help_command_received",
            user_id=user_id,
            username=username,
        )

        return (
            "Доступные команды:\n"
            "/start - Начать работу\n"
            "/help - Показать список команд"
        )