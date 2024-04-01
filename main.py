from datetime import datetime

class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 5000)

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 8000)

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                foglalas = Foglalas(szoba, datum)
                return foglalas
        return None

    def lemondas(self, foglalas):
        if foglalas in self.foglalasok:
            self.foglalasok.remove(foglalas)
            return True
        return False

    def listaz(self):
        for foglalas in self.foglalasok:
            print(f"Szoba: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum}")

# Adatok feltöltése
szalloda = Szalloda("Tibi Szállója")
szalloda.add_szoba(EgyagyasSzoba("101"))
szalloda.add_szoba(KetagyasSzoba("201"))
szalloda.add_szoba(EgyagyasSzoba("102"))
szalloda.add_szoba(KetagyasSzoba("202"))
szalloda.add_szoba(EgyagyasSzoba("103"))

szalloda.foglalasok = [
    Foglalas(szalloda.szobak[0], datetime(2024, 4, 2)),
    Foglalas(szalloda.szobak[1], datetime(2024, 4, 3)),
    Foglalas(szalloda.szobak[2], datetime(2024, 4, 4)),
    Foglalas(szalloda.szobak[3], datetime(2024, 4, 5)),
    Foglalas(szalloda.szobak[4], datetime(2024, 4, 6))
]

# Felhasználói felület
while True:
    print("\n1. Foglalás")
    print("2. Lemondás")
    print("3. Foglalások listázása")
    print("4. Kilépés")
    choice = input("Válasszon egy opciót: ")

    if choice == "1":
        szobaszam = input("Adja meg a szoba számát: ")
        datum = input("Adja meg a foglalás dátumát (ÉÉÉÉ-HH-NN formátumban): ")
        try:
            datum = datetime.strptime(datum, "%Y-%m-%d")
            if datum < datetime.now():
                print("A foglalás dátuma nem lehet múltbeli.")
                continue
        except ValueError:
            print("Helytelen dátum formátum.")
            continue

        foglalas = szalloda.foglalas(szobaszam, datum)
        if foglalas:
            print(f"A foglalás sikeres: Szoba {szobaszam}, Dátum: {datum}")
        else:
            print("A megadott szobaszám nem létezik vagy foglalt ezen a dátumon.")

    elif choice == "2":
        print("Még nincs igazolva a lemondás.")

    elif choice == "3":
        print("Foglalások:")
        szalloda.listaz()

    elif choice == "4":
        print("Kilépés.")
        break

    else:
        print("Érvénytelen.")
