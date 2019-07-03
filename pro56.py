#mugi
n,t=map(int,input().split())
sec=list(map(int,input().split()))
count=0
for i in sec:
  t1=86400-i
  t=t-t1
  count+=1
  if t<=0:
    break  
print(count)
