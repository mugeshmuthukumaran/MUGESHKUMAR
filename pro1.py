m=input()
m=int(s)
z=[]
for i in range(0,m):
    s1=input()
    z.append(s1)
y=[]
for i in zip(*z):
    if i.count(i[0])==len(i):
        y.append(i[0])
    else:
        break
print(''.join(y))
