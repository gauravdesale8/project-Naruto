from shinobi import Shinobi

def main():
    name = input("Enter your name: ").strip().title()
    village = input("Enter your village: ").strip().title()
    rank = input("Enter your rank: ").strip().title()

    shinobi = Shinobi(name, village, rank)

    shinobi.show_profile()

if __name__ == '__main__':
    main()