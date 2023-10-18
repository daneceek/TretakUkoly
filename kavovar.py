import source_data

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 40,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 60,
    }
}
 
resources = {
    "water": 400,
    "milk": 300,
    "coffee": 150,
}



##########################################################################################x
def vhazovac_minci():
    cost = kolik_stoji(choice)
    for value in resources.values():
        if value <= 0:
            print("Na váš nápoj nemáme dostatek ingrediencí.")
            exit()
    celkove_vlozeno = 0
    def zaplaceno(celkove_vlozeno):
        mince = [1, 2, 5, 10, 20, 50]
        print(f"Cena vybraného nápoje je {cost} Kč.")
        print("Prosím, vložte mince 1, 2, 5, 10, 20, 50") 
        for coin in mince:
            vhozena_castka = int(input(f"Kolik {coin} Kč chcete vložit?: "))
            total = coin * vhozena_castka
            celkove_vlozeno += total
        return celkove_vlozeno
    suma = zaplaceno(celkove_vlozeno)
    if suma >= cost:
        print(f"Celkem jste vložili {suma} Kč.")
        print(f"Cena vybraného nápoje je {cost} Kč.")
        print("nápoj se připravuje.")
        vracene_penize = suma - cost
        print(f"Zde jsou peníze zpět : {vracene_penize}")
        kavovar(resources, MENU)
    else:
        print("nezaplatil jste celou částku!")
        print(zaplaceno(celkove_vlozeno))  



def kavovar(resources, MENU):
    global choice
    choice = input("Co byste si dal? (espresso, latte, cappuccino): ")
    if choice == "report":
        for resource, howmuch in resources.items():
            print(resource, ":", howmuch) 
        kavovar(resources, MENU)
    elif choice == "espresso":
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        resources["milk"] -= MENU["espresso"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
        vhazovac_minci()
    elif choice == "latte":
        resources["water"] -= MENU["latte"]["ingredients"]["water"]
        resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
        vhazovac_minci()
    elif choice == "cappuccino":
        resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
        vhazovac_minci()
def kolik_stoji(choice):
    cost = MENU[choice]["cost"]
    return cost


kavovar(resources, MENU)