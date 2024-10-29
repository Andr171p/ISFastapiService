from pydantic import BaseModel

from typing import Literal


class UserRegisterResponse(BaseModel):
    status: Literal['ok'] = 'ok'
    data: str


class UserAuthResponse(BaseModel):
    status: Literal['ok'] = 'ok'
    data: str
