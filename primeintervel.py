m,n=map(int,input().split())
for x in range(m+1,n):
    for i in range(2,x):
        if(x%i==0):
            break
    else:
        print(x,end=" ")
