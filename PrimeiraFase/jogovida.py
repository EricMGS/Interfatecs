def vizinhos(matriz, l, c):
    total = 0
    if l + 1 < len(matriz) and matriz[l+1][c] == '1':
        total += 1
    if l - 1 >= 0 and matriz[l-1][c] == '1':
        total += 1
    if c + 1 < len(matriz[0]) and matriz[l][c+1] == '1':
        total += 1
    if c - 1 >= 0 and matriz[l][c-1] == '1':
        total += 1
    if l + 1 < len(matriz) and c+1 < len(matriz[0]) and matriz[l+1][c+1] == '1':
        total += 1
    if l - 1 >= 0 and c - 1 >= 0 and matriz[l-1][c-1] == '1':
        total += 1
    if l + 1 < len(matriz) and c-1 >= 0 and matriz[l+1][c-1] == '1':
        total += 1
    if l - 1 >= 0 and c + 1 < len(matriz[0]) and matriz[l-1][c+1] == '1':
        total += 1
    return total

def novaMatriz(matriz, t):
    
    for i in range(t):
        novaMatriz = []
        for l in range(len(matriz)):
            linha = []
            for c in range(len(matriz[0])):
                v = vizinhos(matriz, l, c)
                if v == 3:
                    linha.append('1')
                elif v == 2:
                    linha.append(matriz[l][c])
                elif v > 3 or v < 2:
                    linha.append('0')
            novaMatriz.append(linha)
        matriz = novaMatriz
        
    return matriz

l, c = [int(x) for x in input().split()]
matriz = []
for i in range(l):
    matriz.append(list(input()))
    
t = int(input())

matriz = novaMatriz(matriz, t)
for linha in matriz:
    print(*linha, sep='')