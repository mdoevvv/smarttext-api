from openai import OpenAI
from app.core.config import settings
class LLMError(Exception):
    """Raised whenever the LLM provider fails — network, auth, rate limit, etc."""
    pass

class LLMClient:
    def __init__(self):
        if settings.llm_provider.lower() == "groq":
            self._client = OpenAI(api_key=settings.groq_api_key,
                                 base_url="https://api.groq.com/openai/v1")
        else:
            raise ValueError(f"Unsupported LLM provider: {settings.llm_provider}")
        
        self._model = settings.model_name

    def complete(self, prompt: str, system: str | None = None)-> str:
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        try:
            response = self._client.chat.completions.create(
            model = self._model,
            messages = messages,
            max_tokens= 1024,
            temperature = 0.3
                    # For a summarize/QA API you want consistent, factual output, not creative variance
            )
        except Exception as e:
            raise LLMError(f"LLM call failed: {e}") from e    
        content = response.choices[0].message.content
        
        if content is None:
            raise LLMError("Empty response from model")
        return content        
        
llm_client = LLMClient()
