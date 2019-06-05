m,n=raw_input().split()
o=abs(len(m)-len(n))
for i in range(len(m)):
	if len(n)==1 and n[i] in m:
		break
	if i>=len(m) or i>=len(n):
		break
	if n[i]!=n[i] and n[i]:
		o=o+1
print(o)
