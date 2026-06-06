import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.storage import TaskStorage
from src.service import TaskService
from src.notifier import Notifier

class TestServiceIntegration:
    def test_add_task_happy_path(self):
        storage = TaskStorage("test_tasks.json")
        notifier = Notifier()
        service = TaskService(storage, notifier)
        result = service.add_task("Comprar leche")
        assert result is True

    def test_complete_task(self):
        storage = TaskStorage("test_tasks.json")
        notifier = Notifier()
        service = TaskService(storage, notifier)
        service.add_task("Aprender pytest")
        assert service.complete_task("Aprender pytest") is True