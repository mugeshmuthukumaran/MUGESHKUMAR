n,k=map(int,input().split())
m=[]
for i in range(n+1,k):
	if(i%2==1):
		m.append(i) 
print(*m)  
