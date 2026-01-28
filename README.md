## Asynchronous call openai and gemini api

## Install

```bash
uv init -p 3.10
uv venv
source .venv/bin/activate
uv sync
touch .env # add OPENAI_API_KEY and GEMINI_API_KEY here

uv run gpt.py
uv run gemini.py
```
