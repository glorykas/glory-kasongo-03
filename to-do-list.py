tasks = []

# This is to add a new task to the to-do-list

def add_task():
    
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully.")

# This is to view the different tasks in the to-do-list

def view_tasks():
    if len(tasks) == 0:
        print("No tasks to view.")
    else:
        print("List of tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

# This is to delete a task from the to-do-list

def delete_task():

    if len(tasks) == 0:
        print("No task to delete.")
    else:
        print("tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {tasks}")
        choice = int(input("Enter the task number to delete: "))

        if 0 < choice <= len(tasks):
            del tasks[choice -1]
            print("Task deleted successfully. ")
        else:
            print("Invalid task number. ")

# This is to run the command line of the to-do-list application
            
def main():
    while True:
        print("\n===== To-Do-List Application =====")
        print("1. Add Task ")
        print("2. View Tasks ")
        print("3. Delete Task ")
        print("4. Quit ")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            print("Thank you for using the To-Do-List Application. ")
            break
        else:
            print("Invalide choice. Please try again")

if __name__ == "__main__":
    main()
