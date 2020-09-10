import itertools
import random
print(random.__file__)
list = [1,4,3,3,4,2,3,4,5,6,1]
list.sort()
it = itertools.groupby(list)
for k, g in it:
    print(k)

name = 'fever'
print("the index of fe: {}".format(name.find("fe", 0, 3)))