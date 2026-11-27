# FastAPI Master Note (with uv)

> A simple, beginner-friendly guide. Learn how to set up a project, run it, and build a small CRUD API.

---

## 📑 Table of Contents

1. [What is what?](#1-what-is-what)
2. [Install uv](#2-install-uv)
3. [Way 1: Classic `venv` + pip](#3-way-1-classic-venv--pip)
4. [Way 2: uv (recommended)](#4-way-2-uv-recommended)
   - [uv add explained (`fastapi[standard]`)](#uv-add-explained)
   - [uv: All Things (A to Z)](#uv-all-things-a-to-z)
5. [Your first FastAPI app](#5-your-first-fastapi-app)
6. [Run the server](#6-run-the-server)
7. [Pydantic BaseModel (data check)](#7-pydantic-basemodel-data-check)
8. [Full CRUD example (Notes API)](#8-full-crud-example-notes-api)
9. [Error handling (HTTPException)](#9-error-handling-httpexception)
10. [Test your API](#10-test-your-api)
11. [Cheat sheet](#11-cheat-sheet)
12. [Common mistakes](#12-common-mistakes)

---

## 1. What is what?

| Name | Simple meaning |
|---|---|
| **FastAPI** | Python tool to build web APIs fast |
| **uvicorn** | The server that runs your FastAPI app |
| **Pydantic** | Checks your data (is it a string? a list?) |
| **venv** | A private box of packages for one project |
| **uv** | A super fast package manager (like `npm` for Python) |

**uv vs npm (if you know JavaScript):**

| JavaScript | Python (uv) |
|---|---|
| `package.json` | `pyproject.toml` |
| `package-lock.json` | `uv.lock` |
| `node_modules` | `.venv` |
| `npm` | `uv` |

Other package managers: `uv`, `poetry`, `pdm`, `pip-sync`. We use **uv**.

---

## 2. Install uv

```bash
pip install uv
uv --version      # check it works
```

---

## 3. Way 1: Classic `venv` + pip

Good to know, but uv is easier.

### Step 1: Create a virtual environment

```bash
python -m venv .venv
```

- `-m` = run a **module**
- `venv` = the module name
- `.venv` = folder name (the `.` makes it **hidden**; `venv` without dot is **not hidden**)

### Step 2: Activate it (Windows PowerShell)

```powershell
.venv\Scripts\Activate.ps1
```

You will see `(.venv)` in your terminal. ✅

> ⚠️ Check spelling! `Scripts` and `Activate` must be correct.

### Step 3: Install packages

```bash
pip install fastapi uvicorn
```

### Step 4: Save packages to a file

```bash
pip freeze > requirements.txt
```

This saves all package names + versions, so others can install the same ones.

### Step 5: Leave the environment

```bash
deactivate
```

### Run with uvicorn

```bash
uvicorn main:app --reload
```

---

## 4. Way 2: uv (recommended)

uv creates the venv, installs packages, and tracks everything for you.

### Create a new project

```bash
uv init my-project
cd my-project
uv add "fastapi[standard]"
```

> Always use quotes: `"fastapi[standard]"`

### Three ways to start a project

| Command | What it does |
|---|---|
| `uv init folder-name` | Creates a new folder + project files |
| `uv init` | Starts a project in the **current** folder |
| `uv init --bare` | Only creates `pyproject.toml` (minimal) |
| `uv init --app` | Creates an app-style project |

### What files do you get?

```
my-project/
├── .venv/            ← packages live here (auto-created)
├── main.py           ← your code
├── pyproject.toml    ← project info + package list
└── uv.lock           ← exact versions (don't edit by hand!)
```

> 🔒 **uv.lock**: when packages change, uv updates this file automatically. You never edit it yourself.

### Add / install packages

```bash
uv add pandas              # best: installs AND saves to pyproject.toml
uv add numpy
uv pip install pandas      # works, but does NOT update pyproject.toml / uv.lock
pip install pandas         # works, but also does not update them
```

> ✅ Prefer `uv add`. It keeps your project files in sync.

### Useful uv commands

| Command | What it does |
|---|---|
| `uv sync` | Install everything from `pyproject.toml` / `uv.lock` |
| `uv pip list` | Show installed packages |
| `uv pip show fastapi` | Show details of one package |
| `uv tree` | Show packages as a tree (who needs who) |
| `uv run main.py` | Run a Python file |
| `uv run python explore.py` | Run a file with the project's Python |
| `uv venv` | Create a virtual environment |
| `uv python list` | Show available Python versions |
| `uv python install` | Install a Python version |
| `uv python find` | Find a Python on your computer |
| `uv tool list` | Show installed tools |

### Activate / deactivate (optional with uv)

`uv run` already uses the venv for you. But if you want to activate manually:

```powershell
.venv\Scripts\Activate.ps1
deactivate
```

---

### uv add explained

`uv add` = install a package **and** save it in `pyproject.toml` + `uv.lock`.

```bash
uv add fastapi              # only FastAPI
uv add "fastapi[standard]"  # FastAPI + uvicorn + extra tools (recommended)
```

> ⚠️ Spelling: it is `standard`, not `standerd`. Wrong spelling = warning or error.

**What does `fastapi[standard]` give you?**

```
fastapi[standard]  =  fastapi  +  uvicorn  +  fastapi-cli  +  extras
```

| Part | Why you need it |
|---|---|
| `fastapi` | The framework itself |
| `uvicorn` | The server that runs your app |
| `fastapi-cli` | Gives you the `fastapi dev` command |
| extras (httpx, jinja2, python-multipart...) | Testing, HTML templates, file/form uploads |

The `[standard]` part is called an **extra** (a bundle of optional packages).

**Which one to use?**

| Command | Use when |
|---|---|
| `uv add "fastapi[standard]"` | Learning, normal projects ✅ |
| `uv add fastapi uvicorn` | You want a smaller, minimal install |

> 💡 Why quotes? In some terminals, `[ ]` has a special meaning. Quotes keep the command safe.

---

### uv: All Things (A to Z)

#### 1) Install and check

```bash
pip install uv          # install
uv --version            # check version
```

#### 2) Start a project

| Command | What it does |
|---|---|
| `uv init my-app` | New folder + project |
| `uv init` | Project in the current folder |
| `uv init --bare` | Only `pyproject.toml` |
| `uv init --app` | App-style project |
| `uv init --lib` | Library-style project |

```bash
uv init my-app
cd my-app
```

#### 3) Add and remove packages

```bash
uv add pandas                    # add a package
uv add numpy pandas              # add many at once
uv add "requests==2.32.3"        # exact version
uv add "requests>=2.30"          # minimum version
uv add --dev pytest              # dev-only tool (testing, linting)
uv add -r requirements.txt       # import an old requirements file
uv remove pandas                 # remove a package
```

> 📝 `--dev` = tools you need while coding (like `pytest`), not in the final app.

#### 4) Install everything (sync)

```bash
uv sync          # make .venv match pyproject.toml + uv.lock
uv lock          # only update uv.lock (no install)
uv lock --upgrade   # update packages to the newest allowed versions
```

> ✅ Cloned a project from GitHub? Just run `uv sync`.

#### 5) Run things

```bash
uv run main.py                          # run a Python file
uv run python explore.py                # same, with project Python
uv run fastapi dev main.py              # FastAPI dev server
uv run uvicorn main:app --reload        # uvicorn server
uv run pytest                           # run tests
```

You don't need to activate `.venv`. `uv run` does it for you.

#### 6) See what is installed

```bash
uv pip list            # all installed packages
uv pip show fastapi    # details of one package
uv tree                # dependency tree
```

#### 7) Virtual environment

```bash
uv venv                    # create .venv
uv venv --python 3.12      # create with a specific Python
.venv\Scripts\Activate.ps1 # activate (Windows PowerShell)
deactivate                 # leave
```

#### 8) Python versions

```bash
uv python list             # versions you can use
uv python install 3.12     # download and install a version
uv python find             # find Python on your computer
uv python pin 3.12         # lock this project to 3.12
```

#### 9) Pip-style commands (when you need them)

```bash
uv pip install pandas                   # install (does NOT edit pyproject.toml)
uv pip install -r requirements.txt      # install from a file
uv pip freeze                           # list with versions
```

#### 10) Export to requirements.txt

```bash
uv export --format requirements-txt > requirements.txt
```

Use this when a server or teammate still needs `requirements.txt`.

#### 11) Tools (global command-line apps)

```bash
uv tool install ruff       # install a tool for your whole computer
uv tool list               # see installed tools
uv tool run ruff --version # run a tool without installing (short form: uvx ruff --version)
```

#### Quick idea map

```
uv
├── init      → start a project
├── add       → install + save a package
├── remove    → uninstall + update files
├── sync      → install everything from the lock file
├── lock      → update uv.lock
├── run       → run code in the project's venv
├── venv      → create a virtual environment
├── python    → manage Python versions
├── pip       → pip-style commands
├── tree      → show dependency tree
├── export    → make requirements.txt
└── tool      → global CLI tools
```

---

## 5. Your first FastAPI app

Create `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "code running"}
```

**Line by line:**

- `FastAPI()` → creates your app object
- `@app.get("/")` → when someone visits `/`, run the function below
- `return {...}` → FastAPI turns the dict into JSON automatically

---

## 6. Run the server

**Option A: FastAPI CLI (easy)**

```bash
uv run fastapi dev main.py
```

**Option B: uvicorn**

```bash
uv run uvicorn main:app --reload
```

- `main` = file name (`main.py`)
- `app` = the variable inside the file (`app = FastAPI()`)
- `--reload` = auto-restart when you save code

Open in browser:

| URL | What you see |
|---|---|
| `http://127.0.0.1:8000/` | Your API response |
| `http://127.0.0.1:8000/docs` | **Swagger UI** (test your API here) 🎉 |
| `http://127.0.0.1:8000/redoc` | Another docs page |

Stop the server: `Ctrl + C`

---

## 7. Pydantic BaseModel (data check)

`BaseModel` checks your data. If the data is wrong, FastAPI sends an error automatically.

```python
from pydantic import BaseModel

class Term(BaseModel):
    term: str                      # required text
    definition: str                # required text
    example: str | None = None     # optional (can be empty)
    tags: list[str] = []           # list of text, default empty
    learned: bool = False          # true/false, default False
```

| Syntax | Meaning |
|---|---|
| `term: str` | Required string |
| `example: str \| None = None` | Optional string |
| `tags: list[str] = []` | List of strings, default empty |
| `learned: bool = False` | Boolean with default |

---

## 8. Full CRUD example (Notes API)

**CRUD** = **C**reate, **R**ead, **U**pdate, **D**elete.

| Action | HTTP method | URL |
|---|---|---|
| Read all | `GET` | `/terms` |
| Read one | `GET` | `/terms/{term_id}` |
| Create | `POST` | `/terms` |
| Update (some fields) | `PATCH` | `/terms/{term_id}` |
| Delete | `DELETE` | `/terms/{term_id}` |

### Complete `main.py`

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# ---------- Models ----------
class Term(BaseModel):
    term: str
    definition: str
    example: str | None = None
    tags: list[str] = []
    learned: bool = False

class TermUpdate(BaseModel):
    # every field optional, so PATCH can change just one thing
    term: str | None = None
    definition: str | None = None
    example: str | None = None
    tags: list[str] | None = None
    learned: bool | None = None

# ---------- Fake database (a simple list) ----------
terms = []

# ---------- READ ALL ----------
@app.get("/terms")
def get_terms():
    return terms

# ---------- READ ONE ----------
@app.get("/terms/{term_id}")
def get_term(term_id: int):
    for item in terms:
        if item["id"] == term_id:
            return item
    raise HTTPException(status_code=404, detail="term not found")

# ---------- CREATE ----------
@app.post("/terms")
def add_term(data: Term):
    new_term = {"id": len(terms) + 1}
    new_term.update(data.model_dump())   # convert Pydantic model -> dict
    terms.append(new_term)
    return new_term

# ---------- UPDATE (PATCH) ----------
@app.patch("/terms/{term_id}")
def update_term(term_id: int, changes: TermUpdate):
    for item in terms:
        if item["id"] == term_id:
            item.update(changes.model_dump(exclude_unset=True))
            return item
    raise HTTPException(status_code=404, detail="term not found")

# ---------- DELETE ----------
@app.delete("/terms/{term_id}")
def delete_term(term_id: int):
    for item in terms:
        if item["id"] == term_id:
            terms.remove(item)
            return {"msg": "deleted"}
    raise HTTPException(status_code=404, detail="term not found")
```

### Key ideas explained

| Idea | Simple meaning |
|---|---|
| `data: Term` | FastAPI reads the request body and checks it with `Term` |
| `model_dump()` | Turns a Pydantic model into a normal dict |
| `exclude_unset=True` | Only use fields the user **actually sent** (important for PATCH!) |
| `{term_id}` in URL + `term_id: int` | Reads the number from the URL |
| `TermUpdate` | Same as `Term` but all fields optional (`= None`) |

### PUT vs PATCH

- **PUT** = replace the whole thing
- **PATCH** = change only some fields ✅ (we use this)

---

## 9. Error handling (HTTPException)

Import it:

```python
from fastapi import FastAPI, HTTPException
```

Use it when something is wrong:

```python
raise HTTPException(status_code=404, detail="term not found")
```

| Status code | Meaning |
|---|---|
| `200` | OK |
| `201` | Created |
| `404` | Not found |
| `422` | Wrong data (Pydantic sends this automatically) |

> 💡 Use `raise`, not `return`, for errors. `raise` stops the function and sends the correct error code.

---

## 10. Test your API

1. Run: `uv run fastapi dev main.py`
2. Open `http://127.0.0.1:8000/docs`
3. Click an endpoint → **Try it out** → **Execute**

**Example: create a term**

`POST /terms` with this body:

```json
{
  "term": "venv",
  "definition": "A private folder of packages for one project",
  "tags": ["python", "setup"]
}
```

**Response:**

```json
{
  "id": 1,
  "term": "venv",
  "definition": "A private folder of packages for one project",
  "example": null,
  "tags": ["python", "setup"],
  "learned": false
}
```

**Example: update with PATCH** → `PATCH /terms/1`

```json
{ "learned": true }
```

Only `learned` changes. Everything else stays. ✅

---

## 11. Cheat sheet

### Start a new project (fastest way)

```bash
pip install uv
uv init my-api
cd my-api
uv add "fastapi[standard]"
# write code in main.py
uv run fastapi dev main.py
```

### Use someone else's project

```bash
uv sync
uv run fastapi dev main.py
```

### Add packages later

```bash
uv add pandas numpy            # data analysis
uv add --dev pytest            # testing
uv remove numpy                # remove one
```

### Classic way (no uv)

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install fastapi uvicorn
pip freeze > requirements.txt
uvicorn main:app --reload
deactivate
```

---

## 12. Common mistakes

| ❌ Mistake | ✅ Fix |
|---|---|
| `if item["id"] = term_id` | Use `==` for comparing (`=` is for assigning) |
| `notes.update(...)` on a list | `.update()` is for **dicts**. Use `new_note.update(...)` |
| Wrong path `venv\Script\activate` | Correct: `.venv\Scripts\Activate.ps1` |
| `uv add fastapi[standard]` | Use quotes: `uv add "fastapi[standard]"` |
| `uv add "fastapi[standerd]"` (spelling) | Correct spelling: `standard` |
| Using `pip install` inside a uv project | Use `uv add` so `pyproject.toml` updates |
| Editing `uv.lock` by hand | Never. uv manages it |
| Forgetting `--reload` | Add it so the server restarts on save |
| `return` for errors | Use `raise HTTPException(...)` |
| Using `model_dump()` in PATCH | Use `model_dump(exclude_unset=True)` |

---

## 🚀 Next steps

- Add a real database (SQLite + SQLModel or SQLAlchemy)
- Use `pandas` with FastAPI to build small data-analysis APIs
- Learn authentication (JWT)
- Deploy with Docker (great for your DevOps path!)

---

*Happy coding! 🎉*
