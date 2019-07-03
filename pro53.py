#mugi
a=input().split()
m="abcdefghijklmnopqrstuvwxyz"
x=a[0]
c = 0
for i in range(1,len(a)):
    x=x+a[i]
y=x.lower()
y=[*y]
y=list(set(y))
for i in y:
    if i in m:
        c+=1
if c==26:
    print("yes")
else:
    print("no")
