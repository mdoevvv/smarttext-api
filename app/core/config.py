from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    llm_provider: str = "groq"
    groq_api_key: str = ""
    anthropic_api_key: str = ""
    model_name: str = "llama-3.3-70b-versatile"
    max_input_chars: int = 8000

settings = Settings()

