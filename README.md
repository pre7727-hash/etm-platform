# GameTracker

GameTracker is a premium SaaS foundation for competitive gaming analytics, AI player cards, tournaments, teams, organizations, news, public profiles, subscriptions, and future matchmaking.

## Folder Layout

- `frontend/` contains the complete React application.
- `backend/` contains the complete FastAPI application, Alembic migrations, Celery tasks, and API modules.
- Root files contain shared environment, Docker, and project documentation.

## Structure

- `frontend/` - React, JSX, Tailwind CSS, React Router, TanStack Query, Axios, Supabase Auth, Framer Motion, Recharts.
- `backend/` - FastAPI, SQLAlchemy, Alembic, Redis, Celery, WebSockets, Supabase JWT verification, n8n webhook boundary.
- `docker-compose.yml` - Local Postgres, Redis, API, Celery worker, and Vite web app.

## Run With Docker

1. Copy .env.example to .env.
2. Fill in Supabase and n8n values.
3. Run docker compose up --build.
4. Run docker compose exec api alembic upgrade head.
5. Open http://localhost:5173.

The frontend only uses VITE_SUPABASE_ANON_KEY. Never expose SUPABASE_SERVICE_ROLE_KEY to browser code.
"# etm-platform" 
