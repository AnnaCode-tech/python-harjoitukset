while True:

    syote_1 = input("Anna kokonaisluku: ")

    try:
        luku_1 = int(syote_1)
        break
    except ValueError:
        print("Virhe: et antanut kokonaislukua, yritä uudelleen: ")

while True:
    syote_2 = input("Anna toinen kokonaisluku: ")

    try:
        luku_2 = int(syote_2)
        break
    except ValueError:
        print("Virhe: toinen luku ei ole kokonaisluku, yritä uudelleen:")

while True:
    syote_3 = input("Anna kolmas kokonaisluku: ")
    try: 
        luku_3 = int(syote_3)    
        break  
    except ValueError:
        print("Virhe: kolmas luku ei ole kokonaisluku, yritä uudelleen: ")

summa = luku_1 + luku_2 + luku_3
tulo = luku_1 * luku_2 * luku_3
keskiarvo = summa / 3

print("Kiitos luvuista!")
print(f"Lukujen summa on: {summa}")
print(f"Lukujen tulo on: {tulo}")
print(f"Lukujen keskiarvo on: {keskiarvo}")
