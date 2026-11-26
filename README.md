# FastAPI Learning

This repository contains beginner-friendly FastAPI examples.

## Projects

| Folder | What it contains |
|---|---|
| `1.1__js-vs-python` | Python and JavaScript basic examples |
| `1.2__learning-notebook-api` | Notebook API with Pydantic and basic filtering |
| `1.3__fastapi-learing-first_me` | Basic FastAPI API examples |
| `2.1__fastapi_learning_codeWithSagor` | Path parameters, query parameters, Pydantic, and error handling |

## 1. Download the project

### Download with Git

Open a terminal and run:

```powershell
git clone https://github.com/arafat-khan-pathan/FastAPI-Learning.git
cd FastAPI-Learning
```

### Download a ZIP file

1. Open the GitHub repository.
2. Click **Code**.
3. Click **Download ZIP**.
4. Extract the downloaded ZIP file.
5. Open the extracted folder in VS Code.

## 2. Install uv

Open PowerShell and run:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Close and reopen the terminal.

Check that uv is installed:

```powershell
uv --version
```

## 3. Open a project folder

Each project has its own `pyproject.toml` file.

For example:

```powershell
cd 2.1__fastapi_learning_codeWithSagor
```

## 4. Create the virtual environment

Run this command inside a project folder:

```powershell
uv sync
```

This command:

- Creates a `.venv` folder
- Installs Python packages
- Uses `pyproject.toml` and `uv.lock`

## 5. Activate the virtual environment

Activation is optional because `uv run` activates the environment automatically.

Activate manually in PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

The terminal will show `(.venv)` after activation.

If Windows blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Then activate the environment again.

Deactivate the environment:

```powershell
deactivate
```

## 6. Install FastAPI

Most project folders already include FastAPI.

To add FastAPI with standard tools:

```powershell
uv add "fastapi[standard]"
```

To add another package:

```powershell
uv add package-name
```

To remove a package:

```powershell
uv remove package-name
```

## 7. Run a FastAPI project

### Development mode

FastAPI development mode automatically reloads the server after code changes:

```powershell
uv run fastapi dev main.py
```

For the Code With Sagor examples:

```powershell
uv run fastapi dev 01_load.py
```

Run another file by changing the file name:

```powershell
uv run fastapi dev 03_path_q.py
```

### Normal FastAPI mode

Run the server without development tools:

```powershell
uv run fastapi run main.py
```

### Run with Uvicorn

Uvicorn is an ASGI server used by FastAPI.

Run with auto-reload:

```powershell
uv run uvicorn main:app --reload
```

For a file named `01_load.py`:

```powershell
uv run uvicorn 01_load:app --reload
```

Run without auto-reload:

```powershell
uv run uvicorn main:app
```

The `--reload` option restarts the server after code changes.

Stop the server by pressing `Ctrl+C`.

## 8. Open the API

Start the server, then open:

```text
http://127.0.0.1:8000
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

## Common uv commands

| Command | Purpose |
|---|---|
| `uv --version` | Check the uv version |
| `uv sync` | Create the environment and install dependencies |
| `uv run python main.py` | Run a Python file |
| `uv run fastapi dev main.py` | Run in FastAPI development mode |
| `uv run fastapi run main.py` | Run in normal FastAPI mode |
| `uv run uvicorn main:app --reload` | Run Uvicorn with auto-reload |
| `uv run uvicorn main:app` | Run Uvicorn without reload |
| `uv add "fastapi[standard]"` | Add FastAPI and standard tools |
| `uv add package-name` | Add a package |
| `uv remove package-name` | Remove a package |
| `uv lock` | Update `uv.lock` |
| `deactivate` | Exit the virtual environment |
