#mugi
number=int(input())
l=[int(x) for x in input().split()]
av=int(number/2)
l1=l[:av]
l2=l[av::]
m1=sum(l1)//len(l1)
m2=sum(l2)//len(l2)
if m1==m2:
    print("yes")
else:
    print("no")
