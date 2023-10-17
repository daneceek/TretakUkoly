# from math import*
# vyska = int(input("Zadejte výšku zdi v metrech: "))
# sirka = int(input("Zadejte šířku zdi v metrech: "))
# def kolik_plechovek(vyska, sirka):
#         celkova_plocha = vyska * sirka
#         plechovka = 5
#         pocet_plechovek = celkova_plocha / plechovka
#         if celkova_plocha % plechovka != 0:
#                 pocet_plechovek += 1
#                 pocet_plechovek = floor(pocet_plechovek)
#                 return pocet_plechovek
#         else:
#             pocet_plechovek = floor(pocet_plechovek)
#             return pocet_plechovek

        


# print(f"Potřebný počet plechovek bude {kolik_plechovek(vyska, sirka)}.")


#cislo = int(input("zadej číslo a já ti řeknu jestli je prvočíslo: "))

# def je_prvocislo(number):
#     for i in range(2, cislo):
#         if cislo % i == 0:
#             return "není"
#     else:
#         return "je"
    

# while True:
#     print(f"Dané číslo {je_prvocislo(number = cislo)} prvočíslo")
#     break


# travel_diary = []
# def add_country():
#     info = {}
#     cities = []
#     country = input("what's your country?\n")
#     print("type your visited cities, if you want to exit, type exit")
#     while True:
#         visited_cities = input()
#         if visited_cities == "exit":
#             break
#         else:
#             cities.append(visited_cities)
#     visits = int(input("how many times have you visited this country?\n"))
#     info.update({"country":country, "visited_cities":cities, "visits":visits})
#     travel_diary.append(info)
# add_country()
# print("diary updated.")
# print(travel_diary)
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
rok = int(input("Zadejte rok: "))
mesic = input("Zadejte mesic: ")
def vypocet_dni_v_danem_mesici(rok, mesic):
    mesice = ["leden", "unor", "brezen", "duben", "kveten", "cerven", "cervenec", "srpen", "zari", "rijen", "listopad", "prosinec"]
    poradi = mesice[mesic]
    if mesic == "unor":
        return days_in_month[poradi] + 1
    else:
        return days_in_month[poradi]


print(vypocet_dni_v_danem_mesici(rok, mesic))