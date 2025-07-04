from fastapi.exceptions import ResponseValidationError
from sqlalchemy.orm import Session

from api.logger import logger
from api.services.MentorshipProfilesService import insert_new_mentorship_profile, get_users_mentors
from api.services.Monitoramento import Monitoramento
monitor = Monitoramento()

from fastapi import APIRouter, status, Request, HTTPException, Depends
from api.schemas.mentorship_profiles import MentorshipProfilesRead, MentorshipProfilesCreate, MentorProfileRead

router = APIRouter()

import api.db.database as database

# Dependência para FastAPI
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get(
    "/",
    response_model=list[MentorProfileRead],
    status_code=status.HTTP_200_OK,
    summary="Resgatar uma lista do perfil de todos os mentores"
)
async def get_mentorship_profiles(request: Request, db: Session = Depends(get_db)):
    user_ip = request.client.host

    try:
        monitor.registrar_acao(f"Acessou a rota Mentorship Profiles", ip=user_ip)  # MÉTODO DE REGISTRO NO ARQUIVO EXCEL
        query = get_users_mentors(db)

    except Exception as error:
        logger.error(f"Erro na resquisição ('{request.url}')")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        ) from error

    logger.info(f"GET Users-Mentores (VIEW) - ('{request.url}')")
    return query

@router.post(
    "/new_mentorship_profile",
    response_model=MentorshipProfilesRead,
    status_code=status.HTTP_201_CREATED,
    summary="Insere um novo perfil de mentor no banco de dados."
)
async def new_mentorship_profile(new_mentorship_profile_json : MentorshipProfilesCreate, request: Request, db : Session = Depends(get_db)):
    user_ip = request.client.host

    try:
        #print(new_mentorship_profile_json.model_dump())

        query = insert_new_mentorship_profile(new_mentorship_profile_json.model_dump(), db)
        #print(query)
    except ResponseValidationError as fastAPIerror:
        logger.error(fastAPIerror)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(fastAPIerror)
        ) from fastAPIerror

    except Exception as error:
        logger.error(f"Erro na resquisição ('{request.url}')")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(error)
        ) from error

    logger.info(f"Criação do perfil de mentor [IP:{user_ip}] : {new_mentorship_profile_json}")
    return query
