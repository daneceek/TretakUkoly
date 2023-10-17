import random

def random_number_generator(count, min, max):
    result = []
    for _ in range(count):
        result.append(random.randint(min, max))
        
    return result
