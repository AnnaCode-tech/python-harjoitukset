
syote = input("Anna luku: ")
luku1= float(syote)
pienin = luku1
suurin = luku1

while syote!="":
    luku = float(syote)
    if luku < pienin:
        pienin = luku
    elif luku > suurin:
        suurin = luku
    syote = input("Anna uusi luku (tai lopeta ohjelma painamalla Enter): ")
    

print("Ohjelman suoritus loppuu.")
print(f"Pienin luku oli: {pienin}")
print(f"Suurin luku oli: {suurin}")
