# FastAPI Beginner Examples

This folder contains small examples for learning basic FastAPI concepts.

## Files

| File | What it teaches |
|---|---|
| `01_load.py` | Pydantic models and a loan prediction POST API |
| `02_path_p.py` | Path parameters, query parameters, and customer lookup |
| `03_path_q.py` | Filtering customers with query parameters |
| `04_pyd.py` | Structured request bodies and validation with Pydantic |
| `05_main_s_exception.py` | 404 error handling with `HTTPException` |
| `06_try_catch.py` | 404 and 500 error handling with `try/except` |

## Run the project

Open a terminal in the project folder:

```powershell
cd 2.1__fastapi_learning_codeWithSagor
uv sync
uv run fastapi dev 01_load.py
```

Open Swagger documentation in your browser:

```text
http://127.0.0.1:8000/docs
```

To run another file, replace `01_load.py` with the file name:

```powershell
uv run fastapi dev 03_path_q.py
```
