#mugi
x=int(input())
y=list(map(int,input().split()))
z=[]
for i in y:
    if(y.count(i)<=1):
        z.append(i)
E=set(z)
if len(E)==0:
    print("unique")
else:
    print(*E)
