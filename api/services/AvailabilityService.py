from uuid import UUID
from sqlalchemy.orm import Session
from api.logger import logger
from api.models.availability import AvailabilitySlot


# LEITURA DO BANCO DE DADOS
def find_availability_by_mentor(mentor_id : UUID, db : Session) -> list:
    """
    Retorna os horários disponíveis de um mentor pelo seu 'mentor_id'

    Parameters
    ----------
    mentor_id : UUID
        Coluna do banco de dados utilizada no WHERE.

    db : Session
        Sessão ativa do SQLAlchemy para comunicação com o banco.

    Returns
    -------
    list
        Todos os horários disponíveis do mentor + timezone.
    """
    logger.debug(f"Serviço 'find_availability_by_mentor' : Acessando banco de dados")
    return db.query(AvailabilitySlot).filter(AvailabilitySlot.mentor_id == mentor_id).all()
    