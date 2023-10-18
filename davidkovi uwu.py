tuple_vybiracek = ("1", "2", "3")
validni_cislo = validni_jmeno = 0
kontakty = {}
def pridavani():
    validni_cislo = validni_jmeno = 0
    while validni_jmeno == 0:
        validni_jmeno = 1
        jmeno = input("Vyber jmeno: ").strip()
        if jmeno == "":
            print("Je nutno zadat nějaký údaj!")
            validni_jmeno = 0
    while validni_cislo == 0:
        validni_cislo = 1
        try:
            cislo = int(input("Vyber tel. číslo: ").replace(" ", ""))
        except ValueError:
            print("Je nutno zadat číselný údaj!")
            validni_cislo = 0
    return jmeno, cislo
while True:
    propustka = 0
    while propustka == 0:    
        print("1. Přidat kontakt\n2. Odebrat kontakt\n3. Zobrazit kontakty")
        vybiracek = input("")
        if vybiracek in tuple_vybiracek:
            propustka = 1
        else:
            print("Zadána špatná hodnota!")
    if vybiracek == "1":
        funkce_jmeno, funkce_cislo = pridavani()
        kontakty[funkce_jmeno] = funkce_cislo
    elif vybiracek == "2":
        registrovana_cisla = []
        print("0. zpět")
        x = 0
        for i in kontakty.keys():
            x = x + 1
            print(f"{x}. {i}")
            registrovana_cisla.append(x)
        try:
            vybiracek = int(input(""))
        except ValueError:
            print("Zadána špatná hodnota!")
        if vybiracek == 0:
            pass
        elif vybiracek not in registrovana_cisla:
            print("Zadána špatná hodnota!")
        else:
            seznamek = []
            for i in kontakty.keys():
                seznamek.append(i)
            spravny_klic = seznamek[vybiracek-1]
            print(seznamek[vybiracek-1])
            del kontakty[spravny_klic]
    else:
        x=0
        for key, value in kontakty.items():
            x=x+1
            print(f"{x}. Jméno: {key} Číslo: {value}")