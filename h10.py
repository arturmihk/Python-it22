#Artur-Mihk Peterson
#2.11.22
#harjutus10
import re

#kuva failist korralikud IPd
fh = open("paroolid_ipd.txt")
for line in fh:
    if re.search("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", line):
        print(line,end="")


#Kuva korralikult parooli

fh = open("paroolid_ipd.txt")
for line in fh:
    if re.search("^[A-Z0-9]+[A-Z]{1}", line):
        print(line,end="")