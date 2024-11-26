from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.app.middleware.globals import g
from src.app.services.hash_pass import verify_password, get_password_hash
from src.database.models.user import UserModel
from src.app.schemas.user import (
    UserSchema,
    AuthSchema,
    ReplacePasswordSchema,
    DeleteSchema,
    UserAuthResponse,
    UserRegisterResponse,
    UserReplacePasswordResponse
)


from loguru import logger


auth_router = APIRouter()


@auth_router.post(path='/register/', response_model=UserRegisterResponse)
async def register_user(user: UserSchema) -> JSONResponse:
    orm = g.orm
    if await orm.get_user(phone=user.phone):
        return JSONResponse(
            content={
                'status': 'ok',
                'data': 'Вы уже зарегистрированы'
            }
        )
    user.password = get_password_hash(user.password)
    db_user = await orm.add_user(user=UserModel(**user.__dict__))
    logger.info(db_user)
    return JSONResponse(
        content={
            'status': 'ok',
            'data': 'Вы успешно зарегистрированы'
        }
    )


@auth_router.post(path='/auth/', response_model=UserAuthResponse)
async def auth_user(user: AuthSchema) -> JSONResponse:
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
    else:
        return JSONResponse(
            content={
                'status': 'ok',
                'data': 'Неверный пароль'
            }
        )


@auth_router.post(path='/replace-password/', response_model=UserReplacePasswordResponse)
async def replace_password(user: ReplacePasswordSchema) -> JSONResponse:
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


@auth_router.post(path="/delete/")
async def delete_user(user: DeleteSchema) -> JSONResponse:
    orm = g.orm
    _ = await orm.delete_user(user.phone)
    return JSONResponse(
        content={
            "status": "ok",
            "data": "Пользователь удалён"
        }
    )
