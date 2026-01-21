class NotesApp:
    def __init__(self):
        self.notes = []

    def add_notes(self, title, content):
        note = {
            "title": title,
            "content": content
        }
        self.notes.append(note)

    def show_notes(self):
        print("\n---Notes---")
        for note in self.notes:
            print(f" {note['title']} | {note['content']}")