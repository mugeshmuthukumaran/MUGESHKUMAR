#mugi
import sys, string, math
from itertools import permutations, combinations
m = input()
din1 = {}
for c in 'dhoni' :
    din1[c] = 1
#print(din1)
din2 = {}
for c in m :
    if c in din2 :
        din2[c] += 1
    else:
        din2[c] = 1
#print(din2)
if din1 == din2 : 
      print('yes')
else:         
      print('no')
