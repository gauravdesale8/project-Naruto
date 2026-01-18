class Shinobi:
    def __init__(self, name, village, rank):
        self.name = name
        self.village = village
        self.rank = rank

    def show_profile(self):
        print("\n----SHINOBI PROFILE----")
        print("Name: ", self.name)
        print("village: ", self.village)
        print("rank: ", self.rank)

    def rank_message(self):
        if self.rank == 'Genin':
            print("\nReport to your sensei. Training begins today.")
        elif self.rank == 'Chunin':
            print("\nYou are trusted with real missions.")
        elif self.rank == 'Jonin':
            print("\nThe village relies on your experience.")
        else:
            print("\nRank unrecognized. Stay Alert!")