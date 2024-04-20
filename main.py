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

    def __str__(self):
        return f"Szoba: {self.szoba.szobaszam}, Dátum: {self.datum.strftime('%Y-%m-%d')}"


class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []
        self.foglalasok_tombje = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                # Ellenőrizzük, hogy a dátum jövőbeli-e
                if datum < datetime.now():
                    return "A foglalás dátuma nem lehet múltbeli."
                # Ellenőrizzük, hogy a szoba elérhető-e akkor
                for foglalas in self.foglalasok:
                    if foglalas.szoba == szoba and foglalas.datum == datum:
                        return "A szoba már foglalt ezen a dátumon."
                # Visszaadjuk a szoba árát
                foglalas = Foglalas(szoba, datum)
                self.foglalasok.append(foglalas)
                self.foglalasok_tombje.append(foglalas)
                return foglalas
        return "A megadott szobaszám nem létezik."

    def foglalas_ar(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                # Ellenőrizzük, hogy a dátum jövőbeli-e
                if datum < datetime.now():
                    return "A foglalás dátuma nem lehet múltbeli."
                # Ellenőrizzük, hogy a szoba elérhető-e akkor
                for foglalas in self.foglalasok:
                    if foglalas.szoba == szoba and foglalas.datum == datum:
                        return "A szoba már foglalt ezen a dátumon."
                # Visszaadjuk a szoba árát
                return szoba.ar
        return "A megadott szobaszám nem létezik."

    def lemondas(self, foglalas):
        if foglalas in self.foglalasok:
            self.foglalasok.remove(foglalas)
            return True
        return False

    def listaz(self):
        if self.foglalasok:
            print("Foglalások:")
            for foglalas in self.foglalasok:
                print(foglalas)
        else:
            print("Nincsenek foglalások.")


# Adatok feltöltése
szalloda = Szalloda("Tibi Szállója")
szalloda.add_szoba(EgyagyasSzoba("101"))
szalloda.add_szoba(KetagyasSzoba("201"))
szalloda.add_szoba(EgyagyasSzoba("102"))
szalloda.add_szoba(KetagyasSzoba("202"))
szalloda.add_szoba(EgyagyasSzoba("103"))

szalloda.foglalas("101", datetime(2024, 4, 7))
szalloda.foglalas("201", datetime(2024, 4, 8))
szalloda.foglalas("102", datetime(2024, 4, 9))
szalloda.foglalas("202", datetime(2024, 4, 10))
szalloda.foglalas("103", datetime(2024, 4, 11))

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
            ar = szalloda.foglalas_ar(szobaszam, datum)
            if isinstance(ar, int):
                print(f"A foglalás sikeres. Az ára: {ar}")
            else:
                print(ar)
        except ValueError:
            print("Helytelen dátum formátum.")

    elif choice == "2":
        print("Még nincs igazolva a lemondás.")

    elif choice == "3":
        szalloda.listaz()

    elif choice == "4":
        print("Kilépés.")
        break

    else:
        print("Érvénytelen választás.")
