from fastapi import APIRouter, Depends
from app.services.cnpj_service import validar_cnpj
from app.core.rapidapi_auth import rapidapi_auth

router = APIRouter(prefix="/cnpj", tags=["CNPJ"], dependencies=[Depends(rapidapi_auth)])

@router.get("/validate")
def validate(cnpj: str):
    return {"success": True, "cnpj": cnpj, "valid": validar_cnpj(cnpj)}
