import jwt
import os
from datetime import datetime, timedelta, timezone
from typing import Dict, Any
from api.models.user import User
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("JWT_SECRET", "chave_super_secreta_dev")
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("JWT_EXPIRE_MINUTES", 44640))  # 31 dias


def create_access_token(data: User) -> str:
    """
    Gera um token JWT com claims seguros e personalizados.
    """
    now = datetime.now(timezone.utc)
    expire = now + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    payload = {
        "iss": "devmatch.api",                 # Emissor
        "aud": "devmatch.users",               # Público esperado
        "iat": int(now.timestamp()),           # Timestamp (int)
        "nbf": int(now.timestamp()),
        "exp": int(expire.timestamp()),        # Expiração em segundos
        "sub": str(data.id),            # Identificador do usuário
        "email": str(data.email),
        "role": str(data.role),
        "name": str(data.name),
        "avatar_url": str(data.avatar_url),
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token


def verify_token(token: str) -> Dict[str, Any]:
    """
    Valida e decodifica o JWT.
    """
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM], audience="devmatch.users")
        return decoded
    except jwt.ExpiredSignatureError:
        raise ValueError("Token expirado")
    except jwt.InvalidAudienceError:
        raise ValueError("Audiência inválida")
    except jwt.InvalidTokenError:
        raise ValueError("Token inválido ou adulterado")