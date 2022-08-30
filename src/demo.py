import gradio as gr

import api
from schemas import LLMRequest


async def generate(
    prompt: str,
    max_new_tokens: int,
    do_sample: bool,
    early_stopping: bool,
    num_beams: int,
    temperature: float,
    top_k: int,
    top_p: float,
    no_repeat_ngram_size: int,
    num_return_sequences: int,
):
    req = LLMRequest(
        prompt=prompt,
        max_new_tokens=max_new_tokens,
        do_sample=do_sample,
        early_stopping=early_stopping,
        num_beams=num_beams,
        temperature=temperature,
        top_k=top_k,
        top_p=top_p,
        no_repeat_ngram_size=no_repeat_ngram_size,
        num_return_sequences=num_return_sequences,
    )
    task_id: str = await api.api_post(req)
    result: str = await api.api_get(task_id)
    return result


with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            prompt = gr.Textbox(lines=40, max_lines=40, label="Enter prompt")
            with gr.Row():
                gen = gr.Button("Generate")
            with gr.Row():
                model_types = gr.Radio(["BLOOM-176B"], label="Model Types", value="BLOOM-176B")
            with gr.Group() as advanced_option:
                with gr.Row():
                    max_new_tokens = gr.Number(label="Max New Tokens", value=16)
                    do_sample = gr.Checkbox(label="Do Sample", value=True)
                    early_stopping = gr.Checkbox(label="Early Stopping", value=False)
                    num_beams = gr.Number(label="Num Beams", value=1)
                with gr.Row():
                    temperature = gr.Slider(0.0, 1.0, label="Temperature", value=1.0)
                    top_k = gr.Slider(0, 100, label="Top K", value=50)
                    top_p = gr.Slider(0.0, 1.0, label="Top P", value=1.0)
                with gr.Row():
                    no_repeat_ngram_size = gr.Number(label="No Repeat ngram size", value=0)
                    num_return_sequences = gr.Slider(1, 5, label="Num Return Sequences", value=1)
        with gr.Column():
            res = gr.Textbox(lines=60, max_lines=60, label="result")
        gen.click(
            fn=generate,
            inputs=[
                prompt,
                max_new_tokens,
                do_sample,
                early_stopping,
                num_beams,
                temperature,
                top_k,
                top_p,
                no_repeat_ngram_size,
                num_return_sequences,
                model_types,
            ],
            outputs=res,
        )


demo.launch(server_name="0.0.0.0", server_port=7860)
