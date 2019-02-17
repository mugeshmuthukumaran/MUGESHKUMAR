m=int(input())
tot=0
while(m>0):
	dig=m%10
	tot=(tot+(dig*dig))
	m=m//10
print(tot)
