class Task:

    def __init__(self, task_id: int, title: str, description: str):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True
