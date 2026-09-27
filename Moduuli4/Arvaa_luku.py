import random
luku = random.randint(1,10)
print("Leikitäänkö arvausleikkiä?")
arvaus = int(input("Arvaa kokonaisluku välillä 1...10: "))

while arvaus!=luku:
    if arvaus > luku:
        print("Liian suuri luku")
        arvaus = int(input("Arvaa uudestaan: "))
    else:
        print("Liian pieni luku")
        arvaus = int(input("Arvaa uudestaan: "))

print("Oikein!")
print(f"Luku oli {luku}")