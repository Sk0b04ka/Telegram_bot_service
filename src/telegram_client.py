from telegram import Update, BotCommand
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    MessageHandler,
    filters,
)

from dispatcher import CommandDispatcher


class TelegramBotApp:
    def __init__(self, token: str, dispatcher: CommandDispatcher) -> None:
        self._dispatcher = dispatcher
        self._application = ApplicationBuilder().token(token).build()

        self._application.add_handler(
            MessageHandler(filters.TEXT & ~filters.COMMAND, self._handle_text)
        )
        self._application.add_handler(
            MessageHandler(filters.COMMAND, self._handle_command)
        )

    async def _handle_command(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ) -> None:
        message = update.message
        if not message:
            return

        response = await self._dispatcher.dispatch(
            message.text,
            message.from_user.id,
            message.from_user.username,
        )

        await message.reply_text(response)

    async def _handle_text(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ) -> None:
        if update.message:
            await update.message.reply_text(
                "Неизвестная команда. Воспользуйтесь /help, чтобы посмотреть список доступных команд."
            )

    async def _set_commands(self, _) -> None:
        await self._application.bot.set_my_commands(
            [
                BotCommand("start", "Начать работу"),
                BotCommand("help", "Список команд"),
            ]
        )

    def run_polling(self) -> None:
        self._application.post_init = self._set_commands
        self._application.run_polling()