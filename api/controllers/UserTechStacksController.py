from api.logger import logger
from api.models.tech_stacks import UserTechStacks
from api.schemas.tech_stacks import UserTechStacksRead, UserTechStacksCreate
from api.services.Monitoramento import Monitoramento
from api.services.UserTechStacksService import findall_user_tech_stacks, insert_new_user_tech_stacks

monitor = Monitoramento()

from fastapi import APIRouter, Depends, Request, status, HTTPException
from sqlalchemy.orm import Session
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
    response_model=list[UserTechStacksRead],
    status_code=status.HTTP_200_OK,
    summary="Tecnologias dos usuários"
)
async def get_user_tech_stacks(request: Request, db: Session = Depends(get_db)):
    user_ip = request.client.host

    try:
        monitor.registrar_acao(f"Acesso na rota UserTechStacks", ip=user_ip)  # MÉTODO DE REGISTRO NO ARQUIVO EXCEL
        query = findall_user_tech_stacks(db)

    except Exception as error:
        logger.error(f"Erro na resquisição ('{request.url}')")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        ) from error

    logger.info(f"GET Tecnologia dos usuários mentores - ('{request.url}')")
    return query

@router.post(
    "/new_user_tech_stacks",
    response_model=UserTechStacksRead,
    status_code=status.HTTP_201_CREATED,
    summary="Relacionar tecnologias aos usuários"
)
async def new_user_tech_stacks(new_user_tech_stacks : UserTechStacksCreate, request: Request, db : Session = Depends(get_db)):
    user_ip = request.client.host

    try:
        query = insert_new_user_tech_stacks(UserTechStacks(**new_user_tech_stacks.model_dump()), db)

    except Exception as error:
        logger.error(f"Erro na resquisição ('{request.url}')")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        ) from error

    logger.info(f"Inserção de relação [IP:{user_ip}] : {new_user_tech_stacks}")
    return query