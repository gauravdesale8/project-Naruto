from task import Task


def main():
    tasks = []

    while True:
        print("\n---- Task Manager ----")
        print("1. Add a task.")
        print("2. View tasks.")
        print("3. Exit")

        try:
            choice = int(input("Choose an option: "))

            if choice == 1:
                title = input("Enter a task title: ").strip()
                task = Task(title)
                tasks.append(task)

            elif choice == 2:
                print("\n--- Tasks ---")
                for t in tasks:
                    status = "Done" if t.completed else "Pending"
                    print(t.title, "-", status)

            elif choice == 3:
                print("GoodBye!")
                break

            else:
                print("Invalid Choice. Try again.")

        except ValueError:
            print("Please enter a number!")


if __name__ == "__main__":
    main()