#Artur-Mihk Peterson
#1.11.22
#harjutus09
import locale
import datetime
from datetime import timedelta

#Kuupäeva muundamine

aeg = datetime.datetime.now()
print(aeg.strftime("%d. %B %Y"))

#Isikukoodist sünnip
locale.setlocale(locale.LC_ALL, "et_EE")
aeg = datetime.datetime.now()
print(aeg.strftime("%d. %B %Y"))

ik = "50511190903"
sp = (datetime.date(int("20"+ik[1:3]), int(ik[3:5]), int(ik[5:7])))
print(sp)

print(aeg -timedelta(