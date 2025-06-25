# Simple To-Do List Application

todo_list = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Remove Task")
    print("5. Exit")

def view_tasks():
    if not todo_list:
        print("\nNo tasks in the list.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def add_task():
    task = input("Enter the task: ")
    todo_list.append(task)
    print(f"Task '{task}' added successfully!")

def complete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as completed: "))
        completed = todo_list.pop(task_num - 1)
        print(f"Task '{completed}' marked as completed and removed.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def remove_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to remove: "))
        removed = todo_list.pop(task_num - 1)
        print(f"Task '{removed}' removed successfully.")
    except (IndexError, ValueError):
        print("Invalid task number.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")
    
    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        complete_task()
    elif choice == '4':
        remove_task()
    elif choice == '5':
        print("Exiting To-Do List App. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
