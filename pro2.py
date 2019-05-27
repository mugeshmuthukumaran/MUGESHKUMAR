from itertools import combinations
m,n=map(int,input().split())
h=len(str(m))
l=list(combinations(str(m),h-n))
l=sorted(l)
print("".join(l[0]))
