from datetime import datetime, timedelta
from typing import Dict, Any
import jwt
from fastapi import HTTPException, status
from config import SECRET_KEY, ALGORITHM, TOKEN_EXPIRATION


def crear_jwt(user_id: int, username: str) -> str:
    """
    Ejemplo:
        token = crear_jwt(user_id=1020112352, username="alejo")
        # Retorna: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWI..."
    """
    # Crear el payload (datos) del JWT
    payload = {
        "sub": str(user_id),  # "sub" DEBE SER STRING en JWT estándar
        "username": username,
        "iat": datetime.utcnow(),  # "iat" = issued at (cuándo se creó)
        "exp": datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRATION)  # "exp" = expiration
    }
    
    # Codificar el JWT con la clave secreta
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    
    return token


def verificar_token(token: str) -> Dict[str, Any]:
    """
    Args:
        token (str): JWT a verificar (sin el prefijo "Bearer")
    
    Returns:
        Dict[str, Any]: Payload del token (contiene user_id, username, etc.)
    
    Raises:
        HTTPException: Si el token es inválido o está expirado
    
    Ejemplo:
        try:
            payload = verificar_token("eyJhbGciOiJIUzI1NiIs...")
            user_id = payload["sub"]
        except HTTPException:
            # Token inválido o expirado
    """
    try:
        # Decodificar el JWT
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
        # Verificar que contenga el ID del usuario
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido: no contiene ID de usuario",
                headers={"WWW-Authenticate": "Bearer"}
            )
        
        return payload
    
    except jwt.ExpiredSignatureError:
        # El token expiró
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expirado. Por favor, inicia sesión de nuevo",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    except jwt.InvalidTokenError:
        # El token es inválido (firma incorrecta, formato incorrecto, etc.)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token no válido o fue modificado",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    except Exception as e:
        # Cualquier otro error
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Error al verificar el token: {str(e)}",
            headers={"WWW-Authenticate": "Bearer"}
        )


def extraer_token_del_header(authorization: str) -> str:
    """
    Extrae el JWT del header Authorization.
    
    El formato esperado es: "Bearer <token>"
    
    Args:
        authorization (str): Valor del header Authorization
    
    Returns:
        str: El token sin el prefijo "Bearer "
    
    Raises:
        HTTPException: Si el formato es incorrecto
    
    Ejemplo:
        # Header: "Authorization: Bearer eyJhbGc..."
        token = extraer_token_del_header("Bearer eyJhbGc...")
        # Retorna: "eyJhbGc..."
    """
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No hay token de autorización",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    partes = authorization.split()
    
    if len(partes) != 2 or partes[0].lower() != "bearer":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Formato de autorización incorrecto. Usa: Bearer <token>",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    return partes[1]
