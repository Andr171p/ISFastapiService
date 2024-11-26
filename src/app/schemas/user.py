import re
from typing import Literal
from pydantic import BaseModel, field_validator


class UserSchema(BaseModel):
    first_name: str
    last_name: str
    surname: str
    phone: str
    password: str

    @field_validator("password")
    @classmethod
    def validate_password(cls, v: str) -> str:
        if not re.match(r'^[а-яё]+$', v):
            raise ValueError("Пароль должен содержать только строчные русские символы")
        if len(v) != 9:
            raise ValueError("длина пароля должна быть 9 символов")
        return v


class AuthSchema(BaseModel):
    phone: str
    password: str


class ReplacePasswordSchema(BaseModel):
    phone: str
    password: str


class DeleteSchema(BaseModel):
    phone: str


class UserRegisterResponse(BaseModel):
    status: Literal['ok'] = 'ok'
    data: str


class UserAuthResponse(BaseModel):
    status: Literal['ok'] = 'ok'
    data: str


class UserReplacePasswordResponse(BaseModel):
    status: Literal['ok'] = 'ok'
    data: str
