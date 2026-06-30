# maps HTTP endpoints to service functions.
from fastapi import APIRouter, HTTPException
from app.schemas.text import (
    SummarizeRequest, SummarizeResponse,
    QARequest, QAResponse
)
from app.services.text_service import summarize, answer_question
from app.services.llm_client import LLMError

router = APIRouter(prefix="/text", tags=["Text"])


@router.post("/summarize", response_model=SummarizeResponse)
def summarize_text(req: SummarizeRequest):
    try:
        return summarize(req)
    except LLMError as e:
        raise HTTPException(status_code=502, detail=str(e))


@router.post("/qa", response_model=QAResponse)
def qa(req: QARequest):
    try:
        return answer_question(req)
    except LLMError as e:
        raise HTTPException(status_code=502, detail=str(e))