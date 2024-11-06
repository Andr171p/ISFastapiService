from fastapi import FastAPI

from contextlib import asynccontextmanager

from src.app.middleware.globals import GlobalMiddleware, g
from src.app.routers.auth import auth_router
from src.database.services.orm import ORMService

from loguru import logger


@asynccontextmanager
async def lifespan(app: FastAPI) -> None:
    orm_service = ORMService()
    g.set_default('orm', orm_service)
    logger.info("Fastapi startup")
    yield
    del orm_service


app = FastAPI(
    title="IS registration/auth/verify",
    lifespan=lifespan
)

app.include_router(
    router=auth_router,
    prefix="/auth-service"
)

app.add_middleware(GlobalMiddleware)
