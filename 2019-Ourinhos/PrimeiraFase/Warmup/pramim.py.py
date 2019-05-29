primeiro, n = input().split()
n = int(n)

voce = 0
amigo = 0
for i in range(n):
    if primeiro == 'V':
        if i % 2 == 0:
            voce += int(input())
        else:
            amigo += int(input())
    elif primeiro == 'A':
        if i % 2 == 0:
            amigo += int(input())
        else:
            voce += int(input())

print('VOCE: %d AMIGO: %d' %(voce, amigo))
