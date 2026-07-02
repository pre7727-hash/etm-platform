from fastapi import APIRouter
from sqlalchemy import text
from app.api.v1.dependencies import DbSession

router = APIRouter()

@router.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "gametracker-api"}

@router.get("/health/database")
def database_health(db: DbSession) -> dict:
    db.execute(text("select 1"))
    return {"status": "ok", "database": "reachable"}
