n,k=map(int,input().split())
m=[int(x) for x in input().split()]
c=0
for i in range(0,k):
	c=c+m[i]
	print(c)
