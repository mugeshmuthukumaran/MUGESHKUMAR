#mugi
ain=input()
s=''
for i in range(0,len(ain)-1,2):
  if int(ain[i+1])%2==0:
    s+=ain[i]*int(ain[i+1])
  else:
    s+=ain[i]+ain[i+1]
print(s)
