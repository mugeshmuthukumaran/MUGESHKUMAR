#mugi
ain,bi=list(map(int,input().split()))
cin,din=list(map(int,input().split()))
ein,fin=list(map(int,input().split()))
gin,hin=list(map(int,input().split()))
m=din-bi
n=fin-hin
o=ein-cin
p=gin-ain
if (m==n==o==p):
    print("yes")
else:
    print("no")
