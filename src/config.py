from pydantic import BaseSettings, HttpUrl


class LLMSettings(BaseSettings):
    llm_endpoint: HttpUrl
    llm_max_length: int
    # add more


llm_settings = LLMSettings()
