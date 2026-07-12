

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class LLMSettings(BaseSettings):
    GROQ_API_KEY: str
    GROQ_MODEL: str
    LLM_TIMEOUT_SECONDS: int

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

@lru_cache
def get_llm_settings() -> LLMSettings:
    return LLMSettings() 