def show_intro(unpacked_data):
    name, village, rank = unpacked_data

    print("\n----- SHINOBI PROFILE -----")
    print("Name:", name)
    print("Village:", village)
    print("Rank:", rank)

    if rank == 'Genin':
        print("Report to your sensei, Training begins today.")
    elif rank == 'Chunin':
        print("You are trusted with real missions.")
    elif rank == 'Jonin':
        print("The village relies on your experience.")
    else:
        print("Rank Unrecognized. Stay Alert!")