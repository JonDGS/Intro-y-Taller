def divisor():
    num = eval(input('Ingrese el valor que desea procesar: '))
    if isinstance(num, int):
        return p(num,[],2)
    else: return 'La entrada no es valida'
def p(num,l,d):
    if num == d:
        if l == []:
            return 'No posee divisor diferentes de si mismo y 1'
        else:
            return l
    elif num % d == 0:
        return p(num,l + [d],d+1)
    else: return p(num,l,d+1)
    
    
    
