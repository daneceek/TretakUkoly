# Encapsulation - zapouzdření
# Abstraction - abstrakce = dáváme přistup pouze tomu, co je zapotřebí
# Inheritance - dědění
# Polymorphism - mnoho forem, jedna metoda může přepisovat druhou metodu

class WizardPlayer:

    wizard_club = True

    def __init__(self, name="anonym", age = 0):
        
        self._name = name
        self.age = age
        
    def attack(self):
        print("Útok")
        
    def age_checker(self):
        if self.age >= 18:
            print("Můžete hrát")
        else:
            print("Nemůžete hrát. Váš věk je příliš nízký.")
    @staticmethod
    def test_function(n1, n2):
        return n1 + n2
    @classmethod
    def test_function2(cls, n1, n2):
        return cls("Harry", 80)
    
class HeadWizard(WizardPlayer):
    
    def __init__(self, type, name, age):
        super().__init__(name, age)
        self.type = type
        
    
    def avada_kedabra(self):
        print("Avada kedabra")
    
    
    def attack(self):
        print("Útok druhého stupně") 

player1 = WizardPlayer("david", 25)
print(player1._name)
print(player1.age)
player1.attack()


player2 = HeadWizard("lmao", "kys", 8)
player2.avada_kedabra()
player2.attack()
print(player2._name)


# Introspection

# Dunder methods (třeba __init__)
print(dir(player2))
print(player2.__dir__())

# Method resolution order = MRO
print(HeadWizard.mro())






# print(isinstance(player1, WizardPlayer))
# Měnění
# player1.attack = "ahoj"
# print(player1.attack)
# player1.name = "Martin"
# print(player1.name)
#




# player2 = WizardPlayer.test_function2(30, 20)
# print(player2.name)



























# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age



# dog1 = Dog("žeryk", 15)
# dog2 = Dog("kys", 25)
# dog3 = Dog("penis", 8)

# def nejstarsi_pes():
#     roky_psu = [dog1.age, dog2.age, dog3.age]
#     nejstarsi = max(roky_psu)
#     return nejstarsi
# print(f"Věk nejstaršího psa je {nejstarsi_pes()} let")    