from task import Task

def load_task(filename='tasks.txt'):
    tasks = []

    try:
        with open(filename, 'r') as file:
            for line in file:
                title, completed = line.strip().split('|')
                task = Task(title, completed == '1')
                tasks.append(task)
    except FileNotFoundError:
        pass

    return tasks

def save_tasks(tasks, filename = 'tasks.txt'):
    with open(filename, 'w') as file:
        for task in tasks:
            status = "1" if task.completed else "0"
            file.write(f"{task.title} | {status}\n")


def main():
    tasks = load_task()

    while True:
        print("\n---- Task Manager ----")
        print("""
        1. Add a task
        2. View a task
        3. Mark task as done
        4. Exit
        """)

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter a task title: ").strip()
            task = Task(title)
            tasks.append(task)

        elif choice == '2':
            print("\n--- Tasks ---")
            for index, t in enumerate(tasks, start=1 ):
                status = "Done" if t.completed else "Pending"
                print(index, '.', t.title, "-", status)

        elif choice == '3':
            task_no = input("Enter a task no. to mark done: ").strip()

            if task_no.isdigit():
                task_index = int(task_no) - 1

                if 0 <= task_index < len(tasks):
                    tasks[task_index].mark_done()
                    print("Task marked as done.")
                else:
                    print("Invalid task number.")
            else:
                print("\nPlease enter a number.")

        elif choice == '4':
            save_tasks(tasks)
            print("Task saved. GoodBye!")
            break

        else:
            print("Invalid Choice. Try again.")

if __name__ == "__main__":
    main()