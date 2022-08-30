from pydantic import BaseSettings, HttpUrl


class LLMSettings(BaseSettings):
    llm_endpoint: HttpUrl = "https://bloom-176b.jp.ngrok.io"
    llm_max_length: int = 2048
    # add more


llm_settings = LLMSettings()
