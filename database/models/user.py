from .abstract import AbstractModel

from sqlalchemy.orm import Mapped, mapped_column

from datetime import datetime


class UserModel(AbstractModel):
    first_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column()
    surname: Mapped[str] = mapped_column()
    bdate: Mapped[datetime] = mapped_column()
    city: Mapped[str] = mapped_column()
    phone: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column()

    def __repr__(self) -> str:
        return f"User(\n\tid={self.id!r}\n\tФИО={self.first_name} {self.last_name} {self.surname}\n\tbdate={self.bdate}\n\tcity={self.city}\n\tphone={self.phone}\n)"
