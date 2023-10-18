import random


friendly_postavy = {"Draven":
           {"životy": 100,
            "útok": 35,
            "obratnost": 5,
            "obrana": 25}, 
           "Arintheus":{
            "životy": 90,
            "útok": 20,
            "obratnost": 15, 
           "obrana": 20}, 
           "Freyja":{
            "životy": 75,
            "útok": 25,
            "obratnost": 25,
            "obrana": 15
           }}


enemy = {"Drakul":
         {"životy": 60,
            "útok": 20,
            "obratnost": 15,
            "obrana": 30}, 
            "Barlog":
            {
            "životy": 70,
            "útok": 30,
            "obratnost": 10,
            "obrana": 20},
            "Morgath":
            {
            "životy": 110,
            "útok": 15,
            "obratnost": 20,
            "obrana": 15
            }}


def pridavani_hrdinu(friendly_postavy, enemy):
    global charakteristika
    name = input("Zadejte jméno nového hrdiny (string): ")
    lives = int(input("Zadejte životy nového hrdiny (integer): "))
    attack = int(input("Zadejte hodnotu útoku nového hrdiny (integer): "))
    agility  = int(input("Zadejte hodnotu obratnosti nového hrdiny (integer): "))
    defense = int(input("Zadejte hodnotu obrany nového hrdiny (integer): "))
    charakteristika = input("Chcete k novému hrdinovi napsat krátký popisek (string)? Jestli ano, napište jej, pokud ne zmáčkněte (2)\n")
    if charakteristika == "2":
        charakteristika = ()
    friendly_or_enemy = input("chcete hrdinu přidat do seznamu přátelských hrdinů (1), nebo nepřátelských (2)?\n")
    if friendly_or_enemy == "1":
        friendly_postavy.update({name.title() : {"životy" : lives, "útok": attack, "obratnost":agility, "obrana":defense} })
        print("Přidáno")
        print("Nyní se vraťme zpět do výběru akcí. Chcete hrát (1), nebo ještě přidat hrdinu (2)?")
        vyber_modu()
    elif friendly_or_enemy == "2":
        enemy.update({name.title() : {"životy" : lives, "útok": attack, "obratnost":agility, "obrana":defense} })
        print("Přidáno")
        print("Nyní se vraťme zpět do výběru akcí. Chcete hrát (1), nebo ještě přidat hrdinu (2)?")
        vyber_modu()
def hra():
  print("Vítejte ve hře Magic Duel! Ve zkratce je to hra, ve které proti sobě bojují dva hrdinové.")
  print()
  print("Nejdříve si ale vyberte, jestli chcete hrát (1) nebo do hry přidat nové hrdiny (2)")
  vyber_modu()
def vyber_modu():
    choice = input()
    if choice == "1":
        vyber_hrdinu(friendly_postavy)
    elif choice == "2":
        pridavani_hrdinu(friendly_postavy, enemy)

def vyber_hrdinu(friendly_postavy):
    global hero_choice
    print("dostupní hrdinové:")
    for hero in friendly_postavy:
        print(hero)
        print("﹋﹋﹋﹋﹋﹋")
    hero_choice = input("Napište sem jméno zvoleného hrdiny a hra vám k němu vypíše podrobnosti. (stačí malými písmeny)\nVýběr: ")
    if hero_choice.title() in friendly_postavy:
        charakteristika_hrdiny(hero_choice) 
    else:
        hero_choice = ()
        return vyber_hrdinu(friendly_postavy)
