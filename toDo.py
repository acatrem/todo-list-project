import time



while True:
    print("---------To-Do List---------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice (1-5): "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
        continue

    if choice == 1:
        task = input("Enter the task: ")
        if not task.strip():
            print("Task cannot be empty.")
            continue
        
        file = open("tasks.txt", "a")
        file.write(task + "\n")
        file.close()

        print(f"Task '{task}' added.")

    elif choice == 2:
        file = open("tasks.txt", "r")
        tasks = file.readlines()
        file.close()
        if not tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
        
    elif choice == 3:
        file = open("tasks.txt", "r")
        tasks = file.readlines()
        file.close()
        if not tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
            
            try:
                task_number = int(input("Enter the task number to mark as completed: "))
                if task_number < 1 or task_number > len(tasks):
                    print("Invalid task number.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid task number.")
                continue

            completed_task = tasks[task_number - 1].strip()
            tasks[task_number - 1] = f"{completed_task} (Completed)\n"

            file = open("tasks.txt", "w")
            file.writelines(tasks)
            file.close()

            print(f"Task '{completed_task}' marked as completed.")
    
    elif choice == 4:
        file = open("tasks.txt", "r")
        tasks = file.readlines()
        file.close()
        if not tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
            
            try:
                task_number = int(input("Enter the task number to delete: "))
                if task_number < 1 or task_number > len(tasks):
                    print("Invalid task number.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid task number.")
                continue

            deleted_task = tasks[task_number - 1].strip()
            del tasks[task_number - 1]

            file = open("tasks.txt", "w")
            file.writelines(tasks)
            file.close()

            print(f"Task '{deleted_task}' deleted.")
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
    time.sleep(1)

