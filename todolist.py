tasks = []

while True:
    print("\n1. Show Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        if len(tasks) == 0:
            print("No tasks")
        else:
            for i in range(len(tasks)):
                print(i+1, ".", tasks[i])

    elif choice == "2":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added")

    elif choice == "3":
        num = int(input("Enter task number: "))
        if num <= len(tasks):
            tasks.pop(num-1)
            print("Task deleted")
        else:
            print("Invalid number")

    elif choice == "4":
        print("Bye!")
        break

    else:
        print("Invalid choice")