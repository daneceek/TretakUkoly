from generator import get_random_list
from copy import deepcopy


seznam = get_random_list(10, 0,50)
print(seznam)
def quicksort(seznam):
    
    higher = []
    lower = []
    
    
    if len(seznam) > 1 and seznam != False:
        pivot = seznam[0]
        for i in range(1, len(seznam)):
                if seznam[i] <= pivot:
                    lower.append(seznam[i])
                else:
                    higher.append(seznam[i])
        seznam.clear()
        if len(lower) >= 1:
            seznam.append(lower) 
        seznam.append(pivot)
        if len(higher) >= 1:
            seznam.append(higher)
        
         
        
        quicksort(higher)
        
        quicksort(lower)
        
        return seznam
       
        
        
        
        
        
        
    
    # while len(higher) != 1 and len(lower) != 1: 
    #     quicksort(higher)
    #     quicksort(lower)

print(quicksort(seznam))
    
    

