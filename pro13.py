#mugi
num,n1=map(int,input().split())
lis=list(map(int,input().split()))
for i in range(n1):
    u,v=map(int,input().split())
    c=lis[u-1:v]
    print(min(c))
