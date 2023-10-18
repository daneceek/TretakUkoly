import random
zaklad = 1
cislo = 2 
zivoty = 5 
spravna_odpoved  = random.randint(zaklad, cislo)
print("Máš 5 životů")
while True :

    hadani = int(input(f"Zkus uhodnout číslo v rozmezí od 1 do {cislo}!\n"))        
    if (hadani > cislo) or (hadani < zaklad):
        print("Nemůžeš hádat jiná čísla než která jsou v zadaném intervalu!")
        
    elif hadani < spravna_odpoved:
        zivoty -= 1
        if zivoty == 0:
            print(f"Konec hry, máš 0 životů. Správné číslo bylo {spravna_odpoved}")
            break 
        print("Zkus to znovu, napovím že to číslo je vyšší než které jsi právě zadal. ")

    elif hadani > spravna_odpoved:
        zivoty -= 1 
        if zivoty == 0:
            print("Konec hry, máš 0 životů")
            break
        print("Zkus to znovu, napovím že to číslo je nižší než které jsi právě zadal. ")
        
        
    elif spravna_odpoved == hadani:
        print("Výborně, uhodl jsi!")
        cislo += 1
        spravna_odpoved  = random.randint(zaklad, cislo)


    
    



