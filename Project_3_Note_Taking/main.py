def write_note():
    note =  input("Write a note: ")

    with open("notes.txt", "a") as file:
        file.write(note +  "\n")

def read_notes():
    print("\n--- Your Notes ---")

    with open("notes.txt","r") as file:
        for line in file:
            print(line.strip())

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