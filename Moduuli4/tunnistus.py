oikea_tunnus = "etunimi.sukunimi"
oikea_salasana = "avain123"
kokeilu = 1

while kokeilu <=5:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")

#Salasana on oikein, pääsy sallitaan
    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        print("Tervetuloa")
        break
#Ilmoitetaan väärästä käyttäjätunnuksesta tai salasanasta
    if tunnus!= oikea_tunnus or salasana!= oikea_salasana:
        print("Pääsy evätty")
        jäljellä = 5-kokeilu
        print(f"Kokeiluja jäljellä {jäljellä}")
        kokeilu += 1

