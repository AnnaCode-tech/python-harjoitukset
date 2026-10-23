
#Kertaustehtävä 2

luku = int(input("Anna kokonaisluku: "))

if luku%3 == 0 and luku%5 == 0:
    print("Luku on jollinen kolmella ja viidellä!")

elif luku%3 == 0:
    print("Luku on kolmella jaollinen.")

elif luku%5 == 0:
    print("Luku on viidellä jaollinen.")

elif luku%3 == 0 and luku%5 == 0:
    print("Luku on jolline kolmella ja viidellä!")

else:
    print("Luku ei ole jaollinen kolmella eikä viidellä.")
