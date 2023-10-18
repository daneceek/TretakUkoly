import random
body = 0
data = [
    {
        'name': 'Instagram',
        'follower_count': 501,
        'description': 'Sociální platforma',
        'country': 'USA'
    },
    {
        'name': 'Facebook',
        'follower_count': 4,
        'description': 'Sociální platforma',
        'country': 'USA'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 436,
        'description': 'Fotbalový hráč',
        'country': 'Portugal'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 161,
        'description': 'Herec a wrestler',
        'country': 'USA'
    },
    {
        'name': 'Harry Potter film',
        'follower_count': 8,
        'description': 'Film',
        'country': 'USA'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 307,
        'description': 'Podnikatelka',
        'country': 'USA'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 324,
        'description': 'Fotbalista',
        'country': 'Argentina'
    },
    {
        'name': 'Neymar',
        'follower_count': 158,
        'description': 'Fotbalista',
        'country': 'Brazilie'
    },
    {
        'name': 'Eminem',
        'follower_count': 40,
        'description': 'Hudebník',
        'country': 'USA'
    },
    {
        'name': 'Justin Bieber',
        'follower_count': 193,
        'description': 'Hudebník',
        'country': 'Canada'
    },
    {
        'name': 'Emma Watson',
        'follower_count': 111,
        'description': 'Herečka',
        'country': 'Francie'
    }
]

def random_generace_cisla_A():
    global cisloA
    cisloA = random.randint(0,10)
def random_generace_cisla_B():
    global cisloB
    cisloB = random.randint(0, 10)
    if cisloA == cisloB :
        random_generace_cisla_A()
        random_generace_cisla_B()
def vybirani_otazky_A(data, cisloA):
    return f"Porovnejte A: {data[cisloA]['name']}, {data[cisloA]['description']}, z {data[cisloA]['country']}"
def vybirani_otazky_B(data, cisloB):
    return f"Porovnejte B: {data[cisloB]['name']}, {data[cisloB]['description']}, z {data[cisloB]['country']}"
def spravna_odpoved():
    A = {data[cisloA]['follower_count']}
    B = {data[cisloB]['follower_count']}
    for i in A:
        A = int(i)
    for i in B:
        B = int(i)
    if A > B:
        return "A"
    else:
        return "B"
def rozhodnuti():
    rozhodnuti = input("Kdo má více sledujícíh na instagramu? ")
    if rozhodnuti == spravna_odpoved():
        global body
        print("Získáváš bod")
        body += 1
        print(f"Nyní máš {body} bodů")
        dalsi_hra()
    else:
        print("Prohrál jsi!")
        print(f"Celkově jsi získal {body} bodů")
        exit()

def dalsi_hra():
    if spravna_odpoved() == "A":
        print(vybirani_otazky_A(data, cisloA))
        random_generace_cisla_B()
        if cisloA == cisloB :
            random_generace_cisla_A()
            random_generace_cisla_B()
        print(vybirani_otazky_B(data, cisloB))
        rozhodnuti()
        spravna_odpoved()
    else:
        random_generace_cisla_A()
        if cisloA == cisloB :
            random_generace_cisla_A()
            random_generace_cisla_B()
        print(vybirani_otazky_A(data, cisloA))
        print(vybirani_otazky_B(data, cisloB))
        spravna_odpoved()
        rozhodnuti()
random_generace_cisla_A()
random_generace_cisla_B()
print(vybirani_otazky_A(data, cisloA))
print(vybirani_otazky_B(data, cisloB))
spravna_odpoved()
rozhodnuti()

































































