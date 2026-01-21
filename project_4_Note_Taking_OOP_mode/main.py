from notes_app import NotesApp

def main():
    app = NotesApp()

    app.add_notes("Day 1:","Python Done")
    app.add_notes("Day 2","Postgres Done")

    app.show_notes()

if __name__ == '__main__':
    main()