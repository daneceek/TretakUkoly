from generator import random_number_generator
from copy import deepcopy
from excercise import list1
seznam = random_number_generator(10, 0,50)

# def bubblesort_list(seznam):
list_result = deepcopy(seznam)
print(list_result) 

for _ in range(len(list_result) - 1):
        for i in range(len(list_result) - 1):
                if list_result[i] > list_result[i + 1]:
                        list_result[i + 1], list_result[i] = list_result[i], list_result[i + 1]
print(list_result)