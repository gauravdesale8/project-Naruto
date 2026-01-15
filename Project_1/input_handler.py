def get_shinobi_info():
    name = input("Enter your name: ").strip()
    village = input("Enter your village: ").strip()
    rank = input("Enter your rank: ").strip().title()

    return name, village, rank

# .strip() removes accidental spaces
# .title() standardizes chakra flow

def get_mission_count():
    while True:
        try:
            mission_count = int(input("\nHow many missions have you completed? "))
            return mission_count
        except ValueError:
            print("Please enter a valid number.")
