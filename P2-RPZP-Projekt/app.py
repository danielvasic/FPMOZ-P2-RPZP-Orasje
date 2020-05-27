from bottle import route, run, template, request, redirect
import sqlite3
try:
    conn = sqlite3.connect("rpzp.db")
    c = conn.cursor()
    c.execute("PRAGMA encoding='UTF8'")
    c.execute("""
        CREATE TABLE IF NOT EXISTS korisnik (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ime TEXT NOT NULL,
            prezime TEXT NOT NULL,
            email TEXT NOT NULL,
            datum_rodjenja TEXT NOT NULL
        );
    """)
    conn.commit()
except:
    print("Nastala je greška, nisam se uspio spojiti na bazu")


@route("/korisnik/forma")
def forma_korisnika():
    c = conn.cursor()
    c.execute("SELECT * FROM korisnik")
    korisnici = c.fetchall()
    return template("forma", korisnici=korisnici)


@route("/korisnik/dodaj", method="POST")
def dodaj_korisnika():
    ime = request.forms.get("ime")
    prezime = request.forms.get("prezime")
    email = request.forms.get("email")
    datum = request.forms.get("datum_rodjenja")

    sql = """
        INSERT INTO korisnik (ime, prezime, email, datum_rodjenja) VALUES (?, ?, ?, ?)
    """
    c = conn.cursor()
    c.execute(sql, [ime, prezime, email, datum])
    conn.commit()

    redirect("/korisnik/forma")


@route("/korisnik/pobrisi/<id>")
def dodaj_korisnika(id):

    sql = """
        DELETE FROM korisnik WHERE id=?
    """
    c = conn.cursor()
    c.execute(sql, [id])
    conn.commit()
    redirect("/korisnik/forma")


run(host="localhost", port=10000, debug=True)
