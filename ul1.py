#Artur-Mihk Peterson
#2.11.22
#ulessane 1
import math
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




    