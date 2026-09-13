sukupuoli = input("Anna sukupuoli: ")
hemoglobiini = int(input("Anna hemoglobiini (g/l): "))

if sukupuoli == "Nainen" or sukupuoli == "nainen":
    if hemoglobiini > 175:
        print("Hemoglobiinisi on korkea.")
    if 117 <= hemoglobiini <= 175:
        print("Hemoglobiinisi on normaali.")
    if hemoglobiini < 117:
        print("Hemoglobiinisi on matala.")

if sukupuoli == "Mies" or sukupuoli == "mies":
    if hemoglobiini > 195:
        print("Hemoglobiinisi on korkea.")
    if 134 <= hemoglobiini <= 195:
        print("Hemoglobiinisi on normaali.")
    if hemoglobiini < 134:
        print("Hemoglobiinisi on matala.")

else:
    print("Virhe lähtötiedoissa, yritä uudelleen.")