#mugi
m,n=input().split()
k={int(k) for k in input().split()}
l={int(l) for l in input().split()}
if l.issubset(k):
    print("YES")
else:
    print("NO")
