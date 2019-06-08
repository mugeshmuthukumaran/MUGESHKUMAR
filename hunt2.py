#mugi
x=int(input())
y=list(map(int,input().split()))
y.sort(reverse=True)
for i in range(0,x):
  print(y[i],end="")
