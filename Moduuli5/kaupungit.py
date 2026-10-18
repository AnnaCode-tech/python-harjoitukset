#Muodostetaan listamuuttuja
kaupungit = []

#Kysytään kaupunkia 5 kertaa ja tallennetaan syötetyt kaupungit listamuuttujaan

for i in range(5):
    kaupunki = input("Anna kaupungin nimi: ")
    kaupungit.append(kaupunki)

#Tulostetaan listatut kaupungit

print("Listasit seuraavat kaupungit:")

for kaupunki in kaupungit:
    print(kaupunki)
