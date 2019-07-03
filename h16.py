#mugi
n,k=map(int,input().split())
l=list(map(int,input().split()))
l.remove(k)
rl=[]
for i in range(3):
    mi=abs(l[0]-k)
    r=l[0]
    for j in l:
        if abs(j-k)<mi:
            r=j
            mi=abs(j-k)
    rl.append(r)
    l.remove(r)
for i in range(2):
    print(rl[i],end=" ")
print(rl[2])    
