#mugi
nin,k = map(int,input().split())
a = list(map(int,input().split()))
b,cin = 0,[]
for i in range(0,len(a)):
  t = i
  for p in range(0,len(a)):
    for l in range(0,k):
      if l == k-1:
        try:
          b += a[p+i]
        except IndexError:
            t = t-1
            b +=a[t]
      else:
        b += a[i]
    cin.append(b)
    b = 0
for i in range(0,len(a),k):
  b = sum(a[i:i+k])
  cin.append(b)
print(*sorted(set(cin)))