def charakteristika_hrdiny(hero_choice):
    hero_choice = hero_choice.title()
    if hero_choice == "Draven":
        print()
        print(f"Vybrali jste si hrdinu {hero_choice}.")
        print("Popis:")
        print("Draven je válečný hrdina, který se nebojí ničeho. Je to rváč a s ničím se nepáře. Jen není moc obratný.")
        print()
    elif hero_choice == "Arintheus":
        print()
        print(f"Vybrali jste si hrdinu {hero_choice}.")
        print("Popis:")
        print("Arintheus je zdatný, obratný hrdina. Rád se nepozorovaně přiblíží zezadu a zabíjí.")
        print()
    elif hero_choice == "Freyja":
        print()
        print("Popis")
        print(f"Vybrali jste si hrdinu {hero_choice}.")
        print("Freyja je dívka, která ráda střílí z luku a zasahuje nepřátele.")
        print()
    else:
        print()
        print(f"Vybrali jste si hrdinu {hero_choice}.")
        print("Popis")
        print(charakteristika)
        print()
    print("STATISTIKY")
    print()
    print(f"životy: {friendly_postavy[hero_choice]['životy']}")
    print(f"útok: {friendly_postavy[hero_choice]['útok']}")
    print(f"obratnost: {friendly_postavy[hero_choice]['obratnost']}")
    print(f"obrana: {friendly_postavy[hero_choice]['obrana']}")
    print()
    hero_confirm = input("chcete potvrdit výběr hrdiny? Ano - 1 | Ne - 2\n")
    if hero_confirm == "1":
        print(f"VÁŠ HRDINA: {hero_choice}")
        vyber_opponenta(enemy)
    else:
        return vyber_hrdinu(friendly_postavy)
def vyber_opponenta(enemy):
    global enemy_choice
    print("﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋")
    print("Nyní je čas si vybrat svého soupeře. Na výběr máme pár možností:")
    print()
    for enemy_hero in enemy:
        print(enemy_hero)
        print("﹋﹋﹋﹋﹋﹋")
    enemy_choice = input("Napište sem jméno zvoleného hrdiny a hra vám k němu vypíše podrobnosti. (stačí malými písmeny)\nVýběr: ")
    if enemy_choice.title() in enemy:
        charakteristika_enemy(enemy_choice)
    else:
        enemy_choice  = ()
        return vyber_opponenta(enemy)
def charakteristika_enemy(enemy_choice):
    enemy_choice = enemy_choice.title()
    if enemy_choice == "Drakul":
        print(f"Vybrali jste si soupeře {enemy_choice}.")
        print("Drakul je hrdina, jehož hlavní předností je obrana. Má na sobě totiž odolné brnění, které jej chrání.")
        print()
    elif enemy_choice == "Barlog":
        print(f"Vybrali jste si soupeře {enemy_choice}.")
        print("Barlog je hrdina, který dovede rozhodně překvapit svou útočnou silou. Zato jeho životy nestojí za mnoho řečí.")
        print()
    elif enemy_choice == "Morgath":
        print(f"Vybrali jste si soupeře {enemy_choice}.")
        print("Morgath je velmi vitální hrdina. Zato jeho útok není nic moc. Ale i tak dovede nadělat paseku.")
        print() 
    else:
        print()
        print(f"Vybrali jste si hrdinu {enemy_choice}.")
        print(charakteristika)
        print("Popis:")
        print(charakteristika)
        print()
    print("STATISTIKY")
    print()
    print(f"životy: {enemy[enemy_choice]['životy']}")
    print(f"útok: {enemy[enemy_choice]['útok']}")
    print(f"obratnost: {enemy[enemy_choice]['obratnost']}")
    print(f"obrana: {enemy[enemy_choice]['obrana']}")
    print()
    enemy_cofirm = input("chcete potvrdit výběr hrdiny? Ano - 1 | Ne - 2\n")
    if enemy_cofirm == "1":
        print(f"SOUPEŘ: {enemy_choice}")
        boj(enemy_choice, hero_choice,friendly_postavy, enemy)

    else:
        return vyber_opponenta(enemy)
