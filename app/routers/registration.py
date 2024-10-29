from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from app.schemas.request import UserRegisterRequest
from app.schemas.response import UserRegisterResponse
from app.middleware.globals import g
from app.services.hash_pass import get_password_hash

from database.models.user import UserModel

from loguru import logger


registration_router = APIRouter()


@registration_router.post(path='/register_user/', response_model=UserRegisterResponse)
async def register_user(user: UserRegisterRequest) -> JSONResponse:
    orm = g.orm
    user_model = UserModel(
        first_name=user.first_name,
        last_name=user.last_name,
        surname=user.surname,
        bdate=user.bdate,
        city=user.city,
        phone=user.phone,
        password=get_password_hash(user.password)
    )
    if await orm.get_user(phone=user_model.phone):
        # raise HTTPException(status_code=400, detail="User already registered")
        return JSONResponse(
            content={
                'status': 'ok',
                'data': 'Вы уже зарегистрированы'
            }
        )
    registered_user = await orm.create_user(user=user_model)
    logger.info(registered_user)
    return JSONResponse(
        content={
            'status': 'ok',
            'data': 'Вы успешно зарегистрированы'
        }
    )