#Kertaustehtävä 9

tuotteet = []
kappalemaarat = []

while True:
    tuote = input("Mitä tuotetta valmistetaan? ")
    maara = input("Kuinka monta valmistetaan? ")
    ohje = input("Jatketaanko tuotantoa (kyllä/ei)? ")

    tuotteet.append(tuote)
    kappalemaarat.append(maara)

    if ohje.lower() == "ei":
        print("Tuotanto lopetettu.")
        break

print("Valmistetut tuotteet:")

for i in range(len(tuotteet)):
    print(tuotteet[i],":", kappalemaarat[i], "kpl")