import json
import os

# Task class representing each to-do item
class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False

    # Mark task as completed
    def mark_completed(self):
        self.completed = True

    # Represent task for easier display
    def __repr__(self):
        return f"{self.title} - {self.category} [{'Completed' if self.completed else 'Not Completed'}]"

# Save tasks to tasks.json
def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump([task.__dict__ for task in tasks], f, indent=4)

# Load tasks from tasks.json
def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            task_data = json.load(f)
            return [Task(data) for data in task_data]
    except FileNotFoundError:
        return []

# Display all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

# Add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    category = input("Enter task category (e.g., Work, Personal): ")

    new_task = Task(title, description, category)
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task '{title}' added!")

# Mark a task as completed
def complete_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the number of the task to mark as completed: ")) - 1

    if 0 <= task_num < len(tasks):
        tasks[task_num].mark_completed()
        save_tasks(tasks)
        print(f"Task '{tasks[task_num].title}' marked as completed!")
    else:
        print("Invalid task number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the number of the task to delete: ")) - 1

    if 0 <= task_num < len(tasks):
        task = tasks.pop(task_num)
        save_tasks(tasks)
        print(f"Task '{task.title}' deleted!")
    else:
        print("Invalid task number.")

# Main menu for user interaction
def main_menu():
    tasks = load_tasks()

    while True:
        print("\nPersonal To-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()
