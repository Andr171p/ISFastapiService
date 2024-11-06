from sqlalchemy import select

from src.database.services.db import DatabaseSessionService
from src.database.models.user import UserModel


class ORMService(DatabaseSessionService):
    def __init__(self) -> None:
        super().__init__()
        self.init()

    async def create_users(self) -> None:
        async with self.connect() as connection:
            await connection.run_sync(UserModel.metadata.drop_all)
            await connection.run_sync(UserModel.metadata.create_all)

    async def add_user(self, user: UserModel) -> UserModel:
        async with self.session() as session:
            session.add(user)
            await session.commit()
            await session.refresh(user)
        return user

    async def get_user(
            self,
            phone: str = None,
            email: str = None
    ) -> UserModel | None:
        async with self.session() as session:
            if phone:
                query = select(UserModel).where(UserModel.phone == phone)
            elif email:
                select(UserModel).where(UserModel.email == email)
            user = await session.execute(query)
            try:
                return user.scalars().one()
            except Exception as _ex:
                print(_ex)

    async def replace_password(
            self,
            password: str,
            phone: str = None,
            email: str = None
    ) -> UserModel:
        async with self.session() as session:
            if phone:
                query = select(UserModel).where(UserModel.phone == phone)
            elif email:
                query = select(UserModel).where(UserModel.email == email)
            user = await session.execute(query)
            user = user.scalars().first()
            if user:
                user.password = password
                await session.commit()
                return user
            else:
                raise Exception("User not found")
