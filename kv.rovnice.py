import math as m 
print("existuje kv. rovnice : ax2 + bx + c . Tento program vypočítá její kořeny.")
a = int(input("Zadejte číslo 'a' "))
b = int(input("Zadejte číslo 'b' "))
c = int(input("Zadejte číslo 'c'"))
vypocet1 = -b +  m.sqrt(m.pow(b,2) - 4 *a *c)
vypocet1 = -b -  m.sqrt(m.pow(b,2) - 4 *a *c)
vypocet = vypocet1 / 2 *1/a
vypocet2 = vypocet1 / 2 *1/a
print(f"Kořeny jsou {vypocet} a {vypocet2}")