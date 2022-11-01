#Artur-Mihk Peterson
#1.11.22
#harjutus07

import math

#Kujundite ruumala
print("***************** Leiame Ruumala *****************")
loop = 1

def kuup (a):
    print(f"Kuubi ruumala on {a**3}")
def kera (a):
    print(f"Kera ruumala on {round(a**3*math.pi*4/3,2)}")
def koonus (a,b):
    print(f"Koonuse ruumala on {round(a**2*math.pi*b/3,2)}")
def silinder(a,b):
    print(f"Koonuse ruumala on {round(a**2*math.pi*b,2)}")
while loop==1:
    print("Vali kujund: \n1 Kuup \n2 Kera \n3 Koonus \n4 Silinder")
    kujund = int(input("Lisa kujundi number 1-4: "))
    if kujund==1:
        x = int(input("Sisesta kuubi külje pikkus: "))
        kuup(x)
    elif kujund==2:
        y = int(input("Sisesta kera raadius: "))
        kera(y)
    elif kujund==3:
        r = int(input("Sisesta koonuse raadius: "))
        h = int(input("Sisesta koonuse kõrgus: "))
        koonus(r,h)
    elif kujund==4:
        r = int(input("Sisesta silindri raadius: "))
        h = int(input("Sisesta silindri kõrgus: "))
        silinder(r,h)
    else:
        print("Sisestasite vale arvu, sisestage palun 1-4")


#oma funktsiooni loomine parameetritega

def tervita(a="none", b="ge"):
    if b=="et":
        print(f"Tere {a}")
    elif b=="en":
        print(f"Hi {a}")
    else:
        print(f"Hallo {a}")
#funktsiooni välja kutsumine
tervita("Artur","et")
tervita("Mario","en")
tervita("Karl")
