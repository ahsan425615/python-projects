tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added.")

def mark_done(task):
    if task in tasks:
        tasks.remove(task)
        print("Task marked as done.")
    else:
        print("Task not found.")

def delete_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task deleted.")
    else:
        print("Task not found.")

def display_tasks():
    if tasks:
        print("Tasks:")
        for task in tasks:
            print(task)
    else:
        print("No tasks.")

while True:
    print("\nMenu:")
    print("1. Add Task")
    print("2. Mark Task as Done")
    print("3. Delete Task")
    print("4. Display Tasks")
    print("5. Quit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '1':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter task to mark as done: ")
        mark_done(task)
    elif choice == '3':
        task = input("Enter task to delete: ")
        delete_task(task)
    elif choice == '4':
        display_tasks()
    elif choice == '5':
        break
    else:
        print("Invalid input. Please try again.")
1