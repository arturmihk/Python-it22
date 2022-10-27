#Artur-Mihk Peterson
#25.10.22
#harjutus05

#Tärnid
numbrid = [12,43,53,11,52,23,69,72,13,32,35]
for i in numbrid:
    print(i*"*")

#Vanused
vanused = [12,43,53,11,52,23,69,72,13,32,35]
print("Vanim",max(vanused))
print("Noorim",min(vanused))
print("Summa",sum(vanused))
print("Keskmine",sum(vanused)/len(vanused))
#Dublikaat

opilased = ["Juhan","Kati","Mario","Mario","Mati","Mati"]
puh_opilased = []
for i in opilased:
    if i in opilased:
        if opilased.count(i) >= 2:
            opilased.remove(i)
    #if i not in puh_opilased:
     #   puh_opilased.append(i)
        
print(opilased)


#Õpilased
jrk = 1
opilased = ["Juhan","Kati","Maarja","Mario","Mati"]
for i in(opilased):
    print(f"{jrk}. {i}")
    jrk+=1
#küsi millist tahab muuta
muut = int(input("Millist nime sa muuta tahad?"))
uusn = input("Milliseks soovite nime muuta?")
opilased.remove(opilased[muut])
opilased.insert(muut, uusn)
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