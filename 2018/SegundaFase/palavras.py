from collections import Counter

a,b = input().split()
a = Counter(a.lower())
b = Counter(b.lower())

if a == b:
    print('S')
else:
    print('N')
