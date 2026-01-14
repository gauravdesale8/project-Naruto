def get_shinobi_info():
    name = input("Enter your name: ").strip()
    village = input("Enter your village: ").strip()
    rank = input("Enter your rank: ").strip().title()

    return name, village, rank

# .strip() removes accidental spaces
# .title() standardizes chakra flow