from sre_constants import REPEAT
from timeit import repeat


input = 4 # Max Iterations
t = 1 # Total
c = 1

while c <= input:
    t = t * c
    c += 1
    print(t) # answers