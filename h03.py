#Artur-Mihk Peterson
#11.10.22
#harjutus03

#palindroomi kontrollimine
def isPalindroom(p):
    return p == p[::-1]
 
 

p = input("Kas sõna on palindroom: ")
vastus = isPalindroom(p)
 
if vastus:
    print("Sõna on palindroom")
else:
    print("Sõna ei ole palindroom")


"""
#tundide ajad

algus = "8:30"
lopp = "14:15"

hh1,mm1 = algus.split(":")  #teksti tükeldus
minutid1 = int(hh1)*60+int(mm1) #minuti teisendus
hh2,mm2 = lopp.split(":")
minutid2 = int(hh2)*60+int(mm2)

minutid = minutid2-minutid1
hh = minutid//60 #täisarvuline jagamine
mm = minutid%60 #jääk

print(f"Ajaline vahe on {hh}:{mm}")

#emaili kontroll true/false
email = input("Sisesta emial kontrollimiseks: ")
print("@" in email)


#vandumine - teksti asendamie
v = input("Vannu siia 'Kurat küll!': ")
print(v.lower().replace("kurat","*****"))


#Korralik nimi
nimi = input("Sisesta nimi: ")
puh_nimi = nimi.strip().capitalize()

print("Tere,", puh_nimi+"!")

"""







