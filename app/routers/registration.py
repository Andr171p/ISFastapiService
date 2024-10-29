from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.schemas.request import UserRegisterRequest
from app.schemas.response import UserRegisterResponse
from app.middleware.globals import g

from database.models.user import UserModel


registration_router = APIRouter()


@registration_router.post(path='/register_user/', response_model=UserRegisterResponse)
async def register_user(user: UserRegisterRequest) -> JSONResponse:
    orm = g.orm
    registered_user = await orm.create_user(user=user)
    return JSONResponse(
        content={
            'status': 'ok',
            'data': 'Вы успешно зарегистрированы'
        }
    )