import math
a,z=map(int,input().split())
c=[]
b=list(map(int,input().split()))
for j in range(0,z):
    l,h=map(int,input().split())
    c.append([l,h])
for j in c:
    n=j[0]-1
    m=j[1]-1
    print(math.gcd(b[n],b[m]))
