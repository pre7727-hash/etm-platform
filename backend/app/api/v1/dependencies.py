from typing import Annotated
from fastapi import Depends, Header, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import decode_supabase_token

DbSession = Annotated[Session, Depends(get_db)]

def get_current_user_payload(authorization: Annotated[str | None, Header()] = None) -> dict:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication required")
    return decode_supabase_token(authorization.removeprefix("Bearer ").strip())

CurrentUser = Annotated[dict, Depends(get_current_user_payload)]
