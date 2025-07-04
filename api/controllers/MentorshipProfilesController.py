from sqlalchemy.orm import Session

from api.logger import logger
from api.models.mentorship_profiles import MentorshipProfiles
from api.services.MentorshipProfilesService import findall_mentorship_profiles, insert_new_mentorship_profile
from api.services.Monitoramento import Monitoramento
monitor = Monitoramento()

from fastapi import APIRouter, status, Request, HTTPException, Depends
from api.schemas.mentorship_profiles import MentorshipProfilesRead, MentorshipProfilesCreate

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
    response_model=list[MentorshipProfilesRead],
    status_code=status.HTTP_200_OK,
    summary="Resgatar uma lista do perfil de todos os mentores"
)
async def get_mentorship_profiles(request: Request, db: Session = Depends(get_db)):
    user_ip = request.client.host

    try:
        monitor.registrar_acao(f"Usuário acessou a rota Mentorship Profiles", ip=user_ip)  # MÉTODO DE REGISTRO NO ARQUIVO EXCEL
        query = findall_mentorship_profiles(db)

    except Exception as error:
        logger.error(f"Erro na resquisição ('{request.url}')")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        ) from error

    logger.info(f"GET Mentores Cadastrados - ('{request.url}')")
    return query

@router.post(
    "/new_mentorship_profile",
    response_model=MentorshipProfilesRead,
    status_code=status.HTTP_201_CREATED,
    summary="Insere um novo perfil de mentor no banco de dados."
)
def new_mentorship_profile(new_mentorship_profile : MentorshipProfilesCreate, request: Request, db : Session = Depends(get_db)):
    user_ip = request.client.host

    try:
        query = insert_new_mentorship_profile(MentorshipProfiles(**new_mentorship_profile.model_dump()), db)

    except Exception as error:
        logger.error(f"Erro na resquisição ('{request.url}')")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        ) from error

    logger.info(f"Criação do perfil de mentor [IP:{user_ip}] : {new_mentorship_profile}")
    return query