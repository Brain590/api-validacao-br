from fastapi import Header, HTTPException

def rapidapi_auth(
    x_rapidapi_key: str = Header(...),
    x_rapidapi_host: str = Header(...)
):
    if not x_rapidapi_key or not x_rapidapi_host:
        raise HTTPException(status_code=401, detail="Unauthorized")
