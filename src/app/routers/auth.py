from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.app.controllers.users import get_user_model
from src.app.middleware.globals import g
from src.app.services.hash_pass import verify_password, get_password_hash
from src.app.schemas.request import (
    UserAuthRequest,
    UserRegisterRequest,
    UserReplacePasswordRequest
)
from src.app.schemas.response import (
    UserAuthResponse,
    UserRegisterResponse,
    UserReplacePasswordResponse
)

from loguru import logger


auth_router = APIRouter()


@auth_router.post(path='/register/', response_model=UserRegisterResponse)
async def register_user(request: UserRegisterRequest) -> JSONResponse:
    orm = g.orm
    user = await get_user_model(request=request)
    if await orm.get_user(phone=user.phone):
        return JSONResponse(
            content={
                'status': 'ok',
                'data': 'Вы уже зарегистрированы'
            }
        )
    db_user = await orm.add_user(user=user)
    logger.info(db_user)
    return JSONResponse(
        content={
            'status': 'ok',
            'data': 'Вы успешно зарегистрированы'
        }
    )


@auth_router.post(path='/auth/', response_model=UserAuthResponse)
async def auth_user(request: UserAuthRequest) -> JSONResponse:
    orm = g.orm
    db_user = await orm.get_user(phone=request.phone)
    if verify_password(
            plain_password=request.password,
            hashed_password=db_user.password
    ):
        return JSONResponse(
            content={
                'status': 'ok',
                'data': 'Вы успешно авторизованы'
            }
        )
    else:
        return JSONResponse(
            content={
                'status': 'ok',
                'data': 'Неверный пароль'
            }
        )


@auth_router.post(path='/replace-password/', response_model=UserReplacePasswordResponse)
async def replace_password(request: UserReplacePasswordRequest) -> JSONResponse:
    orm = g.orm
    db_user = await orm.replace_password(
        phone=request.phone,
        password=get_password_hash(request.password)
    )
    logger.info(db_user)
    return JSONResponse(
        content={
            'status': 'ok',
            'data': 'Пароль успешно сменён'
        }
    )
