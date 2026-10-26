#Määritellään funktio ennen kuin sitä voi kutsua

def tervehdi(tervehdys, kerrat):
    for i in range(kerrat):
        print(tervehdys + str(i+1) + ". kerran.")
    return

#PÄÄOHJELMA

print("Testataan tervehdys-funktiota:")
tervehdi("Moi", 3)
print("Testataan vielä varmistukseksi..")
tervehdi("Hello!", 5)


