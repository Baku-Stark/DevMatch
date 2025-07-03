from sqlalchemy.orm import Session
from api.logger import logger
from api.models.user import User, MentorProfileView


# INSERIR UM NOVO USUÁRIO NO BANCO DE DADOS
def users_mentors(db : Session):
    logger.debug(f"Serviço 'users_mentors'")
    query = db.query(MentorProfileView).all()
    return query
def insert_new_user(new_user : User, db : Session):
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
    logger.debug(f"Novo usuário : {new_user}")

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# ATUALIZAR INFORMAÇÕES

# APAGAR CONTA