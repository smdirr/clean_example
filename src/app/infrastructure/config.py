from app.infrastructure.repositories import InMemoryTaskRepository


def get_task_repository():
    #  get_task_repository return an InMemoryTaskRepository
    return InMemoryTaskRepository()
