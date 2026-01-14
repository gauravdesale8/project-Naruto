def show_intro(shinobi):
    name, village, rank = shinobi

    print("\n----- SHINOBI PROFILE -----")
    print("Name:", name)
    print("Village:", village)
    print("Rank:", rank)

    if rank == 'Genin':
        print("Train Hard! Your journey begins.")
    elif rank == 'Jonin':
        print("The village counts on you.")
    else:
        print("Serve the village with honor.")