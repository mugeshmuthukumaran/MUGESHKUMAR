m=int(raw_input())
mk=m.split()
c=int(mk[0])
d=int(mk[1])
for i in range(c+1,d):
	if(i%2==0):
		print (i,)
