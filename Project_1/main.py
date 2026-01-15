from input_handler import get_shinobi_info, get_mission_count
from missions import show_intro, show_missions, show_jutsus
from storage import collect_jutsus

def main():
    shinobi = get_shinobi_info()
    show_intro(shinobi)

    mission_count = get_mission_count()
    show_missions(mission_count)

    jutsus = collect_jutsus()
    show_jutsus(jutsus)

if __name__ == '__main__':
    main()