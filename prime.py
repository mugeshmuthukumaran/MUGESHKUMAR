n=int(raw_input())
m=0
for i in range(2,n/2+1):
    if(n%i==0):
        m=m+1
if(m<=0):
    print("yes")
else:
    print("no")
