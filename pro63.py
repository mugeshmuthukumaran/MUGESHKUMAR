#mugi
o=input()
lis=[]
for i in o:
    if i not in lis:
        lis.append(i)
        #print(i)
    else:
        break
print(len(lis))
