import unicodedata
from sys import stdin, stdout, stderr, argv
import os
from string import ascii_uppercase
print(argv) # cesta k tomuto souboru

if len(argv) > 1: 
    filename = argv[1] # pokud existuje, tak se vybere 
    if os.path.isfile(filename):
        stdin = open(filename, "r") 
  
pocet = {}
for znak in ascii_uppercase:
    pocet[znak] = 0

# text = input("zadej text >")
# text = stdin.read()

"""
for znak in text:
    if znak in pocet:
        pocet[znak] += 1
    else:
        pocet[znak] = 1
"""

celkem = 0
while True:
    znak = stdin.read(1) # čtení toho co napíšeme po jednom písmenu
    if znak == "":
        break
    celkem += 1
    znak = unicodedata.normalize("NFKD", znak).encode("ascii", "ignore").decode("ascii")
    znak = znak.upper()  # každý znak se převede na velké písmeno
    if znak in pocet:
        pocet[znak] += 1

print()


def sum(seznam):
    dohromady = 0
    for i in seznam:
        dohromady += i
    return dohromady


def max(seznam):
    nej = -9999999999
    for i in seznam:
        if i > nej:
            nej = i
    return nej


celkem = sum(pocet.values())
nejveci = max(pocet.values())
for k, p in pocet.items():
    print(f"{k}: {p:7d} {pocet[k] / celkem * 100:5.1f}% |{50*p//nejveci*'#'}")
