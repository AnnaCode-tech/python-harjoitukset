
#Kertaustehtävä 1
#Tiedustellaan käyttäjältä lähtötiedot

tuntipalkka = float(input("Mikä on tuntipalkkasi (Euroa)? "))
tunnit = float(input("Kuinka monta tuntia työskentelit tänään? (ilmoita tunteina) "))
paiva = input("Mikä päivä tänään on? ")

#Lasketaan päiväpalkka sunnuntaina (if-lauseke) ja muina päivinä (else) ja 
if paiva.lower() == "sunnuntai":
    palkka = tuntipalkka * 2 * tunnit
    
else:
    palkka = tunnit * tuntipalkka

#Tulostetaan päivän palkka  
print(f"Tienasit tänään {palkka} euroa")



