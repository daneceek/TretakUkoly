from generator import get_random_list
from copy import deepcopy
import string


seznam = [15, 8, 11, 3, 5, 1, 18, 7, 16]
print(seznam)
def quicksort(seznam):
    
    higher = []
    lower = []
    
    
   
    if len(seznam) <= 1:
        return seznam
    else:
        for i in range(1, len(seznam)):
            pivot = seznam[0]
            if seznam[i] <= pivot:
                lower.append(seznam[i])
            else:
                higher.append(seznam[i])
    
    return quicksort(lower) + [pivot] + quicksort(higher)
    
         
        
    
    
        
        
        
       
        
        
        
        
        
        
    
    # while len(higher) != 1 and len(lower) != 1: 
    #     quicksort(higher)
    #     quicksort(lower)

print(quicksort(seznam))
    
    

