from sqlalchemy.orm import Session

from api.logger import logger
from api.models.mentorship_profiles import MentorshipProfiles

#LEITURA DO BANCO DE DADOS
def findall_mentorship_profiles(db : Session) -> list[type[MentorshipProfiles]]:
    """
        Resgatar uma lista do perfil de todos os mentores

        Parameters
        ----------
        db : Session
            Sessão ativa do SQLAlchemy para comunicação com o banco.

        Returns
        -------
        MentorshipProfiles
            Lista dos mentores.
        """
    logger.debug(f"Serviço 'findall_mentorship_profiles' : Acessando banco de dados")
    return db.query(MentorshipProfiles).all()

# INSERÇÃO DE UM NOVO MENTOR (PERFIL)
def insert_new_mentorship_profile(new_mentorship_profile : MentorshipProfiles, db : Session) -> MentorshipProfiles:
    """
    Insere um novo perfil de mentor no banco de dados.

    Parameters
    ----------
    new_mentorship_profile : MentorshipProfiles
        Instância do modelo SQLAlchemy representando o novo usuário mentor.
    db : Session
        Sessão ativa do SQLAlchemy para comunicação com o banco.

    Returns
    -------
    MentorshipProfiles
        O usuário Mentor criado com campos atualizados do banco.
    """
    try:
        logger.debug(f"Inserindo novo usuário (Mentor) : {new_mentorship_profile}")
        db.add(new_mentorship_profile)
    except Exception as error:
        logger.error(error)
    finally:
        db.commit()
        db.refresh(new_mentorship_profile)
    logger.info(f"Perfil de Mentor '{new_mentorship_profile}' criado.")
    return new_mentorship_profile

# ATUALIZAR INFORMAÇÕES DO PERFIL DO MENTOR
#def update_mentorship_profile(upd_mentorship_profile : MentorshipProfiles)