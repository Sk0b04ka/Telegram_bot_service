from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    telegram_token: str

    model_config = SettingsConfigDict(
        env_file=".env.example",
        env_file_encoding="utf-8",
    )


def get_settings() -> Settings:
    return Settings()