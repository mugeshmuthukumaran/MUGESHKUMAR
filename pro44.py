#mugi
h,m,d,s=map(int,input().split())
n=[int(i) for i in input().split()]
a=[m*n[i]+d*n[j]+s*n[k] for i in range(len(n)) for j in range(len(n)) for k in range(len(n)) if i<=j<=k]
print(max(a))
