#mugi
x=int(input())
y=list(map(int,input().split()))
z=[]
for i in y:
    if(y.count(i)>1):
    	print(i)
    	break
else:
	print("unique")
