#Artur-Mihk Peterson
#17.10.22
#harjutus04
import random


#Ruutude kuupide tabel
arv = 1
for i in range (1,11):
    print(arv, end=" ")
    print(arv**2, end=" ")
    print(arv**3, end=" ")
    print()
    arv+=1
    


#Pank

raha = 10000
intress = 0.05
aastad = 5
kasv = 0

for i in range (1,aastad+1):
    print(f"{i} {round(raha,2)} {round(intress*raha,2)} {round(raha+raha*intress,2)} ")
    raha = raha+raha*intress
raha_kokku = print("Summa kokku:",round(raha,2))
kasum = print("Kasum:",round(raha-10000,2))


#arvamismäng
nr = random.randint(1,101)
loop = 1
kordade_arv = 0

print("Arva ära number 1-100")

while loop == 1:
    arva = int(input("Sisesta täisarv: "))
    
    if arva == nr:
        kordade_arv += 1
        if kordade_arv<=3:
            print("Tubli, pakkumisi kokku: ",kordade_arv)
        if kordade_arv >=4:
            print("pakkumisi kokku: ", kordade_arv,)
        loop = 0
    elif arva < nr:
        kordade_arv += 1
        print("Sinu pakkumine on liiga väike")
    else:
        kordade_arv += 1
        print("Sinu pakkumine on liiga suur")
"""
#viisikud
for i in range (1,101):
    if i%5==0:
        print(i)

#korrutus tabel viiega
korrutatav = 5
for i in range (1,11):
    print(f"{korrutatav} x {i} = {korrutatav*i}")



#paaris ja paaritu
"""
"""
for i in range(1,101):
    if i%2==0:
        print(f"arv {i} on paaris ")
    else:
        print(f"arv {i} on paaritu")



#loto
for i in range (5):
    print(random.randint(0,9),end="")
print()
#Tärnid
"""
"""
for i in range (5):
    print("* "*5)

kasv=1
for i in range (5):
    print("* "*kasv)
    kasv+=1

kaha=5
for i in range (5):
    print("* "*kaha)
    kaha-=1




#Jalgpalli meeskond
sugu = input("Sisesta sugu m/n: ")
if sugu=="m":
    vanus = int(input("Sisesta siia oma vanus: "))
    if 16<=vanus<=18:
        print("Oled sobilik jalka meeskonda")
    elif vanus<16:
        print("Sa oled liiga noor proovi kunagi elif vanus<16")
    elif vanus>18:
        print("Kao ära siit vanur raisk")
    else:
        print("Kao ära")
else:
    print("Sa ei saa jalgpalli tiimi sa oled naine")
"""


"""
#müük
toode = int(input("Sisesta toote hind :"))
if toode<=10:
    print("Saad 10% allahindlust")
else:
    print("Saad 20% allahindlust")


#Juubel
sunnip = (input("Sisesta siia oma sünnipäev: "))
dd,mm,yy= sunnip.split(".")
print(yy)
aasta = 2022-int(yy)
jaak = aasta%5
if jaak==0:
    print("Sul on juubel")
else:
    print("Sul ei ole juubel")
"""



'''
#matem
arv1 = int(input("Sisesta arv1: "))
arv2 = int(input("Sisesta arv2: "))
tehe = input("Vali tehe (* / + -): ")
if tehe=="*":
    vastus = arv1*arv2
elif tehe=="/":
    vastus = arv1/arv2
elif tehe=="+":
    vastus = arv1+arv2
elif tehe=="-":
    vastus = arv1-arv2

else:
    vastus = n/a
"""
Mariole meeldib trollida vanaisaga ja vanaemaga
"""
print(f"{arv1}{tehe}{arv2}={vastus}")
print("--------------")





#kas on ruut
a = int(input("Sisesta külg 1: "))
b = int(input("Sisesta külg 2: "))
if a==b:
    print(f"{a} ja {b} moodustavad ruudu")
else:
    print(f"{a} ja {b} moodustacad ristküliku")
'''



