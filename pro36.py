#mugi
import sys,string
a = int(input())
M = [ int(x) for x in input().split()]
a = len(M)
cnt = 0
for i in range(0,a-2) :
    for j in range(i+1, a-1):
        for k in range(j+1, a):
            if M[i] > M[j] > M[k] :
                cnt += 1
print(cnt)
