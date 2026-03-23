class Task:
    def __init__(self,title):
        self.title = title
        self.completed = False

    def mark_done(self):
        self.completed = True

    def display(self, index):
        status = "Done" if self.completed else "Pending"
        print(index, ".", self.title, '-', status)


