from fastapi import APIRouter, Depends, HTTPException
from app.services.cnpj_service import validar_cnpj
from app.core.rapidapi_auth import rapidapi_auth

router = APIRouter(prefix="/cnpj", tags=["CNPJ"], dependencies=[Depends(rapidapi_auth)])

@router.get("/validate")
def validate(cnpj: str):
    try:
        return {"success": True, "cnpj": cnpj, "valid": validar_cnpj(cnpj)}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"success": False, "error": "INTERNAL_SERVER_ERROR", "message": str(e)}
        )
