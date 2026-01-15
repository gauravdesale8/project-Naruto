def collect_jutsus():
    jutsus = []

    print("\n Enter 3 Jutsu names:")
    for i in range(1,4):
        while True:
            jutsu = input(f"Jutsu {i}: ").strip()
            if jutsu:
                jutsus.append(jutsu)
                break
            else:
                print("Jutsu name cannot be empty.")
    return jutsus