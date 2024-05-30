from app.domain.entities import Task
from app.domain.interfaces import TaskRepository

class CreateTaskUseCase:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def execute(self, title: str, description: str):
        new_task = Task(task_id=None, title=title, description=description)
        self.task_repository.add(new_task)
        return new_task

class ListTasksUseCase:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def execute(self):
        return self.task_repository.list()
