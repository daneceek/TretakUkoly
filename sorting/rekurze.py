from generator import get_random_list
from copy import deepcopy

seznam = get_random_list(10, 0,50)

# def bubblesort_list(seznam):
list_result = deepcopy(seznam)
print(list_result)
def rekurze(list_):
    result = deepcopy(list_)
    smaller = []
    bigger = []
    for i in range(len(result)):
        
        if i == 0:
            pivot = result[i]
        else:
            if pivot <= result[i]:
                bigger.append(result[i])
            else:
                smaller.append(result[i])
            rekurze(smaller)
            rekurze(bigger)
    print(smaller)
    print(bigger)
    
    
    
    

rekurze(list_result)