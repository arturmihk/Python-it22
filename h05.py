#Artur-Mihk Peterson
#25.10.22
#harjutus05

#Korduste eemaldamine
opilased = ["Juhan","Kati","Mario","Mario","Mati","Mati"]



#Õpilased
jrk = 1
opilased = ["Juhan","Kati","Maarja","Mario","Mati"]
for i in(opilased):
    print(f"{jrk}. {i}")
    jrk+=1
#küsi millist tahab muuta
muut = int(input("Mitmendat nime sa muuta tahad?"))
uusn = input("Milliseks soovite nime muuta?")
opilased.remove(opilased[muut])
opilased.insert(muut, uusn)


print(opilased)
    
#Niimede lisamine loendisse

nimed = []
for i in range(5):
    nimi = input("Lisa nimi loendisse: ")
    nimed.append(nimi)
nimed.sort()

print(nimed)
print(f"viimati lisatud nimi: {nimed[-1]}")