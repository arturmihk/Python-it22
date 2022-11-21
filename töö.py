#Artur-Mihk Peterson
#21.11.22
#töö
#5. Kaugushüpe
#kasutaja sisestab 3 kaugushüppe tulemust
#sinu programm leiab ning väljastab parima ja keskmise tulemuse
#programmi dialoog kasutajaga on arusaadav ja üheselt mõistetav
#kogu looming salvestatakse tekstifaili
#kood kommenteeritud
f = open("har5", "w")
def kaugush(esi, teine, kolmas):
        suurim = max(esi,teine,kolmas)
        avg = round((esi+teine+kolmas)/3)
        print(f"Sinu parim hüpe oli {suurim}")
        print(f"Sinu keskmine tulemus oli {avg}")
        return suurim
        return avg

esih = int(input("Sisesta siia oma esimene hüpe: "))
teineh = int(input("Sisesta siia oma teine hüpe: "))
kolmash = int(input("Sisesta siia oma kolmas hüpe: "))
kaugush(esih, teineh, kolmash)
