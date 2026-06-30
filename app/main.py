from fastapi import FastAPI
from app.api.v1.routes.text import router as text_router

app = FastAPI(
    title="SmartText API",
    description="LLM-powered summarization and Q&A",
    version="0.1.0",
)

app.include_router(text_router, prefix="/api/v1")


@app.get("/health")
def health():
    return {"status": "ok"}