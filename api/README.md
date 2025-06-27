# DevMatch - Backend

<div align="center">

![Python Version](https://img.shields.io/badge/Python-3.11.x-green)
![Python Project](https://img.shields.io/badge/Python_|_Project-Version_1.0.0-purple)

</div>

**Documentação do Projeto**:

- **Issue**: [Instalação dos pacotes#8](https://github.com/Baku-Stark/DevMatch/issues/8)

> [!NOTE]
>
> Documentação extra encontra-se nos seguintes links [FastAPI HomePage](https://fastapi.tiangolo.com/#run-it), [FastAPI - uvicorn](https://fastapi.tiangolo.com/deployment/manually/#server-machine-and-server-program)

**Base da Aplicação**:

```py
import uvicorn

from fastapi import FastAPI, status
#from routers import api_router
app = FastAPI(
    title="DevMatch - Backend",
    description="Sistema de mentoria para desenvolvedores",
    version="1.0.0",
)

#app.include_router(api_router)

@app.get("/", status_code=status.HTTP_200_OK)
async def home():
    return {"message" : "Hello"}

if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
```