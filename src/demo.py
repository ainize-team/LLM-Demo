import gradio as gr

import api
from schemas import LLMRequest


async def generate(prompt):
    req = LLMRequest(prompt=prompt)
    task_id = await api.api_post(req)
    return await api.api_get(task_id, 5)


demo = gr.Interface(fn=generate, inputs="text", outputs="text")
demo.launch(server_name="0.0.0.0", server_port=7860)
