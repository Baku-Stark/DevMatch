import uvicorn

from fastapi import FastAPI, status
from routes import api_router
app = FastAPI(
    title="DevMatch - Backend",
    description="Sistema de mentoria para desenvolvedores",
    version="1.0.0",
    contact={
        "developer": "https://github.com/Baku-Stark"
    }
)
app.include_router(api_router)

from logger import Logger
logger = Logger(process_name="DevMatch - Backend")

if __name__ == '__main__':
    logger.info("Servidor rodando em http://localhost:8000/ | Docs: http://localhost:8000/docs#/")
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)