from kalkulačka import cislo

# list_vyska = []
# suma = 0 
# while True :
#     vyska = input("Zadejte výšku lidí\n")
#     if vyska == "stop":
#         for i in list_vyska:
#             suma = suma + int(i)
#         print(f"Průměrná výška lidí je {round(suma/len(list_vyska), 1)}")
#     else:
#         list_vyska.append(vyska)
list = []
for i in range(0, 101):
    list.append(i)
for cislo in list:
    if cislo % 3 == 0 and cislo % 5 == 0:
        print("Fizz Buzz")
    elif cislo % 3 == 0:
        print("Fizz")
    elif cislo % 5 == 0:
        print("Buzz")
    else:
        print(cislo)

    

