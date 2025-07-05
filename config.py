from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    HOST: str = '127.0.0.1'
    PORT: int = 8000

    DATABASE_URL: str = 'sqlite+aiosqlite:///./db.sqlite'
    INIT_MODELS: bool = True


settings = Settings()
