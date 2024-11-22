from pydantic import BaseModel

import os
from dotenv import load_dotenv
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent

DOTENV_PATH: Path = BASE_DIR / ".env"


load_dotenv(dotenv_path=DOTENV_PATH)


class DBSettings(BaseModel):
    public_url: str = os.getenv("DB_PUBLIC_URL")


class Settings(BaseModel):
    db: DBSettings = DBSettings()


settings = Settings()
