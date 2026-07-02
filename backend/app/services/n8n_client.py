import httpx
from app.core.config import settings

class N8nClient:
    def __init__(self) -> None:
        self.base_url = str(settings.n8n_webhook_base_url).rstrip("/")
        self.secret = settings.n8n_webhook_secret

    async def trigger(self, workflow: str, payload: dict) -> dict:
        url = f"{self.base_url}/{workflow}"
        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.post(url, json=payload, headers={"X-GameTracker-Webhook-Secret": self.secret})
            response.raise_for_status()
            return response.json()

n8n_client = N8nClient()
