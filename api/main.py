import uvicorn
from starlette.middleware.cors import CORSMiddleware

from logger import logger
from fastapi import FastAPI
from routes import api_router
app = FastAPI(
    title="DevMatch - Backend",
    description="Sistema de mentoria para desenvolvedores",
    version="1.0.0",
    contact={
        "developer": "https://github.com/Baku-Stark"
    }
)

# === CORS ===
origins = [
    "http://localhost:5173",  # Frontend local (Vite)
    "https://devmatch.vercel.app",  # Exemplo: domínio de produção
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # URLs permitidas
    allow_credentials=True,         # Permitir cookies/autenticação
    allow_methods=["*"],            # Permitir todos os métodos HTTP
    allow_headers=["*"],            # Permitir todos os headers
)
# === CORS ===

app.include_router(api_router)

if __name__ == '__main__':
    logger.info("Servidor rodando em http://localhost:8000/ | Docs: http://localhost:8000/docs#/")
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)