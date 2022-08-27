from pydantic import BaseSettings, HttpUrl


class LLMSettings(BaseSettings):
    llm_endpoint: HttpUrl


llm_settings = LLMSettings()
