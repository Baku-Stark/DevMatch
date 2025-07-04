from api.logger import logger
from api.schemas.tech_stacks import UserTechStacksBase, UserTechStacksRead
from api.services.Monitoramento import Monitoramento
from api.services.UserTechStacksService import findall_user_tech_stacks

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