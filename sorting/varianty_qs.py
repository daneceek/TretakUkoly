from generator import get_random_list
from copy import deepcopy



# def quick_sort_1(list_):
#     if len(list_) <= 1:
#         return list_
#     left = []
#     right = []
#     pivot = list_[0]
#     for n in list_[1:]:
#         if n < pivot:
#             left.append(n)
#         else:
#             right.append(n)
#     return quick_sort_1(left) + [pivot] + quick_sort_1(right)

#     return result


# https://youtu.be/MZaf_9IZCrc
def quick_sort_2(list_, l_index=None, r_index=None):
    if l_index is None and r_index is None:  # při prvním volání z hlavního programu
        l_index = 0
        r_index = len(list_) - 1

    if l_index >= r_index:  # ukončení rekurze
        return

    i = l_index - 1
    j = l_index
    pivot = list_[r_index]
    while j <= r_index:
        if list_[j] <= pivot:
            i += 1
            if j != i:  # abych neprohazoval prvek sám se sebou
                list_[j], list_[i] = list_[i], list_[j]
        j += 1
    quick_sort_2(list_, l_index, i - 1)
    quick_sort_2(list_, i + 1, r_index)


def quick_sort_3(list_, l_index=None, r_index=None):
    abcdef = list(range(10))
   
    if l_index is None and r_index is None:
        l_index = 0
        r_index = len(list_) - 1

    if l_index >= r_index:  # ukončení rekurze
        return

    i = l_index
    pivot = list_[r_index]  # pivot je na konci
    j = r_index - 1
    while i < j:
        while list_[i] < pivot and i < r_index:
            i += 1
        while list_[j] > pivot and j > l_index:
            j -= 1
        if i < j:
            list_[j], list_[i] = list_[i], list_[j]
    list_[i], list_[r_index] = list_[r_index], list_[i]  # pivota dám doprostřed, je na pozici i
    quick_sort_3(list_, l_index, i - 1)
    quick_sort_3(list_, i + 1, r_index)


seznam = get_random_list(20)
print(seznam)
quick_sort_3(seznam)
print(seznam)

