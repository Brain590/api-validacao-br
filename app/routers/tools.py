from fastapi import APIRouter, Depends, Query
from app.services.tools_service import gerar_cpf, gerar_cnpj
from app.core.rapidapi_auth import rapidapi_auth

router = APIRouter(prefix="/tools", tags=["Tools"], dependencies=[Depends(rapidapi_auth)])

@router.get("/generate/cpf")
def generate_cpf(formatted: bool = Query(False, description="Whether to return the CPF formatted with dots and dash")):
    return {
        "success": True, 
        "cpf": gerar_cpf(formatted),
        "formatted": formatted
    }

@router.get("/generate/cnpj")
def generate_cnpj(formatted: bool = Query(False, description="Whether to return the CNPJ formatted with dots, slash and dash")):
    return {
        "success": True, 
        "cnpj": gerar_cnpj(formatted),
        "formatted": formatted
    }
