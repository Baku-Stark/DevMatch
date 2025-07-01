from api.services.Monitoramento import Monitoramento
monitor = Monitoramento()

from fastapi import APIRouter, Depends, Request,HTTPException, status
from sqlalchemy.orm import Session

from api.models.Users.user import User
from api.schemas.Users.user import UserCreate, UserRead

router = APIRouter()

import api.db.database as database

# Dependência para FastAPI
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[UserRead], status_code=status.HTTP_200_OK, summary="Rota para ver todos os usuários cadastrados no banco de dados")
def list_users(request: Request, db: Session = Depends(get_db)):
    user_ip = request.client.host
    monitor.registrar_acao(f"Usuário acessou a rota Users", ip=user_ip) # MÉTODO DE REGISTRO NO ARQUIVO EXCEL
    return db.query(User).all()