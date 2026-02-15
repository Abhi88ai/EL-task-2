# Console-based To-Do List Application

FILE_NAME = "tasks.txt"


def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return [task.strip() for task in file.readlines()]
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def add_task(tasks):
    task = input("\nEnter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")


def remove_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_no = int(input("\nEnter task number to remove: "))
        removed = tasks.pop(task_no - 1)
        save_tasks(tasks)
        print(f"Removed task: {removed}")
    except (ValueError, IndexError):
        print("Invalid task number!")


def main():
    tasks = load_tasks()

    while True:
        print("\n==== TO-DO LIST MENU ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice! Please try again.")



