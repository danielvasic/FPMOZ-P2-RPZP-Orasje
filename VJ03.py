# izgradnja klase
# klasa je reprezentacija (apstraktna) objekta iz
# realnog svijeta

class Auto:
    # Klasa se sastoji od konstruktora

    def __init__(self, proizvodjac, tip):
        # atributi se referenciraju 
        # preko lokalnog pokazivaca self
        self.tip = tip
        self.proizvodjac = proizvodjac
        # proizvodjac i tip bez self su 
        # argumenti koji se prosljedjuju 
        # preko konstruktora

    def vozi (self):
        # klasa se sastoji i od metoda
        print ("Ja sam " + 
        self.proizvodjac + " i tip " + 
        self.tip + " i vozim se")

# sada klasu nismo instancirali
# tipično u Pythonu se pravi objekt koji je instanca
# klase

# od jedne klase može se napraviti više objekata
bmw = Auto("BMW", "E322")
audi = Auto("Audi", "Q3")
# voze se automobil BMW i Audi
bmw.vozi()
audi.vozi()

# prosljeđeni argumenti se postavljaju 
# lokalnim vrijednostima pojedinog objekta
# a u drugim metodama se koriste uz pomoć self