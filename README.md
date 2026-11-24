# FastAPI Learning

A small collection of FastAPI and Python examples for learning.

## Projects

- `api-learing-first_me/` - Basic FastAPI CRUD API and query parameter examples
- `learning-notebook-api/` - A learning notebook API with Pydantic models, filtering, search, and statistics
- `js-vs-python/` - Examples comparing JavaScript and Python syntax

## Download Locally

Clone the repository using Git:

```bash
git clone https://github.com/arafat-khan-pathan/FastAPI-Learning.git
cd FastAPI-Learning
```

Alternatively, open the GitHub repository, click **Code**, then **Download ZIP** and extract it.

## Run an API

Install [uv](https://docs.astral.sh/uv/) first.

### Learning Notebook API

```bash
cd learning-notebook-api
uv run fastapi dev main.py
```

### Basic FastAPI API

```bash
cd api-learing-first_me
uv run fastapi dev main.py
```

Open `http://127.0.0.1:8000/docs` in your browser.
