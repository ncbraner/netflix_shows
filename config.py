from pydantic import BaseSettings
import os
from functools import lru_cache
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    secret_key: str = 'SECRET'
    mysql_url = os.getenv('DATABASE_URL')


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
