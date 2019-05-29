def areaInterseccao(x1, y1, r1, x2, y2, r2):
    from math import acos, sin
    
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1/2) #Distância
    if d >= r1 + r2: #Não há interseccção
        return 0
    
    cos1 = (-r2**2 + r1**2 + d**2) / (2 * d * r1)
    cos2 = (-r1**2 + r2**2 + d**2) / (2 * d * r2)
    arc1 = acos(cos1)
    arc2 = acos(cos2)
    A1 = arc1 * r1**2 - (r1**2 * sin(2 * arc1)) / 2
    A2 = arc2 * r2**2 - (r2**2 * sin(2 * arc2)) / 2
    return A1 + A2

def insereCirculo(lamina, x, y, r, index):
    x -= r
    y -= r
    for linha in range(x, x + 2*r):
        for coluna in range(y, y + 2*r):
            lamina[linha][coluna].append(index)


#Define matriz 200x200
lamina = []
for i in range(200):
    lamina.append([])
    for j in range(200):
        lamina[i].append([])

celulas = []
areaCirculos = 0
for circulo in range(int(input())):
    x, y, r = [int(x) for x in input().split()]
    celulas.append((x,y,r))
    insereCirculo(lamina, x, y, r, circulo) #insere celula na lamina
    areaCirculos += 3.1415 * r**2
    
areaInterseccoes = 0
jaCalculados = []
for linha in range(200):
    for coluna in range(200):
        quadrado = lamina[linha][coluna]
        if len(quadrado) >= 2:
            for celula in range(len(quadrado) - 1):
                if quadrado[celula] in jaCalculados:
                    continue
                x1 = celulas[quadrado[celula]][0]
                y1 = celulas[quadrado[celula]][1]
                r1 = celulas[quadrado[celula]][2]
                for celula2 in range(celula+1, len(quadrado)):
                    if quadrado[celula2] in jaCalculados:
                        continue
                    x2 = celulas[quadrado[celula2]][0]
                    y2 = celulas[quadrado[celula2]][1]
                    r2 = celulas[quadrado[celula2]][2]
                    areaInterseccoes += areaInterseccao(x1,y1,r1,x2,y2,r2)
                    jaCalculados.append(quadrado[celula])
                    jaCalculados.append(quadrado[celula2])
                    
print(int(areaCirculos - areaInterseccoes))