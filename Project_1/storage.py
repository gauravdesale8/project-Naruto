def collect_jutsus():
    jutsus = []

    print("\n Enter 3 Jutsu names:")
    for i in range(1,4):
        jutsu = input(f"Jutsu {i}: ").strip()
        jutsus.append(jutsu)

    return jutsus