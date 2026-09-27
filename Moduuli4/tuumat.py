tuumat = float(input("Anna tuumat (negatiivinen arvo lopettaa ohjelman): "))

while tuumat > 0:
    sentit = tuumat * 2.54
    print (f"Tulos: {tuumat} tuumaa on {sentit:5.2f} senttimetriä")
    tuumat = float(input("Anna tuumat: "))
print ("Ohjelma lopetettu.")