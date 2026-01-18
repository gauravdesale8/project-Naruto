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