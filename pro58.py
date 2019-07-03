#mugi
number = int(input())
b = []
ain = number//2 + number
for i in range(1,number+1):
  if i%2==0:
    b.append(i)
for i in range(1,number+1):
  if i%2!=0:
    b.append(i)
for i in range(1,number+1):
  if i%2==0:
    b.append(i)
print(ain)
print(*b)
