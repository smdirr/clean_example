from app.application.use_cases import CreateTaskUseCase, ListTasksUseCase
from app.infrastructure.config import get_task_repository

def main():
    task_repository = get_task_repository()
    
    create_task_use_case = CreateTaskUseCase(task_repository)
    list_tasks_use_case = ListTasksUseCase(task_repository)
    
    while True:
        print("1. Create new list")
        print("2. list all tasks")
        print("3. Exit")
        choice = input("Choice one option: ")
        
        if choice == '1':
            title = input("Task title: ")
            description = input("Description: ")
            create_task_use_case.execute(title, description)
            print("Task created.")
        elif choice == '2':
            tasks = list_tasks_use_case.execute()
            for task in tasks:
                print(f"{task.task_id}: {task.title} - {'Completed' if task.completed else 'Pending'}")
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
