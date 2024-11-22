from typing import Literal
from pydantic import BaseModel, Field


class UserRegisterRequest(BaseModel):
    first_name: str
    last_name: str
    surname: str
    bdate: int
    phone: str
    email: str
    password: str = Field(max_length=10)


class UserAuthRequest(BaseModel):
    phone: str = Field(max_length=20)
    password: str = Field(max_length=20)


class UserReplacePasswordRequest(BaseModel):
    phone: str = Field(max_length=20)
    password: str = Field(max_length=20)


class UserRegisterResponse(BaseModel):
    status: Literal['ok'] = 'ok'
    data: str


class UserAuthResponse(BaseModel):
    status: Literal['ok'] = 'ok'
    data: str


class UserReplacePasswordResponse(BaseModel):
    status: Literal['ok'] = 'ok'
    data: str
