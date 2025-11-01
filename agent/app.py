from fastapi import FastAPI
from .settings import settings
app = FastAPI(
    title=settings.app.name,
    version=settings.app.version,
    root_path=settings.server.root_path,
)

@app.get("/health")
async def health():
    return {"status": "ok"}

__all__ = ["app"]
