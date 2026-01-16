from shinobi import Shinobi

def main():
    name = input("Enter your name: ").strip()
    village = input("Enter your village: ").strip()
    rank = input("Enter your rank: ").strip()

    shinobi = Shinobi(name, village, rank)

    print("\n---SHINOBI PROFIT---")
    print("Name:", shinobi.name)
    print("Village:",shinobi.village)
    print("rank:",shinobi.rank)

if __name__ == '__main__':
    main()