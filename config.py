from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    HOST: str = '127.0.0.1'
    PORT: int = 8000

    DATABASE_URL: str = 'postgresql+asyncpg://postgres:112358@10.82.147.29:3453/postgres'
    INIT_MODELS: bool = False



settings = Settings()
