from input_handler import get_shinobi_info, get_mission_count
from missions import show_intro, show_missions

def main():
    shinobi = get_shinobi_info()
    show_intro(shinobi)

    mission_count = get_mission_count()
    show_missions(mission_count)

if __name__ == '__main__':
    main()