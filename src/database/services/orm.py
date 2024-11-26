from sqlalchemy import select, delete

from src.app.services.hash_pass import verify_password

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

    async def get_user(self, phone: str) -> UserModel | None:
        async with self.session() as session:
            query = select(UserModel).where(UserModel.phone == phone)
            user = await session.execute(query)
            try:
                return user.scalars().one()
            except Exception as _ex:
                print(_ex)

    async def replace_password(
            self,
            password: str,
            phone: str
    ) -> UserModel:
        async with self.session() as session:
            query = select(UserModel).where(UserModel.phone == phone)
            user = await session.execute(query)
            user = user.scalars().first()
            print(user)
            print(user.password)
            print(user.surname.lower())
            if verify_password(plain_password=user.surname.lower(), hashed_password=user.password):
                user.password = password
                await session.commit()
                return user
            else:
                raise Exception("password != surname")

    async def delete_user(self, phone: str) -> bool:
        async with self.session() as session:
            query = delete(UserModel).where(UserModel.phone == phone)
            cursor = await session.execute(query)
            await session.flush()
            return cursor.rowcount > 0
