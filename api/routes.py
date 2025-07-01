from fastapi import APIRouter
api_router = APIRouter()

from controllers.HomeRouter import router as home_router
api_router.include_router(home_router, prefix="", tags=['Home'])