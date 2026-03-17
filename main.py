from fastapi import FastAPI, HTTPException
from typing import List
from models import Task, TaskCreate, TaskStatus

app = FastAPI(title="Task Manager API", version="1.0.0")

# In-memory task store
_tasks: dict[int, Task] = {}
_next_id: int = 1


@app.get("/tasks", response_model=List[Task])
def get_tasks():
    """Return all tasks."""
    return list(_tasks.values())


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(payload: TaskCreate):
    """Create a new task."""
    global _next_id
    task = Task(id=_next_id, **payload.model_dump())
    _tasks[_next_id] = task
    _next_id += 1
    return task


@app.patch("/tasks/{task_id}/complete", response_model=Task)
def complete_task(task_id: int):
    """Mark a task as done."""
    if task_id not in _tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    _tasks[task_id].status = TaskStatus.done
    return _tasks[task_id]


@app.patch("/tasks/{task_id}/start", response_model=Task)
def start_task(task_id: int):
    """Mark a task as in_progress."""
    if task_id not in _tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    _tasks[task_id].status = TaskStatus.in_progress
    return _tasks[task_id]


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    """Delete a task by ID."""
    if task_id not in _tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del _tasks[task_id]
