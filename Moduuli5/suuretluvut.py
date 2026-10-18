#Luodaan listamuuttuja
luvut = []

#Pyydetään käyttäjältä lukuja
while True:
    luku_string = (input("Anna luku (Enter lopettaa ohjelman): "))

#Tutkitaan lopetusehto
    if luku_string == "":
        break

#Muutetaan string-muuttuja luvuksi ja tallennetaan syötetyt luvut listaan
    else:
        luku = float(luku_string)
        luvut.append(luku)

#Järjestetään lista suurimmasta pienimpään ja tulostetaan listan viisi ensimmäistä lukua
luvut.sort(reverse=True)
print("Viisi suurinta lukua ovat:")
for i in range(5):
    print(luvut[i])