from collections import Counter

s = input()
c = Counter(s)

impares = 0
for letra in c.values():
    if letra % 2 != 0:
        if impares == 1:
            print('FALSO')
            break
        else:
            impares = 1
else:
    print('VERDADEIRO')