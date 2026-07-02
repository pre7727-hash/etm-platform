from fastapi import APIRouter
from pydantic import BaseModel, Field
from app.api.v1.dependencies import CurrentUser
from app.services.n8n_client import n8n_client

router = APIRouter()

class PlayerCardRequest(BaseModel):
    prompt: str = Field(min_length=8, max_length=2000)
    game: str = Field(min_length=2, max_length=80)

@router.post("/player-card")
async def request_player_card(payload: PlayerCardRequest, current_user: CurrentUser) -> dict:
    return await n8n_client.trigger("player-card", {"payload": payload.model_dump(), "user": current_user})
