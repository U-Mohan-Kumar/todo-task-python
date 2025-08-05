FILENAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILENAME, "r") as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def main():
    tasks = load_tasks()

    while True:
        print("\n1. View Tasks\n2. Add Task\n3. Remove Task\n4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            if tasks:
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t}")
            else:
                print("No tasks.")
        
        elif choice == "2":
            task = input("Enter task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added.")
        
        elif choice == "3":
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
            try:
                num = int(input("Task number to remove: ")) - 1
                if 0 <= num < len(tasks):
                    removed = tasks.pop(num)
                    save_tasks(tasks)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Enter a valid number.")
        
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()