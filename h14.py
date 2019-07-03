#mugi
from itertools import permutations
n=input()
l=permutations(n)
for j in list(l):
    print("".join(j))
