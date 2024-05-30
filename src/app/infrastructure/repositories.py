from app.domain.interfaces import TaskRepository
from app.domain.entities import Task

class InMemoryTaskRepository(TaskRepository):
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add(self, task):
        task.task_id = self.next_id
        self.next_id += 1
        self.tasks.append(task)

    def get(self, task_id):
        return next((task for task in self.tasks if task.task_id == task_id), None)

    def list(self):
        return self.tasks

    def update(self, task):
        index = next((i for i, t in enumerate(self.tasks) if t.task_id == task.task_id), None)
        if index is not None:
            self.tasks[index] = task
