#mugi
ain,b=input().split()
ain=int(ain)
b=int(b)
s=''
u=2
if(ain+b<=3):
    for i in range(0,ain+b):
        if(i%2!=0):
            s=s+'0'
        else:
            s=s+'1'
else:    
    for i in range(0,ain+b):
        if(i==u):
            s=s+'0'
            if(u==b):
                u=u+2
            else:
                u=u+3
        else:
            s=s+'1'
x=len(s)-1
if(int(s[x])==0):
    print('-1')
elif ain==1 and b==2: 
     print("011")
else:
    print(s)
