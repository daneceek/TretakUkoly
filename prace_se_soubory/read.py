from sys import stdin

with open("myfile.txt", "r") as f:
    znak = f.read(1)
    triznaky = f.read(3)
    radek = f.readline()

    f.seek(0, 1)
    konec = f.read()

    f.seek(0)
    zbytek = f.read()

print(znak, triznaky, radek, konec, zbytek)


# neco = stdin.read()
# print(neco)
