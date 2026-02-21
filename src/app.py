from bot.config import Settings
from bot.logging_config import setup_logging
from bot.repository.user_repository import UserRepository
from bot.handlers.start import StartHandler
from bot.handlers.help import HelpHandler
from bot.dispatcher import CommandDispatcher
from bot.telegram_client import TelegramBotApp


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