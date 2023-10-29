from sys import stdout, stderr
from os import path

stdout.write(path.dirname(__file__))
adr = path.dirname(__file__)

file_haldler = open(adr + "/myfile.txt", "w", -1 , "utf-8")


file_haldler.write("Halo Word!\n")
file_haldler.write("Ahoj miláčku!\n")

file_haldler.flush()
file_haldler.close()

with open("yourfile.txt", "a") as file_haldler:
    c = ord("a")
    while chr(c) != "z":
        file_haldler.write(chr(c))
        c += 1


stdout.write("KOnec\n")
