from api.services.Monitoramento import Monitoramento
monitor = Monitoramento()

from fastapi import APIRouter, Request, status
router = APIRouter()

@router.get("/", status_code=status.HTTP_200_OK, summary="Primeira rota criada para testes")
async def home(request: Request):
    """
    Rota Home
    """
    user_ip = request.client.host

    monitor.registrar_acao(f"Usuário acessou a rota Home", ip=user_ip) # MÉTODO DE REGISTRO NO ARQUIVO EXCEL
    return {"message" : "Hello", "ip": user_ip}