from src.config import get_settings
from src.logging_config import setup_logging
from src.repository.user_repository import UserRepository
from src.handlers.start import StartHandler
from src.handlers.help import HelpHandler
from src.dispatcher import CommandDispatcher
from src.telegram_client import TelegramBotApp


def create_app() -> TelegramBotApp:
    setup_logging()
    settings = get_settings()

    user_repository = UserRepository()

    handlers = [
        StartHandler(user_repository),
        HelpHandler(),
    ]

    dispatcher = CommandDispatcher(handlers)

    return TelegramBotApp(settings.telegram_token, dispatcher)