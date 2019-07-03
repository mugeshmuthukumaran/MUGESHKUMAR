#mugi
import sys
o,k=list(map(str,input().split()))
f=[]
for i in range(0,len(o)-1):
   f=list(o[i:i+2])
   for j in range(0, len(k) - 1):
       if f[0]==k[j] and f[1]==k[j+1]:
           print("yes")
           sys.exit()
print("no")
