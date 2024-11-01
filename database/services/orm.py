from sqlalchemy import select

from database.services.db import DatabaseSessionService
from database.models.user import UserModel


class ORMService(DatabaseSessionService):
    def __init__(self) -> None:
        super().__init__()
        self.init()

    async def create_table(self) -> None:
        async with self.connect() as connection:
            await connection.run_sync(UserModel.metadata.drop_all)
            await connection.run_sync(UserModel.metadata.create_all)

    async def create_user(self, user: UserModel) -> UserModel:
        async with self.session() as session:
            session.add(user)
            await session.commit()
            await session.refresh(user)
        return user

    async def get_user(self, phone: str) -> UserModel | None:
        async with self.session() as session:
            user = await session.execute(
                select(UserModel).where(UserModel.phone == phone)
            )
            try:
                return user.scalars().one()
            except Exception as _ex:
                print(_ex)

    async def replace_password(self, phone: str, password: str) -> UserModel:
        async with self.session() as session:
            user = await session.execute(
                select(UserModel).where(UserModel.phone == phone)
            )
            user = user.scalars().first()
            if user:
                user.password = password
                await session.commit()
                return user
            else:
                raise Exception("User not found")
