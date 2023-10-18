#############LOGIKA################
class Car:
    #konstruktor
    def __init__(self, color, doors, brand):
        self.color = color
        self.doors = doors
        self.brand = brand 
        self.distance = 0
        
    def turn_left(self):
        return f"Auto značky {self.brand} zatočilo doleva."

    def turn_right(self):
        return f"Auto značky {self.brand} zatočilo doprava."

    def go_straight(self):
        self.distance += 10
        return f"Auto popojelo o 10 metrů"
        
    def distance_driven(self):
        return f"Ujetá vzdálenost auta {self.brand} je {self.distance}." 

    def owner(self, owner_name):
        return f"Vlastníkem auta je {owner_name}"  


class VipCar(Car):
    def __init__(self, color, doors, brand, password):
        super().__init__(color, doors, brand)
        self.password = password
        self.software_control = True
    def go_straight(self):
        self.distance += 25
        return f"Auto popojelo o 25 metrů"
    def password_try(self, password_guess):
        if self.password == password_guess:
            return "Správné heslo"
        else:
            return "Špatné heslo"
    def turn_on_off_software_control(self):
        if self.software_control == True:
            self.software_control = False
        elif self.software_control == False:
            self.software_control = True










# atributy = vlastnosti
# metody = funkce 



########POUŽITÍ###############

car_1 = Car("red", 4, "BMW")
car_2 = Car("blue", 2, "Porsche")
car_3 = Car("yellow", 4, "Skoda")

print(car_1.owner("David"))
print(car_2.owner("Hermiona"))

# print(car_3.color)
# car_1.turn_left()
# car_2.turn_right()
# car_1.go_straight()
# car_2.go_straight()
# car_3.turn_left()
# print(car_2.distance_driven())
vip_car1 = VipCar("blue", 4, "Mercedes", "ok")
print(vip_car1.password_try("ok"))
print(vip_car1.software_control)
vip_car1.turn_on_off_software_control()
print(vip_car1.software_control)
vip_car1.turn_on_off_software_control()
print(vip_car1.software_control)
print(vip_car1.go_straight())