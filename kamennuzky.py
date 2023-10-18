import random
x = input("kamen, nuzky nebo papir?\n")
y = random.choice(["kamen", "nuzky", "papir"])
print(f"Soupeř : {y}")
if y == x :
    print("remiza")
elif x == "kamen" and y == "nuzky":
    print("Vyhra")
elif x == "nuzky" and y == "papir":
    print("Vyhra")
elif x == "papir" and y == "kamen":
    print("Vyhra")
elif x == "nuzky" and y == "kamen":
    print("Prohra")
elif x == "kamen" and y == "papir":
    print("Prohra")
elif x == "papir" and y == "nuzky":
    print("Prohra")