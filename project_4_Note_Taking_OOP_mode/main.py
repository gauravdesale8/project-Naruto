from notes_app import NotesApp

def main():
    app = NotesApp()

    while True:
        title = input("Title (or 'exit' to stop): ").strip()
        if title.lower() == "exit":
            break

        content = input("Concept: ").strip()
        app.add_notes(title, content)

    app.show_notes()

if __name__ == '__main__':
    main()