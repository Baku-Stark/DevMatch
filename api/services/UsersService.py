from sqlalchemy.orm import Session
from api.logger import logger
from api.models.user import User, MentorProfileView

# LEITURA DO BANCO DE DADOS
def findall_users(db : Session) -> list[type[User]]:
    """
    Busca TODOS os usuários.

    Parameters
    ----------
    db : Session
        Sessão ativa do SQLAlchemy para comunicação com o banco.

    Returns
    -------
    User
        Todos os usuários cadastrados
    """
    logger.debug(f"Serviço 'findall_users' : Acessando banco de dados")
    return db.query(User).all()

def users_mentors(db : Session) -> list[type[MentorProfileView]] :
    """
    Busca usuários (apenas os mentores)

    Parameters
    ----------
    db : Session
        Sessão ativa do SQLAlchemy para comunicação com o banco.

    Returns
    -------
    User
        O usuário (apenas 'mentors')
    """
    logger.debug(f"Serviço 'users_mentors' : Acessando banco de dados")
    query = db.query(MentorProfileView).all()
    return query

# INSERIR UM NOVO USUÁRIO NO BANCO DE DADOS
def insert_new_user(new_user : User, db : Session) -> User:
    """
    Insere um novo usuário no banco de dados.

    Parameters
    ----------
    new_user : User
        Instância do modelo SQLAlchemy representando o novo usuário.
    db : Session
        Sessão ativa do SQLAlchemy para comunicação com o banco.

    Returns
    -------
    User
        O usuário criado com campos atualizados do banco.
    """
    logger.debug(f"Inserindo novo usuário : {new_user}")

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# ATUALIZAR INFORMAÇÕES

# APAGAR CONTA