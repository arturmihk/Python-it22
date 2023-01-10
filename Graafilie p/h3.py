from tkinter import *

#akna seaded
aken = Tk()
aken.resizable(0, 0)
aken.title("Artur-Mihk Peterson")
aken.configure(background='black')
aken.iconbitmap('favicon.ico')

tekst = Label(aken, bg="red", text="Nimi: Artur-Mihk Peterson\nRühm: IT-22\n2023", font="Tahoma 16 bold italic", fg="blue", padx=20, pady=20)
tekst.pack()


aken.mainloop()