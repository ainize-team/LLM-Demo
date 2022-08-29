import asyncio
import json

import requests
from loguru import logger

from config import llm_settings
from schemas import LLMRequest


async def api_post(data: LLMRequest) -> str:
    endpoint = llm_settings.llm_endpoint
    res = requests.post(
        f"{endpoint}/generate",
        headers={"Content-Type": "application/json", "accept": "application/json"},
        data=json.dumps(dict(data)),
    )
    if res.status_code == 200:
        task_id = res.json()["task_id"]
        logger.info(f"Task ID: {task_id}")
        return task_id
    else:
        logger.error(f"{res.text}")
        return res.json()["massage"]


async def api_get(task_id: str, attempts: int) -> str:
    endpoint = llm_settings.llm_endpoint
    logger.info(f"Left attempts: {attempts - 1} in {task_id}")
    res = requests.get(
        f"{endpoint}/result/{task_id}",
        headers={
            "accept": "application/json",
        },
    )
    if res.status_code == 200 and res.json()["status"] == "completed":
        result = res.json()["result"][0]
        return result
    if attempts <= 0:
        logger.error("GET api Time Out")
        return "error: Server Error"
    await asyncio.sleep(2)

    return await api_get(task_id, attempts - 1)
