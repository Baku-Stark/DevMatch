from sqlalchemy.orm import Session
from api.logger import logger
from api.models.tech_stacks import UserTechStacks


def findall_user_tech_stacks(db : Session) -> list[type[UserTechStacks]]:
    logger.debug(f"Serviço 'findall_user_tech_stacks' : Acessando banco de dados")
    return db.query(UserTechStacks).all()