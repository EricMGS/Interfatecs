from collections import Counter

def binary_search(vet, num):
    esquerda, direita, meio = 0, len(vet), None
    while (esquerda + direita) // 2 != meio:
        meio = (esquerda + direita) // 2
        aux_num = vet[meio]
        if num == aux_num:
            return meio
        elif num > aux_num:
            esquerda = meio
        else:
            direita = meio

def isPrimo(n):
    global primos #Tabela de memorização de números primos
    
    #0, 1 e pares(exceto o 2) não são primos
    if n == 0 or n == 1 or (n != 2 and n % 2 == 0):
        return False
    
    #Inicialmente o número é buscado na tabela de primos
    if binary_search(primos, n) != None:
        return True
    
    #Caso não seja encontrado é calculado sua raíz quadrada pois um número
    #só pode ser ser divisível por números menores ou iguais que sua raiz
    raiz = n ** (1/2)
    i = 0
    #Se fará a verificação de divisibilidade pelos primos menores que a raiz
    while primos[i] <= raiz:
        #Caso seja divisível o número não é primo
        if n % primos[i] == 0:
            return False
        i += 1
        
        #Se a tabela não estiver completa até a raiz será completada
        j = primos[-1] + 1
        while i >= len(primos):
            if isPrimo(j):
                primos.append(j)
            j += 1
            
    #Se nenhum primo até a raiz do número for divisor dele, é primo
    return True


if __name__ == '__main__':
    primos = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,
              53,59,61,67,71,73,79,83,89,97,101,103,107,
              109,113,127,131,137,139,149,151,157,163,167,
              173,179,181,191,193,197,199,211,223,227,229,
              233,239,241,251,257,263,269,271,277,281,283,293,
              307,311,313,317]
    n = int(input())
    for intervalo in range(n):
        a, b = [int(x) for x in input().split()]
        frequencias = Counter()
        if a % 2 == 0:
            if isPrimo(a):
                frequencias += Counter(str(numero))
            a += 1
        for numero in range(a, b+1, 2):
            if isPrimo(numero):
                frequencias += Counter(str(numero))
                
        print('INTERVALO', intervalo + 1)
        for i in range(10):
            print('%d: %d' %(i, frequencias[str(i)]))