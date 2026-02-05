from task import Task


def main():
    tasks = []

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
            print("GoodBye!")
            break

        else:
            print("Invalid Choice. Try again.")

if __name__ == "__main__":
    main()