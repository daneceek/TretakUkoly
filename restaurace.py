velikost = input("Jakou chcete velikost pizzy?")
cena = 0
if velikost == "S":
    cena = 100
elif velikost == "M":
    cena = 150
elif velikost == "L":
    cena = 200  
feferonky = input("Chcete k pizze feferonky?")
if feferonky == "ano" and velikost == "S":
    cena = cena + 20
elif feferonky == "ano" and velikost == "M" :
    cena = cena + 30
elif feferonky == "ano" and velikost == "L" :
    cena = cena + 30
syr = input("Chcete ještě sýr navíc?")
if syr == "ano":
    cena = cena + 15

print(f"Vaše výsledná cena je {cena} Kč")