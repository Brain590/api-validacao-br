from fastapi import APIRouter, Depends
from app.services.cpf_service import validar_cpf
from app.core.rapidapi_auth import rapidapi_auth

router = APIRouter(prefix="/cpf", tags=["CPF"], dependencies=[Depends(rapidapi_auth)])

@router.get("/validate")
def validate(cpf: str):
    return {"success": True, "cpf": cpf, "valid": validar_cpf(cpf)}
