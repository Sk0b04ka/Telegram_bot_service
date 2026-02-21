from config import Settings
from logging_config import setup_logging
from repository.user_repository import UserRepository
from handlers.start import StartHandler
from handlers.help import HelpHandler
from dispatcher import CommandDispatcher
from telegram_client import TelegramBotApp


def create_app() -> TelegramBotApp:
    setup_logging()
    settings = Settings.load()

    user_repository = UserRepository()

    handlers = [
        StartHandler(user_repository),
        HelpHandler(),
    ]

    dispatcher = CommandDispatcher(handlers)

    return TelegramBotApp(settings.telegram_token, dispatcher)