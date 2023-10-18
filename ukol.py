import random
cyklus = True
while cyklus == True: 
    i = random.randint(11, 20)
    for i in range (1, i):
        jmeno = random.choice(["Fanas","Martin", "Ondra", "Maxim", "Jaroslav","Daniel", "Honza", "Danny", "Radim"])
        prijmeni = random.choice(["Krocil", "Balosak", "Skoda", "Stoev", "Herrgott", "Mana", "Dlabaja", "Miklas"])
        cislo_ulice = random.randrange(100, 1000)
        nazvy_ulic = random.choice(["Beach", "Connecticut", "Embassy", "Massachussets", "Green"])
        nazev_mesta = random.choice(["Huntsville AL", "Anchorage AL", "Phoenix AR", "Los Angeles CA", "Atlanta GE"])
        smerovaci_cislo = random.randint(10000, 100000)
        tel_cislo = random.randint(100, 999)
        tel_cislo1 = random.randint(100, 999)
        tel_cislo2 = random.randint(1000, 9999)
        print((jmeno) + " " + (prijmeni))
        print(f"{tel_cislo}-{tel_cislo1}-{tel_cislo2}" )
        print(f"{cislo_ulice} {nazvy_ulic} St., {nazev_mesta} {smerovaci_cislo}")
        print(f"{str(jmeno).lower()}{(prijmeni).lower()}@bogusemail.com")
        print("")
        cyklus = False 
    


