import sqlite3
import tkinter as tk


class Korisnik:
    def __init__(self, ime, prezime, email, lozinka):
        self.ime = ime
        self.prezime = prezime
        self.email = email
        self.lozinka = lozinka


class Baza:
    def __init__(self, naziv_baze):
        self.konekcija = sqlite3.connect(naziv_baze)
        self.stvori_tablice()

    def stvori_tablice(self):
        upit = """
            CREATE TABLE IF NOT EXISTS korisnik (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ime TEXT NOT NULL,
                prezime TEXT NOT NULL,
                email TEXT NOT NULL,
                lozinka TEXT NOT NULL
            )
        """
        self.konekcija.cursor().execute(upit)

    def ubaci_korisnika(self, korisnik):
        upit = "INSERT INTO korisnik VALUES(null, '{}', '{}', '{}', '{}');".format(
            korisnik.ime,
            korisnik.prezime,
            korisnik.email,
            korisnik.lozinka
        )
        self.konekcija.cursor().execute(upit)
        self.konekcija.commit()


class Aplikacija (tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.master = master
        self.master.title("Registrirajte se")
        self.master.geometry("400x300")
        self.baza = Baza("p2rpzp.db")
        self.izgradi_sucelje()

    def izgradi_sucelje(self):
        self.imeLbl = tk.Label(self.master, text="Unesite Vaše ime*:")
        self.imeLbl.grid(column=0, row=0)

        self.imeTxt = tk.Entry(self.master)
        self.imeTxt.grid(column=1, row=0)

        self.prezimeLbl = tk.Label(self.master, text="Unesite Vaše prezime*:")
        self.prezimeLbl.grid(column=0, row=1)

        self.prezimeTxt = tk.Entry(self.master)
        self.prezimeTxt.grid(column=1, row=1)

        self.emailLbl = tk.Label(self.master, text="Unesite Vaš email*:")
        self.emailLbl.grid(column=0, row=2)

        self.emailTxt = tk.Entry(self.master)
        self.emailTxt.grid(column=1, row=2)

        self.lozinkaLbl = tk.Label(self.master, text="Unesite Vašu lozinku*:")
        self.lozinkaLbl.grid(column=0, row=3)

        self.lozinkaTxt = tk.Entry(self.master, show="*")
        self.lozinkaTxt.grid(column=1, row=3)

        self.ubaciBtn = tk.Button(
            self.master,
            text="Registriraj se",
            command=self.ubaci_korisnika,
            width=10, height=2
        )

        self.ubaciBtn.grid(column=0, row=4, columnspan=2,
                           pady=(10, 10))

    def ubaci_korisnika(self):
        korisnik = Korisnik(
            self.imeTxt.get(),
            self.prezimeTxt.get(),
            self.emailTxt.get(),
            self.lozinkaTxt.get()
        )

        self.baza.ubaci_korisnika(korisnik)

        self.imeTxt.delete(0, tk.END)
        self.prezimeTxt.delete(0, tk.END)
        self.emailTxt.delete(0, tk.END)
        self.lozinkaTxt.delete(0, tk.END)


if __name__ == "__main__":
    '''
    baza = Baza("p2rpzp.db")
    korisnik = Korisnik("Daniel", "Vasić",
                        "daniel.vasic@fpmoz.sum.ba", "123456")
    baza.ubaci_korisnika(korisnik)
    '''

    master = tk.Tk()
    app = Aplikacija(master)
    app.mainloop()
