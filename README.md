# LLM-Demo
![Python version](https://img.shields.io/badge/python-3.8+-important)
[![License](https://img.shields.io/badge/license-MIT-blue)](https://opensource.org/licenses/MIT)
![Gradio](https://img.shields.io/badge/gradio-^3.1.7-green)
![Poetry](https://img.shields.io/badge/poetry-1.1.14-red)
</br></br>
Web Demo for Large Language Model with Gradio

---------------
## Issue
> - In Apple Silicon(M1), Python version 3.8 and 3.9 have some error with gradio.
> - Apple silicon users should install 3.10+ version.

-------
## How to Serve

### With Docker

1. Build dockerfile

   ```
   git clone https://github.com/ainize-team/LLM-Demo.git
   cd LLM-Demo
   docker build -t llm-demo .
   ```

2. Run docker image

- Environment Variable
    * `LLM_ENDPOINT` : Your ML model api endpoint url.
    * `LLM_MAX_LENGTH`: Your ML model's max token length.

- example command
```
docker run --name llm-demo -p 8000:7860 -e LLM_ENDPOINT={api_end_point} -e LLM_MAX_LENGTH={max_token_length} llm-demo
```

### Without Docker

1. Install pyenv and poetry

Refer to these links
- [poetry repo](https://github.com/python-poetry/poetry)
- [pyenv repo](https://github.com/pyenv/pyenv)

2. Clone Repo
   ```
   git clone https://github.com/ainize-team/LLM-Demo.git
   cd LLM-Demo
   ```


3. Install python with pyenv

- Write this command to install python `pyenv install 3.8.13`
- To use that version in the shell `pyenv shell 3.8.13`

4. Use poetry

- Install package
  * develop : `poetry install`
  * no develop : `poetry install --no-dev`

- Use this virtual envirionment
    * `. .venv/bin/activate`

5. Execute server

- `python src/demo.py`