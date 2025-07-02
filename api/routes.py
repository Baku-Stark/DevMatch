from fastapi import APIRouter

api_router = APIRouter()

from controllers.HomeRouter import router as home_router
from controllers.UsersController import router as users_router
from controllers.SessionsController import router as session_router
from controllers.AvailabilityController import router as availability_router
from controllers.LanguagesController import router as languages_router
from controllers.TechStacksController import router as tech_stacks_router
# =============================
api_router.include_router(home_router, prefix="/api", tags=['Home'])
api_router.include_router(users_router, prefix="/api/users", tags=["Users"])
api_router.include_router(session_router, prefix="/api/sessions", tags=["Sessions"])
api_router.include_router(availability_router, prefix="/api/availability", tags=["Availability"])
api_router.include_router(languages_router, prefix="/api/languages", tags=["Languages"])
api_router.include_router(tech_stacks_router, prefix="/api/tech_stacks", tags=["Tech Stacks"])