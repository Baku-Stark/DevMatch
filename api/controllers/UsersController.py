from api.services.Monitoramento import Monitoramento
monitor = Monitoramento()

from fastapi import APIRouter, Depends, Request,HTTPException, status
from sqlalchemy.orm import Session

from api.models.Users.user import User, MentorProfileView
from api.schemas.Users.user import UserCreate, UserRead, MentorProfileRead

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

# ACESSANDO A VIEW "view_mentor_profiles"
# Models (MentorProfileView) | Schemas (MentorProfileRead)
@router.get("/mentors", response_model=list[MentorProfileRead], status_code=status.HTTP_200_OK, summary="Acesso à VIEW 'view_mentor_profiles'")
def list_mentors(request: Request, db: Session = Depends(get_db)):
    user_ip = request.client.host
    monitor.registrar_acao(f"Usuário acessou a rota Users-Mentores (VIEW)", ip=user_ip)  # MÉTODO DE REGISTRO NO ARQUIVO EXCEL
    return db.query(MentorProfileView).all()