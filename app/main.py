from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from app.core.config import settings
from app.services.ai_provider import AIProvider
from app.services.next_service import NextService
from app.services.openai_provider import OpenAIProvider


BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"


class NextRequest(BaseModel):
    problem: str


def create_app(ai_provider: AIProvider | None = None) -> FastAPI:
    app = FastAPI(title=settings.app_name)

    app.mount(
        "/static",
        StaticFiles(directory=STATIC_DIR),
        name="static",
    )

    if ai_provider is None:
        ai_provider = OpenAIProvider(
            api_key=settings.openai_api_key,
            model=settings.openai_model,
        )

    app.state.next_service = NextService(ai_provider=ai_provider)

    @app.get("/")
    def root():
        return FileResponse(STATIC_DIR / "index.html")

    @app.post("/api/next")
    def next_action(request: Request, payload: NextRequest):
        return request.app.state.next_service.get_next(payload.problem)

    return app


app = create_app()
