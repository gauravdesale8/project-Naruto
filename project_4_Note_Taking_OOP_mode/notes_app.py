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

    def save_to_file(self, filename = "notes.txt"):
        with open(filename, 'w') as file:
            for note in self.notes:
                file.write(f"{note['title']} | {note['content']}\n")

    def load_from_file(self, filename = 'notes.txt'):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    title, content = line.strip().split('|')
                    self.add_notes(title, content)

        except FileNotFoundError:
            pass