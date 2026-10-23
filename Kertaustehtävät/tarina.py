#Kertaustehtävä 5
#Annetaan ohjeet käyttäjälle

print("Tämä ohjelma kirjoittaa tarinan sana kerrallaan. Tarina on valmis, kun kirjoitat 'loppu'.")

#Alustetaan listamuuttuja
tarina = []

#Pyydetään käyttäjältä sanoja
while True:
    sana = input("Anna sana lisättäväksi tarinaan: ")
    tarina.append(sana)

#Suorituksen lopetusehto
    if sana.lower() == "loppu":
       break

#Poistetaan lopetussana tarinasta
tarina.remove("loppu")

#Alustetaan string-muuttuja tulostusta varten
valmistarina = ""

#Puretaan listamuuttuja string-muuttujaan
for sana in tarina:
    valmistarina = valmistarina + " " + sana

#Tulostetaan lopputulos
print("Tässä tarinasi: ")
print(valmistarina)