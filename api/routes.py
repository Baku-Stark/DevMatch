import importlib
from fastapi import APIRouter
# controllers_config.py

controllers = [
    {
        "module": "controllers.AdminTokenGeneratorController",
        "prefix": "",
        "tags": ["ADMIN"]
    },
    {
        "module": "controllers.HomeRouter",
        "prefix": "/api/v2",
        "tags": ["Home"]
    },
    {
        "module": "controllers.UsersController",
        "prefix": "/api/v2/users",
        "tags": ["Users"]
    },
    {
        "module": "controllers.SessionsController",
        "prefix": "/api/v2/sessions",
        "tags": ["Sessions"]
    },
    {
        "module": "controllers.AvailabilityController",
        "prefix": "/api/availability",
        "tags": ["Availability"]
    },
    {
        "module": "controllers.LanguagesController",
        "prefix": "/api/v2/languages",
        "tags": ["Languages"]
    },
    {
        "module": "controllers.TechStacksController",
        "prefix": "/api/v2/tech_stacks",
        "tags": ["Tech Stacks"]
    },
    {
        "module": "controllers.MentorshipProfilesController",
        "prefix": "/api/v2/mentorship_profiles",
        "tags": ["Mentorship Profiles"]
    },
    {
        "module": "controllers.UserTechStacksController",
        "prefix": "/api/v2/user_tech_stacks",
        "tags": ["Tech Stacks"]
    }
]

api_router = APIRouter()

for conf in controllers:
    module = importlib.import_module(conf['module'])
    router = getattr(module, 'router')
    api_router.include_router(router, prefix=conf['prefix'], tags=conf['tags'])