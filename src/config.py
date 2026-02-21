import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    telegram_token: str

    @staticmethod
    def load() -> "Settings":
        token = os.getenv("TELEGRAM_TOKEN")
        if not token:
            raise RuntimeError("TELEGRAM_TOKEN is not set")
        return Settings(telegram_token=token)