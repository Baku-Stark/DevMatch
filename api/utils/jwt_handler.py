import jwt, os
from datetime import datetime, timedelta, timezone
from typing import Any
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("JWT_SECRET", "chave_super_secreta_dev")
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("JWT_EXPIRE_MINUTES", 44640))  # 31 dias


def create_access_token(data: Any) -> str:
    """
    Gera um token JWT com claims seguros e personalizados.
    Aceita objetos ORM ou Pydantic.
    """
    now = datetime.now(timezone.utc)
    expire = now + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    payload = {
        "iss": "devmatch.api",
        "aud": "devmatch.users",
        "iat": int(now.timestamp()),
        "nbf": int(now.timestamp()),
        "exp": int(expire.timestamp()),
        "sub": str(data.id),
        "email": str(data.email),
        "role": str(data.role),
        "name": str(data.name),
        "avatar_url": str(data.avatar_url),
    }

    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(token: str) -> bool:
    try:
        jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM], audience="devmatch.users")
        return True
    except jwt.ExpiredSignatureError:
        raise ValueError("Token expirado")
    except jwt.InvalidAudienceError:
        raise ValueError("Audiência inválida")
    except jwt.InvalidTokenError:
        raise ValueError("Token inválido ou adulterado")
