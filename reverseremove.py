n=int(raw_input())
m=(raw_input())
vowels = ('a', 'e', 'i', 'o', 'u')  
for x in m: 
	if x in vowels:
		m = m.replace(x,"") 
print (m[::-1])

