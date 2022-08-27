import gradio as gr

import api
from schemas import LLMRequest


async def greet(prompt):
    req = LLMRequest(prompt=prompt)
    task_id = await api.api_post(req)
    return api.api_get(task_id, 5)


demo = gr.Interface(fn=greet, inputs="text", outputs="text")
demo.launch()
