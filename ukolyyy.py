# def absolutni_hodnota(number):
#         if number >= 0:
#                 return number
#         else:
#             number *= -1
#             return number 



# vysledek = absolutni_hodnota(-12)
# print(vysledek)


# def nejvetsi2(cislo1, cislo2):
#         seznam = []
#         seznam.append(cislo1)
#         seznam.append(cislo2)
#         seznam.sort()
#         return seznam[-1]


# vysledek = nejvetsi2(8, 17)
# print(vysledek)


# def nejvetsi2(cislo1, cislo2, cislo3):
#         seznam = []
#         seznam.append(cislo1)
#         seznam.append(cislo2)
#         seznam.append(cislo3)
#         seznam.sort()
#         return seznam[-1]


# vysledek = nejvetsi2(8, 17, 25)
# print(vysledek)

# def nejvetsi(seznam):
#     seznam.sort()
#     return seznam[-1]

# vysledek = nejvetsi([1, 9, 3, 4, 6, 5, 9, 8, 5, 6 ])
# print(vysledek)



# def nejdelsi_string(string1, string2):
#     if len(string1) > len(string2):
#         return string1
#     else:
#         return string2

# vysledek = nejdelsi_string("pes", "veverka")
# print ("nejdelsi slovo je: " + vysledek)


def spoj_stringy(string, symbol):
    veta = []
    for i in string:
        retezec = i + symbol
        veta.append(retezec)
    print(len(veta))

texty = ["ahoj", "jak", "se", "vede"]
print( spoj_stringy(texty, " °-_-> ") )
