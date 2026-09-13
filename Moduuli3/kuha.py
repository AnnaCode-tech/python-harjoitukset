kuha_mitta = int(input("Anna kuhan mitta senttimetreinä "))

if kuha_mitta < 37:
    puuttuu = 37-kuha_mitta
    print(f"Päästä kuha takaisin järveen. Kuha on alamittainen {puuttuu: 4.2f} senttimetriä")
else:
    print("Voit pitää kuhan!")