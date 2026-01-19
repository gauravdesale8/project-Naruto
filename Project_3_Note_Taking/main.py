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
    write_note()
    read_notes()

if __name__ == '__main__':
    main()