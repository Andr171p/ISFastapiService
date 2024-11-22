from src.app.schemas.user import UserRegisterRequest
from src.app.services.hash_pass import get_password_hash
from src.database.models.user import UserModel


async def get_user_model(request: UserRegisterRequest) -> UserModel:
    user_model = UserModel(
        first_name=request.first_name,
        last_name=request.last_name,
        surname=request.surname,
        bdate=request.bdate,
        phone=request.phone,
        email=request.email,
        password=get_password_hash(request.password)
    )
    return user_model
