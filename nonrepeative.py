m=int(input())
l=[int(x) for x in input().split()]
s=[]
for i in range(0,m):
    x=l.count(l[i])
    s.append(x)
x=s.index(1)
print(l[x])
