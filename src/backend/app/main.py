from fastapi import FastAPI
from app.core.config import Settings
from app.api.ticket_routers import ticket_router

app = FastAPI(
    title = Settings.app_name,
    debug = Settings.debug
)


@app.get('/health')
def health_check() -> dict[str, str]:
    return {
        'status' : 'healthy',
        'service' : Settings.app_name,
        'environment' : Settings.app_env
    }
    
app.include_router(ticket_router)