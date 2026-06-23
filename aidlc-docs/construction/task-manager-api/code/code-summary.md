# Code Summary — task-manager-api

## Generated Files

| File | Purpose |
|------|---------|
| `requirements.txt` | Dependencies: fastapi, sqlmodel, uvicorn, pytest, httpx |
| `app/database.py` | SQLite engine, `DATABASE_URL` env, session dependency |
| `app/models.py` | `Task` table, create/update/read schemas, validators |
| `app/routers/tasks.py` | CRUD endpoints on `/tasks` |
| `app/main.py` | FastAPI app with lifespan DB init |
| `tests/conftest.py` | In-memory SQLite fixtures |
| `tests/test_tasks.py` | Tests SC-01 to SC-09 + extras |

## Requirements Coverage

- FR-VAL-01 to FR-VAL-05: Pydantic validators on `TaskCreate` / `TaskUpdate`
- FR-DT-01 to FR-DT-03: UTC `criada_em` with `Z` serializer on `TaskRead`
- All 5 endpoints with correct status codes
- `GET /tasks` ordered by `criada_em` descending
- Partial PUT via `exclude_unset=True`

## Test Scenarios

All scenarios from requirements §6 implemented in `tests/test_tasks.py`.
