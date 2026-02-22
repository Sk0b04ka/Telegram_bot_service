import pytest

from dispatcher import CommandDispatcher
from handlers.start import StartHandler
from handlers.help import HelpHandler
from repository.user_repository import UserRepository


@pytest.mark.asyncio
async def test_start_command():
    repo = UserRepository()
    dispatcher = CommandDispatcher([StartHandler(repo), HelpHandler()])

    response = await dispatcher.dispatch("/start", 1, "user")
    assert "Добро пожаловать" in response


@pytest.mark.asyncio
async def test_help_command():
    repo = UserRepository()
    dispatcher = CommandDispatcher([StartHandler(repo), HelpHandler()])

    response = await dispatcher.dispatch("/help", 1, "user")
    assert "Доступные команды" in response


@pytest.mark.asyncio
async def test_unknown_command():
    repo = UserRepository()
    dispatcher = CommandDispatcher([StartHandler(repo), HelpHandler()])

    response = await dispatcher.dispatch("/unknown", 1, "user")
    assert "Неизвестная команда" in response