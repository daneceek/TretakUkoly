vek = input("Zadejte váš věk:\n")
roky = 90 - int(vek)
mesice = roky * 12
tydny = roky * 52
dny = roky * 365
print(f"Zbývá vám {roky} roků, {mesice} měsíců, {tydny} týdnů a {dny} dnů")