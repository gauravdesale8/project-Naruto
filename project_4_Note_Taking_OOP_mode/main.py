from notes_app import NotesApp

def main():
    app = NotesApp()
    app.load_from_file()

    while True:
        title = input("Title (or 'exit' to stop): ").strip()
        if title.lower() == "exit":
            break

        content = input("Concept: ").strip()
        app.add_notes(title, content)

    app.save_to_file()
    app.show_notes()

if __name__ == '__main__':
    main()