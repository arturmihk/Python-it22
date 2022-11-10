#Artur-Mihk Peterson
#2.11.22
#ül
import math
import random
import datetime
from datetime import date
#Tahvli juurde

failinimi = input("Palun sisestage failinimi: ")
f = open(failinimi)
opilased = []
tana = date.today()
jrk = int(tana.strftime("%d"))
for i in f:
    opilased.append(i)
print("")
print(f"vastama tuleb: {opilased[jrk]}")

f.close()
#Jukebox
"""
failinimi = input("Palun sisestage failinimi: ")
f = open(failinimi, 'r')
jrk = 1
laulud = []
for i in f:
    print(jrk,".",i,end="")
    laulud.append(i)
    jrk+=1
    
print("")
laul = (int(input("Valige laulu järjekorra number: ")))
print(f"Mängitav muusikapala on:{laulud[laul-1]}")





f.close()

#Sissetulekud
fail = open("konto.txt", encoding="UTF-8")
for i in fail:
    if i>"0":
        print(i, end=" ")

fail.close()

#jänesevanemate mure ver.3
ring = int(input("Sisesta ringide arv: "))
porgand = 0
for i in range(ring+1):
    if i%2 == 0:
        porgand += i
print(f"porgandite koguarv on:{porgand}")
        

#Ülikooli vastuvõetud

fail = open("rebased.txt",encoding="UTF-8")
vastuvõetud = []
aastad = [2011,2012,2013,2014,2015,2016,2017,2018,2019]
for rida in fail:
    vastuvõetud.append(int(rida))
aasta = int(input("Mis aastat tahad? "))
index = aastad.index(aasta)

print(vastuvõetud[index])
fail.close()

#male
nisutera = 0.5
a = int(input("Sisestage täisarv: "))
i = 0
while i < a:
    i += 1
    nisutera*=2
print(nisutera)






#täringud

taringud = int(input("mitu täringut tahad? "))
for i in range(taringud):
    print(random.randint(1,6)) 



#Murelikud lapsevanemad


ringid = int(input("Mitu ringi jooksid"))
ring = 0
porgand = 0
while ring<ringid:
    ring +=1
    if ring %2==0:
        porgand+=ring
print(f"porgandite koguarv on:{porgand}")
        




#Äratus


aratus = int(input("Mitu korda äratus äratab?: "))
for i in range(aratus):
    print("tõuse ja sära")




#bussid

reisiad =  int(input("Mitu inimest on bussis: "))
kohad = int(input("Mitu kohta on bussis: "))
busiiarv = math.ceil(reisiad/kohad)
viimases_bussis = reisiad%kohad
if viimases_bussis==0:
    viimases_bussis=40
print(f"Busse vaja: {busiiarv}")
print(f"Viimasses bussis inimesed: {viimases_bussis}")



#Pilved

pilv = int(input("Sisesta siia pilve kõrgus(km): "))
if pilv>=6:
    print("Need on ülemised pilved")
else:
    print("Need ei ole ülemised pilved")

#Aasta liblikas
aasta = 2020
liblikas = " teelehe-mosaiikiliblikas "
lause_keskosa = " aasta liblikas on "
lause = str(aasta),lause_keskosa,liblikas
print(lause)

#Tervitus
print("Tere, Maailm!")
"""