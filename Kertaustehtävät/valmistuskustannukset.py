#Kertaustehtävä 8
#Alustetaan muuttuja kustannukset

kustannukset = [12.5, 8.2, 15.0, 6.5, 10.8]

#Puretaan lista for-loopilla

for kustannus in kustannukset:
    print("Tuotteeen valmistuskustannus:", kustannus, "€")

#Alustetaan muuttja yhteiskustannus ja lasketaan sille arvo

yhteiskustannus = 0

for kustannus in kustannukset:
    yhteiskustannus += kustannus

#Tulostetaan lopputulos

print("Valmistuskustannukset yteensä:", yhteiskustannus,"€")
