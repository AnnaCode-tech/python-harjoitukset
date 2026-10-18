# Otetaan käyttöön satunnislukugeneraattori
import random

# Kysytään käyttäjältä noppien määrä
nopat= int(input ("Kuinka monta noppaa sinulla on? "))

# alustetaan muuuttujat, joka tallettaa noppien silmäluvut ja lukujen summan
luku = 0
summa = 0
arvonnat = []

#for-luuppi suoritetaan käyttäjän ilmoittamalle noppien määrälle
for i in range(nopat):

# Arvotaan silmäluku, lasketaan lukujen summa ja laitetaan arvottu lukema muistiin
  luku = random.randint(1,6)
  summa += luku
  arvonnat.append(luku)
  
 # Tulostetaan tiedot käyttäjälle 
print(f"Arvottiin luvut: {arvonnat}")
print(f"Arvottujen silmälukujen summa on: {summa}")

