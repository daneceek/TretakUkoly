rok = int(input("Zadejte mi rok:\n"))
if rok % 4 == 0:
    if rok % 100 > 0:
        print("Zadaný rok je přestupný")
    elif rok % 100 == 0:
        if rok % 400 == 0:
            print("Zadaný rok je přestupný")
else:
    print("Zadaný rok je nepřestupný")