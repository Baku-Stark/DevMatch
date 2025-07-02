from api.logger import logger
from api.services.Monitoramento import Monitoramento
monitor = Monitoramento()

from fastapi import APIRouter, Depends, Request, status, HTTPException
from sqlalchemy.orm import Session

from api.models.sessions import ScheduledSessionsView, SessionsModel
from api.schemas.sessions import ScheduledSessionsRead, SessionsSchema

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
    response_model=list[SessionsSchema],
    status_code=status.HTTP_200_OK,
    summary="Leitura de todas as sessões"
)
async def all_sessions(request: Request, db : Session = Depends(get_db)):
    user_ip = request.client.host
    try:
        query = db.query(SessionsModel).all()
        monitor.registrar_acao(f"Usuário acessou a rota all_sessions", ip=user_ip)  # MÉTODO DE REGISTRO NO ARQUIVO EXCEL

    except Exception as error:
        logger.error(f"Erro na resquisição ('{request.url}')")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        ) from error

    logger.info(f"GET Todas as sessões - ('{request.url}')")
    return query

# ACESSANDO A VIEW "view_scheduled_sessions"
# Models (ScheduledSessionsView) | Schemas (ScheduledSessionsRead)
@router.get(
    "/scheduled_sessions",
    response_model=list[ScheduledSessionsRead],
    status_code=status.HTTP_200_OK,
    summary="Acesso à VIEW 'view_scheduled_sessions' - Sessões Agendadas"
)
async def scheduled_sessions(request: Request, db : Session = Depends(get_db)):
    user_ip = request.client.host
    try:
        query = db.query(ScheduledSessionsView).all()
        monitor.registrar_acao(f"Usuário acessou a rota scheduled_sessions (VIEW)", ip=user_ip)  # MÉTODO DE REGISTRO NO ARQUIVO EXCEL

    except Exception as error:
        logger.error(f"Erro na resquisição ('{request.url}')")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        ) from error

    logger.info(f"GET Todas as sessões agendadas - ('{request.url}')")
    return query