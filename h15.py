#mugi
def star(m,n):
    k=n[m+1:len(n)]
    s=n[m]
    p=0
    for i in range(0,len(k)):
        if s>k[i]: p=p+1
    if p==len(k): return s
    else:return None
def super(m,n):
    k = n[0:m]
    s = n[m]
    p = 0
    for i in range(0, len(k)):
        if s > k[i]: p = p + 1
    if p == len(k):
        return s
    else:
        return None

n=int(input())
l=list(map(int,input().split()))
s=[]
r=[]
w=0
for i in range(0,n):
    w=star(i,l)
    if w!=None: s.append(w)
for j in range(len(s)):
    w=super(l.index(s[j]),l)
    if w != None: r.append(w)
print(*s)
print(*r)
