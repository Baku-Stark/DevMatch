from uuid import UUID
from sqlalchemy.orm import Session
from api.logger import logger
from api.models.user import User

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
    try:
        db.add(new_user)
    except Exception as error:
        db.rollback()
        logger.error(error)
    finally:
        db.commit()
        db.refresh(new_user)
    return new_user

# ATUALIZAR INFORMAÇÕES

# APAGAR CONTA
def delete_a_user(user_id : UUID, db : Session) -> dict:
    """
    Apagar a conta de um usuário pelo seu UUID.

    Parameters
    ----------
    user_id : UUID
        UUID do usuário que será deletado do banco de dados.

    db : Session
        Sessão ativa do SQLAlchemy para comunicação com o banco.

    Returns
    -------
    dict
        {"ok": True}
    """
    global query

    try:
        logger.debug(f"Serviço 'delete_a_user' : Acessando banco de dados")
        query = db.query(User).filter(User.id == user_id).first()

    except Exception as error:
        db.rollback()
        logger.error(error)

    finally:
        db.delete(query)
        db.commit()
    logger.info(f"Usuário (ID) {user_id} foi deletado.")
    return {"ok": True}