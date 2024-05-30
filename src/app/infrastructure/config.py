from app.infrastructure.repositories import InMemoryTaskRepository

def get_task_repository():
    return InMemoryTaskRepository()
