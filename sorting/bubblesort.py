from generator import get_random_list
from copy import deepcopy

seznam = get_random_list(10, 0,50)

# def bubblesort_list(seznam):
list_result = deepcopy(seznam)

def bubble_sort(list_result):
        result = deepcopy(list_result)
        for _ in range(len(result) - 1):
                for i in range(len(result) - 1):
                        if result[i] > result[i + 1]:
                                result[i + 1], result[i] = result[i], result[i + 1]
        return result
print(bubble_sort(list_result))
