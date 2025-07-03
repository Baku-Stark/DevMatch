from api.logger import logger
from api.services.Monitoramento import Monitoramento
from api.services.UsersService import insert_new_user, users_mentors

monitor = Monitoramento()

from fastapi import APIRouter, Depends, Request, status, HTTPException
from sqlalchemy.orm import Session

from api.models.user import User, MentorProfileView
from api.schemas.user import UserRead, MentorProfileRead, UserCreate

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
        monitor.registrar_acao(f"Usuário acessou a rota Users", ip=user_ip)  # MÉTODO DE REGISTRO NO ARQUIVO EXCEL
        query = db.query(User).all()

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
@router.get(
    "/mentors",
    response_model=list[MentorProfileRead],
    status_code=status.HTTP_200_OK,
    summary="Acesso à VIEW 'view_mentor_profiles'"
)
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
    return users_mentors(db)

# CRIAÇÃO DE UM NOVO USUÁRIO
@router.post(
    "/sign_up",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
    summary="Registrar novos usuários"
)
def sign_up(new_user : UserCreate, request: Request, db : Session = Depends(get_db)):
    user_ip = request.client.host

    try:
        query = insert_new_user(User(**new_user.model_dump()), db)

    except Exception as error:
        logger.error(f"Erro na resquisição ('{request.url}')")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        ) from error

    logger.info(f"Criação do usuário [IP:{user_ip}] : {new_user}")

    return query