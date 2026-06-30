from pydantic import BaseModel, Field


class SummarizeRequest(BaseModel):
    text: str = Field(..., min_length=50, max_length=8000)
    #... means required
    style: str = Field(default="concise", pattern="^(concise|detailed|bullet)$")
    


class SummarizeResponse(BaseModel): #response model
    summary: str
    word_count: int
    style: str


class QARequest(BaseModel):
    context: str = Field(..., min_length=50, max_length=8000)
    question: str = Field(..., min_length=5, max_length=500)


class QAResponse(BaseModel):
    answer: str
    context_used: bool = True