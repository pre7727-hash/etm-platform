from fastapi import APIRouter
from app.api.v1.dependencies import CurrentUser

router = APIRouter()

@router.get("/me")
def read_me(current_user: CurrentUser) -> dict:
    return {"user": current_user}
