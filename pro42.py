#mugi
vk,vj=map(int,input().split())
lis=list(map(int,input().split()))
if vj==1:
    print(min(lis))
elif vj==2:
    print(max(lis[0],lis[vk-1]))
else:
    print(max(lis))
© 2019 GitHub, Inc.
