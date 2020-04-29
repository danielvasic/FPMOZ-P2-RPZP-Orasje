# Rjecnik je struktura u Pythonu koja 
# koristi kljuc - vrijednost 

rjecnik = {}
# inicijalizacija rjecnika preko vitičastih zagrada
rjecnik["kljuc"] = "vrijednost"
# postavljamo kljucu pod nazivom "kljuc" vrijednost pod nazivom "vrijednost"
# ukoliko zelimo procitati vrijednost u uglate zagrade napisemo vrijednost kljuca
# ukoliko kljuc ne postoji Python ce javiti gresku
print (rjecnik["kljuc"])
# isti rjecnik se može iskoristiti vise puta
rjecnik["kljuc2"] = "vrijednost2"
print(rjecnik["kljuc2"])

# ukoliko zelimo iterirati kroz rjecnik možemo koristiti metodu items

for kljuc, vrijednost in rjecnik.items():
    print(kljuc, vrijednost)

#ukoliko zelimo iterirati kroz samo vrijednosti možemo koristiti values metodu
for vrijednost in rjecnik.values():
    print(vrijednost)

# slično vrijedi za metodu keys

for kljuc in rjecnik.keys():
    print(kljuc)