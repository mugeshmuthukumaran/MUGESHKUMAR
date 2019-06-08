#mugi
a=int(input())
b=[]
c=[]
for i in range(0,a):
    b=[int(x) for x in input().split()]
    for j in range(0,len(b)):
        c.append(m2[j])
    b=[]    
c.sort()
print(*c)
