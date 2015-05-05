import random
import pprint

def partition(lst, n): 
    random.shuffle(lst)
    division = len(lst) / float(n) 
    return [ lst[int(round(division * i)): int(round(division * (i + 1)))] for i in xrange(n) ]

deltakere = ["Henrik", "Frode", "Erik", "Ken", "Ingvild", "Tina", "Peder", "Lars", "Steffen", "Oyvind", "Fredrik"]

pprint.pprint(partition(deltakere, 3))
