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

class Jahta(PrevoznoSredstvo):
    def __init__(self, naziv, tip):
        super().__init__(naziv, tip)

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
