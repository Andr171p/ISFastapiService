from fastapi import FastAPI

from contextlib import asynccontextmanager

from app.middleware.globals import GlobalMiddleware, g
from app.routers.registration import registration_router
from app.routers.auth import auth_router

from database.services.orm import ORMService

from loguru import logger


@asynccontextmanager
async def lifespan(app: FastAPI) -> None:
    orm_service = ORMService()
    g.set_default('orm', orm_service)
    logger.info("Fastapi startup")
    yield
    del orm_service


fastapi_app = FastAPI(
    title="IS registration/auth/verify",
    lifespan=lifespan
)

fastapi_app.include_router(
    router=registration_router,
    prefix="/registration"
)


fastapi_app.add_middleware(GlobalMiddleware)
