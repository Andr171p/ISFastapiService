from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger

from src.database.models.base import Base


class AbstractModel(AsyncAttrs, Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        autoincrement=True,
        primary_key=True
    )


class UserModel(AbstractModel):
    first_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column()
    surname: Mapped[str] = mapped_column()
    phone: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column()

    def __repr__(self) -> str:
        return (
            f"User(\n"
            f"\tid={self.id!r}\n"
            f"\tname={self.first_name} {self.last_name} {self.surname}\n"
            f"\tphone={self.phone}\n"
            f"\tpassword={self.password}\n"
            f")"
        )
