def search_tasks(self, keyword):
    print("\n--- Search Results ---")

    found  = False

    for i, task in enumerate(self.tasks, start=1):
        if keyword.lower() in task.title.lower():
            task.display(i)
            found = True

    if not found:
        print("No matching tasks found.")
