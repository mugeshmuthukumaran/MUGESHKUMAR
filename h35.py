#mugi
tin=input()
a=0
for i in range(len(tin)):
    if tin[:i]==tin[i+1:]:
        a=0
        break
    else:
        a=1
if a==0:
    print("YES")
else:
    print("NO")
