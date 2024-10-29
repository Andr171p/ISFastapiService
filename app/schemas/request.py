from datetime import datetime

from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)


class UserRegisterRequest(BaseModel):
    first_name: str
    last_name: str
    surname: str
    bdate: datetime
    city: str
    phone: str = Field(max_length=20)
    password: str = Field(max_length=10)


class UserAuthRequest(BaseModel):
    phone: str = Field(max_length=20)
    password: str = Field(max_length=20)
