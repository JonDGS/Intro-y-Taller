def paresimpares(num):
    if isinstance(num, int):
        x = lambda num : num % 2 == 0
        y = lambda num : num % 2 == 1
        return detectar(num , x), detectar(num, y)
    else:
        'No es un numero o no es un valor entero'
def detectar(num, cdcn):
    if num == 0:
        return 0
    elif cdcn(num % 10):
        return 1 + detectar(num // 10, cdcn)
    else:
        return detectar(num // 10, cdcn)
    
