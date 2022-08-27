import json
from time import sleep

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


def api_get(task_id: str, time: int) -> str:
    endpoint = llm_settings.llm_endpoint
    logger.info(f"Left attempts: {time - 1} in {task_id}")
    res = requests.get(
        f"{endpoint}/result/{task_id}",
        headers={
            "accept": "application/json",
        },
    )
    if res.status_code == 200 and res.json()["status"] == "completed":
        result = res.json()["result"][0]
        return result
    if time <= 0:
        logger.error("GET api Time Out")
        return "error: Server Error"
    sleep(2)
    return api_get(task_id, time - 1)
