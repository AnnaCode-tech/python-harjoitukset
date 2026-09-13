vuosiluku = int(input("Anna vuosiluku: "))

testi1 = vuosiluku % 4
testi2 = vuosiluku % 100
testi3 = vuosiluku % 400

if testi1 == 0 or testi2 == 0 and testi3 == 0:
    print("Vuosi on karkausvuosi")

else:
    print("Vuosi ei ole karkausvuosi")