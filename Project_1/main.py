from input_handler import get_shinobi_info
from missions import show_intro

def main():
    shinobi = get_shinobi_info()
    show_intro(shinobi)

if __name__ == '__main__':
    main()