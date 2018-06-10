def validarnum(num):
        return validar(num,0,0)
def validar(num,d,n):
    if num == 0:
        return 0
    else:
        n += validar((num % 10)*10**(d + 1)) + validar((num // 10 % 100)*10**(d))
        return validar(num // 100, d+2,n)
        
