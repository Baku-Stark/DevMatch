from api.logger import logger
from api.services.Monitoramento import Monitoramento
monitor = Monitoramento()

from fastapi import APIRouter, Depends, Request, status, HTTPException
from sqlalchemy.orm import Session

from api.models.user import User, MentorProfileView
from api.schemas.user import UserRead, MentorProfileRead

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
    response_model=list[UserRead],
    status_code=status.HTTP_200_OK,
    summary="Rota para ver todos os usuários cadastrados no banco de dados"
)
async def list_users(request: Request, db: Session = Depends(get_db)):
    user_ip = request.client.host

    try:
        query = db.query(User).all()
        monitor.registrar_acao(f"Usuário acessou a rota Users", ip=user_ip)  # MÉTODO DE REGISTRO NO ARQUIVO EXCEL

    except Exception as error:
        logger.error(f"Erro na resquisição ('{request.url}')")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        ) from error

    logger.info(f"GET Usuários Cadastrados - ('{request.url}')")
    return query

# ACESSANDO A VIEW "view_mentor_profiles"
# Models (MentorProfileView) | Schemas (MentorProfileRead)
@router.get("/mentors", response_model=list[MentorProfileRead], status_code=status.HTTP_200_OK, summary="Acesso à VIEW 'view_mentor_profiles'")
async def list_mentors(request: Request, db: Session = Depends(get_db)):
    user_ip = request.client.host
    try:
        monitor.registrar_acao(f"Usuário acessou a rota Users-Mentores (VIEW)", ip=user_ip)  # MÉTODO DE REGISTRO NO ARQUIVO EXCEL

    except Exception as error:
        logger.error(f"Erro na resquisição ('{request.url}')")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        ) from error

    logger.info(f"GET Users-Mentores (VIEW) - ('{request.url}')")
    return db.query(MentorProfileView).all()