#mugi
o=input()
b=input()
c="abcdefghijklmnopqrstuvwxyz"
d=[]
e=[]
s=""
for i in range(0,len(o)):
    for j in range(0,len(c)):
        if o[i]==c[j]:
            d.append(j+1)
        if b[i]==c[j]:
            e.append(j+1)
for k in range(0,len(d)):
    tot=d[k]+e[k]
    if(tot<=26):
        s=s+c[tot-1]
    else:
        m=tot-26
        s=s+c[m-1]
print(s)
