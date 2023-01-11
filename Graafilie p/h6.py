from tkinter import *
import time

#akna seaded
aken = Tk()
aken.title('Animatsioon')
aken.iconbitmap('favicon.ico')

#lõuendi loomine
louend = Canvas(aken, width=250, height=250)
louend.pack()
louend.create_rectangle(9, 9, 220, 170,)
louend.create_rectangle(10, 10, 80, 80, fill="red3", outline="")
louend.create_rectangle(10, 100, 80, 170, fill="red3", outline="")

louend.create_rectangle(100, 10, 220, 80, fill="red3", outline="")
louend.create_rectangle(100, 100, 220, 170, fill="red3", outline="")

aken.mainloop()