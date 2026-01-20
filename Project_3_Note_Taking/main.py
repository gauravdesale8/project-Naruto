def write_note():
    title = input("Title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return

    content = input("Content: ").strip()
    if not content:
        print("Content cannot be empty.")
        return

    note = {
        "title" : title,
        "content" : content
    }

    with open("notes.txt", "a") as file:
        file.write(f"{note['title']} | {note['content']}\n")

def read_notes():
    print("\n--- Your Notes ---")

    try:
        with open("notes.txt","r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No notes found yet.")

def main():
    while True:
        print("\n----Notes App----")
        print("""
        1. Add a note,
        2. View notes,
        3. Exit
        """)

        choice = input("Choose an option: ")

        if choice == '1':
            write_note()
        elif choice == '2':
            read_notes()
        elif choice == '3':
            print("GoodBye.")
            break
        else:
            print("Invalid choice. Try Again.")


if __name__ == '__main__':
    main()