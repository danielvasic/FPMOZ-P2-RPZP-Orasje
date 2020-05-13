class PrevoznoSredstvo():
    def __init__(self, naziv, tip):
        self.naziv = naziv
        self.tip = tip
    
    def __str__(self):
        return "{} - {}".format(self.naziv, self.tip)


class Biciklo(PrevoznoSredstvo):
    def __init__(self, naziv, tip):
        super().__init__(naziv, tip)
    
    def vozi (self):
        return "Ja sam biciklo i vozim se na dva točka..."

class Osoba:
    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime

    def __str__(self):
        return self.ime + " " + self.prezime

class Jahta(PrevoznoSredstvo):
    def __init__(self, naziv, tip):
        super().__init__(naziv, tip)
        self.posada = []

    def dodaj_clan_posade (self, osoba):
        self.posada.append(osoba)

    def __iter__(self):
        self.posada = iter(self.posada)
        return self.posada

    def __next__(self):
        next(self.posada)

    def vozi (self):
        return "Ja sam Jahta i vozim se po moru..."

if __name__=="__main__":
    '''
    biciklo = Biciklo("Mountain bike", "xyz")
    jahta = Jahta("Jahta", "xyz")
    print(biciklo)
    print(jahta)
    '''

    biciklo = Biciklo("Mountain bike", "xyz")
    jahta = Jahta("Jahta", "xyz")

    listaPrevoznihSredstava = []
    listaPrevoznihSredstava.append(biciklo)
    listaPrevoznihSredstava.append(jahta)

    for prevoznoSredstvo in listaPrevoznihSredstava:
        print(prevoznoSredstvo.vozi())

    # Dodavanje iteracija kroz kolekcijske klase

    jahta.dodaj_clan_posade(Osoba("Pero", "Peric"))
    jahta.dodaj_clan_posade(Osoba("Mate", "Matic"))
    jahta.dodaj_clan_posade(Osoba("Ana", "Anic"))

    jahta = iter(jahta)

    for osoba in jahta:
        print(osoba)

