import collections
k=input()
d=collections.Counter(k).most_common(1)[0][0]
print(d)
