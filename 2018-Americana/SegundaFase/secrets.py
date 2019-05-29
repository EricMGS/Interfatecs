primos = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277]
fibo = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
fact = [1, 2, 6, 24, 120]

while True:
    try:
        code = input()
        res = 0
        for i in range(len(code)):
            if code[i].isdigit():
                res += (int(code[i]) * (i+1))
            else:
                res += ((ord(code[i]) - 96) * (i+1))
        print('%d: ' %res, end='')
        if res in fact:
            print('ultimate')
        elif res in fibo:
            print('premium')
        elif res in primos:
            print('basic')
        else:
            print('!')
        
    except EOFError:
        break
