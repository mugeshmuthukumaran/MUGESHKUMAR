#mugi
nin=int(input())
l=list(map(int,input().split()))
ain=l
c=[]
while(len(ain)!=1):
	for i in range(len(ain)):
		if i%2!=0:
			c.append(ain[i])
	ain=c
	c=[]
print(l.index(ain[0]))
