from tkinter import *


aken = Tk()
aken.title('Käibemaksukalkulaator')
aken.resizable(0, 0)

#funktsioonid
def arvuta():
    hind = int(float(sisestus.get()))
    kaive = int(float(var.get()))
    kmaks = hind*kaive/100
    kokku = hind+kmaks
    print(hind,kaive,kmaks,kokku)
    km.config(text=str(kmaks)+"€")
    hinds.config(text=str(kokku)+"€")
#sildid
silt = Label(aken, text="Hind käibemaksuta:")
silt.grid(row=0,column=0)

silt = Label(aken, text="Käibemaksumäär:", padx=2, pady=2)
silt.grid(row=4,column=0,sticky="w")

joon = Label(aken, text="_______________________________________________", padx=2, pady=2)
joon.grid(row=6,column=0 ,columnspan=2)

silt = Label(aken, text="Käibemaks:")
silt.grid(row=7,column=0 ,sticky="w")

km = Label(aken, text="0.00€")
km.grid(row=7,column=1 ,sticky="w")

silt = Label(aken, text="Hind käibemaksuta:")
silt.grid(row=8,column=0)

hinds = Label(aken, text="0.00€")
hinds.grid(row=8,column=1, sticky="w")
#sisestusväljad
sisestus = Entry(aken)
sisestus.grid(row=0,column=1)
#nuppp
nupp1 = Button(aken, text="OK", width=10, command=arvuta)
nupp1.grid(row=9, column=1, sticky="e")

#valikukast
var = IntVar()
valikukast = Radiobutton(aken,text="9%", variable=var, value=9,)
valikukast.grid(row=4,column=1,sticky="w")

valikukast = Radiobutton(aken,text="20%", variable=var, value=20,)
valikukast.grid(row=5,column=1,sticky="w")
aken.mainloop()

