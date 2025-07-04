from sqlalchemy.orm import Session
from api.logger import logger
from api.models.tech_stacks import UserTechStacks

# LEITURA DO BANCO DE DADOS
def findall_user_tech_stacks(db : Session) -> list[type[UserTechStacks]]:
    logger.debug(f"Serviço 'findall_user_tech_stacks' : Acessando banco de dados")
    return db.query(UserTechStacks).all()

# INSERTS
def insert_new_user_tech_stacks(new_user_tech_stacks : UserTechStacks, db : Session) -> UserTechStacks:
    try:
        logger.debug(f"Relação Usuário -> Tech Stacks : {new_user_tech_stacks}")
        db.add(new_user_tech_stacks)
    except Exception as error:
        logger.error(error)
    finally:
        db.commit()
        db.refresh(new_user_tech_stacks)
    logger.info(f"Relação {new_user_tech_stacks} feita.")
    return new_user_tech_stacks