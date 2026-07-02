from fastapi import APIRouter
from app.api.v1.routes import ai, auth, health, websocket

api_router = APIRouter()
api_router.include_router(health.router, tags=["health"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(ai.router, prefix="/ai", tags=["ai"])
api_router.include_router(websocket.router, tags=["websocket"])
