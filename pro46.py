#mugi
uin=int(input())
vin=list(map(int,input().split()))
a=0
b=0
vin.sort(reverse=True)
for i in vin:
  vin=a+i
  if b>vin:
    a=vin
  else:
    a=b
    b=vin
print(a,b)
