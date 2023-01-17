#Artur-Mihk Peterson
#17.01.2023
#tkinter töö

from tkinter import *


aken = Tk()
aken.title('Käibemaksukalkulaator')
aken.resizable(0,0)



def banner():
    #reklaam=reklaam.upper()
    #return reklaam
    kordaja = int(sisestus.get())
    lause = str(sisestuslause.get())
    print(kordaja)
    print(lause)
    silt.config(text=(lause))
    

        
    
    
#sildid
siltrk = Label(aken, text="Mitu korda soovite reklaamlasuset kuvada?")
siltrk.grid(row=0,column=0)

siltrl = Label(aken, text="Sisestage reklaamlause:")
siltrl.grid(row=1,column=0, sticky="w")

silt = Label(aken, text="tere")
silt.grid(row=4, column=0, sticky="w")

#Sisestused
sisestus = Entry(aken)
sisestus.grid(row=0,column=1,columnspan=2)
sisestuslause = Entry(aken)
sisestuslause.grid(row=1,column=1,columnspan=2,)

#Nupp
nupp1 = Button(aken, text="OK", width=10,command=banner)
nupp1.grid(row=3, column=2, sticky="e")


"""
#Bänner
def banner(reklaam):
    reklaam=reklaam.upper()
    return reklaam
korda = int(input("Mitu korda soovite reklaamlauset kuvada?"))
teade = input("Sisestage reklaamlasue: ")
for i in range (korda):
    print(banner(teade))
"""
aken.mainloop()