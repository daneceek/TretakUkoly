import random

seznam = []
def get_random_list(n, min = 0, max = 100):
    seznam = []
    if min >= max:
        raise ValueError("Min je vetsi nez max")
    for _ in range(n):
        seznam.append(random.randint(min, max))
        # seznam += [random.randint(min, max)]
    return seznam

