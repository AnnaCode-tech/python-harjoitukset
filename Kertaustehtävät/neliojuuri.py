#Kertaustehtävä 4

from math import sqrt

print("Ohjelma laskee neliöjuuren antamasi kokonaisluvusta. Jos annat nollan ohjelman suoritus loppuu.")

while True:
    luku = int(input("Anna kokonaisluku: ")) 

    if luku == 0:
        print("Ohjelman suoritus loppuu.")
        break

    elif luku < 0:
        print("Virheellinen luku.")

    else:
        print("Neliöjuuri on:", sqrt(luku))