def boj(enemy_choice, hero_choice, friendly_postavy, enemy):
    global statistiky_friendly_hrdiny
    global statistiky_enemy_hrdiny
    hero_choice = hero_choice.title()
    enemy_choice = enemy_choice.title()
    statistiky_friendly_hrdiny = friendly_postavy[hero_choice]
    statistiky_enemy_hrdiny = enemy[enemy_choice]
    print("﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋")
    print(f"STATISTIKY HRDINY ({hero_choice}):")
    print()
    for hero_schopnost, hero_cislo in statistiky_friendly_hrdiny.items():
        print(hero_schopnost,":", hero_cislo)
    print()
    print(f"STATISTIKY PROTIVNÍKA ({enemy_choice}):")
    for enemy_schopnost, enemy_cislo in statistiky_enemy_hrdiny.items():
        print(enemy_schopnost,":", enemy_cislo)
    print()
    print("﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋")
    input("Nyní přejděme k fázi boje.\n\nInfo:\n\nČím vyšší je obratnost hrdiny, tím nižší má soupeř šanci trefit svůj útok.\nObrana je snížení útoku protivníka, čím vyšší, tím vyšší je šance na odkrytí soupeřova útoku.\n\nPro zahájení boje zmáčkněte jakoukoliv klávesu\n")
    print("﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋")
    print(f"{hero_choice} VS {enemy_choice}")
    print()
    print("﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋")
    while True:
        utok_hrdiny(statistiky_friendly_hrdiny, statistiky_enemy_hrdiny, hero_choice, enemy_choice)
        utok_enemy(statistiky_friendly_hrdiny, statistiky_enemy_hrdiny, hero_choice, enemy_choice)
        print("﹋﹋﹋﹋﹋﹋")
        print(f"Životy hrdiny ({hero_choice}) : {statistiky_friendly_hrdiny['životy']}")
        print(f"Životy protivníka ({enemy_choice}): {statistiky_enemy_hrdiny['životy']}")
        print("﹋﹋﹋﹋﹋﹋")
        input("Zmáčkněte libovolné tlačítko pro zahájení dalšího kola.\n")
def utok_hrdiny(statistiky_friendly_hrdiny, statistiky_enemy_hrdiny, hero_choice, enemy_choice):
    print("Útok hrdiny:") 
    print()
    miss_needed_number = 50
    miss_number = random.randint(0, 50)
    if miss_number + statistiky_enemy_hrdiny["obratnost"] >= miss_needed_number:
        print(f"Hrdina {hero_choice} netrefil svůj útok.")
        print("﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋")
    else:
        hrdina_damage = random.randint(0, statistiky_friendly_hrdiny["útok"])
        enemy_protection = random.randint(0, statistiky_enemy_hrdiny["obrana"])
        final_hrdina_damage = hrdina_damage - enemy_protection
        if final_hrdina_damage <= 0:
            print(f"Obrana soupeře {enemy_choice} vykryla útok hrdiny {hero_choice}.")
            print("﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋")
        else:
            statistiky_enemy_hrdiny["životy"] -= final_hrdina_damage
            print(f"Hrdina {hero_choice} zasáhl proivníka {enemy_choice} a sebral mu "+ str(final_hrdina_damage), "životů.")
            print("﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋")
            if statistiky_enemy_hrdiny["životy"] <= 0:
                print()
                print(f"Hrdina {hero_choice} vyhrál nad protivníkem {enemy_choice}.")
                exit()
def utok_enemy(statistiky_friendly_hrdiny, statistiky_enemy_hrdiny, hero_choice, enemy_choice):
    print("Útok protivníka:") 
    print()
    enemy_damage = random.randint(0, statistiky_enemy_hrdiny["útok"])
    hero_protection = random.randint(0, statistiky_friendly_hrdiny["obrana"])
    final_enemy_damage = enemy_damage - hero_protection
    if final_enemy_damage <= 0:
            print(f"Obrana hrdiny {hero_choice} vykryla útok hrdiny {enemy_choice}.")
            print("﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋")
    else:
        statistiky_friendly_hrdiny["životy"] -= final_enemy_damage
        print(f"Soupeř {enemy_choice} zasáhl hrdinu {hero_choice } a sebral mu "+ str(final_enemy_damage), "životů.")
        print("﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋")
        if statistiky_friendly_hrdiny["životy"] <= 0:
            print()
            print(f"Protivník {enemy_choice} vyhrál nad hrdinou {hero_choice}.")
            exit()
hra()