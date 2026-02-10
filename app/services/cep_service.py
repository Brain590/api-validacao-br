import requests
from typing import Optional, Dict, Any

def consultar_cep(cep: str) -> Optional[Dict[str, Any]]:
    cep = ''.join(filter(str.isdigit, cep))
    
    if len(cep) != 8:
        return None

    try:
        r = requests.get(
            f"https://viacep.com.br/ws/{cep}/json/", 
            timeout=10 # Increased timeout to prevent 504
        )
        r.raise_for_status() # Raise exception for 4xx/5xx errors
        
        data = r.json()
        if data.get("erro"):
            return None
        return data
    except (requests.RequestException, ValueError):
        # Handle connection errors, timeouts, or invalid JSON
        return None
