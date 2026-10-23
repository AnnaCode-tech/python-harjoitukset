

while True:
    print("Tuote valmistettu!")
    ohje = input("Jatketaanko tuotantoa (kyllä/ei)? ")

    if ohje.lower() == "ei":
        print("Tuotanto keskeytetty.")
        break