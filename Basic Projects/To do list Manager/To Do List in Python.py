def task():
    tasks = [] 
    print("Welcome to the To Do List ")

    total_task = int(input("Enter how many tasks you want to add = "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)

    print(f"Todays tasks are:\n{tasks}")

    while True: 
        operation = int(input("Enter 1 - Add\n2 - Update\n3 - Delete\n4 - View\n5 - Exit/Stop\nChoice: "))
        
        if operation == 1:
            add = input("Enter task you want to add: ")
            tasks.append(add) 
            print(f"Task '{add}' has been added successfully.")

        elif operation == 2:
            update = input("Enter the task name you want to update: ")
            if update in tasks:
                new_task = input("Enter new task name: ")
                index = tasks.index(update)
                tasks[index] = new_task
                print(f"Task '{update}' updated to '{new_task}'")
            else:
                print(f"Task '{update}' not found.")

        elif operation == 3:
            del_value = input("Enter the task you want to delete: ")
            if del_value in tasks: 
                tasks.remove(del_value)
                print(f"Task '{del_value}' has been deleted.")
            else:
                print(f"Task '{del_value}' not found.")

        elif operation == 4:
            print("Current Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

        elif operation == 5:
            print("Closing the To Do List....")
            break

        else: 
            print("Invalid input, please try again.")

task()
