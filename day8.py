# A Simple To Do List App which allows users to add, view, mark as done, and delete tasks.

tasks = []


def show_menu():
    print("\n===== TO DO LIST APP =====")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark a task as done")
    print("4. Delete a task")
    print("5. Exit")


def show_tasks():
    if len(tasks) == 0:
        print("\nNo tasks added yet.")
    else:
        print("\nYour Tasks:")

        for i in range(len(tasks)):
            task = tasks[i]
            print(str(i + 1) + ". " + task)


def add_task():
    task = input("\nEnter your task: ")

    if task == "":
        print("Task cannot be empty.")
    else:
        tasks.append(task)
        print("Task added successfully!")


def mark_task_done():
    show_tasks()

    if len(tasks) > 0:
        number = input("\nEnter the task number to mark as done: ")

        if number.isdigit():
            number = int(number)

            if number >= 1 and number <= len(tasks):
                if "[Done]" not in tasks[number - 1]:
                    tasks[number - 1] = tasks[number - 1] + " [Done]"
                    print("Task marked as done!")
                else:
                    print("This task is already done.")
            else:
                print("Invalid task number.")
        else:
            print("Please enter a valid number.")


def delete_task():
    show_tasks()

    if len(tasks) > 0:
        number = input("\nEnter the task number to delete: ")

        if number.isdigit():
            number = int(number)

            if number >= 1 and number <= len(tasks):
                removed_task = tasks.pop(number - 1)
                print("Deleted task:", removed_task)
            else:
                print("Invalid task number.")
        else:
            print("Please enter a valid number.")


while True:
    show_menu()

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        mark_task_done()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("\nThank you for using the To Do List App!")
        break

    else:
        print("Invalid choice. Please choose from 1 to 5.")