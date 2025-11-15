import secrets, os

from dotenv import load_dotenv

from api.services.JsonWebTokenService import create_user_jwt, validate_jwt

load_dotenv()
correct_username = os.getenv("BA_USER")
correct_password = os.getenv("BA_PASS")

from typing import Dict
from fastapi import APIRouter, status, HTTPException
from fastapi.params import Depends, Query
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from api.schemas.user import UserRead
security = HTTPBasic()
router = APIRouter()

from api.services.Monitoramento import Monitoramento
monitor = Monitoramento()


@router.post(
    "/admin/TestCreatingToken",
    status_code= status.HTTP_200_OK,
    summary="Rota apenas para administradores testarem a criação de TOKEN (JWT)"
)
async def token_generator(user : UserRead, credentials: HTTPBasicCredentials = Depends(security)) -> object:
    token = create_user_jwt(user)

    is_correct_username = secrets.compare_digest(credentials.username, correct_username)
    is_correct_password = secrets.compare_digest(credentials.password, correct_password)

    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Basic Auth credentials",
            headers={"WWW-Authenticate": "Basic"},
        )

    monitor.registrar_acao(f"Criação de token JWT feita com sucesso!", ip=None)
    return {"token" : token}

@router.post(
    "/admin/TestValidateToken",
    status_code= status.HTTP_200_OK,
    summary="Rota apenas para administradores testarem a validade de um TOKEN (JWT) já criado"
)
async def token_validator(token: str = Query(..., description="JWT a ser validado"), credentials: HTTPBasicCredentials = Depends(security)) -> Dict[str, bool]:
    response_verify_token = validate_jwt(token)

    is_correct_username = secrets.compare_digest(credentials.username, correct_username)
    is_correct_password = secrets.compare_digest(credentials.password, correct_password)

    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Basic Auth credentials",
            headers={"WWW-Authenticate": "Basic"},
        )

    return {"data": response_verify_token}