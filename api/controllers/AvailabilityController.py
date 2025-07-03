from api.logger import logger
from api.services.AvailabilityService import find_availability_by_mentor
from api.services.Monitoramento import Monitoramento
monitor = Monitoramento()

from fastapi import APIRouter, Depends, Request, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID
from api.schemas.availability import AvailabilitySlotRead
import api.db.database as database

router = APIRouter()

# Dependência para o banco
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get(
    "",
    response_model=list[AvailabilitySlotRead],
    status_code=status.HTTP_200_OK,
    summary="Retorna os horários disponíveis de um mentor"
)
async def get_availability_by_mentor(mentor_id: UUID, request: Request, db: Session = Depends(get_db)):
    user_ip = request.client.host
    #logger.debug(f"Requisição (UUID): {mentor_id}")
    try:
        slots = find_availability_by_mentor(mentor_id, db)
        monitor.registrar_acao(
            f"Acesso na AvailabilitySlot (mentor_id={mentor_id})",
            ip=user_ip
        )  # MÉTODO DE REGISTRO NO ARQUIVO EXCEL

        if not slots:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Nenhum horário encontrado para esse mentor."
            )

    except Exception as error:
        logger.error(f"Erro na resquisição ('{request.url}')")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        ) from error

    logger.info(f"GET Horário disponível do mentor - ('{request.url}')")
    return slots