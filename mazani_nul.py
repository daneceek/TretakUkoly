from generator import random_number_generator

seznam = random_number_generator(20, 0,4)
print(seznam) 
nula = 0
for index, cislo in enumerate(seznam):
    
    if cislo == 0:
        
        nula += 1
        
        if nula > 1:
            nula = 0
        
        if nula == 0:
            seznam.pop(index)
print(seznam)        