from api.logger import logger
from api.models.tech_stacks import TechStacks
from api.schemas.tech_stacks import TechStacksRead
from api.services.Monitoramento import Monitoramento
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
    response_model=list[TechStacksRead],
    status_code=status.HTTP_200_OK,
    summary="Rota para ver todas as tecnologias do sistema"
)
async def list_tech_stacks(request: Request, db: Session = Depends(get_db)):
    user_ip = request.client.host

    try:
        query = db.query(TechStacks).all()
        monitor.registrar_acao(f"Acesso na rota Tech Stacks", ip=user_ip)  # MÉTODO DE REGISTRO NO ARQUIVO EXCEL

    except Exception as error:
        logger.error(f"Erro na resquisição ('{request.url}')")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        ) from error

    logger.info(f"GET Tecnologias cadastradas - ('{request.url}')")
    return query