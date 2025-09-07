from uuid import UUID
from api.logger import logger
from api.services.Monitoramento import Monitoramento
from api.services.UsersService import insert_new_user, findall_users, delete_a_user

monitor = Monitoramento()

from fastapi import APIRouter, Depends, Request, status, HTTPException
from sqlalchemy.orm import Session

from api.models.user import User
from api.schemas.user import UserRead, UserCreate

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
        query = findall_users(db)

    except Exception as error:
        logger.error(f"Erro na resquisição ('{request.url}')")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        ) from error

    logger.info(f"GET Usuários Cadastrados - ('{request.url}')")
    return query

# CRIAÇÃO DE UM NOVO USUÁRIO
@router.post(
    "/sign_up",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
    summary="Registrar novos usuários"
)
async def sign_up(new_user : UserCreate, request: Request, db : Session = Depends(get_db)):
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

# USUÁRIO DECIDIU APAGAR SUA CONTA
@router.delete(
    "/delete_user_by_id",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Apagar a conta de um usuário pelo UUID"
)
async def delete_user_by_uuid(user_id : UUID, request: Request, db: Session = Depends(get_db)):
    user_ip = request.client.host
    try:
        query = delete_a_user(user_id, db)

    except Exception as error:
        logger.error(f"Erro na resquisição ('{request.url}')")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        ) from error

    logger.info(f"Conta apagada [IP:{user_ip}] : {user_id}")
    return query