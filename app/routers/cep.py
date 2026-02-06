from fastapi import APIRouter, Depends, HTTPException
from app.services.cep_service import consultar_cep
from app.core.rapidapi_auth import rapidapi_auth

router = APIRouter(prefix="/cep", tags=["CEP"], dependencies=[Depends(rapidapi_auth)])

@router.get("/lookup")
def lookup(cep: str):
    r = consultar_cep(cep)
    if not r:
        raise HTTPException(
            status_code=404,
            detail={"success": False, "error": "CEP_NOT_FOUND"}
        )
    return {"success": True, "data": r}
