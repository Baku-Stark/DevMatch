from sqlalchemy.orm import Session
from api.logger import logger
from api.models.sessions import SessionsModel, ScheduledSessionsView


# LEITURA DO BANCO DE DADOS
def findall_sessions(db : Session) -> list[type[SessionsModel]]:
    """
    Busca TODAS as sessões arquivadas no banco de dados.

    Parameters
    ----------
    db : Session
        Sessão ativa do SQLAlchemy para comunicação com o banco.

    Returns
    -------
    list[type[SessionsModel]]
        Lista de todas as sessões
    """
    logger.debug(f"Serviço 'findall_sessions' : Acessando banco de dados")
    return db.query(SessionsModel).all()

def findall_scheduled_sessions(db : Session) -> list[type[ScheduledSessionsView]]:
    """
    Busca TODAS as sessões AGENDADAS.

    Parameters
    ----------
    db : Session
        Sessão ativa do SQLAlchemy para comunicação com o banco.

    Returns
    -------
    list[type[ScheduledSessionsView]]
        Todos os sessões agendadas
    """
    logger.debug(f"Serviço 'findall_scheduled_sessions' : Acessando banco de dados")
    return db.query(ScheduledSessionsView).all()