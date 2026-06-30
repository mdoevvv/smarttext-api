from app.services.llm_client import llm_client, LLMError
from app.schemas.text import (
    SummarizeRequest, SummarizeResponse,
    QARequest, QAResponse
)

STYLE_INSTRUCTIONS = {
    "concise": "Summarize in 2-3 sentences. Be direct, no filler.",
    "detailed": "Write a thorough summary covering all key points in a short paragraph.",
    "bullet":   "Summarize as 4-6 bullet points. Each bullet is one key idea.",
}

SUMMARIZE_SYSTEM = "You are a precise summarization engine. Follow the style instruction exactly. Output only the summary, nothing else."

QA_SYSTEM = "You are a question-answering engine. Answer ONLY from the provided context. If the answer is not in the context, say 'Not found in the provided text.' Output only the answer." # else, models can prepend useless texts


def summarize(req: SummarizeRequest) -> SummarizeResponse:
    style_instruction = STYLE_INSTRUCTIONS[req.style]

    prompt = f"""Style: {style_instruction}

Text to summarize:
{req.text}"""

    summary = llm_client.complete(prompt, system=SUMMARIZE_SYSTEM)

    return SummarizeResponse(
        summary=summary,
        word_count=len(summary.split()),
        style=req.style,
    )


def answer_question(req: QARequest) -> QAResponse:
    prompt = f"""Context:
{req.context}

Question: {req.question}"""

    answer = llm_client.complete(prompt, system=QA_SYSTEM)

    return QAResponse(answer=answer)