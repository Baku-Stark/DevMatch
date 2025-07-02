from api.logger import logger
from api.models.languages import Languages
from api.services.Monitoramento import Monitoramento
monitor = Monitoramento()

from api.schemas.languages import LanguagesRead

from fastapi import APIRouter, status, Depends, Request, HTTPException
from sqlalchemy.orm import Session

import api.db.database as database

router = APIRouter()

# Dependência para FastAPI
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get(
    "/",
    response_model=list[LanguagesRead],
    status_code=status.HTTP_200_OK,
    summary="Todas línguas cadastradas no banco de dados"
)
async def list_languages(request: Request, db: Session = Depends(get_db)):
    user_ip = request.client.host

    try:
        query = db.query(Languages).all()
        monitor.registrar_acao(f"Usuário acessou a rota Languages", ip=user_ip)  # MÉTODO DE REGISTRO NO ARQUIVO EXCEL

    except Exception as error:
        logger.error(f"Erro na resquisição ('{request.url}')")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        ) from error

    logger.info(f"GET Línguas - ('{request.url}')")
    return query