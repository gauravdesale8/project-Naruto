from notes_app import NotesApp

def main():
    app = NotesApp()

    title = input("Title: ").strip()
    content = input("Concept: ").strip()

    app.add_notes(title, content)
    app.show_notes()

if __name__ == '__main__':
    main()