from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.schemas.request import UserAuthRequest, UserReplacePasswordRequest
from app.schemas.response import UserAuthResponse, UserReplacePasswordResponse
from app.middleware.globals import g
from app.services.hash_pass import get_password_hash, verify_password

from loguru import logger


auth_router = APIRouter()


@auth_router.post(path='/auth_user/', response_model=UserAuthResponse)
async def auth_user(user: UserAuthRequest) -> JSONResponse:
    orm = g.orm
    db_user = await orm.get_user(phone=user.phone)
    if verify_password(
            plain_password=user.password,
            hashed_password=db_user.password
    ):
        return JSONResponse(
            content={
                'status': 'ok',
                'data': 'Вы успешно авторизованы'
            }
        )


@auth_router.post(path='/replace_password/', response_model=UserReplacePasswordResponse)
async def replace_password(user: UserReplacePasswordRequest) -> JSONResponse:
    orm = g.orm
    db_user = await orm.replace_password(
        phone=user.phone,
        password=get_password_hash(user.password)
    )
    logger.info(db_user)
    return JSONResponse(
        content={
            'status': 'ok',
            'data': 'Пароль успешно сменён'
        }
    )
