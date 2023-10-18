
# Deepcopy 
from copy import deepcopy


list_ = [0,1,2,3,4,8]
list__ = deepcopy(list_)

list__[2] = 8
print(list_)