print("---------TERVETULOA LASKINOHJELMAAN----------")

while True:
    print("Valitse mitä toimintoa haluat käyttää:")
    print("A: Yhteenlasku, B: Vähennyslasku, C: Kertolasku, D: Jakolasku, Q = Lopeta ohjelma")
    valinta = input("Anna valintasi: ").upper()

    if valinta == "Q":
        print("Poistutaan...")
        break

    a = float(input("Anna ensimmäinen luku: "))
    b = float(input("Anna toinen luku: "))

    if valinta == "A":
        print(f"Lukujen {a} ja {b} summa on {a+b}.")
    elif valinta == "B":
        print(f"Lukujen {a} ja {b} erotus on {a-b}.")
    elif valinta == "C":
        print(f"Lukujen {a} ja {b} tulo on {a*b}.")
    elif valinta == "D":
        print(f"Lukujen {a} ja {b} osamäärä on {a/b}.")
    else:
        print("Virheellinen valinta.")

print("Ohjelma päättynyt.")

#Keksi parempi kohta ilmoittaa virheellisestä valinnasta
#Kommentoi koodi - mitä se tekee missäkin kohdassa?