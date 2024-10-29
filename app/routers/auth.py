from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.schemas.request import UserAuthRequest
from app.schemas.response import UserAuthResponse
from app.middleware.globals import g


auth_router = APIRouter()


@auth_router.post(path='/auth_user/', response_model=UserAuthResponse)
async def auth_user(user: UserAuthRequest) -> JSONResponse:
    orm = g.orm
    exist_user = await orm.get_user(phone=user.phone)
    if exist_user.password == user.password:
        return JSONResponse(
            content={
                'status': 'ok',
                'data': 'Вы успешно авторизованы'
            }
        )


