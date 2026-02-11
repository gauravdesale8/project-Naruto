class Task:
    def __init__(self, title, completed = False):
        self.title = title
        self.completed = completed

    def mark_done(self):
        self.completed = True
