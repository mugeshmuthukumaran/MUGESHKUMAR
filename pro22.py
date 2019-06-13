#mugi
n1=int(input())
a1=list(map(int,input().split()))
b1=[]
c1=[]
for i1 in range(len(a1)):# for loop starts
    if(i1%2==0):
        b1.append(a1[i1])
    else:
        c1.append(a1[i1])# for loop ends
for j1 in b1:
    d1=sum(b1)
for k1 in c1:
    f1=sum(c1)
if(d1>f1):
    print(d1)
else:
    print(f1)
