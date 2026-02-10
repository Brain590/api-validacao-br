from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.routers import cpf, cnpj, cep, tools

app = FastAPI(
    title="Brazilian Data Validation API",
    description="""
API brasileira para validação de CPF, CNPJ e CEP.

⚠️ Avisos importantes:
- Validação é apenas sintática
- Não comprova titularidade ou existência legal
- CEP consultado via ViaCEP (serviço público)
""",
    version="1.0.0"
)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"success": False, "error": "INTERNAL_SERVER_ERROR", "message": str(exc)},
    )

app.include_router(cpf.router)
app.include_router(cnpj.router)
app.include_router(cep.router)
app.include_router(tools.router)
