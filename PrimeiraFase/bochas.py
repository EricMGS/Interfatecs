n, t = [int(x) for x in input().split()]

pontosB = 0
pontosV = 0
for i in range(t):
    bolimX, bolimY = [int(x) for x in input().split()]
    brancas = []
    vermelhas = []
    for bolas in range(n):
        bX, bY = [int(x) for x in input().split()]
        brancas.append(((bX - bolimX)**2 + (bY - bolimY)**2)**(1/2))
    for bolas in range(n):
        bX, bY = [int(x) for x in input().split()]
        vermelhas.append(((bX - bolimX)**2 + (bY - bolimY)**2)**(1/2))
    
    brancas.sort()
    vermelhas.sort()

    
    i = 0
    while i < len(brancas) and brancas[i] == vermelhas[i]:
        i += 1
        
    if i == len(brancas):
        pass
    elif brancas[i] < vermelhas[i]:
        total = 0
        for bola in brancas[i:]:
            if bola < vermelhas[i]:
                total += 1
        pontosB += total
    elif brancas[i] > vermelhas[i]:
        total = 0
        for bola in vermelhas[i:]:
            if bola < brancas[i]:
                total += 1
        pontosV += total
    
print('PONTOS DAS BOCHAS BRANCAS =', pontosB)
print('PONTOS DAS BOCHAS VERMELHAS =', pontosV)
print('VENCEDOR: ', end='')
if pontosB > pontosV:
    print('BOCHAS BRANCAS')
else:
    print('BOCHAS VERMELHAS')