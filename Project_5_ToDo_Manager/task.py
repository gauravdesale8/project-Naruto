class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def mark_done(self):
        self.completed = True
