# rabbit-backend

FastAPI backend for the Task Manager demo app.

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/tasks` | List all tasks |
| POST | `/tasks` | Create a new task |
| PATCH | `/tasks/{id}/complete` | Mark task as done |
| PATCH | `/tasks/{id}/start` | Mark task as in_progress |
| DELETE | `/tasks/{id}` | Delete a task |

## Task Schema

```json
{
  "id": 1,
  "title": "Fix login bug",
  "description": "Optional description",
  "status": "pending | in_progress | done",
  "priority": "low | medium | high"
}
```

## Run locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

API docs available at `http://localhost:8000/docs`

## Linked Repo

This backend is consumed by [rabbit-frontend](https://github.com/YOUR_ORG/rabbit-frontend).
The frontend's `api_client.py` depends on field names and endpoint paths defined here.
