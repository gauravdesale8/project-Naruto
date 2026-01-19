from shinobi import Shinobi
from missions import MissionHandler

def main():
    name = input("Enter your name: ").strip().title()
    village = input("Enter your village: ").strip().title()
    rank = input("Enter your rank: ").strip().title()

    shinobi = Shinobi(name, village, rank)
    missions = MissionHandler()

    shinobi.show_profile()
    shinobi.rank_message()

    count = input("\nHow many missions have you completed? ")
    missions.show_missions(count)

if __name__ == '__main__':
    main()