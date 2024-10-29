from .abstract import AbstractModel

from sqlalchemy.orm import mapped_column
from sqlalchemy import String, DATE, Column


class UserModel(AbstractModel):
    first_name: str = mapped_column()
    last_name: str = mapped_column()
    surname: str = mapped_column()
    bdate = Column(DATE)
    city: str = mapped_column()
    phone: str = mapped_column()
    password: str = mapped_column()

    def __repr__(self) -> str:
        return f"User(\n\tid={self.id!r}\n\tФИО={self.first_name} {self.last_name} {self.surname}\n\tbdate={self.bdate}\n\tcity={self.city}\n\tphone={self.phone}\n)"
