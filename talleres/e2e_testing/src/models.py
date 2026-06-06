"""
Modelo de datos del gestor de tareas E2E.
Persiste tareas en un archivo JSON.
"""

import json
import os
import uuid


class Task:
    def __init__(self, title: str, task_id: str = None, done: bool = False):
        self.id = task_id or str(uuid.uuid4())[:8]
        self.title = title
        self.done = done

    def to_dict(self):
        return {"id": self.id, "title": self.title, "done": self.done}

    @classmethod
    def from_dict(cls, data: dict):
        return cls(title=data["title"], task_id=data["id"], done=data.get("done", False))


class TaskRepository:
    def __init__(self, filepath: str = "data/tasks.json"):
        self.filepath = filepath
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        if not os.path.exists(filepath):
            self._write([])

    def _read(self):
        with open(self.filepath, "r") as f:
            return json.load(f)

    def _write(self, data: list):
        with open(self.filepath, "w") as f:
            json.dump(data, f, indent=2)

    def all(self):
        return [Task.from_dict(d) for d in self._read()]

    def add(self, title: str) -> Task:
        tasks = self._read()
        # Rechazar títulos vacíos o duplicados
        if not title or not title.strip():
            raise ValueError("El título no puede estar vacío")
        if any(t["title"] == title for t in tasks):
            raise ValueError(f"Ya existe una tarea con el título '{title}'")
        task = Task(title=title.strip())
        tasks.append(task.to_dict())
        self._write(tasks)
        return task

    def complete(self, task_id: str) -> bool:
        tasks = self._read()
        for t in tasks:
            if t["id"] == task_id:
                t["done"] = True
                self._write(tasks)
                return True
        return False

    def delete(self, task_id: str) -> bool:
        tasks = self._read()
        new_tasks = [t for t in tasks if t["id"] != task_id]
        if len(new_tasks) == len(tasks):
            return False
        self._write(new_tasks)
        return True

    def clear(self):
        self._write([])
