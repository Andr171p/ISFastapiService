from pydantic import BaseModel

import os
from dotenv import load_dotenv
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent

DOTENV_PATH: Path = BASE_DIR / ".env"


load_dotenv(dotenv_path=DOTENV_PATH)


class DBSettings(BaseModel):
    public_url: str = ""


class AuthJWT(BaseModel):
    private_key_path: Path = BASE_DIR / "certs" / "jwt-private.pem"
    public_key_path: Path = BASE_DIR / "certs" / "jwt-public.pem"
    algorithm: str = "RS256"


class SMTPSettings(BaseModel):
    adress: str = "smtp.mail.ru"
    port: int = 465


class EmailAuth(BaseModel):
    adress: str = os.getenv("EMAIL_ADRESS")
    password: str = os.getenv("EMAIL_PASSWORD")


class Settings(BaseModel):
    api_prefix: str = ''
    db: DBSettings = DBSettings()
    auth_jwt: AuthJWT = AuthJWT()
    email_auth: EmailAuth = EmailAuth()
    smtp: SMTPSettings = SMTPSettings()


settings = Settings()
