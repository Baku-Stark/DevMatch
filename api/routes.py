from fastapi import APIRouter
api_router = APIRouter()

from controllers.HomeRouter import router as home_router
from controllers.UsersController import router as users_router
from controllers.SessionsController import router as session_router
from controllers.AvailabilityController import router as availability_router
api_router.include_router(home_router, prefix="/api", tags=['Home'])
api_router.include_router(users_router, prefix="/api/users", tags=["Users"])
api_router.include_router(session_router, prefix="/api/sessions", tags=["Sessions"])
api_router.include_router(availability_router, prefix="/api/availability", tags=["Availability"])