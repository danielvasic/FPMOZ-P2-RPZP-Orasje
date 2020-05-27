# Otvaranje datoteke u Python programskom jeziku
# Otvaranje datoteke u modu zapisivanja - w
# Otvaranje datoteke u modu dodavanja - a
datoteka = open("datoteka.txt", "a")

# Zapis u datoteku
# Posebni znak \n se može koristiti za dodavanje novog reda
datoteka.write("Ovo je zapis u datoteku\n")
# Zapis u datoteku preko metode writelines
datoteka.writelines(["Ovo je zapis u datoteku\n"])

datoteka.close()

# Citanje iz datoteka
datoteka = open("datoteka.txt", "r")
# Petlja za isčitavanje liniju po liniju
for line in datoteka.readlines():
    print(line)