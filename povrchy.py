import math as m
polomer = int(input("Zadejte poloměr koule, tento program vypočítá její objem a povrch\n"))
povrch = m.pow(polomer,2) * 4 * m.pi
objem = polomer * m.pi * 4/3
print(f"Povrch koule je {povrch } a objem {objem}")