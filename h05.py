#Artur-Mihk Peterson
#25.10.22
#harjutus05

#Õpilased
jrk = 1
opilased = ["Juhan","Kati","Maarja","Mario","Mati"]
for i in(opilased):
    print(f"{jrk}. {i}")
    jrk+=1
#küsi millist tahab muuta
muut = int(input("Millist nime sa muuta tahad?"))
#ja milleks muudab
opilased.remove(muut)
opilased.insert(muut, input("Milleks tahad muuta :"))
#tee muudatus

print(opilased)
    
#Niimede lisamine loendisse

nimed = []
for i in range(5):
    nimi = input("Lisa nimi loendisse: ")
    nimed.append(nimi)
nimed.sort()
print(nimed)
print(f"viimati lisatud nimi: {nimed[-1]}")