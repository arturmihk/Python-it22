#Artur-Mihk Peterson
#11.10.22
#harjutus02
import math

#Kütusekulu arvutamine
tank = int(input("Mitu L tankisid:"))
labi = int(input("Mitu km läbisid:"))
kulu = tank/labi*100
print("Kütuse kulu on",kulu,"L 100km kohta")





#Arvusüsteemid
ta = int(input("Sisesta täisarv:"))

print("2ndsysteemis:", bin(b))
print("16ndsysteemis", hex(b))





#Ajasisestus
aeg = int(input("Sisesta siia minutid:"))
tunnid = aeg//60
minutid = aeg%60
print("Vastus:",tunnid,":",minutid)

#Kolmunrga hüpotenuus

a,b = 16,9
hs = math.sqrt(pow(a,2)+ b**2)
print("kolmnurga hüpotenuus on",hs)



#Rulluisutajad
keskk = 29.9
aeg = 24
kaugus = round((keskk*aeg)/60,2)
print("Rulluisutajad jõuavad",kaugus,"km kaugusele")


#Pitsa
pitsa = 12.90
sõbrad = 3
joot = 0.1
maks = (pitsa+pitsa*joot)/3
print(sõbrad,"Sõpra peavead maksma",maks,"eurot")

#toote hind
hind = 36.75
ale = 0.4
kogus = 3
summa = round((hind-hind*ale)*3,2)
print(kogus, "toote summa on",summa,"eurot")

#kolmnurga ümbermõõt
a,b,c = 5,5,5
p = a + b + c
print("Kolmnurga ümbermõõt on see: ", p)