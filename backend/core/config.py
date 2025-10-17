# backend/core/config.py
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

class Settings(BaseSettings):
    # PostgreSQL / TimescaleDB
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432

    # MongoDB
    MONGO_USER: str
    MONGO_PASSWORD: str
    MONGO_HOST: str = "localhost"
    MONGO_PORT: int = 27017

    # API Keys
    FINNHUB_API_KEY: str
    VONAGE_API_KEY: str
    VONAGE_API_SECRET: str

    # JWT
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"

    # Member 2 specific
    REDIS_URL: str
    TS_HOST: str
    TS_PORT: int

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Create a single global settings instance
settings = Settings()
