from generator import get_random_list
from copy import deepcopy

seznam = get_random_list(10, 0,50)

# def bubblesort_list(seznam):
list_ = deepcopy(seznam)


def insert_sort(list_):
    result = deepcopy(list_)
    print(result)
    for i in range(0, len(result)):
        j = i
        while result[j] < result[j - 1] and j > 0:
            
            result[j - 1], result[j] = result[j], result[j - 1]
            j -= 1
    return result

print(insert_sort(list_))

