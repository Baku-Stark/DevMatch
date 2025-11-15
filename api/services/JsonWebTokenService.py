from api.schemas.user import UserRead
from api.utils.jwt_handler import verify_token, create_access_token


def create_user_jwt(user : UserRead) -> str:
    """
    Criar um novo JWT para um determinado usuário

    Parameters
    ----------
    user : UserRead
        Usuário escolhido

    Returns
    -------
    token
        Token JWT criado com sucesso
    """
    return create_access_token(user)

def validate_jwt(token: str) -> bool:
    """
    Verificação de token do usuário JÁ CRIADO.

    Parameters
    ----------
    token : str
        Token a ser testado para validação

    Returns
    -------
    bool
        TRUE caso o token é valido e FALSE se não
    """
    return verify_token(token)