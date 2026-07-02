from functools import lru_cache
from pydantic import AnyHttpUrl, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")
    environment: str = "local"
    project_name: str = "GameTracker"
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_cors_origins: str = "http://localhost:5173,http://127.0.0.1:5173"
    database_url: str
    redis_url: str = "redis://localhost:6379/0"
    celery_broker_url: str = "redis://localhost:6379/1"
    celery_result_backend: str = "redis://localhost:6379/2"
    supabase_url: AnyHttpUrl | str
    supabase_anon_key: str
    supabase_service_role_key: str = Field(default="")
    supabase_jwks_url: AnyHttpUrl | str | None = None
    supabase_jwt_secret: str = ""
    supabase_jwt_audience: str = "authenticated"
    n8n_webhook_base_url: AnyHttpUrl | str
    n8n_webhook_secret: str

    @property
    def cors_origins(self) -> list[str]:
        return [origin.strip() for origin in self.api_cors_origins.split(",") if origin.strip()]

@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
