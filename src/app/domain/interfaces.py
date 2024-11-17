from abc import ABC, abstractmethod


class TaskRepository(ABC):

    @abstractmethod
    def add(self, task):
        pass

    @abstractmethod
    def get(self, task_id):
        pass

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def update(self, task):
        pass
