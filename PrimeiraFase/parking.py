n = int(input())

lista = []
for i in range(n):
    lista.append([int(x) for x in input().split()])

pri = 0
for i in range(n):
    if lista[i][0] * 60 + lista[i][1] < lista[pri][0] * 60 + lista[pri][1]:
        pri = i

ult = 0
for i in range(n):
    if lista[i][2] * 60 + lista[i][3] > lista[ult][2] * 60 + lista[ult][3]:
        ult = i
        
dif = (lista[ult][2] * 60 + lista[ult][3]) - (lista[pri][0] * 60 + lista[pri][1])
print(dif)