# vaha = input("Chcete vypočítat své BMI? Jestli ano, tak sem napište svou váhu v kg\n")
# vyska = input("a sem svou výšku v metrech\n")
# bmi =  int(vaha) / float(vyska)**2
# bmi=int(bmi)
# print(bin("Vaše BMI je:" + str(bmi)) )

list = []
for i in range(101):
    if (i == 2) or (i == 3) or (i == 5):
        list.append(i)
    if (i % 2 > 0) and (i % 3 > 0) and (i % 5 > 0):
        list.append(i)

print(list)