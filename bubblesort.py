from generator import get_random_list
from copy import deepcopy

seznam = get_random_list(10, 0,50)

# def bubblesort_list(seznam):
list_result = deepcopy(seznam)
print(list_result) 

for _ in range(len(list_result) - 1):
        for i in range(len(list_result) - 1):
                if list_result[i] > list_result[i + 1]:
                        list_result[i + 1], list_result[i] = list_result[i], list_result[i + 1]
print(list_result)
print(list_result)
print("dnes jsem to zandal")