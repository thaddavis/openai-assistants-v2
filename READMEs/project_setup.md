# TLDR

Project Setup

##

```sh
python -m venv .venv
source .venv/bin/activate
pip install uv
uv init
rm hello.py
touch main.py
echo "print('Hello World')" > main.py
uv run main.py
touch .env
echo "OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>" > .env
uv add openai python-dotenv
# ...
```