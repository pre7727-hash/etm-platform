from functools import lru_cache
from jose import JWTError, jwt
from fastapi import HTTPException, status
from app.core.config import settings

@lru_cache
def get_jwt_key() -> str:
    if not settings.supabase_jwt_secret:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Set SUPABASE_JWT_SECRET for local HS256 verification or add JWKS validation before production.")
    return settings.supabase_jwt_secret

def decode_supabase_token(token: str) -> dict:
    try:
        return jwt.decode(token, get_jwt_key(), algorithms=["HS256"], audience=settings.supabase_jwt_audience)
    except JWTError as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication token") from exc
