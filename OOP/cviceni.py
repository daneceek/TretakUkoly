class Omacka:
    
    def __init__(self) -> None:
        self.__mouka = 0
        self.__voda = 0
    @property
    def voda(self):
        return self.__voda
    
    @property
    def mouka(self):
        return self.__mouka

    @mouka.setter
    def mouka(self, value):
        if value >= 0:
            self.__mouka = value
        
    def serviruj(self):
        if (self.__voda > self.__mouka):
            return "Omačka"
        else:
            return "Fuj"
        
    def pridej_mouku(self, kolik):
        if (self.__voda > self.__mouka + kolik):
            self.__mouka += kolik 
        

omacka = Omacka()
omacka.mouka = 100
omacka.voda = 500 
print(omacka.serviruj())