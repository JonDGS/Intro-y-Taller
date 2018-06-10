def t(num):
    if isinstance(num, int):
        return p(num,0, 0)
    else:
        return 'El valor ingresado no es un numero: '
def p(num, r,d):
    if num == 0:
        return r
    elif num%10 == 0:
        return p(num // 10, (num % 10)*10**(d) + r, d+1)
    elif (num%10)%3 == 0:
        return p(num // 10, r, d)
    else:
        return p(num // 10, (num % 10)*10**(d) + r, d+1)
        
    
