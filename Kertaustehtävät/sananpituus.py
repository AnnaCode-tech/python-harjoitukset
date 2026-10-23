#Kertaustehtävä 7

sanalista = ["se", "joka", "päästi", "koirat", "ulos", "oli", "huolimaton"]
pitkatsanat = []

for sana in sanalista:
    kirjaimet = len(sana)

    if kirjaimet > 5:
        pitkatsanat.append(sana)

print("Sanat: ",sanalista)
pitkia = len(pitkatsanat)
print("Pitkiä yli 5:n kirjaimen sanoja on: ",pitkia)