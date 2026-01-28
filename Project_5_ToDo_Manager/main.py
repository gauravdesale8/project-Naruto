from task import Task

def main():
    tasks = []

    title = input("Enter a task: ").strip()
    task = Task(title)
    tasks.append(task)

    print("\n---Tasks---")
    for t in tasks:
        print(t.title, "-", "Done" if t.completed else "Pending")



if __name__ == "__main__":
    main()