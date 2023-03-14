from random import *

lot = set([])
def lotto():
    while(True):
        if len(lot)==6:
            break
        lot.add(randint(1, 45))
lotto()
print(lot)