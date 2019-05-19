a, l = [int(x) for x in input().split()]

dic = {}

for i in range(l):
    key, frase = input().split()
    key = int(key)
    dic.update({key : frase})
    
e = int(input())
p = 1


for i in range(e):
    if (input()== 'true'):
        p=p*2+1
    else:
        p = p*2
        

print (dic[p])
