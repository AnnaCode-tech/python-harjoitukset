#Kertaustehtävä 6

print("Ohjelma kerää lukuja listaan ja tulostaa listan sellaisenaan ja suuruusjärjtestyksessä.")
print("Ohjelman suoritus loppuu, jos syötät nollan.")

lista = []

while True:
    arvo = float(input("Anna luku: "))

    if arvo == 0:
        print("Ohjelman suoritus loppuu.")
        break

    else:
        lista.append(arvo)
        uusilista = sorted(lista)
        print("Lista syöttöjärjestyksessä: ", lista)
        print("Lista suuruusjärjestyksessä: ", uusilista)