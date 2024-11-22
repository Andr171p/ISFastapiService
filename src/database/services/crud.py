from sqlalchemy import select

from src.database.models.base import Base
from src.database.services.db import DatabaseSessionService


class MainModel:
    full_name: str
    sur_name: str
    email: str


class Applicant(MainModel):
    snils: str


class CRUDService(DatabaseSessionService):
    def __init__(self, model: Base) -> None:
        super().__init__()
        self._model = model

    async def add(self, item: Base) -> Base:
        async with self.session() as session:
            session.add(item)
            await session.commit()
            await session.refresh(item)
        return item

    async def get(self, email: str) -> Base:
        async with self.session() as session:
            query = select(self._model).where(self._model.email == email)
            item = await session.execute(query)
            return item.scalars().one()

    async def get(self, password: int) -> Base:
        ...


class ORMApplicantService(CRUDService):
    def add_applicant(self, applicant: Applicant) -> ...:
        ...