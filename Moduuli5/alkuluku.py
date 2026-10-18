# Pyydetään kokonaisluku
luku = int(input("Anna kokonaisluku: "))

#Alustetaan muuttujat
jakajat = list(range(2, luku))
jaannokset = []

#Lasketaan jakojäännökset muilla kuin 1:llä ja luvulla itsellään
for jakaja in jakajat:
    jakojaannos = luku % jakaja
    jaannokset.append(jakojaannos)

#Tutkitaan jaollisuus    
if 0 in jaannokset:
    print ("Luku ei ole alkuluku.")

else:
    print ("Luku on alkuluku.")
    