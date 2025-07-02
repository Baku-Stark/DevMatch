from fastapi import APIRouter
api_router = APIRouter()

from controllers.HomeRouter import router as home_router
from controllers.UsersController import router as users_router
from controllers.SessionsController import router as session_router
api_router.include_router(home_router, prefix="", tags=['Home'])
api_router.include_router(users_router, prefix="/users", tags=["Users"])
api_router.include_router(session_router, prefix="/sessions", tags=["Sessions"])