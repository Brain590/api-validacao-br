from fastapi import FastAPI
from app.routers import cpf, cnpj, cep

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

app.include_router(cpf.router)
app.include_router(cnpj.router)
app.include_router(cep.router)
