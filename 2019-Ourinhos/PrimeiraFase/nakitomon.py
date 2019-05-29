n = int(input())

danette = []
silvio = []

for i in range(n):
    danette.append([int(x) for x in input().split()])

for i in range(n):
    silvio.append([int(x) for x in input().split()])
    
danette.sort(reverse=True)
silvio.sort(reverse=True)

placarD = 0
placarS = 0
empates = 0
for i in range(n):
    if danette[i] > silvio[i]:
        placarD += 1
    elif danette[i] < silvio[i]:
        placarS += 1
    else:
        empates += 1
                    
print('danette venceu:', placarD)
print('silvio venceu:', placarS)
print('empates:', empates)