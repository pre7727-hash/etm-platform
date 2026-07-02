from app.core.celery_app import celery_app

@celery_app.task(name="ai.process_player_card")
def process_player_card(job_id: str) -> dict:
    return {"job_id": job_id, "status": "queued"}
