class UnknownHandler:
    async def handle(self) -> str:
        return "Неизвестная команда. Воспользуйтесь /help, чтобы посмотреть список доступных команд."