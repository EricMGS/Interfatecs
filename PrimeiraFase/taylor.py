fat = [1, 2, 24, 720, 40320, 3628800]

def taylor(x):
    total = 0
    for i in range(6):
        total += ((-1)**i  * ((x**(2*i)) / fat[i]))
        
    return total

pi = 3.1415

n = int(input())
if n != 90:
    r = n * pi/180
    t = taylor(r)
    
    
    t = str(t)
    if len(t) < 6:
        t += '000000'
    
    if int(t[5]) < 7:
        print(t[:5])
    else:
        t = t[:5]
        t = float(t) + 0.001
        t = str(t)
        
        if len(t) < 6:
            t += '000000'
        print(t[:5])
else:
    print('0.000')