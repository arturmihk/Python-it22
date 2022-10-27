#Artur-Mihk Peterson
#27.10.22
#harjutus06

minu_fail = open("s6pru_l6ustaraamat.txt", "r")

reformikad = 0
keskerak = 0
erakonnad = []

for i in minu_fail.readlines():
    enimi,pnimi,er,palk = i.split(" ")
    if er=="RE":
        reformikad+=1
    elif er=="KE":
        keskerak+=1
    #Leiab erinevad erakonnad
    if er not in erakonnad:
        erakonnad.append(er)
#Lisa kõik poliitiuke nimed uude faili
    with open("poliitikud.txt", "a") as fail_kirjutamiseks:
        fail_kirjutamiseks.write(enimi + " " + pnimi + "\n" )

print(f"Reformikaid kokku: {reformikad}")
print(f"Keskerakaid kokku: {keskerak}")
print(f"Erakondi kokku: {len(erakonnad)}")


minu_fail.close 