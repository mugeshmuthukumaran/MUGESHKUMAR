#mugi
def check(l):
        cin=1
        for v in range(0,len(l)-1):
                if l[v]!=l[v+1]:
                        cin=cin+1
                else:
                    break
        return cin
number=int(input())
lin=list(map(int,input().split()))
for v in range(0,len(lin)):
        if lin[v]>0:
                lin[v]=1
        else:
             lin[v]=0
s=""
for v in range(0,len(lin)):
        k=lin[v::]
        s=s+str(check(k))+" "
print(s.strip())
