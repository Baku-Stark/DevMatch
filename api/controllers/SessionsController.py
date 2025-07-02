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
    try:
        user_ip = request.client.host
        monitor.registrar_acao(f"Usuário acessou a rota all_sessions", ip=user_ip)  # MÉTODO DE REGISTRO NO ARQUIVO EXCEL

    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        ) from error

    return db.query(SessionsModel).all()

# ACESSANDO A VIEW "view_scheduled_sessions"
# Models (ScheduledSessionsView) | Schemas (ScheduledSessionsRead)
@router.get(
    "/scheduled_sessions",
    response_model=list[ScheduledSessionsRead],
    status_code=status.HTTP_200_OK,
    summary="Acesso à VIEW 'view_scheduled_sessions'"
)
async def scheduled_sessions(request: Request, db : Session = Depends(get_db)):
    try:
        user_ip = request.client.host
        monitor.registrar_acao(f"Usuário acessou a rota scheduled_sessions (VIEW)", ip=user_ip)  # MÉTODO DE REGISTRO NO ARQUIVO EXCEL

    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        ) from error

    return db.query(ScheduledSessionsView).all()